PARP1 (P09874) - Variant Analysis Workflow Log
Team Member 1: Gene and Variant Selection, AlphaMissense, DeMaSk
Course: Protein Structure Data Analysis
Date: April 2026



# STEP 1: GENE SELECTION

Protein: PARP1 (Poly [ADP-ribose] polymerase 1)
UniProt accession: P09874
Organism: Homo sapiens
Function: DNA repair enzyme; mediates poly-ADP-ribosylation;
          key role in base excision repair and single-strand
          break repair.

# STEP 2: VARIANT COLLECTION — ClinVar
Database: ClinVar (https://www.ncbi.nlm.nih.gov/clinvar/)
Date accessed: April 2026

Search query:
  - Search term: PARP1[gene]
  - Filter: Molecular consequence → Missense variant

Results:
  - Total missense variants returned: 106
  - Pathogenic: 0
  - Likely pathogenic: 0
  - Uncertain significance (VUS): 89
  - Likely benign: 8
  - Benign: 4
  - Named conditions: PARP1-related disorder,
                      Hereditary renal cell carcinoma

Download format: Variation file (CSV)

# STEP 3: VARIANT COLLECTION — COSMIC

Database: COSMIC v103, GRCh38
URL: https://cancer.sanger.ac.uk/cosmic/gene/analysis?ln=PARP1
Date accessed: April 2026

Steps performed:
  1. Navigated to PARP1 gene page in COSMIC
  2. Clicked "Variants" in left sidebar menu
  3. Sorted table by "Count" column (descending)
  4. Retained only entries with Mutation Type =
     "Substitution - Missense"
     (excluded: coding silent, nonsense, unknown, indels)
  5. Applied minimum count threshold of 4
     (to prioritise recurrently mutated positions
     likely under positive selection in cancer)
  6. Exported table as CSV

Overall COSMIC statistics for PARP1:
  - Total unique samples with PARP1 mutations: 1,079
  - Samples with missense substitutions: 550 (50.97%)
  - Total entries in variants table: 912

Final COSMIC selection (18 missense variants, count >= 4):
  Variant   | Count
  ----------|------
  V762A     | 15
  A502V     | 11
  G597S     | 6
  A709T     | 6
  S904T     | 6
  R18H      | 4
  K59N      | 4
  G92E      | 4
  P146L     | 4
  A178V     | 4
  D307N     | 4
  P377S     | 4
  T594M     | 4
  K629E     | 4
  P750L     | 4
  A828V     | 4
  R878W     | 4
  P881L     | 4


# STEP 4: MERGING DATASETS

- ClinVar and COSMIC variant lists were merged
- Duplicates were removed
- Cross-referenced with MAVISp simple mode output for PARP1
  (PARP1-simple_mode_Mavisp.csv) to identify cBioPortal sources

Source breakdown after merging:
  - ClinVar only:                66 variants
  - ClinVar + cBioPortal:        29 variants
  - COSMIC + cBioPortal:         13 variants
  - COSMIC + ClinVar + cBioPortal: 3 variants
  - COSMIC only:                  2 variants
  - TOTAL:                      113 unique missense variants

Variants present in all 3 databases (strongest evidence):
  - V762A, P377S, R18H


# STEP 5: ALPHAMISSENSE — PATHOGENICITY PREDICTION

Tool: AlphaMissense
Reference: Cheng et al., Science (2023)
Source: AlphaFold database entry for P09874

Download URL:
https://alphafold.ebi.ac.uk/files/AF-P09874-F1-aa-substitutions.csv

File contents:
  - 19,266 rows (all possible single AA substitutions in PARP1)
  - Columns: protein_variant, am_pathogenicity, am_class

Classification thresholds (MAVISp framework):
  - Likely Pathogenic:  score > 0.564
  - Ambiguous:          score 0.340 - 0.564
  - Likely Benign:      score < 0.340

Each of the 113 variants was matched by protein_variant notation. All 113 variants were successfully scored.

Results summary:
  - Likely Pathogenic: 26 variants (23.0%)
  - Ambiguous:         13 variants (11.5%)
  - Likely Benign:     74 variants (65.5%)


# STEP 6: DEMASK — GAIN/LOSS OF FUNCTION PREDICTION

Tool: DeMaSk 
Web server: https://demask.princeton.edu/

Steps performed:
  1. Retrieved canonical FASTA sequence of PARP1 from
     UniProt (P09874)
  2. Submitted FASTA sequence to DeMaSk web server
  3. Downloaded output file (tab-separated .txt)
  4. Matched each variant using WT + position + variant
     notation (e.g. V762A)

Classification thresholds (MAVISp framework):
  - LOF (Loss of Function):  delta_fitness <= -0.25
  - GOF (Gain of Function):  delta_fitness >= +0.25
  - Neutral:                 between -0.25 and +0.25

All 113 variants were successfully matched and scored.

Results summary:
  - LOF:     19 variants (16.8%)
  - Neutral: 94 variants (83.2%)
  - GOF:      0 variants (0.0%)


STEP 7: FINAL VARIANT TABLE

All results were combined into a single Excel file:
  PARP1_FINAL_Variant_Table.xlsx

Sheets:
  1. Master Variant List - all 113 variants with sources
  2. Analysis Table - AlphaMissense + DeMaSk scores for all
  3. Summary - classification counts and percentages


# STEP 8: FILES USED / PRODUCED

Input files:
  - comic.xlsx
      (COSMIC + ClinVar data, 4 sheets)
  - AF-P09874-F1-aa-substitutions.csv
      (AlphaMissense scores, downloaded from AlphaFold DB)
  - 542fb81cb8a5189ba889.txt
      (DeMaSk output for PARP1 canonical sequence)
  - PARP1-simple_mode_Mavisp.csv
      (MAVISp simple mode output, used for cBioPortal
       source cross-referencing)
  - Gene_mutationsTue_Apr_21_17_58_01_2026.csv
      (Full COSMIC export, all 893 entries unfiltered)

Output files:
  - PARP1_FINAL_Variant_Table.xlsx
      (Master variant list + complete analysis table)
 

# DATABASES AND TOOLS — REFERENCES

ClinVar:
https://www.ncbi.nlm.nih.gov/clinvar/

COSMIC:
https://cancer.sanger.ac.uk/cosmic

cBioPortal:
https://www.cbioportal.org/

AlphaFold / AlphaMissense:
https://alphafold.ebi.ac.uk/entry/P09874

DeMaSk:
https://demask.princeton.edu/

MAVISp:
https://services.healthtech.dtu.dk/mavisp/MAVISp_simple_mode
 

