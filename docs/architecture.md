# Architecture and engineering notes

The v1.0 prototype uses CSV inputs, Python standard-library rule evaluation, and JSON outputs.

1. `data/auth_events.csv` provides synthetic authentication events.
2. `sentinelwatch/detect.py` groups events by account and source IP, then flags five failures followed by a successful login within ten minutes.
3. `data/accounts.csv` describes synthetic identity-control state; `sentinelwatch/controls.py` checks MFA, privileged access review, and inactive enabled accounts.
4. `sentinelwatch/report.py` correlates findings and produces a deterministic investigation packet.

No inbound networking, external AI model, cloud infrastructure, or automated account action exists. A production implementation would require validated schema, normalized identities, timestamp bounds, deduplication, ingestion protections, RBAC, monitoring, and robust testing.
