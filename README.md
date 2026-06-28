# Synergy_TP

A six-task Python project repository completed as part of the **Synergy — Software/ML Domain Taskphase**. Tasks cover Linux fundamentals, Python scripting, CSV parsing, data cleaning, visualization, and a conceptual technical report.

---

## Repository Structure

```
Synergy_TP/
├── .gitignore                            ← Excludes venv, __pycache__, system files
├── README.md                             ← You are here
├── venv/                                 ← Local virtual environment (not tracked by Git)
│
├── task_1/                               ← Linux & Python environment setup
│   ├── README.md
│   ├── requirements.txt
│   ├── setup_log.md                      ← Exact commands used during setup
│   ├── linux_commands.md                 ← 16 Linux CLI commands documented
│   ├── src/
│   │   └── hello.py                      ← Python script using requests library
│   └── data/
│       └── sample.txt                    ← Sample file for Linux command demos
│
├── task_2/                               ← Student submission analyzer
│   ├── README.md
│   ├── requirements.txt
│   ├── src/
│   │   ├── analyzer.py                   ← 6 core analysis functions with type hints
│   │   └── main.py                       ← CLI entry point and terminal output
│   ├── data/
│   │   └── submissions.csv               ← Input: student submission data
│   └── output/
│       └── .gitkeep
│
├── task_3/                               ← Manual CSV parser vs pandas comparison
│   ├── README.md
│   ├── src/
│   │   ├── manual_parser.py              ← Pure file I/O parser (no csv, no pandas)
│   │   ├── pandas_parser.py              ← Same analysis using pandas
│   │   └── main.py                       ← Runs both, compares, writes report
│   ├── data/
│   │   └── submissions.csv               ← Input: same format as task_2
│   └── output/
│       ├── manual_summary.json           ← Summary from manual parser
│       ├── pandas_summary.json           ← Summary from pandas parser
│       └── comparison_report.md          ← Differences and observations
│
├── task_4/                               ← Messy CSV data cleaning pipeline
│   ├── README.md
│   ├── requirements.txt
│   ├── src/
│   │   ├── clean_data.py                 ← 9 cleaning functions (one per concern)
│   │   ├── validate_data.py              ← 17 post-cleaning validation checks
│   │   └── main.py                       ← Orchestrates clean → validate → report
│   ├── data/
│   │   └── messy_students.csv            ← Raw input with duplicates, mixed units, typos
│   └── output/
│       ├── cleaned_students.csv          ← Final cleaned dataset
│       ├── summary_before.json           ← Stats before cleaning
│       ├── summary_after.json            ← Stats after cleaning
│       └── cleaning_report.md            ← Full cleaning decisions log
│
├── task_5/                               ← Matplotlib visualizations
│   ├── README.md
│   ├── requirements.txt
│   ├── src/
│   │   ├── visualize.py                  ← 4 plotting functions (matplotlib only)
│   │   └── main.py                       ← Loads task_4 output, generates 3 plots
│   └── output/
│       ├── domain_average_score.png      ← Bar chart: avg score by domain
│       ├── attendance_vs_score.png       ← Scatter: attendance % vs score
│       ├── submission_status_count.png   ← Bar chart: submitted vs not submitted
│       └── plot_summary.md               ← Written explanation of each plot
│
└── task_6/                               ← Conceptual technical report
    ├── README.md
    ├── report/
    │   ├── Software_ML_Taskphase_Report.pdf   ← Final submission (PDF)
    │   └── Software_ML_Taskphase_Report.docx  ← Source document (DOCX)
    └── assets/                                ← Figures or tables used in report
```

---

## Task 1 — Python Virtual Environment & Linux Basics

**Goal:** Set up a Python project with a virtual environment, manage dependencies, and document 16 Linux CLI commands.

**Key concepts:** `venv`, `pip freeze`, `.gitignore`, `pwd/ls/cd/mkdir/grep/chmod/find` and more.

**Run:**
```bash
source venv/bin/activate
pip install -r task_1/requirements.txt
python task_1/src/hello.py
```

**Expected output:**
```
Hello, Synergy_TP!
Python virtual environment is working correctly.
requests library version: 2.31.0
```

---

## Task 2 — Student Submission Analyzer

**Goal:** Read student data from CSV, compute summary statistics, and write a JSON report. Built with type hints, exception handling, and stdlib only.

**Key concepts:** Functions with type hints, `csv.DictReader`, `json.dump`, exception handling, `sys.argv`.

**Run:**
```bash
python task_2/src/main.py task_2/data/submissions.csv task_2/output/summary.json
```

**Outputs:** `task_2/output/summary.json`

---

## Task 3 — Manual CSV Parser vs Pandas

**Goal:** Parse the same CSV file twice — once using raw `open()` and string operations, once with pandas — and compare outputs.

**Key concepts:** Manual line iteration, `str.split(',')`, `setdefault` groupby, `pd.read_csv()`, `groupby().mean()`.

**Run:**
```bash
python task_3/src/main.py task_3/data/submissions.csv
```

**Outputs:** `manual_summary.json`, `pandas_summary.json`, `comparison_report.md`

---

## Task 4 — Messy CSV Data Cleaning

**Goal:** Systematically clean a broken dataset with duplicates, mixed units, word-form numbers, out-of-range values, and inconsistent categories.

**Key concepts:** One function per cleaning concern, median imputation, lookup-table standardization, unit normalization, post-cleaning validation.

**Run:**
```bash
python task_4/src/main.py task_4/data/messy_students.csv task_4/output/cleaned_students.csv
```

**Outputs:** `cleaned_students.csv`, `summary_before.json`, `summary_after.json`, `cleaning_report.md`

---

## Task 5 — Matplotlib Visualizations

**Goal:** Generate 3 plots from the Task 4 cleaned data using only matplotlib.

**Plots:**
- Bar chart: average score by domain
- Scatter plot: attendance % vs score (coloured by submission status)
- Bar chart: submitted vs not submitted count

**Run:**
```bash
python task_5/src/main.py task_4/output/cleaned_students.csv task_5/output
```

**Outputs:** `domain_average_score.png`, `attendance_vs_score.png`, `submission_status_count.png`

---

## Task 6 — Conceptual Technical Report

**Goal:** A 10-page formal report covering the theory, design decisions, and observations behind Tasks 1–5. Written in Times New Roman, A4, with 2 formatted tables and 7 references.

**Report file:**
```
task_6/report/Software_ML_Taskphase_Report.pdf
```

**Sections:** Abstract · Introduction · Development Environment · Python & File Handling · CSV Parsing & Pandas · Data Cleaning · Visualization · Reflection · Conclusion · References

---

## Quick Start

```bash
# 1. Clone
git clone https://github.com/blackfang007/Synergy_TP.git
cd Synergy_TP

# 2. Virtual environment
python3 -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# 3. Install all dependencies
pip install requests pandas matplotlib

# 4. Run all tasks in order
python task_1/src/hello.py
python task_2/src/main.py task_2/data/submissions.csv task_2/output/summary.json
python task_3/src/main.py task_3/data/submissions.csv
python task_4/src/main.py task_4/data/messy_students.csv task_4/output/cleaned_students.csv
python task_5/src/main.py task_4/output/cleaned_students.csv task_5/output
```

---

## Author

**Siddeshwar** | MIT Manipal — Mathematics and Computing
GitHub: [@blackfang007](https://github.com/blackfang007) | Repository: [Synergy_TP](https://github.com/blackfang007/Synergy_TP) | Branch: `main`