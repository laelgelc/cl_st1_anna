#!/usr/bin/env python3
"""
Calculate corpus size for the tagged guideline corpus.

Expected input structure:
    corpus/07_tagged/<state>/<text_id>.txt

Example:
    corpus/07_tagged/ac/ac_ef_1.txt
    corpus/07_tagged/se/se_inf_1.txt

Expected tagged-file format:
    word<TAB>tag<TAB>lemma

Output:
    corpus_size/corpus_size.tsv

Output format:
    Header included
    Tab-separated
    Columns:
        Strata
        Text Count
        Word Count
"""

import re
from collections import defaultdict
from pathlib import Path


# --- Configuration ---
CORPUS_ROOT = Path("corpus/07_tagged")
OUTPUT_DIR = Path("corpus_size")
OUTPUT_FILE = OUTPUT_DIR / "corpus_size.tsv"

STATE_PATTERN = re.compile(r"^[a-z]{2}$")


def natural_sort_key(text):
    """Return a natural-sort key that treats digit runs as integers."""
    parts = re.split(r"(\d+)", str(text))
    return [int(part) if part.isdigit() else part.lower() for part in parts]


def is_state_folder(path: Path) -> bool:
    """Return True if path is a state-level tagged corpus folder."""
    return (
            path.is_dir()
            and STATE_PATTERN.match(path.name)
            and not path.name.startswith("_")
            and not path.name.startswith(".")
    )


def is_countable_token(word: str, tag: str) -> bool:
    """
    Return True if a tagged line should count as a word/token.

    Punctuation, symbols, and numeric-only tokens are excluded.
    Unicode alphabetic words, including accented Portuguese words, are included.
    """
    if not word:
        return False

    if not word[0].isalpha():
        return False

    if tag.startswith(("PUNCT", "SYM")):
        return False

    return True


def count_tokens_in_tagged_file(path: Path) -> int:
    """
    Count token lines in a TreeTagger output file.

    Each valid tagged token line counts as one word/token.
    """
    words = 0

    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            parts = line.split("\t")

            if len(parts) < 3:
                parts = line.split()

            if len(parts) < 3:
                continue

            word, tag, _lemma = parts[:3]

            if is_countable_token(word, tag):
                words += 1

    return words


def main():
    total_files = 0
    total_words = 0

    file_counts_strata = defaultdict(int)
    word_counts_strata = defaultdict(int)

    if not CORPUS_ROOT.exists():
        raise FileNotFoundError(f"Corpus directory does not exist: {CORPUS_ROOT}")

    if not CORPUS_ROOT.is_dir():
        raise NotADirectoryError(f"Corpus path is not a directory: {CORPUS_ROOT}")

    strata_dirs = sorted(
        [
            path for path in CORPUS_ROOT.iterdir()
            if is_state_folder(path)
        ],
        key=lambda path: natural_sort_key(path.name),
    )

    if not strata_dirs:
        raise FileNotFoundError(
            f"No state folders found under {CORPUS_ROOT}. "
            "Expected folders such as ac, es, mg, sp, etc."
        )

    for strata_dir in strata_dirs:
        strata = strata_dir.name

        text_files = sorted(
            strata_dir.glob("*.txt"),
            key=lambda path: natural_sort_key(path.name),
        )

        for text_file in text_files:
            words = count_tokens_in_tagged_file(text_file)

            file_counts_strata[strata] += 1
            word_counts_strata[strata] += words

            total_files += 1
            total_words += words

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        f.write("Strata\tText Count\tWord Count\n")

        for strata in sorted(file_counts_strata, key=natural_sort_key):
            f.write(
                f"{strata}\t"
                f"{file_counts_strata[strata]}\t"
                f"{word_counts_strata[strata]}\n"
            )

        f.write("\n")
        f.write(f"overall\t{total_files}\t{total_words}\n")

    print(f"Corpus sizes saved to {OUTPUT_FILE}")
    print(f"Total texts: {total_files}")
    print(f"Total words: {total_words}")


if __name__ == "__main__":
    main()