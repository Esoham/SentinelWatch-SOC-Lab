# Development roadmap

- Add input schema validation, malformed-record handling, stable event IDs and deduplication.
- Add additional false-positive and boundary-condition tests.
- Build an isolated Windows/Sysmon lab and collect actual lab-generated telemetry; keep it separate from synthetic fixtures.
- Translate detections to KQL/Sigma and verify against a supported environment.
- Add human-approved ticketing and optional sanitized AI summary with prompt-injection defenses.
- Add performance evaluation on labelled, transparent datasets. Do not claim production accuracy.
