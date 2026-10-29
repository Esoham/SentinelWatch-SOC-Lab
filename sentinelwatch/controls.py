"""Read-only assessment of fictional identity control records."""
import csv

def assess_controls(accounts):
    findings = []
    for account in accounts:
        user = account["user"]
        checks = [
            (account["mfa_enabled"].lower() != "true", "MFA_DISABLED", "high", "Enable and verify MFA for this account"),
            (account["privileged"].lower() == "true" and account["access_review_current"].lower() != "true", "PRIVILEGED_REVIEW_OVERDUE", "high", "Have owner review privileged access"),
            (account["active"].lower() != "true" and account["access_enabled"].lower() == "true", "INACTIVE_ACCOUNT_ENABLED", "medium", "Review account disablement with owner"),
        ]
        for triggered, control, severity, recommendation in checks:
            if triggered:
                findings.append({"user": user, "control": control, "severity": severity, "recommendation": recommendation, "status": "requires_owner_review"})
    return findings

def load_accounts(path):
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))
