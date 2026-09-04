# Discovery Search Playbook

Use this file only for `BOOTSTRAP`, `TARGETED_EXPANSION`, and `WEEKLY_DISCOVERY`.

## Pass A: scholarly ecosystem

For each selected domain, identify:
- peer-reviewed journals or publisher sections with sustained coverage;
- PubMed/Europe PMC query patterns or alerts;
- official journal issue/early-online feeds when useful.

Resolve candidates to publisher/journal pages. Do not use a ranking list as final evidence.

## Pass B: institutes, labs, and researchers

Start from official research institutes, universities, centers, and group directories. Follow to group/lab pages, then identify PIs/researchers.

Prefer researcher candidates supported by:
- official group membership;
- corresponding/senior authorship in relevant peer-reviewed work;
- maintainership of important tools/resources.

Use ORCID/institutional profiles for identity. Google Scholar is monitoring/discovery only.

## Pass C: software and workflows

Search official repositories, documentation, package registries, and release pages. Capture the stable release/update endpoint, not only the repository home page.

High-value examples include workflow engines, widely used genomics/single-cell/metagenomics/proteomics tools, and environment/package infrastructure.

## Pass D: databases and infrastructure

Search official NCBI, EMBL-EBI, Ensembl, UniProt, PDB/PDBe, Bioconductor, GDC, gnomAD, GTEx, Reactome, PRIDE, MGnify, and related resource/update pages when relevant to the domain.

Capture migration, API, schema, authentication, reference, annotation, archive, taxonomy, and service-update endpoints when available.

## Pass E: cross-check and canonicalization

For each candidate:
1. open the official page;
2. confirm organization/project identity;
3. confirm domain fit;
4. identify monitoring method/endpoint;
5. search the current registry for normalized URL/name aliases;
6. only then create a new record.

## Search quality rules

- Use multiple narrow searches rather than one broad `best bioinformatics sources` query.
- Search snippets are candidate generators, not evidence.
- Do not use Persian-language web sources unless explicitly requested.
- Do not add low-value sources to meet a quota.
- When coverage is thin, report the gap instead of inventing sources.
