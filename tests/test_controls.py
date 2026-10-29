import unittest
from sentinelwatch.controls import assess_controls
from sentinelwatch.report import build_report

class ControlTests(unittest.TestCase):
    def test_mfa_gap(self):
        a = {"user":"test","mfa_enabled":"false","privileged":"false","access_review_current":"true","active":"true","access_enabled":"true"}
        self.assertEqual([x["control"] for x in assess_controls([a])], ["MFA_DISABLED"])

    def test_privileged_review(self):
        a = {"user":"test","mfa_enabled":"true","privileged":"true","access_review_current":"false","active":"true","access_enabled":"true"}
        self.assertEqual(assess_controls([a])[0]["control"], "PRIVILEGED_REVIEW_OVERDUE")

    def test_inactive_account_enabled(self):
        a = {"user":"test","mfa_enabled":"true","privileged":"false","access_review_current":"true","active":"false","access_enabled":"true"}
        self.assertEqual(assess_controls([a])[0]["control"], "INACTIVE_ACCOUNT_ENABLED")

    def test_no_findings(self):
        a = {"user":"test","mfa_enabled":"true","privileged":"false","access_review_current":"true","active":"true","access_enabled":"true"}
        self.assertEqual(assess_controls([a]), [])

    def test_correlates_alert_and_control(self):
        report = build_report("data/auth_events.csv", "data/accounts.csv")
        self.assertEqual(len(report["alerts"]), 1)
        self.assertEqual({f["user"] for f in report["correlated_findings"]}, {"alex"})
