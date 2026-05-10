Input file for analysis is available under "Downloadable data - Analysis & MDs (1,000 frames, only protein)" on: https://www.dsimb.inserm.fr/ATLAS/database/ATLAS/5ws1_A/5ws1_A.html


# 0. Create project folder
```bash
ssh s253719@pupil4.healthtech.dtu.dk
cd /home/projects/22117_protein_structure/projects/group12/s253719
mkdir src
cd src
  base: C:\Users\heszt\Documents\MSc\DTU\Sem2\Protein\Project\Data
  scp -r 5ws1_A_analysis s253719@pupil4.healthtech.dtu.dk:/home/projects/22117_protein_structure/projects/group12/s253719/src
mkdir atlas_data
mv 5ws1_A_analysis/ atlas_data/
mkdir pdbs
cd pdbs
```

# 1.	Convert the trajectory files
```bash
mkdir 1_Convert_trajectory_files 
cd 1_Convert_trajectory_files
gmx trjconv -f ../../atlas_data/5ws1_A_analysis/5ws1_A_R1.xtc -s ../../atlas_data/5ws1_A_analysis/5ws1_A_R1.tpr -o 5ws1_A_R1.pdb  -fit rot+trans
gmx trjconv -f ../../atlas_data/5ws1_A_analysis/5ws1_A_R2.xtc -s ../../atlas_data/5ws1_A_analysis/5ws1_A_R2.tpr -o 5ws1_A_R2.pdb  -fit rot+trans
gmx trjconv -f ../../atlas_data/5ws1_A_analysis/5ws1_A_R3.xtc -s ../../atlas_data/5ws1_A_analysis/5ws1_A_R3.tpr -o 5ws1_A_R3.pdb  -fit rot+trans
cd ../
```

# 2.	Compute the main-chain RMSD matrix
```bash
mkdir 2_Mainchain_RMSD_matrix
cd 2_Mainchain_RMSD_matrix
gmx_mpi rms -f ../../atlas_data/5ws1_A_analysis/5ws1_A_R1.xtc -s ../../atlas_data/5ws1_A_analysis/5ws1_A_R1.tpr  -o rmsd_R1.xvg -m rmsd_matrix_R1.xpm
gmx_mpi rms -f ../../atlas_data/5ws1_A_analysis/5ws1_A_R2.xtc -s ../../atlas_data/5ws1_A_analysis/5ws1_A_R2.tpr  -o rmsd_R2.xvg -m rmsd_matrix_R2.xpm
gmx_mpi rms -f ../../atlas_data/5ws1_A_analysis/5ws1_A_R3.xtc -s ../../atlas_data/5ws1_A_analysis/5ws1_A_R3.tpr  -o rmsd_R3.xvg -m rmsd_matrix_R3.xpm
cd ../
```

# 3.	Clustering of the trajectories
```bash
mkdir 3_Clustering_trajectories
cd 3_Clustering_trajectories
gmx_mpi cluster -f ../../atlas_data/5ws1_A_analysis/5ws1_A_R1.xtc -s ../../atlas_data/5ws1_A_analysis/5ws1_A_R1.tpr -dm rmsd_matrix_R1.xpm -o rmsd_clust_R1.xpm -g cluster_R1.log -sz clust_size_R1.xvg -cl clusters_R1.pdb -clid clust_id_R1.xvg -dist rmsd_dist_R1.xvg -method gromos  -cutoff  0.18
gmx_mpi cluster -f ../../atlas_data/5ws1_A_analysis/5ws1_A_R2.xtc -s ../../atlas_data/5ws1_A_analysis/5ws1_A_R2.tpr -dm rmsd_matrix_R2.xpm -o rmsd_clust_R2.xpm -g cluster_R2.log -sz clust_size_R2.xvg -cl clusters_R2.pdb -clid clust_id_R2.xvg -dist rmsd_dist_R2.xvg -method gromos  -cutoff  0.17
gmx_mpi cluster -f ../../atlas_data/5ws1_A_analysis/5ws1_A_R3.xtc -s ../../atlas_data/5ws1_A_analysis/5ws1_A_R3.tpr -dm rmsd_matrix_R3.xpm -o rmsd_clust_R3.xpm -g cluster_R3.log -sz clust_size_R3.xvg -cl clusters_R3.pdb -clid clust_id_R3.xvg -dist rmsd_dist_R3.xvg -method gromos  -cutoff  0.16
cd ../
```

