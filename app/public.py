# app/main.py
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from utils import get_summary

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Solar Data Dashboard", layout="wide")

# -------------------- COLOR PALETTE --------------------
palette = dict(Benin="#66c2a5", Togo="#fc8d62", **{"Sierra Leone": "#8da0cb"})

# -------------------- TITLE & INTRO --------------------
st.title("Cross-Country Solar Data Dashboard")
st.markdown(
    "Upload your cleaned datasets below and explore solar radiation metrics across **Benin**, **Sierra Leone**, and **Togo** interactively."
)

# -------------------- FILE UPLOADERS --------------------
st.sidebar.header("📂 Upload Cleaned CSV Files")

uploaded_benin = st.sidebar.file_uploader("Upload Benin CSV", type="csv", key="benin")
uploaded_sierra = st.sidebar.file_uploader("Upload Sierra Leone CSV", type="csv", key="sierra")
uploaded_togo = st.sidebar.file_uploader("Upload Togo CSV", type="csv", key="togo")

dfs = []

if uploaded_benin is not None:
    df_benin = pd.read_csv(uploaded_benin)
    df_benin["Country"] = "Benin"
    dfs.append(df_benin)

if uploaded_sierra is not None:
    df_sierra = pd.read_csv(uploaded_sierra)
    df_sierra["Country"] = "Sierra Leone"
    dfs.append(df_sierra)

if uploaded_togo is not None:
    df_togo = pd.read_csv(uploaded_togo)
    df_togo["Country"] = "Togo"
    dfs.append(df_togo)

if len(dfs) == 0:
    st.warning("⚠️ Please upload at least one country's cleaned CSV file to continue.")
    st.stop()

# Combine uploaded data
df = pd.concat(dfs, ignore_index=True)

# -------------------- SIDEBAR FILTERS --------------------
st.sidebar.header(" Filters")
countries = st.sidebar.multiselect(
    "Select Countries",
    options=df["Country"].unique().tolist(),
    default=df["Country"].unique().tolist(),
)
metric = st.sidebar.selectbox("Select Metric", ["GHI", "DNI", "DHI"])

# Filter data based on sidebar selection
filtered = df[df["Country"].isin(countries)]

# -------------------- VISUAL COMPARISON --------------------
st.subheader(f"{metric} Comparison Across Countries")

col1, col2 = st.columns(2)

# Barplot (Left)
with col1:
    st.markdown("**Average Values (Bar Chart)**")
    avg_values = (
        filtered.groupby("Country")[metric]
        .mean()
        .sort_values(ascending=False)
    )
    fig_bar, ax_bar = plt.subplots(figsize=(5, 4))
    sns.barplot(x=avg_values.index, y=avg_values.values, palette=palette, ax=ax_bar)
    ax_bar.set_xlabel("")
    ax_bar.set_ylabel(f"Mean {metric} (W/m²)")
    st.pyplot(fig_bar)

# Boxplot (Right)
with col2:
    st.markdown("**Distribution (Boxplot)**")
    fig_box, ax_box = plt.subplots(figsize=(5, 4))
    sns.boxplot(x="Country", y=metric, data=filtered, palette=palette, ax=ax_box)
    ax_box.set_xlabel("")
    ax_box.set_ylabel(f"{metric} (W/m²)")
    st.pyplot(fig_box)

# -------------------- SUMMARY TABLE --------------------
st.subheader(" Summary Statistics")
summary = get_summary(filtered)
st.dataframe(summary)

# -------------------- KEY INSIGHTS --------------------
st.subheader(" Key Observations")
st.markdown(
    """
- **Benin** records the highest average solar irradiance, ideal for solar projects.  
- **Togo** shows stable irradiance and lower variability.  
- **Sierra Leone** exhibits lower average irradiance due to higher humidity influence.
"""
)

# -------------------- DOWNLOAD FILTERED DATA --------------------
csv = filtered.to_csv(index=False).encode("utf-8")
st.download_button("⬇ Download Filtered Data", csv, "filtered_data.csv", "text/csv")

# -------------------- FOOTER --------------------
st.markdown("---")
st.caption("Developed by **Muhajer Hualis** | 10 Academy AI Mastery Program Week 0 Challenge")
