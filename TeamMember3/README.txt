# MutateX Stability Analysis — Foolproof Step-by-Step Protocol
## Group 12 / Team Member 3 (Gudrún) — PARP1 single-structure stability on 5WS1

**Goal:** compute folding-free-energy changes (ΔΔG) for 9 cancer-associated PARP1 variants using FoldX/MutateX on the catalytic-domain crystal structure 5WS1, plus a saturation scan at each position so you can talk about mutational tolerance.

**Estimated time:** ~2 hours total wall-clock (10 min PyMOL prep + 10 min upload/setup + 15 min repair + 60–90 min mutation scan + 5 min extraction). You can do other things while MutateX runs in the background.

---

## The 9 positions you will scan

You only need the **structural** numbers in the protocol below. The UniProt numbers are listed for cross-reference.

| Variant | UniProt | Structural (5WS1) | poslist entry |
|---|---|---|---|
| A709T | 709 | 50 | `AA50` |
| L713R | 713 | 54 | `LA54` |
| P750L | 750 | 91 | `PA91` |
| A828V | 828 | 169 | `AA169` |
| T867P | 867 | 208 | `TA208` |
| R878W | 878 | 219 | `RA219` |
| I879R | 879 | 220 | `IA220` |
| P881L | 881 | 222 | `PA222` |
| S904T | 904 | 245 | `SA245` |

Conversion rule: structural number = UniProt number − 659.

---

## A. Local prep in PyMOL (10 minutes, on your laptop)

You need to download 5WS1, clean it up, and save it as a plain PDB file with only chain A protein atoms.

1. **Open PyMOL** on your laptop.

2. **Download the structure.** In the PyMOL command line at the bottom, type:
   ```
   fetch 5WS1, async=0
   ```
   This downloads PDB 5WS1 directly into your session.

3. **Look at what's in the file.** In the right-hand panel you'll see one object called `5WS1`. Click the `S` button next to it to show the sequence at the top — this lets you confirm the residue range. You should see chain A. Hover over the residues at each end to confirm it covers ~660 to ~1011.

4. **Remove crystallographic waters.** In the command line:
   ```
   remove solvent
   ```
   This deletes all water molecules. FoldX is more reproducible without crystal waters.

5. **Remove any other heteroatoms.** 5WS1 may have ions or buffer molecules. To check, type:
   ```
   print cmd.get_chains("5WS1")
   ```
   and
   ```
   iterate hetatm, print(resn)
   ```
   The output lists every non-protein residue still in the file. If you see anything other than the protein chain (e.g. SO4, EDO, GOL, IPA, ZN), remove it with:
   ```
   remove hetatm
   ```
   (This wipes everything that isn't a standard amino acid. We're keeping only protein for the stability calculation.)

6. **Confirm only chain A is left.** 5WS1 may have multiple chains depending on the deposition. Keep only chain A:
   ```
   remove not chain A
   ```
   This deletes any other chains.

7. **Verify the structure looks right.** Click the `S` button again to look at the sequence — it should show one continuous chain A of protein residues. Type `print cmd.count_atoms("polymer")` to see how many protein atoms remain (you should see a few thousand).

8. **Save as plain PDB.** From the menu: **File → Export Molecule…**
   - In the dialog, set **Selection** to `5WS1` (or `polymer`).
   - Click **Save…**.
   - In the Save dialog, **set the format to "PDB" (not mmCIF)** — this is important, MutateX only reads PDB.
   - Save the file as `5WS1A_clean.pdb` somewhere easy to find (e.g. Desktop or your project folder).

9. **Sanity check.** Close PyMOL completely and re-open it, then drag your saved `5WS1A_clean.pdb` into the new session. Confirm there are no waters, only one chain, and the sequence looks continuous from ~residue 1 to ~352 (5WS1 numbering).

That's it for the local prep. Keep `5WS1A_clean.pdb` handy — you'll upload it to the server next.

---

## B. Connect to the server and create your project folder (5 minutes)

1. **Open a terminal on your laptop.**
   - Mac/Linux: open the Terminal app.
   - Windows: open MobaXTerm (or any SSH client you used in Lecture 3).

