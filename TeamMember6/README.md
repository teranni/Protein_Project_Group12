# Stability Analysis in Ensemble Mode using MutateX

## Data gathering 

> ssh s253689@pupil4.healthtech.dtu.dk server

> cd /home/projects/22117_protein_structure/projects/group12/

> mkdir s253689

> cd s253689

> mkdir src

> cd src

> mkdir mutatex

> cd mutatex

> cp -r ../../../s253719/src/mutatex/self-scan .

Team Member 5 already gathered all the necessary documents, except poslist, to start the self scan

> cd self-scan

> nano poslist.txt 

add the variants relevant for analysis from [this list](https://github.com/teranni/Protein_Project_Group12/blob/main/TeamMember1/PARP1_FINAL_Variant_Table.xlsx) to the document in A-chain format. (only cosmic counts over 4 and in the correct sequence area, so substract the variants by 659 to get the correct position in the structure)

#### if not already done by amazing teammate copy the necessary files for analysis

> cp /home/projects/22117_protein_structure/lecture5/mutatex_templates/mutatex/templates/foldxsuite5/repair_runfile_template.txt .

> cp /home/projects/22117_protein_structure/lecture5/mutatex_templates/mutatex/templates/foldxsuite5/mutate_runfile_template.txt .

> cp /home/projects/22117_protein_structure/lecture5/mutatex_templates/mutatex/templates/foldxsuite5/mutation_list.txt .


## Self Scan
> conda deactivate

> conda activate /home/ctools/protein_structure_course/

#### Python Script to add Chain 

> cp /home/projects/22117_protein_structure/lecture7/group0/src/mutatex/ensemble_mode/chainize.py .

> python chainize.py R*_model_1-3.pdb > R*_model_1-3A.pdb

adds Chain A to all pdb files

### actual Self Scan

> nohup mutatex R*_model_1-3A.pdb -p 3 -x /home/ctools/foldx/foldx -m mutation_list.txt -f suite5 -R repair_runfile_template.txt -M mutate_runfile_template.txt -q poslist.txt -c -L -l -v -s -a &

the self scan was done one by one and the star was exchanged for 1, 2 or 3 depending on the used replica in that instance

#### Check Self-Scan Results

> cd /results_selfmutation/mutation_ddgs

> cat R*/selfmutation_energies.dat


## Ensemble Mode

> cd ../../../

> mkdir ensemble_mode

> cd ensemble_mode

> cp /home/projects/22117_protein_structure/lecture5/mutatex_templates/mutatex/templates/foldxsuite5/repair_runfile_template.txt .

> cp /home/projects/22117_protein_structure/lecture5/mutatex_templates/mutatex/templates/foldxsuite5/mutate_runfile_template.txt .

> cp /home/projects/22117_protein_structure/lecture5/mutatex_templates/mutatex/templates/foldxsuite5/mutation_list.txt .

> cp -r ../self-scan/repair .

> cp ../self-scan/*pdb .

> cp ../self-scan/poslist.txt .

#### Reactivate Conda

>conda deactivate

>conda activate /home/ctools/protein_structure_course/

## Actual Ensemble Mode Analysis

> nohup mutatex R*_model_1-3A.pdb -p 3 -x /home/ctools/foldx/foldx -m mutation_list.txt -f suite5 -R repair_runfile_template.txt -M mutate_runfile_template.txt -q poslist.txt -c -L -l -v -a &

the analysis was done one by one and the star was exchanged for 1, 2 or 3 depending on the used replica in that instance

### Extract Results as CSV file

> ddg2excel -p R*_model_1-3A.pdb -l mutation_list.txt -q poslist.txt -d results/mutation_ddgs/final_averages/ -o R*energies -F csv

### Create Heatmap for Visualisation

> ddg2heatmap -p R*_model_1-3A.pdb -l mutation_list.txt -q poslist.txt -d results/mutation_ddgs/final_averages/ -o R*heatmap

