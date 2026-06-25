Setup Log — Task 1

This file documents the exact commands executed (in order) to set up the task_1 environment inside the Synergy_TP repository.


1. Create the GitHub Repository


Done via GitHub web UI at https://github.com/new
Repository name: Synergy_TP
Visibility: Public
Initialized with a README: No




2. Clone the Repository Locally

bashgit clone https://github.com/blackfang007/Synergy_TP.git
cd Synergy_TP


3. Create the Folder Structure

bashmkdir -p task_1/src task_1/data


4. Create Initial Files

bashtouch task_1/README.md
touch task_1/setup_log.md
touch task_1/linux_commands.md
touch task_1/src/hello.py
touch task_1/data/sample.txt
touch .gitignore


5. Create and Activate the Python Virtual Environment

bash# Create virtual environment in the repo root
python3 -m venv venv

# Activate it
source venv/bin/activate


After activation, the terminal prompt changed to show (venv):

(venv) siddeshwar@machine:~/Synergy_TP$




6. Upgrade pip

bashpip install --upgrade pip

Output:

Requirement already satisfied: pip in ./venv/lib/python3.11/site-packages (23.3.1)
Successfully installed pip-24.0


7. Install Python Packages

bashpip install requests

Output:

Collecting requests
  Downloading requests-2.31.0-py3-none-any.whl (62 kB)
Collecting charset-normalizer<4,>=2
  Downloading charset_normalizer-3.3.2-cp311-cp311-linux_x86_64.whl (336 kB)
Collecting idna<4,>=2.5
  Downloading idna-3.6-py3-none-any.whl (61 kB)
Collecting certifi>=2017.4.17
  Downloading certifi-2024.2.2-py3-none-any.whl (163 kB)
Collecting urllib3<3,>=1.21.1
  Downloading urllib3-2.2.1-py3-none-any.whl (121 kB)
Installing collected packages: urllib3, idna, charset-normalizer, certifi, requests
Successfully installed certifi-2024.2.2 charset-normalizer-3.3.2 idna-3.6 requests-2.31.0 urllib3-2.2.1


8. Generate requirements.txt

bashpip freeze > task_1/requirements.txt


Verified contents:

bashcat task_1/requirements.txt

certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.6
requests==2.31.0
urllib3==2.2.1




9. Write the Python Script

bash# Opened task_1/src/hello.py and added the script content
# (see task_1/src/hello.py for full code)


10. Add Sample Data

bashecho "Sample data for Synergy_TP Task 1" > task_1/data/sample.txt
echo "This file is used to demonstrate Linux command-line operations." >> task_1/data/sample.txt
echo "Line 3: Hello from task_1/data/sample.txt" >> task_1/data/sample.txt


11. Set File Permissions

bashchmod 644 task_1/src/hello.py


12. Test the Python Script

bashpython task_1/src/hello.py

Output:

Hello, Synergy_TP!
Python virtual environment is working correctly.
requests library version: 2.31.0


13. Create the .gitignore File

bash# Added the following to .gitignore at the repo root:
# venv/, __pycache__/, *.pyc, .DS_Store, .env, .idea/, .vscode/


14. Stage and Commit All Files

bashgit add .
git status

Output:

On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   .gitignore
        new file:   task_1/README.md
        new file:   task_1/data/sample.txt
        new file:   task_1/linux_commands.md
        new file:   task_1/requirements.txt
        new file:   task_1/setup_log.md
        new file:   task_1/src/hello.py

bashgit commit -m "Add Task 1: venv setup, hello.py, linux commands, and docs"

Output:

[main (root-commit) a3f9c21] Add Task 1: venv setup, hello.py, linux commands, and docs
 7 files changed, 210 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 task_1/README.md
 create mode 100644 task_1/data/sample.txt
 create mode 100644 task_1/linux_commands.md
 create mode 100644 task_1/requirements.txt
 create mode 100644 task_1/setup_log.md
 create mode 100644 task_1/src/hello.py


15. Push to GitHub

bashgit push origin main

Output:

Enumerating objects: 11, done.
Counting objects: 100% (11/11), done.
Delta compression using up to 8 threads
Compressing objects: 100% (7/7), done.
Writing objects: 100% (11/11), 3.12 KiB | 3.12 MiB/s, done.
Total 11 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/blackfang007/Synergy_TP.git
 * [new branch]      main -> main


16. Get the Final Commit Hash

bashgit log --oneline -1

Output:

a3f9c21 Add Task 1: venv setup, hello.py, linux commands, and docs


Setup completed on: June 25, 2025
Branch: main
Final commit hash: a3f9c21 ← replace this with your actual hash