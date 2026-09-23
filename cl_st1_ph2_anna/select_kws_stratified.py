#!/usr/bin/env python3
"""
select_kws_stratified.py

Selects all *positive* keywords (POSKW) from key-lemma tables produced upstream
(e.g., by `keylemmas.py`), without per-stratum quotas or human-weighting.

What it does
------------
1) Reads every `*.txt` key-lemma file in a user-specified input directory
   (one file per stratum/subcorpus).
2) Extracts lemmas whose final column is `POSKW`, applying additional filters:
   - drop lemmas containing Unicode punctuation
   - drop lemmas containing any digits
   - drop lemmas containing any uppercase letters (keep lowercase-only)
3) Writes outputs to a user-specified output directory:
   - one file per stratum: `<stratum>.txt` (all filtered POSKW lemmas in file order)
   - one consolidated, de-duplicated list: `keywords.txt` (alphabetical)

Typical usage
-------------
python select_kws_stratified.py \
    --input-dir corpus/08_keylemmas \
    --output-dir corpus/09_kw_selected
"""

import os
import glob
import unicodedata
import argparse

# -----------------------------------------------------------
# Helpers
# -----------------------------------------------------------

def contains_punctuation(s: str) -> bool:
    """Return True if any character in s is Unicode punctuation."""
    return any(unicodedata.category(ch).startswith("P") for ch in s)


def load_poskw(filepath: str):
    """
    Load POSKW lemmas from a keylemma file.
    Skips header, punctuation, digits, uppercase.
    Returns lemmas in file order.
    """
    lemmas = []
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()[1:]  # skip header

    for line in lines:
        parts = line.strip().split()
        if len(parts) < 2:
            continue
        lemma, status = parts[0], parts[-1]

        # filtering criteria
        if status != "POSKW":
            continue
        if contains_punctuation(lemma):
            continue
        if any(ch.isdigit() for ch in lemma):
            continue
        if any(ch.isupper() for ch in lemma):
            continue

        lemmas.append(lemma)

    return lemmas


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description=(
            "Select all filtered POSKW lemmas from key-lemma tables, "
            "without quotas or human-weighting."
        )
    )
    parser.add_argument(
        "--input-dir",
        required=True,
        help="Directory containing key-lemma .txt files (one per stratum).",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Directory where per-stratum and consolidated keyword lists will be written.",
    )
    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = args.output_dir

    os.makedirs(output_dir, exist_ok=True)

    # Load all strata
    strata = {}
    pattern = os.path.join(input_dir, "*.txt")
    filepaths = sorted(glob.glob(pattern))

    if not filepaths:
        print(f"No .txt key-lemma files found in: {input_dir}")
        return

    print(f"Reading key-lemma files from: {input_dir}")
    for filepath in filepaths:
        name = os.path.basename(filepath).replace(".txt", "")
        strata[name] = load_poskw(filepath)
        print(f"  {name:<20} → loaded {len(strata[name])} POSKW lemmas (after filtering)")

    # Per-stratum selection is now simply "all filtered lemmas"
    selected_by_stratum = strata

    # Build consolidated list (no quotas, no special ordering beyond filename sort)
    consolidated = []
    for name in sorted(selected_by_stratum):
        consolidated.extend(selected_by_stratum[name])

    unique_lemmas = sorted(set(consolidated))
    total_count = len(consolidated)
    unique_count = len(unique_lemmas)

    print("\n=== Keyword Summary ===")
    print(f"Total POSKW lemmas (incl. duplicates): {total_count}")
    print(f"Unique POSKW lemmas:                  {unique_count}")
    print(f"Duplicates removed in consolidated:   {total_count - unique_count}")
    print("=======================\n")

    # Write per-stratum outputs
    for name, words in sorted(selected_by_stratum.items()):
        outpath = os.path.join(output_dir, f"{name}.txt")
        with open(outpath, "w", encoding="utf-8") as fout:
            for w in words:
                fout.write(w + "\n")
        print(f"Wrote {len(words):>5} lemmas → {outpath}")

    # Write consolidated (deduplicated, sorted)
    cons_path = os.path.join(output_dir, "keywords.txt")
    with open(cons_path, "w", encoding="utf-8") as fout:
        for w in unique_lemmas:
            fout.write(w + "\n")

    print(f"\nFinal unique keywords written: {len(unique_lemmas)} → {cons_path}")


if __name__ == "__main__":
    main()