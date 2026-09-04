# Source Policy

Policy version: 1.0.0

## Roles

Assign one primary role to each source:

- `PRIMARY_EVIDENCE`: closest official source for an event/change.
- `DISCOVERY`: index/search/feed used to find candidate items.
- `MONITORING`: stable endpoint used to detect new activity.
- `CONTEXT`: useful explanatory source but not final authority.

A source can have supporting secondary roles in `notes`, but do not blur the primary role.

## Preferred hierarchy

### Scholarly literature
1. Peer-reviewed journal/publisher article page for final evidence.
2. PubMed or Europe PMC for discovery, metadata, and alerts.
3. Journal/publisher issue feeds for monitoring.
4. Institutional press release for context only when it links to the underlying work.

Do not approve preprint services for the Radar source handoff. A journal may publish mixed content; record `peer_review_scope=MIXED` when individual item types still require downstream verification.

### Software
1. Official repository release page/tag.
2. Official documentation/release notes.
3. Official package registry or project site.
4. Issue tracker only for a specific verified change.

### Databases and infrastructure
1. Official service/resource site.
2. Official release notes, status page, API docs, migration notice, schema docs, or changelog.
3. Host institution announcement when it links to the underlying change.

### Labs and institutes
1. Official institute/university/lab page.
2. Official publication/news feed.
3. Verified institutional researcher page.

### Researchers
1. Official institutional profile or lab page.
2. ORCID for identity and publication linkage.
3. Google Scholar for discovery/alerts only.

## Hard reject / review conditions

Reject or mark `NEEDS_REVIEW` when any applies:

- no official/canonical identity can be established;
- source is a preprint service and the approved Radar policy excludes preprints;
- source exists only as a listicle, repost, scraped mirror, or generic aggregator;
- source role cannot be stated clearly;
- duplicate of an existing canonical record;
- domain relevance is weak or incidental;
- activity/status cannot be verified and the resource is not intentionally stable;
- monitoring endpoint points to an unofficial mirror when an official endpoint exists.

## Language policy

Use English-language official/international sources by default. Do not use Persian-language sources unless explicitly requested.