# 4.	Evaluate the population of each cluster
```bash
mkdir 4_Evaluate_cluster_populations
cd 4_Evaluate_cluster_populations
  base: C:\Users\heszt\Documents\MSc\DTU\Sem2\Protein\Project\Data
  scp -r plot.py s253719@pupil4.healthtech.dtu.dk:/home/projects/22117_protein_structure/projects/group12/s253719/src/pdbs/4_Evaluate_cluster_populations
python plot.py -r R1 -n 5 --cluster_input_dir ../3_Clustering_trajectories --rmsd_input_dir ../2_Mainchain_RMSD_matrix
python plot.py -r R2 -n 7 --cluster_input_dir ../3_Clustering_trajectories --rmsd_input_dir ../2_Mainchain_RMSD_matrix
python plot.py -r R3 -n 8 --cluster_input_dir ../3_Clustering_trajectories --rmsd_input_dir ../2_Mainchain_RMSD_matrix
cd ../../
```

# 5.	Prepare for self-scan (Deliver to Team Member 6)
```bash
mkdir mutatex
cd mutatex
mkdir self-scan
cd self-scan

cp /home/projects/22117_protein_structure/lecture7/group0/src/mutatex/self-scan/mutate_runfile_template.txt .
cp /home/projects/22117_protein_structure/lecture7/group0/src/mutatex/self-scan/mutation_list.txt .
cp /home/projects/22117_protein_structure/lecture7/group0/src/mutatex/self-scan/repair_runfile_template.txt .
nano poslist.txt

cd ../../pdbs/3_Clustering_trajectories/
mkdir cluster_R1
cp clusters_R1.pdb cluster_R1
cd cluster_R1
csplit -f model_ -b "%02d.pdb" ../clusters_R1.pdb '/^MODEL/' '{*}' 
cat model_01.pdb model_02.pdb model_03.pdb > R1_model_1-3.pdb
cp R1_model_1-3.pdb ../../../mutatex/self-scan/
mkdir cluster_R2
cp clusters_R2.pdb cluster_R2
cd cluster_R2
csplit -f model_ -b "%02d.pdb" ../clusters_R2.pdb '/^MODEL/' '{*}' 
cat model_01.pdb model_02.pdb model_03.pdb > R2_model_1-3.pdb
cp R2_model_1-3.pdb ../../../mutatex/self-scan/
mkdir cluster_R3
cp clusters_R3.pdb cluster_R3
cd cluster_R3
csplit -f model_ -b "%02d.pdb" ../clusters_R3.pdb '/^MODEL/' '{*}' 
cat model_01.pdb model_02.pdb model_03.pdb > R3_model_1-3.pdb
cp R3_model_1-3.pdb ../../../mutatex/self-scan/
```
# 6. Visualisation in pyMOL

Open: R2_model_1-3.pdb

```python
intra_fit R2_model_1-3
set all_states, on
dss
show cartoon
color cyan, ss h
color magenta, ss s
color green, ss l+''
# Save: Figure 10

# Manual select RMSF peaks
set_name sele, rmsf_peaks
% Manual select mutational variant sites
set_name sele, variants
select overlap, rmsf_peaks and variants
color yellow, ss s

set cartoon_transparency, 0.5, R2_model_1-3
set cartoon_transparency, 0.1, rmsf_peaks
color orange, rmsf_peaks
set cartoon_transparency, 0.1, variants
color magenta, variants
set cartoon_transparency, 0.1, overlap
color red, overlap
label overlap and name CA, "%s%s" % (resn,resi)

set all_states, off
bg white
# Save: Figure 11
```
