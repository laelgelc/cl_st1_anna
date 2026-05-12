#!/usr/bin/env python3
import os
import time
import subprocess
import multiprocessing
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm


# ---------------------------------------------------------
# Worker
# ---------------------------------------------------------
def tag_file(task):
    infile, outfile = task
    os.makedirs(os.path.dirname(outfile), exist_ok=True)

    start = time.time()
    with open(infile, "r", encoding="utf-8") as fin, \
            open(outfile, "w", encoding="utf-8") as fout:
        subprocess.run(
            ["tree-tagger-portuguese2"],
            stdin=fin, stdout=fout, check=True
        )
    return infile, time.time() - start


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------
def main():

    INPUT_BASE = Path("corpus/02_extracted")
    OUTPUT_BASE = Path("corpus/07_tagged")
    OUTPUT_BASE.mkdir(parents=True, exist_ok=True)

    # Gather all immediate subfolders under corpus/02_extracted (e.g., es, mg, rj, sp)
    folders = sorted([p for p in INPUT_BASE.iterdir() if p.is_dir()])
    if not folders:
        print("No folders found under corpus/02_extracted. Exiting.")
        return

    tasks = []

    # Collect files and map each to mirrored output subfolder
    for folder in folders:
        # folder.name examples:
        #   "es", "mg", "rj", "sp"
        out_subfolder = OUTPUT_BASE / folder.name

        for infile in sorted(folder.glob("*.txt")):
            outfile = out_subfolder / infile.name
            tasks.append((str(infile), str(outfile)))

    total = len(tasks)
    if total == 0:
        print("No text files to tag under corpus/02_extracted. Exiting.")
        return

    print(f"Total files to tag: {total}\n")
    print(f"Input root directory: {INPUT_BASE}")
    print(f"Output root directory: {OUTPUT_BASE}\n")

    # Determine number of workers
    n_workers = max(1, multiprocessing.cpu_count() - 1)
    print(f"Using {n_workers} workers...\n")

    # Run parallel tagging
    with ProcessPoolExecutor(max_workers=n_workers) as executor:
        for infile, elapsed in tqdm(
                executor.map(tag_file, tasks),
                total=total,
                desc="Tagging files",
                unit="file"):
            print(f"✓ {os.path.basename(infile)} tagged in {elapsed:.1f}s")

    print("\nAll tagging complete.\n")


if __name__ == "__main__":
    main()