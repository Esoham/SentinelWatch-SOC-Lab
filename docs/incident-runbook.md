# Tier 1 incident runbook — SW-AUTH-001

1. Verify alert rule, timestamps, account, source IP, and raw source event references.
2. Check whether the sequence is explained by legitimate activity, password resets, or a known system.
3. Validate MFA state and look for independent identity, endpoint, and session evidence.
4. Record facts, unknowns, severity rationale, and investigation notes.
5. Escalate to an authorized responder under local policy if compromise is suspected.
6. Request human approval for containment; do not disable users or systems automatically.
7. Close with a documented disposition and any follow-up control or detection changes.

**Important:** five failures followed by a success may indicate guessing, but it is not proof of brute-force compromise.
