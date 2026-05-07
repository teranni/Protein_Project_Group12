## log onto server and gather the data
> cd /home/projects/22117_protein_structure/projects/group12/

> mkdir s253689

> cd s253689

> mkdir src

> cd src

> mkdir mutatex

> cd mutatex

> cp -r ../../../s253719/src/mutatex/self-scan .

> cd self-scan

> nano poslist.txt 

add the variants relevant for analysis from this list "link" to the document in A-chain format. only numbers over 4 and in the correct sequence area, so calculate the variants by 659 to get the correct position for the variants

> cp /home/projects/22117_protein_structure/lecture5/mutatex_templates/mutatex/templates/foldxsuite5/repair_runfile_template.txt .
> cp /home/projects/22117_protein_structure/lecture5/mutatex_templates/mutatex/templates/foldxsuite5/mutate_runfile_template.txt .
> cp /home/projects/22117_protein_structure/lecture5/mutatex_templates/mutatex/templates/foldxsuite5/mutation_list.txt .


## start conda
conda deactivate
conda activate /home/ctools/protein_structure_course/


## copy python script to add chain A into pdb files and run it
cp /home/projects/22117_protein_structure/lecture7/group0/src/mutatex/ensemble_mode/chainize.py .

python chainize.py R*_model_1-3.pdb > R*_model_1-3A.pdb


## self scan
> nohup mutatex R3_model_1-3A.pdb -p 3 -x /home/ctools/foldx/foldx -m mutation_list.txt -f suite5 -R repair_runfile_template.txt -M mutate_runfile_template.txt -q poslist.txt -c -L -l -v -s -a & 

##check self-scan results
> cd /results_selfmutation/mutation_ddgs 
> cat R*/selfmutation_energies.dat


### gather datafiles for ensemble
> cd ../../../
> mkdir ensemble_mode
> cd ensemble_mode

> cp /home/projects/22117_protein_structure/lecture5/mutatex_templates/mutatex/templates/foldxsuite5/repair_runfile_template.txt .
> cp /home/projects/22117_protein_structure/lecture5/mutatex_templates/mutatex/templates/foldxsuite5/mutate_runfile_template.txt .
> cp /home/projects/22117_protein_structure/lecture5/mutatex_templates/mutatex/templates/foldxsuite5/mutation_list.txt .
> cp -r ../self-scan/repair . 
> cp ../self-scan/*pdb . 
> cp ../self-scan/poslist.txt .

## reactivate conda
conda deactivate
conda activate /home/ctools/protein_structure_course/

## start ensemble 
> nohup mutatex R3_model_1-3A.pdb -p 3 -x /home/ctools/foldx/foldx -m mutation_list.txt -f suite5 -R repair_runfile_template.txt -M mutate_runfile_template.txt -q poslist.txt -c -L -l -v -a &

# extract results as CSV file
ddg2excel -p R*_model_1-3A.pdb -l mutation_list.txt -q poslist.txt -d results/mutation_ddgs/final_averages/ -o R*energies -F csv

# create heatmap for visualisation
ddg2heatmap -p R*_model_1-3A.pdb -l mutation_list.txt -q poslist.txt -d results/mutation_ddgs/final_averages/ -o R*heatmap

