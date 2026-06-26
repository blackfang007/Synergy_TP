import json
import os


def read_csv_manual(file_path: str) -> list[dict]:
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: '{file_path}'")

    rows: list[dict] = []
    header: list[str] = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f):
           
            line = line.strip()

           
            if not line:
                continue

            fields = line.split(",")

            
            if line_num == 0 or not header:
                header = [col.strip() for col in fields]
                continue

           
            if len(fields) != len(header):
                print(f"  [Warning] Skipping malformed row {line_num + 1}: {line!r}")
                continue

            row = {header[i]: fields[i].strip() for i in range(len(header))}
            rows.append(row)

    if not header:
        raise ValueError(f"CSV file is empty: '{file_path}'")
    if not rows:
        raise ValueError(f"No valid data rows found in: '{file_path}'")

    return rows


def convert_types(rows: list[dict]) -> list[dict]:
   
    converted: list[dict] = []

    for i, row in enumerate(rows):
        try:
            score = int(row["score"])
        except (ValueError, KeyError):
            print(f"  [Warning] Skipping row {i + 2}: invalid score '{row.get('score', 'missing')}'")
            continue

        converted.append({
            "name":      row["name"],
            "domain":    row["domain"],
            "task":      row["task"],
            "score":     score,
            "submitted": row.get("submitted", "no").lower() == "yes",
        })

    return converted


def calculate_summary(rows: list[dict]) -> dict:
    
    if not rows:
        return {}

    submitted     = [r for r in rows if r["submitted"]]
    not_submitted = [r for r in rows if not r["submitted"]]
    below_five    = [r["name"] for r in rows if r["score"] < 5]

    avg_score = round(sum(r["score"] for r in rows) / len(rows), 2)
    highest   = max(rows, key=lambda r: r["score"])
    lowest_submitted = min(submitted, key=lambda r: r["score"]) if submitted else None

    
    domain_scores: dict[str, list[int]] = {}
    for r in rows:
        domain_scores.setdefault(r["domain"], []).append(r["score"])
    domain_avg = {
        d: round(sum(s) / len(s), 2)
        for d, s in domain_scores.items()
    }

    return {
        "total_students":   len(rows),
        "submitted_count":  len(submitted),
        "missing_count":    len(not_submitted),
        "average_score":    avg_score,
        "highest_scorer": {
            "name":   highest["name"],
            "domain": highest["domain"],
            "score":  highest["score"],
        },
        "lowest_scorer_submitted": {
            "name":   lowest_submitted["name"],
            "domain": lowest_submitted["domain"],
            "score":  lowest_submitted["score"],
        } if lowest_submitted else None,
        "domain_wise_average":  domain_avg,
        "missing_submissions":  [r["name"] for r in not_submitted],
        "students_below_5":     below_five,
    }


def write_json(data: dict, output_path: str) -> None:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)