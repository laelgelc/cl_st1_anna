#!/usr/bin/env python3
"""
Calculate corpus size for the tagged guideline corpus.

Expected input structure:
    corpus/07_tagged/<state>/<text_id>.txt

Example:
    corpus/07_tagged/ac/ac_ef_1.txt
    corpus/07_tagged/go/go_em_1.txt
    corpus/07_tagged/se/se_inf_1.txt

Expected tagged-file format:
    word<TAB>tag<TAB>lemma

Output:
    corpus_size/corpus_size.tsv
    corpus_size/corpus_size_ample.tsv, when --ample is used

Output format:
    Header included
    Tab-separated
    Columns:
        Strata
        Stage
        Text Count
        Word Count
"""

import argparse
import re
from collections import defaultdict
from pathlib import Path


# --- Configuration ---
CORPUS_ROOT = Path("corpus/07_tagged")
OUTPUT_DIR = Path("corpus_size")
OUTPUT_FILE = OUTPUT_DIR / "corpus_size.tsv"
OUTPUT_FILE_AMPLE = OUTPUT_DIR / "corpus_size_ample.tsv"

STATE_PATTERN = re.compile(r"^[a-z]{2}$")

STAGE_ORDER = [
    "inf",
    "inf_e_ef",
    "inf_ef",
    "ef",
    "ef_e_em",
    "em",
]

AMPLE_STAGE_ORDER = [
    "inf",
    "inf_10_camp_exp",
    "inf_12_camp_exp_escuta_fala",
    "inf_1_concepces",
    "inf_2_principios",
    "inf_3_direitos",
    "inf_4_planejamento",
    "inf_5_acolhimento",
    "inf_8_camp_exp",
    "inf_adaptacoes",
    "inf_agrupamentos",
    "inf_alfabetizar",
    "inf_apresentacao",
    "inf_aspectos_pedagogicos",
    "inf_avaliacao",
    "inf_cam_exp",
    "inf_camp_ex",
    "inf_camp_exp",
    "inf_campo_e_indigena",
    "inf_campo_exp",
    "inf_concepcao_de_infancia",
    "inf_curriculo",
    "inf_curriculo_e_ppp",
    "inf_direitos_de_aprendizagem",
    "inf_diversidade_etnico_racial",
    "inf_e_ef",
    "inf_e_ef_apresentacao",
    "inf_e_ef_intro",
    "inf_ef",
    "inf_espacos",
    "inf_final",
    "inf_finalidade",
    "inf_formacao_de_professores",
    "inf_formacao_leitora",
    "inf_funcao_social",
    "inf_inclusao",
    "inf_intro",
    "inf_intro_14_matriz_saberes",
    "inf_intro_16_temas_integradores",
    "inf_intro_19_dinamicas",
    "inf_intro_20_avaliacao",
    "inf_ludico",
    "inf_natureza",
    "inf_objetivos",
    "inf_organizacao",
    "inf_papel_do_professor",
    "inf_planejamento",
    "inf_principios",
    "inf_provinha",
    "inf_respeito_e_diversidade",
    "inf_trajetoria",
    "inf_transicoes",
    "ef",
    "ef_anos_finais_ciencias_da_natureza",
    "ef_anos_finais_linguagens_ingles",
    "ef_anos_iniciais_arte",
    "ef_anos_iniciais_ciencias_da_natureza",
    "ef_anos_iniciais_ciencias_humanas_geo",
    "ef_anos_iniciais_ciencias_humanas_historia",
    "ef_anos_iniciais_ciencias_humanas_intro",
    "ef_anos_iniciais_ensino_religioso",
    "ef_anos_iniciais_linguagens_arte",
    "ef_anos_iniciais_linguagens_ed_fis",
    "ef_anos_iniciais_linguagens_intro",
    "ef_anos_iniciais_linguagens_lp",
    "ef_anos_iniciais_matematica",
    "ef_ch_geo",
    "ef_ch_his",
    "ef_ciencias",
    "ef_ciencias_da_natureza",
    "ef_ciencias_da_natureza_intro",
    "ef_ciencias_humanas_geo",
    "ef_ciencias_humanas_his",
    "ef_ciencias_humanas_intro",
    "ef_ciencias_humas_intro",
    "ef_e_em_tema_integrador",
    "ef_ensino_religioso",
    "ef_er",
    "ef_intro",
    "ef_linguagens_arte",
    "ef_linguagens_ed_fis",
    "ef_linguagens_ingles",
    "ef_linguagens_intro",
    "ef_linguagens_lp",
    "ef_matematica",
    "ef_matematica_intro",
    "em",
]


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


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Calculate corpus size by state/stratum and stage."
    )

    parser.add_argument(
        "--ample",
        action="store_true",
        help=(
            "Use the ample stage categories and write output to "
            "corpus_size/corpus_size_ample.tsv."
        ),
    )

    return parser.parse_args()


def extract_stage_from_filename(path: Path, strata: str, stage_order: list[str]) -> str:
    """
    Extract the stage from a tagged filename.

    Examples:
        ac_ef_1.txt -> ef
        go_em_1.txt -> em
        se_inf_1.txt -> inf
        es_ef_anos_finais_linguagens_ingles_1.txt
            -> ef, without --ample
            -> ef_anos_finais_linguagens_ingles, with --ample
    """
    stem = path.stem
    prefix = f"{strata}_"

    if not stem.startswith(prefix):
        raise ValueError(
            f"Could not extract stage from {path}: "
            f"filename does not start with expected prefix {prefix!r}"
        )

    remainder = stem[len(prefix):]

    for stage in sorted(stage_order, key=len, reverse=True):
        if remainder == stage or remainder.startswith(f"{stage}_"):
            return stage

    raise ValueError(
        f"Could not extract a known stage from {path}. "
        f"Expected one of: {', '.join(stage_order)}"
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
    args = parse_args()

    stage_order = AMPLE_STAGE_ORDER if args.ample else STAGE_ORDER
    output_file = OUTPUT_FILE_AMPLE if args.ample else OUTPUT_FILE

    total_files = 0
    total_words = 0

    file_counts = defaultdict(int)
    word_counts = defaultdict(int)

    total_files_by_stage = defaultdict(int)
    total_words_by_stage = defaultdict(int)

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
            stage = extract_stage_from_filename(text_file, strata, stage_order)
            words = count_tokens_in_tagged_file(text_file)

            file_counts[(strata, stage)] += 1
            word_counts[(strata, stage)] += words

            total_files_by_stage[stage] += 1
            total_words_by_stage[stage] += words

            total_files += 1
            total_words += words

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with output_file.open("w", encoding="utf-8") as f:
        f.write("Strata\tStage\tText Count\tWord Count\n")

        for strata_dir in strata_dirs:
            strata = strata_dir.name

            for stage in stage_order:
                key = (strata, stage)

                if key not in file_counts:
                    continue

                f.write(
                    f"{strata}\t"
                    f"{stage}\t"
                    f"{file_counts[key]}\t"
                    f"{word_counts[key]}\n"
                )

        f.write("\n")

        for stage in stage_order:
            if stage not in total_files_by_stage:
                continue

            f.write(
                f"overall\t"
                f"{stage}\t"
                f"{total_files_by_stage[stage]}\t"
                f"{total_words_by_stage[stage]}\n"
            )

        f.write(f"overall\toverall\t{total_files}\t{total_words}\n")

    print(f"Corpus sizes saved to {output_file}")
    print(f"Total texts: {total_files}")
    print(f"Total words: {total_words}")


if __name__ == "__main__":
    main()