# app/utils.py
import pandas as pd

def load_data():
    """Load cleaned CSVs and combine with country labels."""
    paths = {
        "Benin": "../data/benin_clean.csv",
        "Sierra Leone": "../data/sierraleone_clean.csv",
        "Togo": "../data/togo_clean.csv"
    }
    dfs = []
    for country, path in paths.items():
        df = pd.read_csv(path)
        df["Country"] = country
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
