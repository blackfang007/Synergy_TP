Task 1 — Python Virtual Environment & Linux Basics

Description

This folder contains Task 1 of the Synergy_TP project. The goal is to demonstrate:


Setting up a Python project using a virtual environment
Managing dependencies with pip and requirements.txt
Writing a basic Python script
Documenting essential Linux command-line operations
Maintaining a clean repository structure with .gitignore



Folder Structure

Synergy_TP/
├── .gitignore
└── task_1/
    ├── README.md               ← You are here
    ├── requirements.txt        ← Python dependencies
    ├── setup_log.md            ← Step-by-step setup commands
    ├── linux_commands.md       ← Linux CLI command reference
    ├── src/
    │   └── hello.py            ← Main Python script
    └── data/
        └── sample.txt          ← Sample data file


Prerequisites


Python 3.8 or higher
pip (comes with Python)
Git



Setup Instructions

1. Clone the Repository

bashgit clone https://github.com/blackfang007/Synergy_TP.git
cd Synergy_TP

2. Create the Virtual Environment

bashpython3 -m venv venv

3. Activate the Virtual Environment

On Linux / macOS:

bashsource venv/bin/activate

On Windows:

bashvenv\Scripts\activate

After activation, your terminal prompt will show (venv) at the beginning:

(venv) user@machine:~/Synergy_TP$

4. Install Dependencies

bashpip install -r task_1/requirements.txt

Expected output:

Successfully installed certifi-2024.2.2 charset-normalizer-3.3.2 idna-3.6 requests-2.31.0 urllib3-2.2.1


Running the Python Script

Run this command from the Synergy_TP repository root:

bashpython task_1/src/hello.py

Expected output:

Hello, Synergy_TP!
Python virtual environment is working correctly.
requests library version: 2.31.0


Deactivating the Virtual Environment

Once done, deactivate the virtual environment with:

bashdeactivate


Files Reference

FilePurposesrc/hello.pyMain Python script demonstrating venv and package usagerequirements.txtPinned list of installed Python packagessetup_log.mdExact commands used to set up this project from scratchlinux_commands.mdDocumentation of 16 essential Linux CLI commandsdata/sample.txtSample text file used for Linux command demonstrations


Notes


The venv/ folder is excluded from Git via .gitignore — always recreate it locally using the steps above.
The requirements.txt was generated using pip freeze > task_1/requirements.txt inside the active virtual environment.
All Linux commands in linux_commands.md were executed from the Synergy_TP root directory.



Author: Siddeshwar | Branch: main | Repository: Synergy_TP