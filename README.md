# SentinelWatch — Security Operations & Risk Intelligence

**Defensive portfolio lab | Python 3.10+ | Standard library only | Synthetic data**

## Business question
How can a Tier 1 analyst identify a suspicious login sequence, correlate it with identity-control weaknesses, and prepare an evidence-based escalation packet without prematurely declaring a compromise?

## Security, development, and business
- **Security:** Five failed logins followed by success from the same user/IP within ten minutes; human-reviewed triage and escalation.
- **Development:** Modular Python, deterministic JSON reporting, automated tests, and documented limitations.
- **Business:** MFA and privileged-access review gaps, actionable control findings, and recommendations for accountable owners.

## Quick start
Run from the repository root:
```bash
python -m unittest discover -s tests -v
python -m sentinelwatch.detect --input data/auth_events.csv --output outputs/alerts.json
python -m sentinelwatch.report --auth data/auth_events.csv --accounts data/accounts.csv --output outputs/investigation.json
```

## Verified local demo
Nine fictional authentication events generated one triage alert. Four fictional accounts generated three identity-control findings; two correlate to the alerted account. All eight local unit tests passed on the initial build. These counts are **not** estimates of precision, recall, production performance, or demonstrated incidents.

## Documentation
See [architecture](docs/architecture.md), [incident runbook](docs/incident-runbook.md), [business risk assessment](docs/business-risk-assessment.md), and [threat model](docs/threat-model.md).

## Limitations
No real telemetry, SIEM, EDR, cloud deployment, AI API, account disablement, or automated response is implemented. Source IPs are documentation-only ranges. The identity join uses a synthetic username, not a production-ready principal ID. All decisions require human investigation.

[Interactive portfolio case study](https://esoham.github.io/projects/sentinelwatch.html)
