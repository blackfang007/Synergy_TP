Linux Commands Documentation

This file documents the Linux commands used during the setup and development of Task 1 in the Synergy_TP project.


1. pwd

What it does: Prints the full path of the current working directory.

Command used:

bashpwd

Output observed:

/home/siddeshwar/Synergy_TP


2. ls

What it does: Lists files and directories in the current directory.

Command used:

bashls

Output observed:

task_1  .gitignore  README.md


3. ls -la

What it does: Lists all files and directories (including hidden ones) in long format, showing permissions, ownership, size, and modification date.

Command used:

bashls -la

Output observed:

total 36
drwxrwxr-x 4 siddeshwar siddeshwar 4096 Jun 25 10:00 .
drwxr-xr-x 8 siddeshwar siddeshwar 4096 Jun 25 09:45 ..
drwxrwxr-x 2 siddeshwar siddeshwar 4096 Jun 25 10:00 .git
-rw-rw-r-- 1 siddeshwar siddeshwar  220 Jun 25 09:50 .gitignore
-rw-rw-r-- 1 siddeshwar siddeshwar  512 Jun 25 09:55 README.md
drwxrwxr-x 5 siddeshwar siddeshwar 4096 Jun 25 10:00 task_1


4. cd

What it does: Changes the current working directory to the specified path.

Command used:

bashcd task_1

Output observed:

(no output — directory changed successfully)


Verified with pwd:

/home/siddeshwar/Synergy_TP/task_1




5. mkdir

What it does: Creates a new directory. The -p flag creates parent directories as needed.

Command used:

bashmkdir -p task_1/src task_1/data

Output observed:

(no output — directories created successfully)


Verified with ls task_1:

data  src




6. touch

What it does: Creates an empty file, or updates the timestamp of an existing file.

Command used:

bashtouch task_1/data/sample.txt

Output observed:

(no output — file created successfully)


Verified with ls task_1/data:

sample.txt




7. cat

What it does: Displays the contents of a file in the terminal.

Command used:

bashcat task_1/data/sample.txt

Output observed:

Sample data for Synergy_TP Task 1
This file is used to demonstrate Linux command-line operations.
Line 3: Hello from task_1/data/sample.txt


8. echo

What it does: Prints text to the terminal or writes text into a file using output redirection.

Command used:

bashecho "Sample data for Synergy_TP Task 1" > task_1/data/sample.txt
echo "This file is used to demonstrate Linux command-line operations." >> task_1/data/sample.txt
echo "Line 3: Hello from task_1/data/sample.txt" >> task_1/data/sample.txt

Output observed:

(no terminal output — text was written directly into sample.txt)


9. cp

What it does: Copies a file or directory to a new location.

Command used:

bashcp task_1/data/sample.txt task_1/data/sample_copy.txt

Output observed:

(no output — file copied successfully)


Verified with ls task_1/data:

sample.txt  sample_copy.txt




10. mv

What it does: Moves or renames a file or directory.

Command used:

bashmv task_1/data/sample_copy.txt task_1/data/sample_backup.txt

Output observed:

(no output — file renamed successfully)


Verified with ls task_1/data:

sample.txt  sample_backup.txt




11. rm

What it does: Removes (deletes) a file. Use with caution — deletion is permanent.

Command used:

bashrm task_1/data/sample_backup.txt

Output observed:

(no output — file deleted successfully)


Verified with ls task_1/data:

sample.txt




12. grep

What it does: Searches for a pattern (string or regex) inside a file and prints matching lines.

Command used:

bashgrep "Sample" task_1/data/sample.txt

Output observed:

Sample data for Synergy_TP Task 1


13. find

What it does: Searches for files and directories within a directory tree based on name, type, or other criteria.

Command used:

bashfind . -name "*.py"

Output observed:

./task_1/src/hello.py


14. head

What it does: Displays the first N lines of a file (default is 10).

Command used:

bashhead -5 task_1/requirements.txt

Output observed:

certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.6
requests==2.31.0
urllib3==2.2.1


15. tail

What it does: Displays the last N lines of a file (default is 10).

Command used:

bashtail -5 task_1/requirements.txt

Output observed:

certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.6
requests==2.31.0
urllib3==2.2.1


16. wc

What it does: Counts lines, words, and characters in a file. The -l flag counts only lines.

Command used:

bashwc -l task_1/requirements.txt

Output observed:

5 task_1/requirements.txt


17. chmod

What it does: Changes the file permissions. 644 means the owner can read/write, and others can only read.

Command used:

bashchmod 644 task_1/src/hello.py

Output observed:

(no output — permissions updated successfully)


Verified with ls -la task_1/src/:

-rw-r--r-- 1 siddeshwar siddeshwar 312 Jun 25 10:10 hello.py




All commands were executed on Ubuntu 22.04 LTS inside the Synergy_TP project directory.