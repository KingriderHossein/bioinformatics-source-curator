# Source Scoring

Scoring version: 1.0.0

Apply hard gates before scoring. Scores rank eligible sources; they never rescue an ineligible source.

Score each dimension from 0 to 5.

## 1. Authority
- 5: official project, institution, journal/publisher, recognized index, or canonical database
- 4: official subproject/group with clear institutional ownership
- 3: reputable but secondary organization or community resource
- 2: weak authority or unclear governance
- 1: informal/unverified source
- 0: deceptive, anonymous, or unusable

## 2. Domain relevance
- 5: core source for the assigned domain
- 4: frequent high-value coverage
- 3: useful but broad/mixed coverage
- 2: occasional relevance
- 1: rare/incidental relevance
- 0: out of scope

## 3. Activity / currency
Judge relative to the source type. Stable reference resources may update less frequently than software.
- 5: clearly active with recent expected updates
- 4: active, normal cadence
- 3: slower but still maintained/useful
- 2: activity uncertain or sparse
- 1: likely dormant
- 0: dead/retired without archival value

## 4. Primariness
- 5: direct official evidence for the events it reports
- 4: official project/institution feed very close to the event
- 3: discovery index or authoritative metadata source
- 2: secondary summary
- 1: aggregator/repost
- 0: unverifiable

## 5. Monitorability
- 5: stable API, RSS/Atom, GitHub Releases, structured changelog, or equivalent machine-friendly endpoint
- 4: reliable email alert or stable official release/news page
- 3: searchable official page with consistent structure
- 2: manual monitoring is possible but fragile
- 1: social-only or highly unstable endpoint
- 0: no practical monitoring path

## Total and priority

`total_score = Authority + Relevance + Activity + Primariness + Monitorability`

- `A`: 21-25
- `B`: 16-20
- `C`: 11-15
- `REJECT`: 0-10

A hard-gate failure sets `status=REJECTED` or `NEEDS_REVIEW` regardless of total score.

## Radar eligibility

Set `approved_for_radar=TRUE` only when all are true:

- status is `ACTIVE`;
- priority is `A` or `B`;
- source role is useful for discovery/monitoring/primary evidence;
- source is not a preprint service under the current policy;
- canonical endpoint and monitoring path are verified.
