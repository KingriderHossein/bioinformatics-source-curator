# Cadence and Scheduling Contract

Scheduling belongs to the outer automation/orchestrator. This Skill defines run behavior.

## Daily: DAILY_MAINTENANCE

Default daily work:
1. read unresolved `06_REVIEW_QUEUE` items due for attention;
2. check broken/changed monitoring endpoints already flagged;
3. check Priority A sources whose `last_checked` is due;
4. verify pending affiliations or canonical URLs when evidence is available;
5. update status/last_checked only when actually checked;
6. append change/run logs;
7. refresh `10_RADAR_SOURCES` only if approved source state changed.

Do not run broad source discovery by default.

## Weekly: WEEKLY_DISCOVERY

Rotate across domains so coverage remains balanced. For selected domains:
1. discover new candidates using `search-playbook.md`;
2. verify and deduplicate;
3. score eligible candidates;
4. add A/B candidates to active registry;
5. send uncertain candidates to review queue;
6. record rejected candidates and reasons;
7. refresh Radar handoff when needed.

## Monthly: MONTHLY_AUDIT

Audit all active A/B sources and a sample of C sources:
- canonical URL still valid;
- organization/project still active;
- monitoring endpoint still works;
- scope still relevant;
- score still justified;
- duplicates/renames/mergers;
- inactive or superseded resources;
- taxonomy coverage gaps.

Downgrade or retire with evidence. Do not delete historical records.

## Quarterly or on demand

Review taxonomy and query library. Add new domains only under the taxonomy extension rule.
