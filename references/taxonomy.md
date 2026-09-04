# Core Bioinformatics Taxonomy

Schema version: 1.0.0

Use stable IDs even if display labels evolve. A source can map to more than one domain, but assign one primary domain and place secondary coverage in notes or an extension table.

| ID | Domain | Scope examples |
|---|---|---|
| D01 | Genomics & Variant Analysis | assembly, annotation, variant calling, population genomics, pangenomes |
| D02 | Transcriptomics & RNA Biology | bulk RNA-seq, isoforms, splicing, RNA regulation |
| D03 | Single-cell Omics | scRNA-seq, scATAC-seq, multimodal single-cell analysis |
| D04 | Spatial Omics | spatial transcriptomics/proteomics, spatial analysis methods |
| D05 | Long-read Sequencing | long-read assembly, isoforms, methylation, variant analysis |
| D06 | AI / Machine Learning for Biology | foundation models, ML methods, biological sequence/modeling applications |
| D07 | Structural Bioinformatics | structure prediction, docking, protein/RNA structure, design tooling |
| D08 | Metagenomics, Microbiome & AMR | taxonomic/functional profiling, microbial genomics, AMR informatics |
| D09 | Proteomics & Metabolomics | MS analysis, identification, quantification, metabolomics workflows |
| D10 | Systems Biology & Multi-omics | metabolic/network models, pathway analysis, multi-omics integration |
| D11 | Clinical Bioinformatics & Precision Medicine | clinical genomics, interpretation, cancer genomics, clinical resources |
| D12 | Workflow Engineering & Reproducibility | Nextflow/Snakemake/Galaxy, containers, packaging, workflow standards |
| D13 | Databases, Reference Resources & Infrastructure | archives, annotations, reference datasets, APIs, schemas, cloud/data services |

## Extension rule

Add a new domain only when at least one of these is true:

1. It has a distinct source ecosystem that cannot be represented cleanly by current domains.
2. It requires a materially different monitoring strategy.
3. It repeatedly creates ambiguous classification in at least three verified records.

Do not create a domain solely because one paper uses a new buzzword.
