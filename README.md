# Protein_Project_Group12

## Overview

This repository contains the computational workflow and analyses performed for the stability and mutation analysis of the PARP1 protein. The project integrates molecular dynamics (MD), mutational scanning, pathogenicity prediction, and docking studies.


## Project Goals

The project aims to assess:

* Prediction of pathogenicity of PARP1 variants
* Structural stability of PARP1
* Effects of mutations on protein stability and local interactions
* Conformational diversity from MD simulations
* Ligand binding through docking approaches


## Project Structure

The repository is organized by team member contributions. Each member has a dedicated folder containing their analysis and supporting files:

* `TeamMember1/`
* `TeamMember2/`
* `TeamMember3/`
* `TeamMember4/`
* `TeamMember5/`
* `TeamMember6/`
  
### Contents of Each Folder

Each TeamMemberX folder contains:

A README describing the workflow and analysis performed.
Optionally:
* Scripts (e.g., .py)
* Data files (e.g., .xlsx)
* Any additional files required for the analysis

These folders document:

* Step-by-step pipelines followed
* Commands executed (primarily via terminal)
* Tools and parameters used
* Notes relevant for reproducibility


## Team Contributions (Summary)

A reduced MAVISp-inspired framework was applied, with tasks distributed as follows:

* **Team Member 1**

  * Gene and variant selection (ClinVar, COSMIC, cBioPortal, MAVISp annotations)
  * Prediction of pathogenicity (AlphaMissense, DeMask)

* **Team Member 2**

  * Structure selection (PDBMiner, AlphaFold/AlphaFill)
  * Docking of free protein and complexes

* **Team Member 3**

  * Assessment of mutation effects on **protein stability** (MutateX / FoldX, ΔΔG folding)

* **Team Member 4**

  * Assessment of mutation effects on **local interactions** (MutateX / FoldX, binding ΔΔG)

* **Team Member 5**

  * Ensemble generation and MD analyses using simulation databases

* **Team Member 6**

  * Stability calculations in **ensemble mode**


## Acknowledgments

This project was conducted as part of a protein structure and computational biology course, using established tools such as:

* GROMACS
* FoldX
* MutateX
