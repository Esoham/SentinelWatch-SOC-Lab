"""Defensive SOC detection demo using fictional authentication telemetry."""
import csv
import json
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

def parse_time(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))

def detect_login_sequences(events, threshold=5, window_minutes=10):
    """Find repeated failures followed by success for the same account and IP."""
    groups = defaultdict(list)
    for event in events:
        if event.get("event_type") in ("login_failure", "login_success"):
            groups[(event["user"], event["source_ip"])].append(event)
    alerts = []
    for (user, ip), records in groups.items():
        records.sort(key=lambda e: parse_time(e["timestamp"]))
        for index, event in enumerate(records):
            if event["event_type"] != "login_success":
                continue
            success_at = parse_time(event["timestamp"])
            failures = [
                r for r in records[:index]
                if r["event_type"] == "login_failure"
                and timedelta(0) <= success_at - parse_time(r["timestamp"]) <= timedelta(minutes=window_minutes)
            ]
            if len(failures) >= threshold:
                alerts.append({
                    "alert_id": f"SW-{len(alerts)+1:04d}",
                    "rule_id": "SW-AUTH-001",
                    "severity": "medium",
                    "user": user,
                    "source_ip": ip,
                    "failure_count": len(failures),
                    "success_time": event["timestamp"],
                    "first_failure_time": failures[0]["timestamp"],
                    "status": "needs_analyst_review",
                    "rationale": "Repeated authentication failures followed by success from same source",
                    "mitre_attack": "T1110 (Brute Force); investigate before attributing intent"
                })
    return alerts

def run(input_path, output_path):
    with open(input_path, newline="", encoding="utf-8") as handle:
        events = list(csv.DictReader(handle))
    alerts = detect_login_sequences(events)
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text(json.dumps({"synthetic_data": True, "events_analyzed": len(events), "alerts": alerts}, indent=2) + "\n", encoding="utf-8")
    return alerts

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/auth_events.csv")
    parser.add_argument("--output", default="outputs/alerts.json")
    args = parser.parse_args()
    print(f"{len(run(args.input, args.output))} alerts written to {args.output}")
