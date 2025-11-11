# app/utils.py
import pandas as pd
import streamlit as st

def load_data():
    """Load cleaned CSVs and combine with country labels."""
    paths = {
        "Benin": "../data/benin_clean.csv",
        "Sierra Leone": "../data/sierraleone_clean.csv",
        "Togo": "../data/togo_clean.csv"
    }
    dfs = []
    for country, path in paths.items():
        try:
            df = pd.read_csv(path)
            df["Country"] = country
            dfs.append(df)
        except FileNotFoundError:
            st.warning(f"⚠️ Data for {country} not found. Using sample placeholder data.")
            # Create small placeholder dataframe so app still runs
            df = pd.DataFrame({
                "GHI": [240.56,201.96,230.56],
                "DNI": [167.19,116.38,151.26],
                "DHI": [115.36, 113.72, 116.44],
                "Country": [country] * 3
            })
            dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

def get_summary(df):
    """Generate summary table (mean, median, std) for solar metrics."""
    summary = (
        df.groupby("Country")[["GHI", "DNI", "DHI"]]
        .agg(["mean", "median", "std"])
        .round(2)
    )
    return summary