2. **Connect to the server.** Type (replacing `s242701` with your DTU username and `pupil4` with your group's pupil server — Group 12 is on pupil4 according to the data-availability statement):
   ```
   ssh s242701@pupil4.healthtech.dtu.dk
   ```
   Enter your password and approve the 2FA prompt. You should now see a server prompt like `[s242701@pupil4 ~]$`.

3. **Navigate to the group project folder.**
   ```
   cd /home/projects/22117_protein_structure/projects/group12
   ```
   If this folder doesn't exist yet, create it:
   ```
   mkdir -p /home/projects/22117_protein_structure/projects/group12
   cd /home/projects/22117_protein_structure/projects/group12
   ```

4. **Create a sub-folder for the new stability run.** Don't overwrite the old run.
   ```
   mkdir mutatex_stability_5ws1
   chmod -R a+rwX mutatex_stability_5ws1
   cd mutatex_stability_5ws1
   ```
   The `chmod` line gives the rest of the group access. The `cd` puts you inside the new folder.

5. **Confirm where you are.** Run:
   ```
   pwd
   ```
   It should print `/home/projects/22117_protein_structure/projects/group12/mutatex_stability_5ws1`. **Keep this terminal window open.**

---

## C. Upload your PDB to the server (2 minutes)

1. **Open a SECOND terminal window on your laptop** (the first one stays connected to the server).

2. **Navigate to wherever you saved `5WS1A_clean.pdb`.** For example:
   ```
   cd ~/Desktop
   ```

3. **Copy the file to the server.** Replace `s242701` and `pupil4` again:
   ```
   scp 5WS1A_clean.pdb s242701@pupil4.healthtech.dtu.dk:/home/projects/22117_protein_structure/projects/group12/mutatex_stability_5ws1/
   ```
   You'll be prompted for your password and 2FA. When it finishes, the file is on the server.

4. **Verify in the server terminal.** Switch back to the first (server) terminal and run:
   ```
   ls
   ```
   You should see `5WS1A_clean.pdb` listed.

You can close the second (local) terminal now.

---

## D. Activate the course Conda environment (1 minute)

In the server terminal:
```
conda activate /home/ctools/protein_structure_course
```
Your prompt will now have `(protein_structure_course)` at the front. This makes `naccess`, `mutatex`, `foldx`, and `ddg2excel` available.

If `conda activate` fails with "command not found", initialise it once with `source /home/ctools/miniconda3/etc/profile.d/conda.sh` then re-run the activate command.

---

## E. Run NACCESS (2 minutes)

NACCESS computes the relative solvent accessibility (RSA) of every residue, which you'll use in the Results to interpret the mutational landscape (buried sites are sensitive, exposed sites are tolerant).

1. **Run NACCESS:**
   ```
   naccess 5WS1A_clean.pdb
   ```
   Output appears in less than a minute. NACCESS creates `5WS1A_clean.rsa`, `5WS1A_clean.asa`, and `5WS1A_clean.log` in the current folder.

2. **Pull the RSA values for your 9 positions.** Run these one by one and write down the numbers:
   ```
   grep " 50 " 5WS1A_clean.rsa - 
   grep " 54 " 5WS1A_clean.rsa
   grep " 91 " 5WS1A_clean.rsa
   grep " 169 " 5WS1A_clean.rsa
   grep " 208 " 5WS1A_clean.rsa
   grep " 219 " 5WS1A_clean.rsa
   grep " 220 " 5WS1A_clean.rsa
   grep " 222 " 5WS1A_clean.rsa
   grep " 245 " 5WS1A_clean.rsa
   ```

| Variant | UniProt | Structural (5WS1) | poslist entry |
|---|---|---|---|
| A709T | 709 | 50 | `AA50` | - 0.0
| L713R | 713 | 54 | `LA54` | = 0.2
| P750L | 750 | 91 | `PA91` | = 61.8
| A828V | 828 | 169 | `AA169` | = 67.0
| T867P | 867 | 208 | `TA208` | = 8.4
| R878W | 878 | 219 | `RA219` | = 34.3
| I879R | 879 | 220 | `IA220` | = 22.3
| P881L | 881 | 222 | `PA222` | = 20.9
| S904T | 904 | 245 | `SA245` | = 5.6

Conversion rule: structural number = UniProt number − 659.


   Each command prints one line. The number you want is the **4th value** on the line — that's the side-chain relative accessibility (RSA, in %). Save these in a text file or note app — you'll need them for the Results section. (RSA > 25% = exposed, < 20% = buried.)

---

## F. Set up the MutateX input files (3 minutes)

You need three template/input files in your working folder.

1. **Copy the FoldX repair template:**
   ```
   cp /home/projects/22117_protein_structure/lecture5/mutatex_templates/mutatex/templates/foldxsuite5/repair_runfile_template.txt .
   ```
   (The dot at the end means "into the current folder".)

2. **Copy the FoldX mutation template:**
   ```
   cp /home/projects/22117_protein_structure/lecture5/mutatex_templates/mutatex/templates/foldxsuite5/mutate_runfile_template.txt .
   ```

3. **Copy the standard mutation list (all 20 amino acids):**
   ```
   cp /home/projects/22117_protein_structure/lecture5/mutatex_templates/mutatex/templates/foldxsuite5/mutation_list.txt .
   ```

4. **Create the position list — this is your variant list.** Use nano (text editor):
   ```
   nano poslist.txt
   ```
   In the editor, paste these 9 lines exactly (one per line, no trailing spaces):
   ```
   AA50
   LA54
   PA91
   AA169
   TA208
   RA219
   IA220
   PA222
   SA245
   ```
   Save with **Ctrl+O** then Enter, exit with **Ctrl+X**.

5. **Verify the file:**
   ```
   cat poslist.txt
   ```
   You should see your 9 positions printed back. Make sure each line starts with a single capital letter (the wild-type residue), then `A` (chain), then the structural residue number. No spaces, no extra characters.

6. **Final check of the working folder:**
   ```
   ls
   ```
   You should see:
   ```
   5WS1A_clean.pdb
   5WS1A_clean.rsa  (and .asa, .log)
   mutate_runfile_template.txt
   mutation_list.txt
   poslist.txt
   repair_runfile_template.txt
   ```

---

## G. Run MutateX (the main calculation, 60–120 minutes — runs in background)

1. **Launch MutateX with `nohup` so it survives if your SSH disconnects:**
   ```
   nohup mutatex 5WS1A_clean.pdb -p 4 -m mutation_list.txt -x /home/ctools/foldx/foldx -f suite5 -R repair_runfile_template.txt -M mutate_runfile_template.txt -q poslist.txt -L -l -v -C none &
   ```

   Plain-English breakdown of every flag:
   - `5WS1A_clean.pdb` — your input structure.
   - `-p 4` — use 4 CPU cores (the maximum we're allowed to grab).
   - `-m mutation_list.txt` — substitute to all 20 amino acids at each position.
   - `-x /home/ctools/foldx/foldx` — path to the FoldX executable.
   - `-f suite5` — FoldX format version 5.
   - `-R repair_runfile_template.txt` — template for the repair step.
   - `-M mutate_runfile_template.txt` — template for the mutation step.
   - `-q poslist.txt` — only mutate the 9 positions you listed (no full saturation across the whole protein, which would take days).
   - `-L -l -v` — logging flags (let mutatex log to a file, log verbose, write log).
   - `-C none` — don't clean up intermediate files (you can inspect them later).
   - `&` at the end — run in background; you get the prompt back immediately.

   You'll see something like `[1] 12345` printed (the process ID). The job is now running in the background.

2. **Confirm it started.** Run:
   ```
   jobs
   ```
   You should see one running job. Or:
   ```
   top -u s242701
   ```
   (replace with your username). You should see one or more `foldx` processes running. Press `q` to exit `top`.

3. **Watch progress in real time (optional):**
   ```
   tail -f nohup.out
   ```
   This streams the log to your terminal. Press **Ctrl+C** to stop watching (this only stops the watching, not the calculation).

4. **What to expect.** MutateX will:
   - Print "Starting repair stage…" — this takes ~10–15 minutes.
   - Print "Starting mutations stage…" — this is the long part, ~5–10 min per position × 9 positions = 45–90 min.
   - Print "All done!" when it's finished.

5. **It's safe to disconnect.** Because of `nohup`, you can close the terminal and the calculation keeps running. To check on it later: SSH back in, `cd` to the same folder, and run:
   ```
   tail -n 20 nohup.out
   ```
   If you see "All done!" the run finished. If not, check `jobs` (will be empty if disconnected then reconnected — use `pgrep -u s242701 foldx` instead to see if FoldX is still running).

---

## H. Extract the results (2 minutes — once "All done!" appears)

1. **Confirm the run finished:**
   ```
   tail -n 5 nohup.out
   ```
   The last line should say `All done!`. If not, wait longer or come back later.

2. **Run ddg2excel to aggregate the ΔΔG values into a CSV:**
   ```
   ddg2excel -p 5WS1A_clean.pdb -l mutation_list.txt -q poslist.txt -d results/mutation_ddgs/5WS1A_clean_model0_checked_Repair/ -F csv
   ```
   This creates a file called `energies.csv` in your folder.

3. **Take a quick look:**
   ```
   head energies.csv
   column -s, -t energies.csv | head
   ```
   You should see one row per position with the average ΔΔG (over 5 FoldX runs) for each of the 20 amino-acid substitutions.

4. **Also check the repair log** — you'll quote the before/after ΔG in your Results:
   ```
   grep Total repair/repair_5WS1A_clean_model0_checked/FoldXrun.log
   ```
   You'll see a list of `Total = ...` lines. The first is the starting ΔG; the last is the post-repair ΔG (should be lower, ideally negative).

---

## I. Download everything to your laptop (2 minutes)

1. **Open a fresh local terminal on your laptop** (or use the existing one).

2. **Navigate to where you want the results:**
   ```
   cd ~/Desktop
   mkdir parp1_stability_5ws1
   cd parp1_stability_5ws1
   ```

3. **Download the CSV and the repair log:**
   ```
   scp s242701@pupil4.healthtech.dtu.dk:/home/projects/22117_protein_structure/projects/group12/mutatex_stability_5ws1/energies.csv .
   scp s242701@pupil4.healthtech.dtu.dk:/home/projects/22117_protein_structure/projects/group12/mutatex_stability_5ws1/5WS1A_clean.rsa .
   scp s242701@pupil4.healthtech.dtu.dk:/home/projects/22117_protein_structure/projects/group12/mutatex_stability_5ws1/repair/repair_5WS1A_clean_model0_checked/FoldXrun.log ./repair_FoldXrun.log
   ```

4. **Optional but useful — download the repaired PDB so you can compare in PyMOL:**
   ```
   scp s242701@pupil4.healthtech.dtu.dk:/home/projects/22117_protein_structure/projects/group12/mutatex_stability_5ws1/repair/repair_5WS1A_clean_model0_checked/5WS1A_clean_Repair.pdb .
   ```

5. **Open `energies.csv` in Excel.** This is the raw data you'll cite. Send it to me when ready and I'll rewrite the Methods, Results and Discussion sections around the new dataset.

---

## Troubleshooting

**`mutatex: command not found`** → conda environment not active. Re-run `conda activate /home/ctools/protein_structure_course`.

**Repair fails, FoldX complains about missing residues** → check your PDB for gaps in the resolved residues. 5WS1 is mostly complete; if there are gaps inside the structure, MutateX warns but continues. Gaps at the very start/end (N/C terminus) are fine. If gaps are *inside* the chain near one of your variant positions, drop that variant.

**`naccess: command not found`** → same fix as above.

**Job seems stuck** → run `tail -f nohup.out`. If the last log line is from >30 min ago and `pgrep -u s242701 foldx` shows no FoldX process, the job died. Check `nohup.out` for an error message and re-run.

**SSH disconnected before "All done!"** → that's fine, the calculation keeps running thanks to `nohup`. SSH back in and check with `tail nohup.out`.

**ddg2excel warns about Zinc** → ignore. Standard warning when a metal ion is in the structure (5WS1 has a Zn).

**The numbers in your CSV use structural numbering (e.g. row labelled "R 219")** → that's expected. When you write up Results, use UniProt numbering for clarity (R878W, not R219W) and just say once in Methods that "5WS1 uses an offset of 659 (structural = UniProt − 659)".

---

When you're done, send me the new `energies.csv` and your NACCESS RSA values and I'll rewrite the Methods, Results, and Discussion sections to use the expanded dataset. The Discussion will write itself once you have 9 variants instead of 3.

