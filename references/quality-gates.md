# Quality Gates

Before finalizing a substantial run, confirm:

## Identity and evidence
- every added/updated source has an official/canonical URL or is explicitly `NEEDS_REVIEW`;
- verification evidence supports the recorded organization, source role, and status;
- no final decision depends only on a search snippet or generic listicle;
- researcher identity is not inferred from name matching alone when ambiguity exists.

## Policy
- no preprint service appears in the approved Radar source handoff under the default policy;
- discovery sources are not mislabeled as primary evidence;
- Persian-language sources were not used unless explicitly requested;
- hard-gate failures were not rescued by scores.

## Registry integrity
- new records were deduplicated against canonical URLs/names/ORCIDs;
- IDs are unique;
- scores sum correctly and priority matches thresholds;
- manual notes and compatible user extensions were preserved;
- historical rejected/retired records were not silently deleted.

## Monitoring
- approved A/B sources have a practical monitoring method;
- monitoring endpoint is official/canonical when possible;
- `last_checked`/`last_verified` dates reflect actual checks, not the current date by default.

## Logs and handoff
- run counts are measured, not estimated;
- material mutations have change-log entries;
- Radar handoff contains only active approved A/B sources;
- source approval is not described as item-level peer-review verification.
