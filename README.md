# Synergy_TP

A two-task Python project repository covering Linux CLI fundamentals, virtual environment setup, and core Python programming concepts including file I/O, data analysis, type hints, and exception handling.

---

## Repository Structure

```
Synergy_TP/
├── .gitignore              ← Excludes venv, __pycache__, system files
├── README.md               ← You are here
├── venv/                   ← Local virtual environment (not tracked by Git)
├── task_1/                 ← Linux & Python environment setup
│   ├── README.md
│   ├── requirements.txt
│   ├── setup_log.md
│   ├── linux_commands.md
│   ├── src/
│   │   └── hello.py
│   └── data/
│       └── sample.txt
└── task_2/                 ← Python data analysis program
    ├── README.md
    ├── requirements.txt
    ├── src/
    │   ├── analyzer.py
    │   └── main.py
    ├── data/
    │   └── submissions.csv
    └── output/
        └── summary.json
```

---

## Task 1 — Python Virtual Environment & Linux Basics

### Overview
Set up a clean Python project using a virtual environment, manage dependencies with `pip`, write a basic Python script, and document essential Linux command-line operations.

### Key Concepts Covered
- Creating and activating a Python `venv`
- Installing packages and generating `requirements.txt` via `pip freeze`
- Writing a Python script that uses an installed library
- Configuring `.gitignore` to exclude the virtual environment and cache files
- Documenting 16 Linux CLI commands: `pwd`, `ls`, `ls -la`, `cd`, `mkdir`, `touch`, `cat`, `echo`, `cp`, `mv`, `rm`, `grep`, `find`, `head`, `tail`, `wc`, `chmod`

### Run

```bash
# Activate virtual environment first
source venv/bin/activate          # Linux / macOS
venv\Scripts\activate             # Windows

# Install dependencies
pip install -r task_1/requirements.txt

# Run the script
python task_1/src/hello.py
```

### Expected Output

```
Hello, Synergy_TP!
Python virtual environment is working correctly.
requests library version: 2.31.0
```

### Files
| File | Description |
|---|---|
| `src/hello.py` | Python script demonstrating venv and package usage |
| `requirements.txt` | Pinned pip dependencies |
| `setup_log.md` | Step-by-step commands used during setup |
| `linux_commands.md` | 16 Linux CLI commands with usage and output |
| `data/sample.txt` | Sample text file used in Linux command demos |

---

## Task 2 — Python Recap: Student Submission Analyzer

### Overview
A Python program that reads student submission data from a CSV file and generates a structured JSON summary report. Built using functions, lists, dictionaries, file I/O, exception handling, and type hints — entirely with the Python standard library.

### Key Concepts Covered
- Functions with full **argument and return type hints**
- **CSV reading** with `csv.DictReader` and row-level validation
- **JSON writing** with `json.dump`
- **Exception handling** for missing files, invalid scores, empty CSVs, and missing output directories
- CLI argument parsing with `sys.argv`

### Run

```bash
python task_2/src/main.py task_2/data/submissions.csv task_2/output/summary.json
```

### Expected Output

```
=======================================================
       Student Submission Analyzer — Task 2
=======================================================

  Total students       : 7
  Submitted            : 5
  Missing submissions  : 2
  Average score        : 4.86
  Highest scorer       : Isha (9)
  Lowest scorer (submitted): Rohan (4)

  Missing submissions  : Kabir, Dev
  Scoring below 5      : Kabir, Rohan, Dev

  Domain-wise averages :
    ML              : 5.0
    Web             : 5.0
    Electronics     : 9.0
    Mechanical      : 0.0

  Summary written to   : task_2/output/summary.json

=======================================================
  Analysis complete.
=======================================================
```

### Functions in analyzer.py
| Function | Description |
|---|---|
| `read_submissions` | Reads and validates CSV into a list of dicts |
| `get_submitted_students` | Filters students who submitted |
| `calculate_average_score` | Computes mean score |
| `get_domain_wise_average` | Returns per-domain average as a dict |
| `get_missing_submissions` | Returns names of non-submitters |
| `write_summary` | Writes summary dict to a JSON file |

### Files
| File | Description |
|---|---|
| `src/analyzer.py` | All 6 core analysis functions with type hints |
| `src/main.py` | CLI entry point and terminal output |
| `data/submissions.csv` | Input student data |
| `output/summary.json` | Generated JSON report |

---

## Quick Start (Both Tasks)

```bash
# 1. Clone the repository
git clone https://github.com/blackfang007/Synergy_TP.git
cd Synergy_TP

# 2. Create and activate the virtual environment
python3 -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# 3. Run Task 1
pip install -r task_1/requirements.txt
python task_1/src/hello.py

# 4. Run Task 2 (no extra installs needed)
python task_2/src/main.py task_2/data/submissions.csv task_2/output/summary.json
```

---

## Author

**Siddeshwar** | GitHub: [@blackfang007](https://github.com/blackfang007)
Repository: [Synergy_TP](https://github.com/blackfang007/Synergy_TP) | Branch: `main`