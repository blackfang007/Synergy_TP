# Task 4 — Data Cleaning Report

## Overview

This report documents every cleaning decision applied to `messy_students.csv`.
Each section covers one cleaning step, the problem it addresses, the rule applied,
and the justification for that rule.

---

## Before Cleaning

- Total rows         : 11
- Total columns      : 9
- Duplicate rows     : 1
- Missing values     : {'attendance_percent': 1, 'score': 1, 'weight': 1}
- Unique domains     : ['ml', 'Web Dev', 'ML', 'electronics', 'web', 'MACHINE LEARNING', 'Mechanical', 'Electronics', 'web development']
- Unique submitted   : ['yes', 'Yes', 'no', 'Y', 'N']

---

## After Cleaning

- Total rows         : 10
- Total columns      : 9
- Duplicate rows     : 0
- Missing values     : {}
- Unique domains     : ['ML', 'Web', 'Electronics', 'Mechanical']
- Unique submitted   : ['yes', 'no']

---

## Cleaning Steps

### Step 1 — Remove Duplicates
**Problem:** Row S005 (Rohan) appeared twice with identical values.
**Rule:** `drop_duplicates()` keeping the first occurrence.
**Justification:** Exact duplicates add no information and inflate row counts.
Keeping the first occurrence is the safest default when no timestamp is available.

### Step 2 — Standardize Domain Names
**Problem:** The domain column had 8 variants for 4 logical categories:
`ml`, `ML`, `MACHINE LEARNING`, `web`, `Web Dev`, `web development`, `electronics`, `Electronics`.
**Rule:** Applied a lookup dictionary mapping all variants to their canonical form:
- ml / ML / MACHINE LEARNING → ML
- web / Web Dev / web development → Web
- electronics / Electronics → Electronics
- Mechanical → Mechanical
**Justification:** Inconsistent casing and naming would cause incorrect groupby results in analysis.

### Step 3 — Clean attendance_percent
**Problem:** Values had mixed formats: `92%`, `88`, `-10`, `105%`, and blank.
**Rule:**
- Strip `%` suffix and convert to float.
- Values below 0 or above 100 are physically impossible → replaced with NaN.
- NaN values (including original blanks and invalidated values) → filled with column median.
**Justification:** -10% and 105% attendance cannot exist. Median imputation is preferred over mean
because it is robust to the outliers we just removed.

### Step 4 — Clean score
**Problem:** S004 (Isha) had score `nine` (word form). S009 (Omkar) had a blank score.
**Rule:**
- Word-form numbers (zero through ten) converted using a lookup table.
- Remaining non-numeric values and blanks → NaN → filled with column median.
**Justification:** Word-form numbers are unambiguous and should be preserved rather than dropped.

### Step 5 — Clean study_hours
**Problem:** S005 (Rohan) had study_hours `two` (word form).
**Rule:** Same word-to-number lookup as scores. NaN → median fill.
**Justification:** Consistent with the score cleaning approach.

### Step 6 — Clean height → height_cm
**Problem:** Heights were in two different units: `170 cm` and `1.62 m`.
**Rule:**
- Values ending in `cm` → strip unit, parse as float.
- Values ending in `m` (metres) → strip unit, multiply by 100.
- Column renamed from `height` to `height_cm` to make the unit explicit.
- NaN → median fill.
**Justification:** All heights must be in the same unit for any distance/similarity computation.
Renaming the column prevents future unit ambiguity.

### Step 7 — Clean weight → weight_kg
**Problem:** Weights had inconsistent suffixes: `65 kg`, `55kg`, blank (S003).
**Rule:** Strip `kg` suffix (with or without space), parse as float. NaN → median fill.
**Justification:** Unit is already kilograms in all cases — only formatting was inconsistent.

### Step 8 — Normalize submitted
**Problem:** The submitted column had 5 variants: `yes`, `Yes`, `Y`, `no`, `N`.
**Rule:**
- yes / Yes / Y / true / 1 → 'yes'
- no / N / false / 0 → 'no'
- Missing or unrecognized → 'no' (conservative default).
**Justification:** Consistent boolean representation is required for groupby and filtering.

### Step 9 — Handle Remaining Missing Values
**Problem:** After individual cleaning steps, some NaN values may remain.
**Rule:** Numeric columns → median fill. Categorical columns → mode fill.
Identity columns (name, student_id) → drop row.
**Justification:** Dropping identity-less rows is safer than inventing a student ID.

---

## Validation Result:  ALL CHECKS PASSED

All 9 validation criteria were checked programmatically after cleaning (see `validate_data.py`).

---

*Report generated automatically by task_4/src/main.py*