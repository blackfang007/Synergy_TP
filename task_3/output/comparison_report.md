# Task 3 — CSV Parser Comparison Report

## Overview

This report compares the output of the manual CSV parser (pure file I/O) with the
pandas-based parser across the same dataset and the same summary calculations.

---

## Manual Parser Summary

- Total students       : 7
- Submitted            : 5
- Missing submissions  : 2
- Average score        : 4.86
- Highest scorer       : Isha (9)
- Missing names        : Kabir, Dev
- Students below 5     : Kabir, Rohan, Dev
- Domain averages      : {'ML': 5.0, 'Web': 5.0, 'Electronics': 9.0, 'Mechanical': 0.0}

---

## Pandas Parser Summary

- Total students       : 7
- Submitted            : 5
- Missing submissions  : 2
- Average score        : 4.86
- Highest scorer       : Isha (9)
- Missing names        : Kabir, Dev
- Students below 5     : Kabir, Rohan, Dev
- Domain averages      : {'Electronics': 9.0, 'ML': 5.0, 'Mechanical': 0.0, 'Web': 5.0}

---

## Comparison Result:  MATCH

Both parsers produced **identical results** across all fields.

---

## Key Observations

1. **Manual parsing** reads the file line by line using `open()` and `str.split(',')`,
   giving full visibility into how raw text becomes structured data.
2. **Pandas parsing** uses `pd.read_csv()`, which handles encoding, type inference,
   and missing values automatically with far less code.
3. Both approaches produce the same numerical results when the input is clean.
4. Manual parsing requires explicit type conversion and row validation; pandas handles
   these in a single `read_csv()` call with `dtype` or `errors='coerce'` options.
5. For large datasets, pandas is significantly faster due to vectorized C-level operations.
   Manual parsing scales poorly as row count grows.
