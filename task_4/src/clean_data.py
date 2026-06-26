import pandas as pd
import json
import os




def load_data(file_path: str) -> pd.DataFrame:
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Input file not found: '{file_path}'")

    df = pd.read_csv(file_path, dtype=str)  

    if df.empty:
        raise ValueError(f"Input file is empty: '{file_path}'")

   
    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

    return df



def generate_summary(df: pd.DataFrame) -> dict:
   
    summary = {
        "total_rows":    int(len(df)),
        "total_columns": int(len(df.columns)),
        "columns":       list(df.columns),
        "missing_values": {
            col: int(df[col].isna().sum())
            for col in df.columns
            if df[col].isna().sum() > 0
        },
        "duplicate_rows": int(df.duplicated().sum()),
    }

  
    for col in ["domain", "submitted"]:
        if col in df.columns:
            summary[f"unique_{col}"] = df[col].dropna().unique().tolist()

    return summary




def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
   
    before = len(df)
    df = df.drop_duplicates()
    removed = before - len(df)
    if removed:
        print(f"  [remove_duplicates] Removed {removed} duplicate row(s).")
    return df.reset_index(drop=True)




DOMAIN_MAP = {
    "ml":               "ML",
    "ML":               "ML",
    "machine learning": "ML",
    "MACHINE LEARNING": "ML",
    "web":              "Web",
    "web dev":          "Web",
    "Web Dev":          "Web",
    "web development":  "Web",
    "electronics":      "Electronics",
    "Electronics":      "Electronics",
    "mechanical":       "Mechanical",
    "Mechanical":       "Mechanical",
}

def standardize_domains(df: pd.DataFrame) -> pd.DataFrame:
    
    def normalize(val: str) -> str:
        if pd.isna(val):
            return val
        
        if val in DOMAIN_MAP:
            return DOMAIN_MAP[val]
        return DOMAIN_MAP.get(val.strip().lower().replace("  ", " "), val)

    df = df.copy()
    df["domain"] = df["domain"].apply(normalize)
    return df




def clean_attendance(df: pd.DataFrame) -> pd.DataFrame:
    
    df = df.copy()

    
    df["attendance_percent"] = (
        df["attendance_percent"]
        .astype(str)
        .str.replace("%", "", regex=False)
        .str.strip()
    )
    df["attendance_percent"] = pd.to_numeric(df["attendance_percent"], errors="coerce")

    
    invalid_mask = (df["attendance_percent"] < 0) | (df["attendance_percent"] > 100)
    invalid_count = invalid_mask.sum()
    if invalid_count:
        print(f"  [clean_attendance] {invalid_count} out-of-range value(s) replaced with NaN.")
    df.loc[invalid_mask, "attendance_percent"] = None

    
    median_val = df["attendance_percent"].median()
    missing = df["attendance_percent"].isna().sum()
    if missing:
        print(f"  [clean_attendance] {missing} missing value(s) filled with median ({median_val}).")
    df["attendance_percent"] = df["attendance_percent"].fillna(median_val)

    return df




WORD_TO_NUM = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
}

def clean_scores(df: pd.DataFrame) -> pd.DataFrame:
    
    df = df.copy()

    def parse_score(val: str) -> float:
        if pd.isna(val):
            return float("nan")
        val = str(val).strip().lower()
        if val in WORD_TO_NUM:
            return float(WORD_TO_NUM[val])
        try:
            return float(val)
        except ValueError:
            return float("nan")

    df["score"] = df["score"].apply(parse_score)

    missing = df["score"].isna().sum()
    if missing:
        median_val = df["score"].median()
        print(f"  [clean_scores] {missing} missing/invalid score(s) filled with median ({median_val}).")
        df["score"] = df["score"].fillna(median_val)

    df["score"] = df["score"].astype(float)
    return df




