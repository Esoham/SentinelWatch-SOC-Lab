"""Deterministic security-to-business report; no external AI or network calls."""
import argparse
import json
from csv import DictReader
from pathlib import Path
from sentinelwatch.detect import detect_login_sequences
from sentinelwatch.controls import assess_controls, load_accounts

def build_report(auth_csv, accounts_csv):
    with open(auth_csv, newline="", encoding="utf-8") as handle:
        events = list(DictReader(handle))
    alerts = detect_login_sequences(events)
    findings = assess_controls(load_accounts(accounts_csv))
    impacted = {a["user"] for a in alerts}
    correlated = [f for f in findings if f["user"] in impacted]
    return {
        "data_classification": "synthetic_training_data",
        "events_analyzed": len(events),
        "alerts": alerts,
        "control_findings": findings,
        "correlated_findings": correlated,
        "business_assessment": {
            "potential_impact": "Unauthorized access could affect confidentiality and operations; not confirmed",
            "priority": "analyst_review",
            "owner": "Security Operations / Identity Owner",
            "recommended_action": "Validate authentication and MFA evidence, review privileged access, escalate per approved SOP",
            "decision_authority": "human_analyst"
        },
        "limitations": ["No real telemetry or identity provider", "No proof of compromise", "No production detection quality estimate", "No live SIEM/EDR integration"]
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--auth", default="data/auth_events.csv")
    parser.add_argument("--accounts", default="data/accounts.csv")
    parser.add_argument("--output", default="outputs/investigation.json")
    args = parser.parse_args()
    result = build_report(args.auth, args.accounts)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"{len(result['alerts'])} alerts, {len(result['control_findings'])} control findings")

if __name__ == "__main__":
    main()
