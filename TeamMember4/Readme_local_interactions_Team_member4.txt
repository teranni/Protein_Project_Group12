PyMol:
#Load structure
fetch 6M3I, async=0

#Remove crystallographic water molecules
remove solvent

#Keep only the relevant protein chains
select parp1_hpf1, polymer.protein
remove not parp1_hpf1

#Clean view
bg_color white

#Save the prepared structure as a PDB file
save 6M3I_clean.pdb, parp1_hpf1

#Color chains
color orange, chain B
color green, chain A

#Select mutation sites
select mut_sites, chain B and resi 828+878+904
show sticks, mut_sites
color red, mut_sites

#Label mutation sites
label chain B and resi 828 and name CA, "ALA828"
label chain B and resi 878 and name CA, "ARG878"
label chain B and resi 904 and name CA, "SER904"

set label_size, 24
set label_color, black

#Show PARP1 residues within 5 Å of HPF1 interface
select interface_5A_A, byres (chain A within 5 of chain B)
show sticks, interface_5A_A
color cyan, interface_5A_A

#Show HPF1 residues within 5 Å of PARP1 interface
select interface_5A_B, byres (chain B within 5 of chain A)
show sticks, interface_5A_B
color yellow, interface_5A_B

#Keep mutation sites red on top
color red, mut_sites
show sticks, mut_sites

#Save image
png 6M3I_interface_mutations.png, dpi=300


Ubuntu:
#Log in to the server
ssh s254123@pupil4.healthtech.dtu.dk

#Fetched the template files from lecture5/group0
>cd /home/projects/22117_proteins_2025/lecture5/group0

cp /home/projects/22117_protein_structure/lecture5/group0/mutatex_stability/ *template.txt .

scp -r /mnt/c/Users/ramin/Downloads/exam_1 s254123@pupil4:/home/projects/22117_protein_structure/lecture5/group12/

#Prepared files for the analysis
6M3I_clean.pdb  #cleaned PDB file
mutation_list.txt  
mutate_runfile_template.txt
interface_runfile_template.txt
repair_runfile_template.txt
poslist.txt #Rewriten list

#Instal and activate conda environment
bash /home/ctools/anaconda3-2024.10-1/bin/conda init
conda activate /home/ctools/protein_structure_course

#Run mutatex 
nohup mutatex 6M3I_clean.pdb -p 2 -m mutation_list.txt -x /home/ctools/foldx/foldx -f suite5 -R repair_runfile_template.txt -M mutate_runfile_template.txt -q poslist.txt -L -l -v -C  none -B  -I interface_runfile_template.txt &

#Checking progress and output
jobs
cat nohup.out
ls exam_1

#Run ddg2excel to get the final csv file with the results
ddg2excel -p 6M3I_clean.pdb -l mutation_list.txt -q poslist.txt -d results/interface_ddgs/final_averages/A-B/ -F csv

#Run ddg2heatmap
ddg2heatmap -p 6M3I_clean.pdb -l mutation_list.txt -q poslist.txt -d results/interface_ddgs/final_averages/A-B/

#Downloaded all the files from server through local terminal
scp -r s254123@pupil4.healthtech.dtu.dk:/home/people/s254123/exam_1 .


RStudio:
#Loading library
library(pheatmap)

#Data
data <- matrix(c(
  0.2751,0,-0.47302,-0.9522,-0.80562,-0.38652,-1.6364,-0.68272,-0.22736,0.20222,0.0954,0.30738,-1.10662,-0.5011,0.08506,0.4084,-0.12942,0.28686,-0.19454,-1.02682,
  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
  0.0224,-0.0026,0.007,0.01526,-0.00774,-0.06232,-0.02822,-0.08954,-0.00386,0,0.01796,0.00622,-0.02644,-0.00402,-0.06254,0.17848,0.1895,-0.32586,-0.93378,-0.02518
), nrow = 3, byrow = TRUE)

rownames(data) <- c("A828V", "R878W", "S904T")

colnames(data) <- c(
  "Gly","Ala","Val","Leu","Ile","Met","Phe","Trp","Pro","Ser",
  "Thr","Cys","Tyr","Asn","Gln","Asp","Glu","Lys","Arg","His"
)


#Vertical layout
data_vertical <- t(data)

#Color palette
colors <- colorRampPalette(c(
  "#2166AC",
  "#67A9CF",
  "#F7F7F7",
  "#F4A582",
  "#B2182B"
))(200)

breaks <- seq(-2, 1, length.out = 201)

#Save heatmap
png("clean_heatmap.png", width = 1000, height = 1600, res = 300)

pheatmap(
  data_vertical,
  color = colors,
  breaks = breaks,
  cluster_rows = FALSE,
  cluster_cols = FALSE,
  border_color = "grey85",
  fontsize = 12,
  fontsize_row = 11,
  fontsize_col = 12,
  cellwidth = 55,
  cellheight = 28,
  display_numbers = TRUE,
  number_format = "%.2f",
  number_color = "black",
  angle_col = 0,
  legend = TRUE,
  legend_breaks = c(-2, -1, 0, 1),
  legend_labels = c("-2", "-1", "0", "1"),
  main = NA
)
