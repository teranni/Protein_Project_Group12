Team Member 2 – Structure Selection and Docking Analysis

1. Retrieved the full-length PARP1 sequence from UniProt (P09874).
2. Investigated available experimental structures in the Protein Data Bank (PDB).
3. Selected the AlphaFold model for full-length structural visualization.
4. Evaluated structural confidence using pLDDT and PAE metrics.
5. Visualized domain organization and catalytic domain using PyMOL.
6. Retrieved experimental crystal structure 6NRH from RCSB PDB for ligand-binding analysis.
7. Performed molecular docking using SwissDock with AutoDock Vina.
8. Used KYP as ligand and 6NRH as target structure.
9. Analyzed docking poses and binding affinity.
10. Generated structural figures in PyMOL.

Tools used: 
- UniProt
- AlphaFold Protein Structure Database
- RCSB Protein Data Bank
- PyMOL
- SwissDock
- AutoDock Vina
Figures: 
PARP1_AlphaFold_pLDDT.png
-	 Figure 1 pymol.png
-	Figure 2 pymol.png
-	Figure 3 pymol.png
-	Figure 4 pymol.png
Structures: 
For docking:      
Parameters:
- Target: 6NRH
- Ligand: KYP
- Chain: A
- Heteroatoms kept: None
- Docking box: centered around the catalytic pocket
- Exhaustiveness: 8
- Best predicted affinity: -11.811 kcal/mol

 PyMOL visualization of docking result:
- The best-ranked docking pose was visualized in PyMOL. Residues within 4 Å of the docked ligand were highlighted to show the local binding environment.
  
Commands: 
 load AF-P09874-F1-model_v6.pdb
hide everything
show cartoon
bg_color white


Kode til confidence: 
load AF-P09874-F1-model_v6.pdb
show cartoon
coloraf AF-P09874-F1-model_v6_A

Kode til domain:

hide everything
show cartoon
color grey80, all

select domain1, resi 8-90
color green, domain1

select domain2, resi 109-197
color orange, domain2

select domain3, resi 230-293+329-346
color purple, domain3

select domain4, resi 393-475
color limegreen, domain4

select domain5, resi 534-632
color yellow, domain5

select domain6, resi 666-793
color cyan, domain6

select domain7, resi 798-1008
color blue, domain7

orient
-	Zoom

Code for catalytic domain:
hide everything
show cartoon
color grey80, all

select catalytic_domain, resi 798-1008
color blue, catalytic_domain

set cartoon_transparency, 0.3, all
set cartoon_transparency, 0.0, catalytic_domain

orient
zoom catalytic_domain




Code for ligand binding site docking:

load 6NRH.pdb
hide everything
show cartoon
color grey80, all

select ligand, organic
show sticks, ligand
color red, ligand

select pocket, byres (ligand around 4)
show sticks, pocket
color cyan, pocket

zoom ligand, 8



Structure Selection and Docking:

- Protein: Human PARP1
- UniProt ID: P09874
- Length: 1014 residues

Structure Selection:
The full-length PARP1 structure was searched in UniProt, PDB, and the AlphaFold Protein Structure Database.

No experimentally resolved full-length PARP1 structure was available in PDB. Therefore, the AlphaFold model AF-P09874-F1 was selected because it covers residues 1–1014.

For ligand-binding analysis, the experimental crystal structure 6NRH was used because it represents the PARP1 catalytic domain bound to an inhibitor and provides high-resolution information about the catalytic binding pocket.

## AlphaFold Model Assessment
The AlphaFold model was evaluated using:
- pLDDT confidence scores
- Predicted Aligned Error (PAE)
- visual inspection in PyMOL
The model showed high confidence in structured domains and lower confidence in flexible linker regions. PAE indicated that domain orientation should be interpreted cautiously, especially for docking-related applications.


Domain Analysis:
The PARP1 structure was divided into seven domains based on AlphaFold structural domain annotations:

- Domain 1: residues 8–90
- Domain 2: residues 109–197
- Domain 3: residues 230–293 and 329–346
- Domain 4: residues 393–475
- Domain 5: residues 534–632
- Domain 6: residues 666–793
- Domain 7: residues 798–1008

The catalytic domain was highlighted separately because it is responsible for enzymatic activity and ligand binding.

Docking / Ligand-Binding Analysis:
The PDB structure 6NRH was used for ligand-binding analysis. The ligand-binding site was visualized in PyMOL by highlighting the ligand and surrounding residues within approximately 4 Å.

This was used to interpret how inhibitors bind in the catalytic pocket of PARP1.


