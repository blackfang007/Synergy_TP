# Task 5 — Matplotlib Visualizations

## Objective

Generate three properly labelled plots from the cleaned dataset produced in Task 4. Uses only matplotlib — no seaborn. All plots are saved as PNG files using `savefig()`.

---

## Folder Structure

```
task_5/
├── README.md
├── output/
│   ├── domain_average_score.png      ← Bar chart: avg score by domain
│   ├── attendance_vs_score.png       ← Scatter: attendance % vs score
│   ├── submission_status_count.png   ← Bar chart: submitted vs not
│   └── plot_summary.md               ← Written explanation of each plot
└── src/
    ├── visualize.py                  ← All plotting functions
    └── main.py                       ← Entry point
```

---

## Dependency

Task 5 requires the cleaned CSV from Task 4. Run Task 4 first if not already done:

```bash
python task_4/src/main.py task_4/data/messy_students.csv task_4/output/cleaned_students.csv
```

---

## Setup

```bash
pip install pandas matplotlib
```

---

## Run Command

From the `Synergy_TP` root:

```bash
python task_5/src/main.py task_4/output/cleaned_students.csv task_5/output
```

---

## Expected Terminal Output

```
=======================================================
     Task 5 — Matplotlib Visualizations
=======================================================

[1/5] Loading cleaned data...
      Loaded 10 rows from 'task_4/output/cleaned_students.csv'.

[2/5] Generating Plot 1: Average Score by Domain...
  [plot 1] Saved → task_5/output/domain_average_score.png

[3/5] Generating Plot 2: Attendance vs Score...
  [plot 2] Saved → task_5/output/attendance_vs_score.png

[4/5] Generating Plot 3: Submission Status Count...
  [plot 3] Saved → task_5/output/submission_status_count.png

[5/5] Writing plot summary...
  [summary] Saved → task_5/output/plot_summary.md

=======================================================
  All outputs saved to: task_5/output
=======================================================
```

---

## Plots

| File | Type | What it shows |
|---|---|---|
| `domain_average_score.png` | Bar chart | Mean score per domain, sorted descending, value-labelled |
| `attendance_vs_score.png` | Scatter plot | Attendance % vs score, colour-coded by submission status, student name annotations |
| `submission_status_count.png` | Bar chart | Count of submitted (green) vs not submitted (red) students |

---

## Functions in visualize.py

| Function | Description |
|---|---|
| `load_cleaned_data` | Loads Task 4 output CSV with numeric type enforcement |
| `plot_domain_average_score` | Bar chart with value labels and grid |
| `plot_attendance_vs_score` | Scatter plot with legend and student name annotations |
| `plot_submission_status_count` | Bar chart with count labels, green/red colouring |
| `write_plot_summary` | Writes `plot_summary.md` with 3–5 line explanation per plot |

---

*Author: Siddeshwar | Branch: `main` | Repository: [Synergy_TP](https://github.com/blackfang007/Synergy_TP)*