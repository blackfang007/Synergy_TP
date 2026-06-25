import csv
import json
import os
from typing import Any
Student = dict[str, Any]
def read_submissions(filepath: str) -> list[Student]:
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Input file not found: '{filepath}'")

    students: list[Student] = []

    with open(filepath, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        if reader.fieldnames is None:
            raise ValueError(f"CSV file is empty: '{filepath}'")

        for line_num, row in enumerate(reader, start=2): 
            
            try:
                score = int(row["score"])
            except (ValueError, KeyError):
                print(f"  [Warning] Skipping row {line_num}: invalid score '{row.get('score', 'missing')}'")
                continue

            students.append({
                "name":      row["name"].strip(),
                "domain":    row["domain"].strip(),
                "task":      row["task"].strip(),
                "score":     score,
                "submitted": row["submitted"].strip().lower() == "yes",
            })

    if not students:
        raise ValueError(f"No valid student records found in: '{filepath}'")

    return students




def get_submitted_students(students: list[Student]) -> list[Student]:
   
    return [s for s in students if s["submitted"]]



def calculate_average_score(students: list[Student]) -> float:
   
    if not students:
        return 0.0
    total = sum(s["score"] for s in students)
    return round(total / len(students), 2)




def get_domain_wise_average(students: list[Student]) -> dict[str, float]:
   
    domain_scores: dict[str, list[int]] = {}

    for s in students:
        domain = s["domain"]
        domain_scores.setdefault(domain, []).append(s["score"])

    return {
        domain: round(sum(scores) / len(scores), 2)
        for domain, scores in domain_scores.items()
    }




def get_missing_submissions(students: list[Student]) -> list[str]:
    
    return [s["name"] for s in students if not s["submitted"]]




def write_summary(summary: dict[str, Any], output_path: str) -> None:
    
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4)