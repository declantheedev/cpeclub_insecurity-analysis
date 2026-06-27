# Data Cleaning Pipeline
# Spatiotemporal Analysis of Insecurity in Nigeria

import os
import pandas as pd
from tabulate import tabulate

# File Paths

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_PATH = os.path.join(BASE_DIR, "data", "raw_nigeria_conflict.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "cleaned_nigeria_conflict.csv")

# Load Dataset

def load_data(path):
    try:
        df = pd.read_csv(path)

        # Rename ACLED column
        if "admin1" in df.columns:
            df.rename(columns={"admin1": "state"}, inplace=True)

        print("Dataset loaded successfully.")

        return df

    except FileNotFoundError:
        print("Error: Input file not found.")
        exit()

# Remove Missing Geographic Data

def drop_missing_geo(df):

    df["state"] = df["state"].astype(str).str.strip()
    df["state"] = df["state"].replace(["", "nan", "None"], pd.NA)

    df = df.dropna(subset=["state"])

    return df

# Convert Data Types

def cast_types(df):

    df["fatalities"] = pd.to_numeric(df["fatalities"], errors="coerce")
    df["event_date"] = pd.to_datetime(df["event_date"], errors="coerce")

    df = df.dropna(subset=["fatalities", "event_date"])

    df["fatalities"] = df["fatalities"].astype(int)

    return df

# Standardize State Names

def standardize_states(df):

    state_mapping = {
        "abuja federal capital territory": "Federal Capital Territory",
        "fct": "Federal Capital Territory",
        "f.c.t": "Federal Capital Territory",
        "kaduna state": "Kaduna",
        "kaduna": "Kaduna",
        "borno state": "Borno",
        "borno": "Borno",
        "zamfara state": "Zamfara",
        "zamfara": "Zamfara",
        "niger state": "Niger",
        "niger": "Niger",
    }

    df["state"] = (
        df["state"]
        .str.strip()
        .str.lower()
        .replace(state_mapping)
        .str.title()
    )

    return df

# Create Month-Year Column

def add_month_year(df):

    df["month_year"] = df["event_date"].dt.strftime("%Y-%m")

    return df

# Save Cleaned Dataset

def save_data(df, path):

    os.makedirs(os.path.dirname(path), exist_ok=True)

    df.to_csv(path, index=False)

# Main Program

def main():

    # Load Dataset
    df = load_data(INPUT_PATH)

    # Data Cleaning Pipeline
    df = drop_missing_geo(df)
    df = cast_types(df)
    df = standardize_states(df)
    df = add_month_year(df)

    # Save Cleaned Dataset
    save_data(df, OUTPUT_PATH)

    # Display Cleaning Summary

    print("\n" + "=" * 90)
    print("           STAGE 4 - DATA CLEANING PIPELINE COMPLETED")
    print("=" * 90)

    print(f"\nCleaned dataset saved successfully to:\n{OUTPUT_PATH}")

    print("\nCleaning Summary")
    print("-" * 90)
    print(f"Total Records : {len(df)}")
    print(f"Total Columns : {len(df.columns)}")

    # Display Preview
    
    preview = df[
        [
            "event_date",
            "state",
            "location",
            "event_type",
            "sub_event_type",
            "fatalities",
            "month_year",
        ]
    ].head(20)

    print("\nPreview of Cleaned Dataset (First 20 Records)")
    print("-" * 90)

    print(
        tabulate(
            preview,
            headers="keys",
            tablefmt="fancy_grid",
            showindex=False,
        )
    )

    print("\nData cleaning completed successfully.")

# Run Program
if __name__ == "__main__":
    main()