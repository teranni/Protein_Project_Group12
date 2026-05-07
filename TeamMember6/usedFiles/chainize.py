#!/usr/bin/env python3

import sys

def add_chain_a(pdb_file):
    with open(pdb_file, 'r') as fh:
        for line in fh:
            line = line.rstrip("\n")
            if line.startswith("ATOM") or line.startswith("HETATM"):
                tmp = list(line)
                # Ensure the line is long enough
                if len(tmp) > 21:
                    tmp[21] = "A"  # Set chain ID to A
                line = "".join(tmp)
            print(line)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <pdb_file>")
        sys.exit(1)

    add_chain_a(sys.argv[1])
