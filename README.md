# SentinelWatch — Security Operations & Risk Intelligence

**Defensive portfolio lab | Python 3.10+ | Wazuh 4.14.1 | Docker / WSL 2 | Synthetic detection dataset**

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

## Live SIEM infrastructure milestone (October 29, 2026)

Deployed **Wazuh 4.14.1 single-node** on a Windows HP Envy using **Docker Desktop with WSL 2**. The manager, indexer, and dashboard containers were confirmed `Up` using `docker compose ps`, and the dashboard login was reached successfully. Generated local TLS certificates and configured a Compose override using `ports: !override` so published host ports **443, 9200, 1514, 1515, 514/UDP, and 55000** bind to **127.0.0.1** rather than all host interfaces. This is a **local lab deployment**, not a public service or production system.

**Not yet completed:** default-credential rotation, Windows agent enrollment, ingestion of real endpoint telemetry, validated Wazuh alert rules, and sanitized investigation screenshots. The Python dashboard remains a **separate synthetic demonstration**; it is not connected to Wazuh. See [Windows Wazuh lab setup](docs/wazuh-windows-lab.md). **Never commit generated certificates, private keys, passwords, or raw personal event logs.**

## Interactive dashboard and cloud-ready queries
- [Open the interactive SOC dashboard](https://esoham.github.io/projects/sentinelwatch-console.html) — fictional data, browser-side filtering, investigation and control findings.
- [Microsoft Sentinel KQL hunting queries](cloud/sentinel/) — sign-in correlation and privileged-role audit review.
- [Cloud setup and cost/safety guidance](cloud/README.md) — requires a separately authorized Azure environment. Queries are published but **have not been executed in a live tenant**.

## Documentation
See [architecture](docs/architecture.md), [incident runbook](docs/incident-runbook.md), [business risk assessment](docs/business-risk-assessment.md), and [threat model](docs/threat-model.md).

## Limitations
A local Wazuh SIEM stack has been launched, but no endpoint agent, verified live telemetry, EDR integration, cloud deployment, AI API, account disablement, or automated response is implemented. Cloud KQL is provided as unvalidated hunting-query examples. Source IPs are documentation-only ranges. The identity join uses a synthetic username, not a production-ready principal ID. All decisions require human investigation.

[Interactive portfolio case study](https://esoham.github.io/projects/sentinelwatch.html)
