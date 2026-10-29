# Cloud extension — Microsoft Sentinel + Entra ID

This folder contains **Azure-ready KQL hunting queries**, not evidence of a deployed cloud service.

## Prerequisites
- An Azure subscription and a Log Analytics workspace with Microsoft Sentinel enabled.
- Authorization to access Microsoft Entra sign-in and audit logs.
- Appropriate log connectors and ingestion permissions.
- A defined budget and data retention policy. Cloud ingestion, retention, and Sentinel usage may incur charges; review current Azure pricing before enabling resources.

## Deployment workflow
1. Create or select an isolated, authorized test tenant/subscription and workspace.
2. Enable Microsoft Sentinel on the workspace, then configure Entra sign-in and audit log ingestion according to Microsoft's current connector documentation.
3. Confirm the `SigninLogs` and `AuditLogs` tables contain authorized **lab-generated** events. If no events are present, do not claim a successful live query.
4. Run `sentinel/signin-failures-then-success.kql` as a hunting query. Review results, false positives, clock skew, duplicate events, and permissions.
5. Run `sentinel/privileged-role-activity.kql` to review privileged identity changes.
6. Document query execution time, anonymized evidence, false-positive analysis, analyst decision, and cost. Export **sanitized** screenshots only.
7. Consider a scheduled analytic rule only after validating it on appropriately labelled test data and obtaining authorization.

## Data handling and safe AI use
Do not commit tenant IDs, account identifiers, tokens, private IP inventories, customer data, or raw production logs. Do not upload sensitive event logs to a public AI chatbot. Treat log fields as untrusted content and keep human approval for response actions.

## Important implementation notes
- `ResultType == "0"` is used as the successful Entra sign-in result; validate against the connector schema in your tenant.
- The sign-in query joins failures and successes by **UserId and IPAddress** within ten minutes; it is a candidate detection that may produce benign matches or duplicate matches.
- This is a **hunting query**, not a tuned production alert, and is not equivalent to endpoint EDR coverage.
- Azure configuration has **not** been performed through this repository.
