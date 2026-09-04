# Bioinformatics Source Curator

A reusable ChatGPT Skill for building and maintaining a verified, monitorable source registry for bioinformatics intelligence.

## What it owns

- source taxonomy and source discovery
- official/canonical source verification
- source scoring and priority
- monitoring methods/endpoints
- Google Sheets registry state
- review/rejection/change/run logs
- approved-source handoff to Bioinformatics Intelligence Radar

## What it does not own

It does not replace the Bioinformatics Intelligence Radar. The Curator answers **where should we look?**; the Radar answers **what happened and why does it matter?**

## State ownership

The live Google Sheet is the canonical operational state. GitHub is used for version-controlled protocol files, policies, schemas, default configuration, validation code, CI, and non-authoritative examples.

Do not maintain an independent live registry in GitHub. This avoids two competing sources of truth.

## Default cadence

- Daily: maintenance only
- Weekly: incremental source discovery
- Monthly: deep audit and rescoring

## Scientific policy

Preprint services are excluded from the approved Radar source set by default. Individual scholarly items remain subject to the Radar's item-level peer-review verification.

## Version-controlled operational assets

- `config/defaults.yaml` — reference defaults corresponding to `00_CONFIG`; not live state.
- `scripts/validate_registry_csv.py` — deterministic validation for exported registry CSV files.
- `.github/workflows/validate-registry.yml` — CI validation of the committed active-registry example.
- `examples/registry-active-demo.csv` — validated active A-priority registry snapshot from the 2026-09-04 demonstration run.
- `examples/radar-handoff-demo.csv` — corresponding materialized Radar handoff example.
- `examples/bootstrap-demo-2026-09-04.md` — end-to-end run record including rejection and review-queue cases.

## Demo

The repository includes a complete bootstrap example covering D01 Genomics & Variant Analysis, D10 Systems Biology & Multi-omics, and D12 Workflow Engineering & Reproducibility. It demonstrates:

- source verification and scoring;
- approved A-priority sources;
- BioModels routed to `NEEDS_REVIEW` during endpoint migration;
- bioRxiv rejected under the preprint policy;
- Radar 2.5.0 compatibility checking;
- materialized Radar handoff generation.

## Protocol

Current protocol: **1.0.0**
