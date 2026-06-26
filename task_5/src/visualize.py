import os
import pandas as pd
import matplotlib
matplotlib.use("Agg") 
import matplotlib.pyplot as plt


def load_cleaned_data(file_path: str) -> pd.DataFrame:
   
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Cleaned data not found: '{file_path}'\n"
            "Run Task 4 first: python task_4/src/main.py ..."
        )

    df = pd.read_csv(file_path)

    if df.empty:
        raise ValueError(f"Cleaned data file is empty: '{file_path}'")

   
    numeric_cols = ["attendance_percent", "score", "study_hours", "height_cm", "weight_kg"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df




def plot_domain_average_score(df: pd.DataFrame, output_path: str) -> None:

    domain_avg = df.groupby("domain")["score"].mean().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(8, 5))

    bars = ax.bar(
        domain_avg.index,
        domain_avg.values,
        color=["#4C72B0", "#DD8452", "#55A868", "#C44E52"],
        edgecolor="black",
        linewidth=0.7,
        width=0.5,
    )

    
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.1,
            f"{height:.2f}",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold",
        )

    ax.set_title("Average Score by Domain", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Domain", fontsize=12)
    ax.set_ylabel("Average Score", fontsize=12)
    ax.set_ylim(0, max(domain_avg.values) + 1.5)
    ax.yaxis.grid(True, linestyle="--", alpha=0.7)
    ax.set_axisbelow(True)

    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  [plot 1] Saved → {output_path}")




def plot_attendance_vs_score(df: pd.DataFrame, output_path: str) -> None:
    
    submitted     = df[df["submitted"] == "yes"]
    not_submitted = df[df["submitted"] == "no"]

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.scatter(
        submitted["attendance_percent"],
        submitted["score"],
        color="#4C72B0",
        edgecolors="black",
        linewidths=0.5,
        s=100,
        label="Submitted",
        zorder=3,
    )
    ax.scatter(
        not_submitted["attendance_percent"],
        not_submitted["score"],
        color="#C44E52",
        edgecolors="black",
        linewidths=0.5,
        s=100,
        marker="X",
        label="Not Submitted",
        zorder=3,
    )

    
    for _, row in df.iterrows():
        ax.annotate(
            row["name"],
            (row["attendance_percent"], row["score"]),
            textcoords="offset points",
            xytext=(6, 4),
            fontsize=8,
            color="black",
        )

    ax.set_title("Attendance (%) vs Score", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Attendance (%)", fontsize=12)
    ax.set_ylabel("Score", fontsize=12)
    ax.legend(fontsize=10)
    ax.yaxis.grid(True, linestyle="--", alpha=0.7)
    ax.xaxis.grid(True, linestyle="--", alpha=0.7)
    ax.set_axisbelow(True)

    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  [plot 2] Saved → {output_path}")




def plot_submission_status_count(df: pd.DataFrame, output_path: str) -> None:
    
    counts = df["submitted"].value_counts()
    labels = [label.capitalize() for label in counts.index]
    colors = ["#55A868" if label == "Yes" else "#C44E52" for label in labels]

    fig, ax = plt.subplots(figsize=(6, 5))

    bars = ax.bar(
        labels,
        counts.values,
        color=colors,
        edgecolor="black",
        linewidth=0.7,
        width=0.4,
    )

    
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.05,
            str(int(height)),
            ha="center",
            va="bottom",
            fontsize=12,
            fontweight="bold",
        )

    ax.set_title("Submission Status Count", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Submission Status", fontsize=12)
    ax.set_ylabel("Number of Students", fontsize=12)
    ax.set_ylim(0, max(counts.values) + 1.5)
    ax.yaxis.grid(True, linestyle="--", alpha=0.7)
    ax.set_axisbelow(True)

    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  [plot 3] Saved → {output_path}")




def write_plot_summary(output_path: str) -> None:
   
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    content = """# Task 5 — Plot Summary

## Plot 1: Average Score by Domain (`domain_average_score.png`)

This bar chart shows the mean score for each academic domain — ML, Web, Electronics,
and Mechanical. Each bar is labelled with its exact value. The chart reveals which
domains perform strongest on average and helps identify whether students in certain
tracks are consistently underperforming, which could guide mentorship or resource allocation.

---

## Plot 2: Attendance (%) vs Score (`attendance_vs_score.png`)

This scatter plot maps each student's attendance percentage on the x-axis against their
score on the y-axis. Points are coloured and shaped by submission status: blue circles
for submitted, red crosses for not submitted. Each point is annotated with the student's
name. The plot surfaces whether higher attendance correlates with higher scores, and
visually separates students who submitted from those who did not.

---

## Plot 3: Submission Status Count (`submission_status_count.png`)

This bar chart counts the total number of students who submitted versus those who did not.
Green represents submitted, red represents not submitted, with exact counts labelled on
each bar. It gives an immediate overview of overall submission compliance across the cohort.
"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  [summary] Saved → {output_path}")