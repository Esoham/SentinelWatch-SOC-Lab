# Threat model — local prototype

**Assets:** synthetic authentication and account records, detection logic, and report integrity.

**Trust boundaries:** CSV inputs are untrusted; output reports may be read by analysts. This project does not connect to live identity providers or security tools.

**Potential failures:** malformed timestamps or fields causing errors, log injection, inaccurate identity matches, duplicate alerts, misleading correlations, and sensitive data leakage if real logs were substituted.

**Controls in this version:** public synthetic records only, no embedded secrets, deterministic read-only analysis, explicit human review.

**Not yet implemented:** complete schema validation, durable event IDs and deduplication, permissions, authenticated ingestion, and production logging.
