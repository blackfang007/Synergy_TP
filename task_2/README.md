Task 2 — Python Recap: Student Submission Analyzer

Description

This folder contains Task 2 of the Synergy_TP project. The program reads student submission data from a CSV file and generates a structured summary report in JSON format.

It demonstrates:


Functions with type hints
List and dictionary operations
File I/O (CSV reading, JSON writing)
Exception handling (missing files, invalid data, empty CSVs)



Folder Structure

task_2/
├── README.md                  ← You are here
├── requirements.txt           ← Python dependencies (none — stdlib only)
├── data/
│   └── submissions.csv        ← Input: student submission data
├── output/
│   └── summary.json           ← Output: generated analysis report
└── src/
    ├── analyzer.py            ← Core analysis functions
    └── main.py                ← Entry point / CLI runner


Input Format

The input CSV file (data/submissions.csv) must have these columns:

ColumnTypeDescriptionnamestringStudent namedomainstringDomain (ML, Web, Electronics, etc.)taskstringTask identifier (e.g. Task1)scoreintScore achieved (0–10)submittedstringyes or no

Example:

csvname,domain,task,score,submitted
Aarav,ML,Task1,8,yes
Meera,Web,Task1,6,yes
Kabir,ML,Task1,0,no


Setup Instructions

1. Clone the Repository

bashgit clone https://github.com/blackfang007/Synergy_TP.git
cd Synergy_TP

2. Create and Activate the Virtual Environment

bashpython3 -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

3. Install Requirements

This task uses only Python standard library modules (csv, json, os, sys). No external packages are required.

bashpip install -r task_2/requirements.txt


Running the Program

Run this command from the Synergy_TP repository root:

bashpython task_2/src/main.py task_2/data/submissions.csv task_2/output/summary.json

Expected Terminal Output

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


Output Format

The program writes output/summary.json with this structure:

json{
    "total_students": 7,
    "submitted_count": 5,
    "missing_count": 2,
    "average_score": 4.86,
    "highest_scorer": {
        "name": "Isha",
        "domain": "Electronics",
        "score": 9
    },
    "lowest_scorer_submitted": {
        "name": "Rohan",
        "domain": "Web",
        "score": 4
    },
    "domain_wise_average": {
        "ML": 5.0,
        "Web": 5.0,
        "Electronics": 9.0,
        "Mechanical": 0.0
    },
    "missing_submissions": ["Kabir", "Dev"],
    "students_below_5": ["Kabir", "Rohan", "Dev"]
}


Functions in analyzer.py

FunctionDescriptionread_submissionsReads and validates the CSV file into a list of dictsget_submitted_studentsFilters students who submitted their workcalculate_average_scoreComputes mean score across a list of studentsget_domain_wise_averageReturns per-domain average score as a dictionaryget_missing_submissionsReturns names of students who did not submitwrite_summaryWrites the summary dict to a JSON file


Error Handling

ScenarioBehaviourInput CSV file not foundPrints a clear error message and exits with code 1CSV file is emptyRaises ValueError with a descriptive messageInvalid score value in a rowPrints a warning and skips that row; continuesOutput folder does not existAutomatically created using os.makedirs(exist_ok=True)Wrong number of CLI argumentsPrints usage instructions and exits with code 1


Author: Siddeshwar | Branch: main | Repository: Synergy_TP