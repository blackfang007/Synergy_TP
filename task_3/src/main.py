import sys
import os
import json

sys.path.insert(0, os.path.dirname(__file__))

from manual_parser import read_csv_manual, convert_types, calculate_summary, write_json as write_json_manual
from pandas_parser import read_csv_pandas, calculate_summary_pandas, write_json as write_json_pandas

MANUAL_OUTPUT  = "task_3/output/manual_summary.json"
PANDAS_OUTPUT  = "task_3/output/pandas_summary.json"
REPORT_OUTPUT  = "task_3/output/comparison_report.md"


def compare_summaries(manual: dict, pandas_s: dict) -> list[str]:
   
    differences: list[str] = []
    keys_to_check = [
        "total_students", "submitted_count", "missing_count",
        "average_score", "missing_submissions", "students_below_5",
    ]
    for key in keys_to_check:
        v1 = manual.get(key)
        v2 = pandas_s.get(key)
        if isinstance(v1, list) and isinstance(v2, list):
            if sorted(str(x) for x in v1) != sorted(str(x) for x in v2):
                differences.append(f"- `{key}`: manual={v1}, pandas={v2}")
        elif v1 != v2:
            differences.append(f"- `{key}`: manual={v1}, pandas={v2}")

    
    d1 = manual.get("domain_wise_average", {})
    d2 = pandas_s.get("domain_wise_average", {})
    for domain in set(list(d1.keys()) + list(d2.keys())):
        if d1.get(domain) != d2.get(domain):
            differences.append(
                f"- `domain_wise_average[{domain}]`: manual={d1.get(domain)}, pandas={d2.get(domain)}"
            )
    return differences


def write_comparison_report(manual: dict, pandas_s: dict, differences: list[str], output_path: str) -> None:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    match_status = " MATCH" if not differences else " DIFFERENCES FOUND"

    lines = [
        "# Task 3 — CSV Parser Comparison Report\n",
        "## Overview\n",
        "This report compares the output of the manual CSV parser (pure file I/O) with the",
        "pandas-based parser across the same dataset and the same summary calculations.\n",
        "---\n",
        "## Manual Parser Summary\n",
        f"- Total students       : {manual['total_students']}",
        f"- Submitted            : {manual['submitted_count']}",
        f"- Missing submissions  : {manual['missing_count']}",
        f"- Average score        : {manual['average_score']}",
        f"- Highest scorer       : {manual['highest_scorer']['name']} ({manual['highest_scorer']['score']})",
        f"- Missing names        : {', '.join(manual['missing_submissions'])}",
        f"- Students below 5     : {', '.join(manual['students_below_5'])}",
        f"- Domain averages      : {manual['domain_wise_average']}\n",
        "---\n",
        "## Pandas Parser Summary\n",
        f"- Total students       : {pandas_s['total_students']}",
        f"- Submitted            : {pandas_s['submitted_count']}",
        f"- Missing submissions  : {pandas_s['missing_count']}",
        f"- Average score        : {pandas_s['average_score']}",
        f"- Highest scorer       : {pandas_s['highest_scorer']['name']} ({pandas_s['highest_scorer']['score']})",
        f"- Missing names        : {', '.join(pandas_s['missing_submissions'])}",
        f"- Students below 5     : {', '.join(pandas_s['students_below_5'])}",
        f"- Domain averages      : {pandas_s['domain_wise_average']}\n",
        "---\n",
        f"## Comparison Result: {match_status}\n",
    ]

    if not differences:
        lines.append("Both parsers produced **identical results** across all fields.\n")
    else:
        lines.append("The following differences were detected:\n")
        lines.extend(differences)
        lines.append("")

    lines += [
        "---\n",
        "## Key Observations\n",
        "1. **Manual parsing** reads the file line by line using `open()` and `str.split(',')`,",
        "   giving full visibility into how raw text becomes structured data.",
        "2. **Pandas parsing** uses `pd.read_csv()`, which handles encoding, type inference,",
        "   and missing values automatically with far less code.",
        "3. Both approaches produce the same numerical results when the input is clean.",
        "4. Manual parsing requires explicit type conversion and row validation; pandas handles",
        "   these in a single `read_csv()` call with `dtype` or `errors='coerce'` options.",
        "5. For large datasets, pandas is significantly faster due to vectorized C-level operations.",
        "   Manual parsing scales poorly as row count grows.\n",
    ]

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python task_3/src/main.py <input_csv>")
        sys.exit(1)

    input_path = sys.argv[1]

    print("=" * 55)
    print("     Task 3 — Manual CSV Parser vs Pandas")
    print("=" * 55)

    
    print("\n[1/4] Running manual parser...")
    try:
        raw_rows      = read_csv_manual(input_path)
        typed_rows    = convert_types(raw_rows)
        manual_summary = calculate_summary(typed_rows)
        write_json_manual(manual_summary, MANUAL_OUTPUT)
        print(f"      Manual summary written → {MANUAL_OUTPUT}")
    except (FileNotFoundError, ValueError) as e:
        print(f"[Error] Manual parser failed: {e}")
        sys.exit(1)

    
    print("\n[2/4] Running pandas parser...")
    try:
        df             = read_csv_pandas(input_path)
        pandas_summary = calculate_summary_pandas(df)
        write_json_pandas(pandas_summary, PANDAS_OUTPUT)
        print(f"      Pandas summary written  → {PANDAS_OUTPUT}")
    except (FileNotFoundError, ValueError) as e:
        print(f"[Error] Pandas parser failed: {e}")
        sys.exit(1)

    
    print("\n[3/4] Comparing outputs...")
    differences = compare_summaries(manual_summary, pandas_summary)
    if differences:
        print(f"        {len(differences)} difference(s) found.")
    else:
        print("    Both parsers produced identical results.")

    print("\n[4/4] Writing comparison report...")
    write_comparison_report(manual_summary, pandas_summary, differences, REPORT_OUTPUT)
    print(f"      Report written              → {REPORT_OUTPUT}")

   
    print("\n" + "-" * 55)
    print("  Results (Manual Parser)")
    print("-" * 55)
    print(f"  Total students      : {manual_summary['total_students']}")
    print(f"  Submitted           : {manual_summary['submitted_count']}")
    print(f"  Missing             : {manual_summary['missing_count']}")
    print(f"  Average score       : {manual_summary['average_score']}")
    print(f"  Highest scorer      : {manual_summary['highest_scorer']['name']} ({manual_summary['highest_scorer']['score']})")
    print(f"  Missing names       : {', '.join(manual_summary['missing_submissions'])}")
    print(f"  Below 5             : {', '.join(manual_summary['students_below_5'])}")
    print("\n" + "=" * 55)
    print("  Task 3 complete.")
    print("=" * 55 + "\n")


if __name__ == "__main__":
    main()