# SentinelWatch + Wazuh — Windows local lab

**Status: installation plan only. Not deployed or validated on the author's laptop.**

## Goal
Monitor a Windows lab endpoint using the Wazuh agent and a self-hosted Wazuh single-node stack running in Docker Desktop with WSL 2. Produce authorized lab events, triage alerts, and record sanitized evidence in SentinelWatch.

## Phase 0 — prerequisites (PowerShell, read-only)
```powershell
Get-CimInstance Win32_ComputerSystem | Select-Object Manufacturer,Model,@{Name="RAM_GB";Expression={[math]::Round($_.TotalPhysicalMemory/1GB,1)}}
Get-CimInstance Win32_Processor | Select-Object Name,NumberOfCores,NumberOfLogicalProcessors
Get-PSDrive C | Select-Object Name,@{Name="Free_GB";Expression={[math]::Round($_.Free/1GB,1)}}
wsl --status
Get-CimInstance Win32_OperatingSystem | Select-Object Caption,Version
```
Do not paste device serial numbers, personal usernames, private addresses, or other sensitive information into public issues.

## Deployment choice
The [official Wazuh Docker deployment guide](https://documentation.wazuh.com/current/deployment-options/docker/wazuh-container.html) supports a single-node manager/indexer/dashboard stack on Windows with Docker Desktop and WSL 2. It lists at least four CPU cores, 8 GB of memory **for the Docker host**, and 50 GB of disk. Prefer 16 GB or more total laptop RAM to leave Windows usable.

If the machine does not have sufficient spare RAM or disk, **do not install the full stack**. Instead use the existing local Python lab, a lighter VM on another machine, or a separate authorized host.

## Phase 1 — install (only after verifying hardware)
1. Check Windows virtualization and WSL 2 support using Microsoft's current documentation.
2. Install Docker Desktop from the official site and use the WSL 2 Linux-container backend.
3. Follow the current Wazuh single-node Docker instructions; pin a documented release tag rather than using an unreviewed latest branch.
4. Configure the WSL 2 kernel `vm.max_map_count` as required by the Wazuh indexer.
5. Generate the required certificates, configure unique strong passwords, and restrict exposed services to localhost or a trusted lab network.
6. Verify all three containers are healthy before installing the Windows agent.
7. Install the Windows agent from the official Wazuh guide and enroll it in the local manager.

## Phase 2 — validation
- Confirm the agent is connected and reports Windows security telemetry.
- Generate only benign, authorized test events on your own test machine/account.
- Record Wazuh rule ID, event timestamp, event source, analyst reasoning, and false-positive checks.
- Keep raw host logs, access tokens, certificates, and credentials out of GitHub.
- Export redacted screenshots and an incident narrative; distinguish observed evidence from simulated findings.

## Phase 3 — engineering
- Add and test a custom Wazuh detection rule in an isolated lab.
- Document rule validation, coverage, gaps, and human-approved escalation.
- Link findings to business controls (MFA, least privilege, review cadence).
- Publish a reproducible lab write-up without publishing sensitive logs.

## Boundaries
No cloud resources are needed for this local Wazuh lab. Wazuh software is open source; host resources, electricity, and any optional cloud services are separate costs. No production monitoring or automated containment is claimed.

## Sources
- [Wazuh Docker deployment](https://documentation.wazuh.com/current/deployment-options/docker/wazuh-container.html)
- [Wazuh Windows agent installation](https://documentation.wazuh.com/current/installation-guide/wazuh-agent/wazuh-agent-package-windows.html)
- [Docker Desktop on Windows](https://docs.docker.com/desktop/setup/install/windows-install/)
