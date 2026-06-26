import pandas as pd

VALID_DOMAINS = {"ML", "Web", "Electronics", "Mechanical"}


def validate_cleaned_data(df: pd.DataFrame) -> bool:
   
    all_passed = True

    def check(name: str, passed: bool, detail: str = "") -> None:
        nonlocal all_passed
        status = " PASS" if passed else " FAIL"
        msg = f"  [{status}] {name}"
        if detail:
            msg += f" — {detail}"
        print(msg)
        if not passed:
            all_passed = False

    
    dup_ids = df["student_id"].duplicated().sum()
    check("No duplicate student_id", dup_ids == 0,
          f"{dup_ids} duplicate(s) found" if dup_ids else "")

    
    att = pd.to_numeric(df["attendance_percent"], errors="coerce")
    att_invalid = att.isna().sum() + ((att < 0) | (att > 100)).sum()
    check("attendance_percent numeric and 0–100", att_invalid == 0,
          f"{att_invalid} invalid value(s)" if att_invalid else "")

    
    score = pd.to_numeric(df["score"], errors="coerce")
    score_invalid = score.isna().sum() + (score < 0).sum()
    check("score numeric and non-negative", score_invalid == 0,
          f"{score_invalid} invalid value(s)" if score_invalid else "")

    
    hrs = pd.to_numeric(df["study_hours"], errors="coerce")
    hrs_invalid = hrs.isna().sum() + (hrs < 0).sum()
    check("study_hours numeric and non-negative", hrs_invalid == 0,
          f"{hrs_invalid} invalid value(s)" if hrs_invalid else "")

   
    h = pd.to_numeric(df["height_cm"], errors="coerce")
    h_invalid = h.isna().sum() + (h <= 0).sum()
    check("height_cm numeric and positive", h_invalid == 0,
          f"{h_invalid} invalid value(s)" if h_invalid else "")

    
    w = pd.to_numeric(df["weight_kg"], errors="coerce")
    w_invalid = w.isna().sum() + (w <= 0).sum()
    check("weight_kg numeric and positive", w_invalid == 0,
          f"{w_invalid} invalid value(s)" if w_invalid else "")

    
    valid_sub = {"yes", "no"}
    sub_invalid = (~df["submitted"].isin(valid_sub)).sum()
    check("submitted contains only 'yes'/'no'", sub_invalid == 0,
          f"{sub_invalid} invalid value(s): {df[~df['submitted'].isin(valid_sub)]['submitted'].unique().tolist()}" if sub_invalid else "")

    
    domain_invalid = (~df["domain"].isin(VALID_DOMAINS)).sum()
    check("domain contains only valid values", domain_invalid == 0,
          f"{domain_invalid} invalid value(s): {df[~df['domain'].isin(VALID_DOMAINS)]['domain'].unique().tolist()}" if domain_invalid else "")

    
    critical = ["student_id", "name", "domain", "attendance_percent",
                "score", "study_hours", "height_cm", "weight_kg", "submitted"]
    for col in critical:
        if col in df.columns:
            nan_count = df[col].isna().sum()
            check(f"No NaN in '{col}'", nan_count == 0,
                  f"{nan_count} NaN(s) found" if nan_count else "")

    return all_passed