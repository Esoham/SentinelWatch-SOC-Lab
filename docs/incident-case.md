# Investigation case SW-0001 (synthetic)

**Observation:** Five authentication failures for user `alex` from `192.0.2.10` between 08:00 and 08:04 UTC, followed by a success at 08:05 UTC.

**Rule:** SW-AUTH-001; alert severity medium; status needs analyst review.

**Related control findings:** MFA disabled and privileged-access review overdue. These data are fictional and linked on synthetic username only.

**Assessment:** suspicious sequence requiring investigation, not a confirmed incident.

**Next steps:** validate logs, gather session and MFA evidence, confirm asset owner and permitted activity, and escalate according to documented procedures.
