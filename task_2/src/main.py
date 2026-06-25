import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from analyzer import (
    read_submissions,
    get_submitted_students,
    calculate_average_score,
    get_domain_wise_average,
    get_missing_submissions,
    write_summary,
)
def main() -> None:
    
    if len(sys.argv) != 3:
        print("Usage: python task_2/src/main.py <input_csv> <output_json>")
        print("Example: python task_2/src/main.py task_2/data/submissions.csv task_2/output/summary.json")
        sys.exit(1)

    input_path  = sys.argv[1]
    output_path = sys.argv[2]

    print("=" * 55)
    print("       Student Submission Analyzer — Task 2")
    print("=" * 55)

    
    try:
        students = read_submissions(input_path)
    except FileNotFoundError as e:
        print(f"\n[Error] {e}")
        print("Please check that the input CSV path is correct.")
        sys.exit(1)
    except ValueError as e:
        print(f"\n[Error] {e}")
        sys.exit(1)

    
    submitted        = get_submitted_students(students)
    missing_names    = get_missing_submissions(students)
    avg_score        = calculate_average_score(students)
    domain_avg       = get_domain_wise_average(students)

    total_students   = len(students)
    submitted_count  = len(submitted)
    missing_count    = len(missing_names)

   
    highest = max(students, key=lambda s: s["score"])

   
    lowest = min(submitted, key=lambda s: s["score"]) if submitted else None

   
    below_five = [s["name"] for s in students if s["score"] < 5]

   
    print(f"\n  Total students       : {total_students}")
    print(f"  Submitted            : {submitted_count}")
    print(f"  Missing submissions  : {missing_count}")
    print(f"  Average score        : {avg_score}")
    print(f"  Highest scorer       : {highest['name']} ({highest['score']})")
    if lowest:
        print(f"  Lowest scorer (submitted): {lowest['name']} ({lowest['score']})")

    print(f"\n  Missing submissions  : {', '.join(missing_names) if missing_names else 'None'}")
    print(f"  Scoring below 5      : {', '.join(below_five) if below_five else 'None'}")

    print("\n  Domain-wise averages :")
    for domain, avg in domain_avg.items():
        print(f"    {domain:<15} : {avg}")

    
    summary = {
        "total_students":   total_students,
        "submitted_count":  submitted_count,
        "missing_count":    missing_count,
        "average_score":    avg_score,
        "highest_scorer": {
            "name":   highest["name"],
            "domain": highest["domain"],
            "score":  highest["score"],
        },
        "lowest_scorer_submitted": {
            "name":   lowest["name"],
            "domain": lowest["domain"],
            "score":  lowest["score"],
        } if lowest else None,
        "domain_wise_average":    domain_avg,
        "missing_submissions":    missing_names,
        "students_below_5":       below_five,
    }

   
    try:
        write_summary(summary, output_path)
        print(f"\n  Summary written to   : {output_path}")
    except OSError as e:
        print(f"\n[Error] Could not write output file: {e}")
        sys.exit(1)

    print("\n" + "=" * 55)
    print("  Analysis complete.")
    print("=" * 55 + "\n")


if __name__ == "__main__":
    main()