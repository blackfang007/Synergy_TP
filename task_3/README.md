# Task 3 — Manual CSV Parser and Pandas Comparison

## Objective

Build a CSV parser manually using only Python file I/O (no `csv` module, no pandas), then repeat the same analysis using pandas. Compare both outputs and produce a report explaining the differences and trade-offs.

---

## Folder Structure

```
task_3/
├── README.md
├── data/
│   └── submissions.csv        ← Input student data
├── output/
│   ├── manual_summary.json    ← Summary from manual parser
│   ├── pandas_summary.json    ← Summary from pandas parser
│   └── comparison_report.md  ← Comparison and observations
└── src/
    ├── manual_parser.py       ← Pure file I/O parser (no csv, no pandas)
    ├── pandas_parser.py       ← Pandas-based parser
    └── main.py                ← Entry point and report writer
```

---

## Required Packages

```
pandas
```

Install with:
```bash
pip install -r task_3/requirements.txt
```

---

## Setup Instructions

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
python task_3/src/main.py task_3/data/submissions.csv
```

---

## Expected Terminal Output

```
=======================================================
     Task 3 — Manual CSV Parser vs Pandas
=======================================================

[1/4] Running manual parser...
      Manual summary written → task_3/output/manual_summary.json

[2/4] Running pandas parser...
      Pandas summary written  → task_3/output/pandas_summary.json

[3/4] Comparing outputs...
      ✅ Both parsers produced identical results.

[4/4] Writing comparison report...
      Report written              → task_3/output/comparison_report.md

-------------------------------------------------------
  Results (Manual Parser)
-------------------------------------------------------
  Total students      : 7
  Submitted           : 5
  Missing             : 2
  Average score       : 4.86
  Highest scorer      : Isha (9)
  Missing names       : Kabir, Dev
  Below 5             : Kabir, Rohan, Dev

=======================================================
  Task 3 complete.
=======================================================
```

---

## Expected Output Files

| File | Description |
|---|---|
| `output/manual_summary.json` | JSON summary produced by the manual parser |
| `output/pandas_summary.json` | JSON summary produced by the pandas parser |
| `output/comparison_report.md` | Markdown report comparing both outputs |

---

## Implemented Logic

### manual_parser.py
- Opens the CSV using `open()` and iterates line by line
- Strips whitespace and skips empty or malformed rows
- Splits each line on commas — no `csv` module used
- Converts types manually: `int()` for score, string comparison for submitted
- Computes all summary statistics using plain Python loops and list comprehensions

### pandas_parser.py
- Loads the CSV in one call using `pd.read_csv()`
- Uses `pd.to_numeric()` with `errors='coerce'` for safe type conversion
- Computes statistics using pandas aggregation methods: `.mean()`, `.groupby()`, `.idxmax()`

### main.py
- Runs both parsers on the same input file
- Compares outputs field by field
- Writes a structured markdown comparison report with observations

---

*Author: Siddeshwar | Branch: `main` | Repository: [Synergy_TP](https://github.com/blackfang007/Synergy_TP)*