def clean_study_hours(df: pd.DataFrame) -> pd.DataFrame:
   
    df = df.copy()

    def parse_hours(val: str) -> float:
        if pd.isna(val):
            return float("nan")
        val = str(val).strip().lower()
        if val in WORD_TO_NUM:
            return float(WORD_TO_NUM[val])
        try:
            return float(val)
        except ValueError:
            return float("nan")

    df["study_hours"] = df["study_hours"].apply(parse_hours)

    missing = df["study_hours"].isna().sum()
    if missing:
        median_val = df["study_hours"].median()
        print(f"  [clean_study_hours] {missing} missing/invalid value(s) filled with median ({median_val}).")
        df["study_hours"] = df["study_hours"].fillna(median_val)

    df["study_hours"] = df["study_hours"].astype(float)
    return df




def clean_height(df: pd.DataFrame) -> pd.DataFrame:
   
    df = df.copy()

    def parse_height(val: str) -> float:
        if pd.isna(val):
            return float("nan")
        val = str(val).strip().lower()
        if val.endswith("cm"):
            return float(val.replace("cm", "").strip())
        elif val.endswith(" m") or (val.endswith("m") and not val.endswith("cm")):
            return float(val.replace("m", "").strip()) * 100
        try:
            return float(val)
        except ValueError:
            return float("nan")

    df["height_cm"] = df["height"].apply(parse_height)
    df.drop(columns=["height"], inplace=True)

    missing = df["height_cm"].isna().sum()
    if missing:
        median_val = df["height_cm"].median()
        print(f"  [clean_height] {missing} missing value(s) filled with median ({median_val}).")
        df["height_cm"] = df["height_cm"].fillna(median_val)

    return df




def clean_weight(df: pd.DataFrame) -> pd.DataFrame:
 
    df = df.copy()

    def parse_weight(val: str) -> float:
        if pd.isna(val):
            return float("nan")
        val = str(val).strip().lower().replace("kg", "").strip()
        try:
            return float(val)
        except ValueError:
            return float("nan")

    df["weight_kg"] = df["weight"].apply(parse_weight)
    df.drop(columns=["weight"], inplace=True)

    missing = df["weight_kg"].isna().sum()
    if missing:
        median_val = df["weight_kg"].median()
        print(f"  [clean_weight] {missing} missing value(s) filled with median ({median_val}).")
        df["weight_kg"] = df["weight_kg"].fillna(median_val)

    return df




SUBMITTED_TRUE  = {"yes", "y", "true", "1"}
SUBMITTED_FALSE = {"no",  "n", "false", "0"}

def clean_submitted(df: pd.DataFrame) -> pd.DataFrame:
   
    df = df.copy()

    def normalize(val: str) -> str:
        if pd.isna(val):
            return "no"
        val = str(val).strip().lower()
        if val in SUBMITTED_TRUE:
            return "yes"
        if val in SUBMITTED_FALSE:
            return "no"
        return "no"

    df["submitted"] = df["submitted"].apply(normalize)
    return df




def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
 
    df = df.copy()

    numeric_cols = ["attendance_percent", "score", "study_hours", "height_cm", "weight_kg"]
    for col in numeric_cols:
        if col in df.columns:
            missing = df[col].isna().sum()
            if missing:
                median_val = df[col].median()
                df[col] = df[col].fillna(median_val)
                print(f"  [handle_missing] '{col}': {missing} NaN(s) filled with median ({median_val}).")

    if "domain" in df.columns:
        missing = df["domain"].isna().sum()
        if missing:
            mode_val = df["domain"].mode()[0]
            df["domain"] = df["domain"].fillna(mode_val)
            print(f"  [handle_missing] 'domain': {missing} NaN(s) filled with mode ('{mode_val}').")

    if "submitted" in df.columns:
        missing = df["submitted"].isna().sum()
        if missing:
            df["submitted"] = df["submitted"].fillna("no")
            print(f"  [handle_missing] 'submitted': {missing} NaN(s) filled with 'no'.")

    for col in ["name", "student_id"]:
        if col in df.columns:
            missing = df[col].isna().sum()
            if missing:
                before = len(df)
                df = df.dropna(subset=[col])
                print(f"  [handle_missing] '{col}': dropped {before - len(df)} row(s) with missing identity.")

    return df.reset_index(drop=True)

def save_cleaned_data(df: pd.DataFrame, output_path: str) -> None:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"  [save] Cleaned data saved → {output_path}")