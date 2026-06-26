import json
import os
import pandas as pd


def read_csv_pandas(file_path: str) -> pd.DataFrame:
   
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: '{file_path}'")

    df = pd.read_csv(file_path)

    if df.empty:
        raise ValueError(f"CSV file is empty: '{file_path}'")

    
    df["score"]     = pd.to_numeric(df["score"], errors="coerce").fillna(0).astype(int)
    df["submitted"] = df["submitted"].str.strip().str.lower() == "yes"

    return df


def calculate_summary_pandas(df: pd.DataFrame) -> dict:
   
    submitted_df     = df[df["submitted"]]
    not_submitted_df = df[~df["submitted"]]
    below_five       = df[df["score"] < 5]["name"].tolist()

    avg_score = round(df["score"].mean(), 2)
    highest   = df.loc[df["score"].idxmax()]
    lowest_submitted = (
        submitted_df.loc[submitted_df["score"].idxmin()]
        if not submitted_df.empty else None
    )

    domain_avg = (
        df.groupby("domain")["score"]
        .mean()
        .round(2)
        .to_dict()
    )

    return {
        "total_students":   len(df),
        "submitted_count":  int(df["submitted"].sum()),
        "missing_count":    int((~df["submitted"]).sum()),
        "average_score":    float(avg_score),
        "highest_scorer": {
            "name":   highest["name"],
            "domain": highest["domain"],
            "score":  int(highest["score"]),
        },
        "lowest_scorer_submitted": {
            "name":   lowest_submitted["name"],
            "domain": lowest_submitted["domain"],
            "score":  int(lowest_submitted["score"]),
        } if lowest_submitted is not None else None,
        "domain_wise_average":  domain_avg,
        "missing_submissions":  not_submitted_df["name"].tolist(),
        "students_below_5":     below_five,
    }


def write_json(data: dict, output_path: str) -> None:
   
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)