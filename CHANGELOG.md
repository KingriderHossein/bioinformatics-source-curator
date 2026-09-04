# Changelog

## 1.0.0 - 2026-09-04

- Initial production-ready Source Curator protocol.
- Added 13-domain core bioinformatics taxonomy.
- Added source hierarchy, hard gates, five-dimension scoring, and A/B/C priorities.
- Added daily maintenance, weekly discovery, and monthly audit modes.
- Added Google Sheets operational schema with registry, monitoring, review, rejection, change, run-log, and Radar handoff tabs.
- Added explicit exclusion of preprint services from the approved Radar source handoff.
- Added compatibility boundary with Bioinformatics Intelligence Radar 2.5.x.
- Added deterministic CSV registry validator.
- Added version-controlled default configuration under `config/defaults.yaml` while keeping Google Sheets as canonical live state.
- Added an audited end-to-end bootstrap demonstration from 2026-09-04 with active registry and Radar handoff examples.
- Added explicit demonstration cases for BioModels `NEEDS_REVIEW` during endpoint migration and bioRxiv rejection under the preprint policy.
- Added GitHub Actions CI to validate the committed active-registry example with the protocol validator.
- Documented the state-ownership boundary so GitHub examples cannot be mistaken for a second live registry.
