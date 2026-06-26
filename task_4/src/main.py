import sys
import os
import json

sys.path.insert(0, os.path.dirname(__file__))

from clean_data import (
    load_data,
    generate_summary,
    remove_duplicates,
    standardize_domains,
    clean_attendance,
    clean_scores,
    clean_study_hours,
    clean_height,
    clean_weight,
    clean_submitted,
    handle_missing_values,
    save_cleaned_data,
)
from validate_data import validate_cleaned_data

# Derive output dir from output_path argument
def get_output_dir(output_csv_path: str) -> str:
    return os.path.dirname(os.path.abspath(output_csv_path))


def write_json(data: dict, path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def write_report(
    summary_before: dict,
    summary_after: dict,
    validation_passed: bool,
    report_path: str,
) -> None:
    
    os.makedirs(os.path.dirname(report_path), exist_ok=True)

    lines = [
        "# Task 4 — Data Cleaning Report\n",
        "## Overview\n",
        "This report documents every cleaning decision applied to `messy_students.csv`.",
        "Each section covers one cleaning step, the problem it addresses, the rule applied,",
        "and the justification for that rule.\n",
        "---\n",
        "## Before Cleaning\n",
        f"- Total rows         : {summary_before['total_rows']}",
        f"- Total columns      : {summary_before['total_columns']}",
        f"- Duplicate rows     : {summary_before['duplicate_rows']}",
        f"- Missing values     : {summary_before.get('missing_values', {})}",
        f"- Unique domains     : {summary_before.get('unique_domain', [])}",
        f"- Unique submitted   : {summary_before.get('unique_submitted', [])}\n",
        "---\n",
        "## After Cleaning\n",
        f"- Total rows         : {summary_after['total_rows']}",
        f"- Total columns      : {summary_after['total_columns']}",
        f"- Duplicate rows     : {summary_after['duplicate_rows']}",
        f"- Missing values     : {summary_after.get('missing_values', 'None')}",
        f"- Unique domains     : {summary_after.get('unique_domain', [])}",
        f"- Unique submitted   : {summary_after.get('unique_submitted', [])}\n",
        "---\n",
        "## Cleaning Steps\n",
        "### Step 1 — Remove Duplicates",
        "**Problem:** Row S005 (Rohan) appeared twice with identical values.",
        "**Rule:** `drop_duplicates()` keeping the first occurrence.",
        "**Justification:** Exact duplicates add no information and inflate row counts.",
        "Keeping the first occurrence is the safest default when no timestamp is available.\n",
        "### Step 2 — Standardize Domain Names",
        "**Problem:** The domain column had 8 variants for 4 logical categories:",
        "`ml`, `ML`, `MACHINE LEARNING`, `web`, `Web Dev`, `web development`, `electronics`, `Electronics`.",
        "**Rule:** Applied a lookup dictionary mapping all variants to their canonical form:",
        "- ml / ML / MACHINE LEARNING → ML",
        "- web / Web Dev / web development → Web",
        "- electronics / Electronics → Electronics",
        "- Mechanical → Mechanical",
        "**Justification:** Inconsistent casing and naming would cause incorrect groupby results in analysis.\n",
        "### Step 3 — Clean attendance_percent",
        "**Problem:** Values had mixed formats: `92%`, `88`, `-10`, `105%`, and blank.",
        "**Rule:**",
        "- Strip `%` suffix and convert to float.",
        "- Values below 0 or above 100 are physically impossible → replaced with NaN.",
        "- NaN values (including original blanks and invalidated values) → filled with column median.",
        "**Justification:** -10% and 105% attendance cannot exist. Median imputation is preferred over mean",
        "because it is robust to the outliers we just removed.\n",
        "### Step 4 — Clean score",
        "**Problem:** S004 (Isha) had score `nine` (word form). S009 (Omkar) had a blank score.",
        "**Rule:**",
        "- Word-form numbers (zero through ten) converted using a lookup table.",
        "- Remaining non-numeric values and blanks → NaN → filled with column median.",
        "**Justification:** Word-form numbers are unambiguous and should be preserved rather than dropped.\n",
        "### Step 5 — Clean study_hours",
        "**Problem:** S005 (Rohan) had study_hours `two` (word form).",
        "**Rule:** Same word-to-number lookup as scores. NaN → median fill.",
        "**Justification:** Consistent with the score cleaning approach.\n",
        "### Step 6 — Clean height → height_cm",
        "**Problem:** Heights were in two different units: `170 cm` and `1.62 m`.",
        "**Rule:**",
        "- Values ending in `cm` → strip unit, parse as float.",
        "- Values ending in `m` (metres) → strip unit, multiply by 100.",
        "- Column renamed from `height` to `height_cm` to make the unit explicit.",
        "- NaN → median fill.",
        "**Justification:** All heights must be in the same unit for any distance/similarity computation.",
        "Renaming the column prevents future unit ambiguity.\n",
        "### Step 7 — Clean weight → weight_kg",
        "**Problem:** Weights had inconsistent suffixes: `65 kg`, `55kg`, blank (S003).",
        "**Rule:** Strip `kg` suffix (with or without space), parse as float. NaN → median fill.",
        "**Justification:** Unit is already kilograms in all cases — only formatting was inconsistent.\n",
        "### Step 8 — Normalize submitted",
        "**Problem:** The submitted column had 5 variants: `yes`, `Yes`, `Y`, `no`, `N`.",
        "**Rule:**",
        "- yes / Yes / Y / true / 1 → 'yes'",
        "- no / N / false / 0 → 'no'",
        "- Missing or unrecognized → 'no' (conservative default).",
        "**Justification:** Consistent boolean representation is required for groupby and filtering.\n",
        "### Step 9 — Handle Remaining Missing Values",
        "**Problem:** After individual cleaning steps, some NaN values may remain.",
        "**Rule:** Numeric columns → median fill. Categorical columns → mode fill.",
        "Identity columns (name, student_id) → drop row.",
        "**Justification:** Dropping identity-less rows is safer than inventing a student ID.\n",
        "---\n",
        f"## Validation Result: {' ALL CHECKS PASSED' if validation_passed else ' SOME CHECKS FAILED'}\n",
        "All 9 validation criteria were checked programmatically after cleaning (see `validate_data.py`).\n",
        "---\n",
        "*Report generated automatically by task_4/src/main.py*",
    ]

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: python task_4/src/main.py <input_csv> <output_csv>")
        sys.exit(1)

    input_path  = sys.argv[1]
    output_path = sys.argv[2]
    output_dir  = get_output_dir(output_path)

    SUMMARY_BEFORE = os.path.join(output_dir, "summary_before.json")
    SUMMARY_AFTER  = os.path.join(output_dir, "summary_after.json")
    REPORT_PATH    = os.path.join(output_dir, "cleaning_report.md")

    print("=" * 55)
    print("     Task 4 — Messy CSV Cleaner")
    print("=" * 55)

   
    print("\n[1/5] Loading data...")
    try:
        df = load_data(input_path)
    except (FileNotFoundError, ValueError) as e:
        print(f"[Error] {e}")
        sys.exit(1)
    print(f"      Loaded {len(df)} rows × {len(df.columns)} columns.")

    
    summary_before = generate_summary(df)
    write_json(summary_before, SUMMARY_BEFORE)
    print(f"      Before summary written → {SUMMARY_BEFORE}")

    
    print("\n[2/5] Cleaning data...")
    df = remove_duplicates(df)
    df = standardize_domains(df)
    df = clean_attendance(df)
    df = clean_scores(df)
    df = clean_study_hours(df)
    df = clean_height(df)
    df = clean_weight(df)
    df = clean_submitted(df)
    df = handle_missing_values(df)

    
    col_order = ["student_id", "name", "domain", "attendance_percent",
                 "score", "study_hours", "height_cm", "weight_kg", "submitted"]
    df = df[[c for c in col_order if c in df.columns]]
    print(f"      Cleaning complete. {len(df)} rows remain.")

   
    summary_after = generate_summary(df)
    write_json(summary_after, SUMMARY_AFTER)
    print(f"      After summary written  → {SUMMARY_AFTER}")

    
    print("\n[3/5] Validating cleaned data...")
    validation_passed = validate_cleaned_data(df)

    
    print("\n[4/5] Saving cleaned CSV...")
    save_cleaned_data(df, output_path)

    
    print("\n[5/5] Writing cleaning report...")
    write_report(summary_before, summary_after, validation_passed, REPORT_PATH)
    print(f"      Report written          → {REPORT_PATH}")

    print("\n" + "=" * 55)
    print(f"  Rows before : {summary_before['total_rows']}")
    print(f"  Rows after  : {summary_after['total_rows']}")
    print(f"  Duplicates  : {summary_before['duplicate_rows']} removed")
    print(f"  Validation  : {'PASSED' if validation_passed else ' FAILED'}")
    print("=" * 55 + "\n")


if __name__ == "__main__":
    main()