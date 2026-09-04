# Bioinformatics Intelligence Radar Handoff

Contract version: 1.0.0
Compatible baseline: Bioinformatics Intelligence Radar protocol 2.5.x

## Ownership

- Source Curator owns source discovery, source-level verification, scoring, monitoring metadata, registry state, and `10_RADAR_SOURCES`.
- Radar owns item discovery/eligibility, peer-review verification for scholarly papers, event verification, deduplication, ranking, and reporting.
- The outer orchestrator owns scheduling and transfer between them.
- Source Curator must not invoke Radar directly.

## Export filter

Include a registry source in `10_RADAR_SOURCES` only when:
- `status=ACTIVE`;
- `approved_for_radar=TRUE`;
- `priority` is `A` or `B`;
- canonical URL and monitoring endpoint are verified;
- the source is not a preprint service under the current policy.

## Critical boundary

Source-level approval never proves that an individual paper is peer-reviewed. Journals and indexes can contain mixed item types. Radar must apply its current item-level peer-review policy before exposing scholarly items.

Likewise, an approved software/database source does not prove that every observed change is important; Radar verifies the concrete release/change against the primary source.

## Handoff fields

Use:
`target_id`, `domain_id`, `source_type`, `source_name`, `official_url`, `source_role`, `monitoring_method`, `monitoring_endpoint`, `priority`, `last_verified`.

Do not pass source scores as scientific evidence. Scores are curation metadata only.

## Compatibility check

When GitHub access is available and a material integration change is requested, read the current `KingriderHossein/Bioinformatics-Intelligence-Radar` `SKILL.md` and CHANGELOG/version first. If the Radar contract is newer than 2.5.x, adapt this handoff conservatively and preserve Radar's stricter eligibility rules.
