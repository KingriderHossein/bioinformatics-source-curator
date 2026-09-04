# Bootstrap Demo — 2026-09-04

This document records a real end-to-end Source Curator bootstrap run. It is an auditable example, not the live registry state.

## Simulated user prompt

> Create a new Google Sheets source registry for the bioinformatics Radar. Bootstrap high-value sources for D01 Genomics & Variant Analysis, D10 Systems Biology & Multi-omics, and D12 Workflow Engineering & Reproducibility. Use official English-language sources only, exclude preprints, score and deduplicate candidates, create monitoring records, log all mutations, and refresh the Radar handoff.

## Run summary

| Field | Value |
|---|---|
| Run mode | `SHEET_SETUP + BOOTSTRAP` |
| Domains touched | `D01, D10, D12` |
| Candidates reviewed | `7` |
| Added | `6` |
| Updated | `0` |
| Rejected | `1` |
| Needs review | `1` |
| Errors | `0` |
| Radar handoff refreshed | `YES` |

## Active A-priority sources exported to the Radar handoff

1. GENCODE Human Release History — D01 — score 23/25
2. Reactome Content Service — D10 — score 25/25
3. COBRApy Releases — D10 — score 24/25
4. Nextflow Releases — D12 — score 25/25
5. Snakemake Releases — D12 — score 25/25

See `registry-active-demo.csv` and `radar-handoff-demo.csv` for the versioned demonstration records.

## Policy outcomes exercised

### BioModels — `NEEDS_REVIEW`

The legacy EMBL-EBI BioModels endpoint reported a migration/read-only state and directed API users toward the new BioModels service. Because the canonical monitoring endpoint was not treated as fully re-verified during the run, the candidate was not approved for the Radar handoff.

Evidence checked during the run:
- https://www.ebi.ac.uk/biomodels/
- https://www.biomodels.org

### bioRxiv — `REJECTED`

bioRxiv was used as a policy-test candidate. It is a preprint service and therefore fails the default `EXCLUDE_FROM_RADAR` hard gate. It must not appear in the approved Radar source handoff under protocol 1.0.0.

Evidence:
- https://www.biorxiv.org/

## Radar compatibility

The live Bioinformatics Intelligence Radar repository was checked during this run and was at protocol 2.5.0. Its item-level peer-review gate remains stricter than source-level approval. Source Curator approval therefore does not prove that an individual scholarly item is peer-reviewed.

Radar repository:
- https://github.com/KingriderHossein/Bioinformatics-Intelligence-Radar

## State ownership

- **Google Sheets:** canonical live operational registry, review queue, monitoring state, run logs, and current materialized Radar handoff.
- **GitHub:** versioned protocol, default config, validation code, CI, schemas/policies, and non-authoritative examples/snapshots.

Do not turn the committed example files into a second live registry.
