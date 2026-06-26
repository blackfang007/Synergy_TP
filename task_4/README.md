# Task 4 — Messy CSV Cleaning

## Objective

Clean a deliberately messy CSV dataset using pandas. Handle duplicates, inconsistent units, word-form numbers, out-of-range values, and mixed formatting — with one function per cleaning concern. Produce a clean dataset, before/after summaries, and a written cleaning report.

---

## Folder Structure

```
task_4/
├── README.md
├── data/
│   └── messy_students.csv         ← Raw messy input
├── output/
│   ├── cleaned_students.csv       ← Cleaned output
│   ├── summary_before.json        ← Stats before cleaning
│   ├── summary_after.json         ← Stats after cleaning
│   └── cleaning_report.md         ← Full cleaning decisions log
└── src/
    ├── clean_data.py              ← All cleaning functions
    ├── validate_data.py           ← Post-cleaning validation
    └── main.py                    ← Entry point
```

---

## Setup

```bash
git clone https://github.com/blackfang007/Synergy_TP.git
cd Synergy_TP
python3 -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
pip install pandas
```

---

## Run Command

From the `Synergy_TP` root:

```bash
python task_4/src/main.py task_4/data/messy_students.csv task_4/output/cleaned_students.csv
```

---

## Expected Terminal Output

```
=======================================================
     Task 4 — Messy CSV Cleaner
=======================================================

[1/5] Loading data...
      Loaded 11 rows × 9 columns.
      Before summary written → task_4/output/summary_before.json

[2/5] Cleaning data...
  [remove_duplicates] Removed 1 duplicate row(s).
  [clean_attendance] 2 out-of-range value(s) replaced with NaN.
  [clean_attendance] 3 missing value(s) filled with median (88.0).
  [clean_scores] 1 missing/invalid score(s) filled with median (7.0).
  [clean_weight] 1 missing value(s) filled with median (58.0).
      Cleaning complete. 10 rows remain.
      After summary written  → task_4/output/summary_after.json

[3/5] Validating cleaned data...
  [✅ PASS] No duplicate student_id
  [✅ PASS] attendance_percent numeric and 0–100
  ... (17 checks total — all pass)

[4/5] Saving cleaned CSV...
      Cleaned data saved → task_4/output/cleaned_students.csv

[5/5] Writing cleaning report...
      Report written → task_4/output/cleaning_report.md

=======================================================
  Rows before : 11
  Rows after  : 10
  Duplicates  : 1 removed
  Validation  : ✅ PASSED
=======================================================
```

---

## Cleaning Steps Summary

| Step | Function | Problem Fixed |
|---|---|---|
| 1 | `remove_duplicates` | S005 (Rohan) appeared twice |
| 2 | `standardize_domains` | 8 domain variants → 4 canonical values |
| 3 | `clean_attendance` | `%` suffix, -10 and 105% out-of-range, blanks |
| 4 | `clean_scores` | `nine` word-form, blank score for S009 |
| 5 | `clean_study_hours` | `two` word-form |
| 6 | `clean_height` | Mixed `cm` and `m` units → all `height_cm` |
| 7 | `clean_weight` | Inconsistent `kg` suffix → all `weight_kg` |
| 8 | `clean_submitted` | `yes/Yes/Y` and `no/N` → uniform `yes`/`no` |
| 9 | `handle_missing_values` | Final NaN sweep with median/mode imputation |

---

## Validation Checks (17 total)

All checks in `validate_data.py` must pass before the output is saved:
- No duplicate `student_id`
- `attendance_percent` numeric and 0–100
- `score`, `study_hours`, `height_cm`, `weight_kg` numeric and non-negative
- `submitted` contains only `yes` or `no`
- `domain` contains only `ML`, `Web`, `Electronics`, or `Mechanical`
- No NaN in any critical column

---

*Author: Siddeshwar | Branch: `main` | Repository: [Synergy_TP](https://github.com/blackfang007/Synergy_TP)*