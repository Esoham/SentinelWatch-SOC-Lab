import unittest
from sentinelwatch.detect import detect_login_sequences

class DetectionTests(unittest.TestCase):
    def test_detects_five_failures_then_success(self):
        records = [{"timestamp": f"2026-10-20T08:0{i}:00Z", "user": "alex", "source_ip": "192.0.2.1", "event_type": "login_failure"} for i in range(5)]
        records.append({"timestamp": "2026-10-20T08:05:00Z", "user": "alex", "source_ip": "192.0.2.1", "event_type": "login_success"})
        self.assertEqual(len(detect_login_sequences(records)), 1)

    def test_does_not_mix_accounts_or_sources(self):
        records = [{"timestamp": f"2026-10-20T08:0{i}:00Z", "user": "alex", "source_ip": "192.0.2.1", "event_type": "login_failure"} for i in range(5)]
        records.append({"timestamp": "2026-10-20T08:05:00Z", "user": "alex", "source_ip": "192.0.2.2", "event_type": "login_success"})
        self.assertEqual(detect_login_sequences(records), [])

    def test_old_failures_do_not_trigger(self):
        records = [{"timestamp": f"2026-10-20T07:0{i}:00Z", "user": "alex", "source_ip": "192.0.2.1", "event_type": "login_failure"} for i in range(5)]
        records.append({"timestamp": "2026-10-20T08:05:00Z", "user": "alex", "source_ip": "192.0.2.1", "event_type": "login_success"})
        self.assertEqual(detect_login_sequences(records), [])
if __name__ == "__main__":
    unittest.main()
