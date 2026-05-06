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

The repository is organized to reflect both the overall workflow and individual contributions.

### Individual Work Documentation

Each team member has a dedicated README file:

* `README_TeamMember1`
* `README_TeamMember2`
* `README_TeamMember3`
* `README_TeamMember4`
* `README_TeamMember5`
* `README_TeamMember6`

These files include:

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
