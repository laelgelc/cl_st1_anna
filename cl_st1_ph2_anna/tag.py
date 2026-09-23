#!/usr/bin/env python3

import multiprocessing
import os
import subprocess
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

from tqdm import tqdm


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------
INPUT_BASE = Path("corpus/02_extracted")
OUTPUT_BASE = Path("corpus/07_tagged")
INPUT_EXTENSION = ".md"
OUTPUT_EXTENSION = ".txt"


# ---------------------------------------------------------
# Helpers
# ---------------------------------------------------------
def is_corpus_folder(path: Path) -> bool:
    """Return True if path is an input corpus group folder."""
    return (
            path.is_dir()
            and not path.name.startswith("_")
            and not path.name.startswith(".")
    )


def gather_tasks(input_base: Path, output_base: Path) -> list[tuple[str, str]]:
    """Collect input/output file pairs for tagging."""
    folders = sorted(p for p in input_base.iterdir() if is_corpus_folder(p))

    if not folders:
        return []

    print("Corpus folders to process:")
    for folder in folders:
        print(f"  - {folder.name}")
    print()

    tasks = []

    for folder in folders:
        out_subfolder = output_base / folder.name

        for infile in sorted(folder.glob(f"*{INPUT_EXTENSION}")):
            outfile = out_subfolder / f"{infile.stem}{OUTPUT_EXTENSION}"
            tasks.append((str(infile), str(outfile)))

    return tasks


def clean_text_for_treetagger(text: str) -> str:
    """Remove Markdown marker characters that should not be tagged as tokens."""
    return text.translate(str.maketrans("", "", "*#"))


# ---------------------------------------------------------
# Worker
# ---------------------------------------------------------
def tag_file(task: tuple[str, str]) -> tuple[str, float]:
    infile, outfile = task
    os.makedirs(os.path.dirname(outfile), exist_ok=True)

    start = time.time()

    with open(infile, "r", encoding="utf-8") as fin:
        text = fin.read()

    cleaned_text = clean_text_for_treetagger(text)

    with open(outfile, "w", encoding="utf-8") as fout:
        subprocess.run(
            ["tree-tagger-portuguese2"],
            input=cleaned_text,
            stdout=fout,
            text=True,
            check=True,
        )

    return infile, time.time() - start


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------
def main() -> None:
    OUTPUT_BASE.mkdir(parents=True, exist_ok=True)

    if not INPUT_BASE.exists():
        print(f"Input directory not found: {INPUT_BASE}")
        return

    tasks = gather_tasks(INPUT_BASE, OUTPUT_BASE)

    total = len(tasks)
    if total == 0:
        print(
            f"No Markdown files to tag under {INPUT_BASE} corpus folders. "
            "Exiting."
        )
        return

    print(f"Total files to tag: {total}\n")
    print(f"Input root directory: {INPUT_BASE}")
    print(f"Input extension: {INPUT_EXTENSION}")
    print(f"Output root directory: {OUTPUT_BASE}")
    print(f"Output extension: {OUTPUT_EXTENSION}")
    print("Characters removed before tagging: * #\n")

    n_workers = max(1, multiprocessing.cpu_count() - 1)
    print(f"Using {n_workers} workers...\n")

    with ProcessPoolExecutor(max_workers=n_workers) as executor:
        for infile, elapsed in tqdm(
                executor.map(tag_file, tasks),
                total=total,
                desc="Tagging files",
                unit="file",
        ):
            print(f"✓ {os.path.basename(infile)} tagged in {elapsed:.1f}s")

    print("\nAll tagging complete.\n")


if __name__ == "__main__":
    main()