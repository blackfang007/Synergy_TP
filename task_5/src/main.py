import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from visualize import (
    load_cleaned_data,
    plot_domain_average_score,
    plot_attendance_vs_score,
    plot_submission_status_count,
    write_plot_summary,
)


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: python task_5/src/main.py <cleaned_csv> <output_dir>")
        print("Example: python task_5/src/main.py task_4/output/cleaned_students.csv task_5/output")
        sys.exit(1)

    input_path = sys.argv[1]
    output_dir = sys.argv[2]

    
    PLOT_1  = os.path.join(output_dir, "domain_average_score.png")
    PLOT_2  = os.path.join(output_dir, "attendance_vs_score.png")
    PLOT_3  = os.path.join(output_dir, "submission_status_count.png")
    SUMMARY = os.path.join(output_dir, "plot_summary.md")

    print("=" * 55)
    print("     Task 5 — Matplotlib Visualizations")
    print("=" * 55)

    
    print("\n[1/5] Loading cleaned data...")
    try:
        df = load_cleaned_data(input_path)
    except (FileNotFoundError, ValueError) as e:
        print(f"\n[Error] {e}")
        sys.exit(1)
    print(f"      Loaded {len(df)} rows from '{input_path}'.")

   
    print("\n[2/5] Generating Plot 1: Average Score by Domain...")
    plot_domain_average_score(df, PLOT_1)

    
    print("\n[3/5] Generating Plot 2: Attendance vs Score...")
    plot_attendance_vs_score(df, PLOT_2)

    
    print("\n[4/5] Generating Plot 3: Submission Status Count...")
    plot_submission_status_count(df, PLOT_3)

    
    print("\n[5/5] Writing plot summary...")
    write_plot_summary(SUMMARY)

    print("\n" + "=" * 55)
    print("  All outputs saved to:", output_dir)
    print("  domain_average_score.png")
    print("  attendance_vs_score.png")
    print("  submission_status_count.png")
    print("  plot_summary.md")
    print("=" * 55 + "\n")


if __name__ == "__main__":
    main()