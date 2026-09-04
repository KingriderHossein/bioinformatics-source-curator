---
name: bioinformatics-source-curator
description: Build, verify, score, maintain, and audit a structured source registry for bioinformatics intelligence, then write approved sources, monitoring endpoints, review decisions, and run logs to Google Sheets. Use when the user asks to create or maintain a bioinformatics news/source database, discover journals/labs/researchers/tools/databases worth monitoring, verify source quality, build monitoring watchlists or query libraries, refresh sources on a daily/weekly/monthly cadence, or prepare an approved source handoff for Bioinformatics Intelligence Radar. Exclude preprint services from the approved Radar source set unless the user explicitly changes that policy.
---

# Bioinformatics Source Curator

Protocol version: 1.0.0

Maintain the source layer of a bioinformatics intelligence system. Curate **where to look**; do not replace the downstream Radar, which decides **what happened today**.

## Core invariants

1. Prefer primary and official sources. Use secondary pages only for discovery or context.
2. Separate `DISCOVERY` sources from `PRIMARY_EVIDENCE` sources. Never treat an index, search engine, or Google Scholar as the final evidence for a claim.
3. Exclude preprint services from the approved Radar source set. Do not register bioRxiv, medRxiv, arXiv, or similar services as approved scholarly monitoring sources unless the user explicitly changes the policy.
4. Verify each candidate before approval. A high score cannot override a failed hard gate.
5. Keep the registry stateful. Update an existing canonical record instead of creating duplicates.
6. Never rebuild the whole Google Sheet on a maintenance run. Read the live schema, append or patch only the necessary records, and preserve user-owned notes, formulas, validation, and formatting.
7. Use English-language official/international sources by default. Do not use Persian-language sources unless explicitly requested.
8. Do not invent counts, activity, release status, affiliations, monitoring endpoints, or verification dates.
9. Do not invoke another Skill from inside this Skill. Produce a handoff that an outer orchestrator can pass to Bioinformatics Intelligence Radar.
10. Treat source approval as **source-level trust**, not item-level scientific eligibility. Radar must still verify each paper's peer-review status and each event's primary evidence.

## Choose the run mode

Select one mode from the request and current registry state:

- `SHEET_SETUP`: create the workbook/tabs/schema when no registry exists.
- `BOOTSTRAP`: populate an empty or very small registry across the core taxonomy.
- `TARGETED_EXPANSION`: add sources for one or more specified domains.
- `DAILY_MAINTENANCE`: process review flags, broken/changed endpoints, high-priority source health, and pending records. Do not run broad source discovery by default.
- `WEEKLY_DISCOVERY`: discover and verify new source candidates using rotating domain coverage.
- `MONTHLY_AUDIT`: rescore active A/B sources, detect inactivity/duplication/scope drift, and downgrade or retire weak sources.
- `EXPORT_RADAR_HANDOFF`: materialize the current approved A/B source set for the Radar.

If the user says only "run the curator" and a Sheet already exists, use `DAILY_MAINTENANCE`. If no Sheet exists, use `SHEET_SETUP` followed by a small `BOOTSTRAP` pass.

## Required reference routing

Load references progressively:

- Read `references/taxonomy.md` for domain IDs, scope, and extension rules.
- Read `references/source-policy.md` before accepting or rejecting candidates.
- Read `references/search-playbook.md` for `BOOTSTRAP`, `TARGETED_EXPANSION`, or `WEEKLY_DISCOVERY`.
- Read `references/scoring.md` before assigning scores or priorities.
- Read `references/sheet-schema.md` before creating or editing the Google Sheet.
- Read `references/cadence.md` for scheduled/daily/weekly/monthly runs.
- Read `references/radar-handoff.md` for `EXPORT_RADAR_HANDOFF` or any Radar integration.
- Read `references/quality-gates.md` before finalizing a substantial run.

## Standard workflow

1. **Resolve state and mode.** Identify the target Sheet, current date, requested domains, and run mode.
2. **Read current registry state.** Inspect the exact tabs/headers needed. Do not assume the workbook is unchanged from a previous run.
3. **Discover only when the mode permits it.** Search broadly enough to create candidates, then resolve each candidate to an official/canonical source.
4. **Canonicalize and deduplicate.** Match by normalized official URL, organization/project identity, ORCID for researchers, and known aliases before creating a new ID.
5. **Apply hard gates.** Reject or queue uncertain records before scoring.
6. **Score eligible candidates.** Apply the five-dimension model in `references/scoring.md`.
7. **Decide disposition.** Use `ACTIVE`, `NEEDS_REVIEW`, `REJECTED`, `INACTIVE`, or `RETIRED` and record the reason.
8. **Write minimal changes.** Append new records and patch verified fields on existing records. Never erase manual notes merely because a new run does not reproduce them.
9. **Update monitoring state.** Record method, endpoint, cadence, last check, and errors where applicable.
10. **Update logs.** Write measurable counts and errors to `08_CHANGE_LOG` and `09_RUN_LOG`.
11. **Refresh Radar handoff when material changes occurred.** Export only approved active A/B sources; do not export preprint services.
12. **Run quality gates.** Fix failures or state the exact limitation.

## Candidate acceptance behavior

For every candidate, capture enough evidence to answer:

- What is this source?
- Which domain(s) does it cover?
- Is the URL official/canonical?
- Is its role discovery, monitoring, or primary evidence?
- Is it active or intentionally stable?
- How can it be monitored?
- Why is it relevant to working bioinformaticians?
- Is it suitable for the Radar handoff?

Do not approve a record from a search-result snippet alone. Follow the result to the official source.

## Researcher behavior

Build researcher watchlists from evidence such as official lab/group pages, institute staff pages, corresponding/senior authorship in relevant peer-reviewed literature, or maintainership of important resources. Use ORCID and official institutional profiles for identity when available.

Use Google Scholar only as a monitoring/discovery channel. Do not treat Scholar metrics or a Scholar profile as the authoritative source for affiliation or scientific claims.

## Google Sheets behavior

When the Google Sheets connector is available, use the workbook as the canonical operational state. Follow `references/sheet-schema.md` exactly for new workbooks. For existing workbooks, preserve compatible user extensions and do not silently rename or remove columns.

If the Sheets connector is unavailable, return a dry-run table of proposed mutations with `action`, `target_tab`, `record_id`, `field`, `old_value`, `new_value`, and `evidence`; never claim that the Sheet was updated.

## Daily versus discovery behavior

Do not perform full internet-wide source discovery every day. Use:

- daily = maintenance and exception handling,
- weekly = incremental discovery,
- monthly = deep audit and rescoring.

The automation/orchestrator owns scheduling. This Skill owns what each run does.

## Output contract

For an interactive run, return a concise Persian operational summary unless another language is requested:

- `Run mode`
- `Domains touched`
- `Candidates reviewed`
- `Added`
- `Updated`
- `Rejected`
- `Needs review`
- `Radar handoff refreshed: YES/NO`
- `Errors or coverage limits`

Report only counts actually observed during the run.

## Repository compatibility

Keep compatibility with Bioinformatics Intelligence Radar protocol 2.5.x unless the repository shows a newer version. Before making a material integration change, inspect the current Radar `SKILL.md`/CHANGELOG when GitHub access is available and adapt the handoff rather than assuming an older contract.
