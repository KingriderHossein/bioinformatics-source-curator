# Google Sheets Schema

Schema version: 1.0.0

The workbook is operational state, not a decorative report. Use these tabs for new workbooks.

## 00_CONFIG
Columns: `key`, `value`, `description`, `updated_at`

Seed keys:
- `protocol_version = 1.0.0`
- `preprint_policy = EXCLUDE_FROM_RADAR`
- `default_source_language = ENGLISH_INTERNATIONAL`
- `radar_priority = A,B`
- `daily_mode = DAILY_MAINTENANCE`
- `weekly_mode = WEEKLY_DISCOVERY`
- `monthly_mode = MONTHLY_AUDIT`

## 01_TAXONOMY
Columns:
`domain_id`, `domain_name`, `scope`, `search_synonyms`, `status`, `owner`, `last_reviewed`

## 02_SOURCE_REGISTRY
Columns:
`source_id`, `domain_id`, `subdomain`, `source_type`, `source_name`, `organization`, `official_url`, `source_role`, `verification_evidence_url`, `peer_review_scope`, `monitoring_method`, `monitoring_endpoint`, `cadence`, `authority_score`, `relevance_score`, `activity_score`, `primariness_score`, `monitorability_score`, `total_score`, `priority`, `approved_for_radar`, `status`, `last_verified`, `last_checked`, `owner`, `notes`

Allowed `source_type` values:
`JOURNAL`, `INDEX`, `INSTITUTE`, `LAB`, `DATABASE`, `SOFTWARE`, `DATA_REPOSITORY`, `STANDARDS_BODY`, `OFFICIAL_NEWS`, `OTHER`

Allowed `source_role` values:
`PRIMARY_EVIDENCE`, `DISCOVERY`, `MONITORING`, `CONTEXT`

Allowed `peer_review_scope` values:
`YES`, `MIXED`, `NO`, `NOT_APPLICABLE`, `UNKNOWN`

Allowed `status` values:
`ACTIVE`, `NEEDS_REVIEW`, `REJECTED`, `INACTIVE`, `RETIRED`

## 03_RESEARCHERS
Columns:
`researcher_id`, `domain_id`, `name`, `affiliation`, `official_profile_url`, `lab_url`, `orcid_url`, `scholar_url`, `monitoring_method`, `monitoring_endpoint`, `priority`, `status`, `last_verified`, `owner`, `notes`

## 04_MONITORING
Columns:
`monitor_id`, `target_kind`, `target_id`, `method`, `endpoint`, `cadence`, `last_checked`, `last_success`, `status`, `consecutive_errors`, `notes`

`target_kind` is `SOURCE` or `RESEARCHER`.

## 05_QUERY_LIBRARY
Columns:
`query_id`, `domain_id`, `purpose`, `query_text`, `target_system`, `cadence`, `status`, `last_tested`, `notes`

Purpose examples: `SOURCE_DISCOVERY`, `LITERATURE_ALERT`, `RELEASE_CHECK`, `INFRASTRUCTURE_CHANGE`.

## 06_REVIEW_QUEUE
Columns:
`queue_id`, `record_kind`, `record_id_or_candidate`, `reason`, `evidence_url`, `proposed_action`, `assigned_to`, `status`, `created_at`, `resolved_at`, `resolution_notes`

## 07_REJECTED
Columns:
`rejected_id`, `domain_id`, `candidate_name`, `candidate_url`, `candidate_type`, `reason_code`, `reason`, `checked_at`, `checked_by`, `notes`

## 08_CHANGE_LOG
Columns:
`change_id`, `run_id`, `timestamp`, `record_kind`, `record_id`, `action`, `field`, `old_value`, `new_value`, `evidence_url`, `actor`

Actions: `ADD`, `UPDATE`, `DOWNGRADE`, `UPGRADE`, `REJECT`, `RETIRE`, `RESTORE`.

## 09_RUN_LOG
Columns:
`run_id`, `run_mode`, `started_at`, `completed_at`, `domains_touched`, `candidates_reviewed`, `added`, `updated`, `rejected`, `needs_review`, `errors`, `radar_handoff_refreshed`, `notes`

Record only measured counts.

## 10_RADAR_SOURCES
Columns:
`target_id`, `domain_id`, `source_type`, `source_name`, `official_url`, `source_role`, `monitoring_method`, `monitoring_endpoint`, `priority`, `last_verified`

This is a materialized handoff, not a second source of truth. Rebuild it from active approved A/B records after material changes.

## IDs

Use zero-padded sequential IDs within each table when the Sheet is the only shared writer:
- `SRC-000001`
- `RES-000001`
- `MON-000001`
- `QRY-000001`
- `QUE-000001`
- `REJ-000001`
- `CHG-000001`
- `RUN-YYYYMMDD-001`

Before allocating a new sequential ID, read the relevant ID column to avoid collisions.

## Write safety

- Never overwrite an entire tab during maintenance just to simplify a patch.
- Preserve user-added compatible columns to the right of the canonical schema.
- Do not erase manual `notes`/`owner` fields unless the user explicitly asks.
- Re-read target rows before updating if another writer may have changed them.
- Prefer append for logs and patch for registry records.
