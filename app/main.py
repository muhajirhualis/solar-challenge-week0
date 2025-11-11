import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data, get_summary

# Page config
st.set_page_config(page_title="Solar Data Dashboard", layout="wide")

# Add color consistency
palette = dict(Benin="#66c2a5", Togo="#fc8d62", **{"Sierra Leone":"#8da0cb"})
sns.boxplot(palette=palette)
sns.barplot(palette=palette)


# Responsive spacing
st.markdown("<br>", unsafe_allow_html=True)

# Title and Intro
st.title(" Cross-Country Solar Data Dashboard")
st.markdown("Visual comparison of solar radiation metrics across Benin, Sierra Leone, and Togo.")

# Load data
df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
countries = st.sidebar.multiselect(
    "Select Countries", ["Benin", "Sierra Leone", "Togo"], default=["Benin", "Sierra Leone", "Togo"]
)
metric = st.sidebar.selectbox("Select Metric", ["GHI", "DNI", "DHI"])

# Filter data
filtered = df[df["Country"].isin(countries)]


#  Visual Comparison — Boxplot and Bar Chart 
st.subheader(f"{metric} Comparison Across Countries")

col1, col2 = st.columns(2)

#  Barplot (Left)
with col1:
    st.markdown("**Average Values (Bar Chart)**")
    avg_values = (
        filtered.groupby("Country")[metric]
        .mean()
        .sort_values(ascending=False)
    )
    fig2, ax2 = plt.subplots(figsize=(5, 4))
    sns.barplot(x=avg_values.index, y=avg_values.values, palette="Set2", ax=ax2)
    ax2.set_xlabel("")
    ax2.set_ylabel(f"Mean {metric} (W/m²)")
    st.pyplot(fig2)
    
#  Boxplot (Right)
with col2:
    st.markdown("**Distribution (Boxplot)**")
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.boxplot(x="Country", y=metric, data=filtered, palette="Set2", ax=ax)
    ax.set_xlabel("")
    ax.set_ylabel(f"{metric} (W/m²)")
    st.pyplot(fig)
    
# Summary Table
st.subheader("Summary Statistics")
summary = get_summary(filtered)
st.dataframe(summary)

# Key Insights
st.subheader("Key Observations")
st.markdown("""
- **Benin** records the highest average solar irradiance, ideal for solar projects.  
- **Togo** shows stable irradiance and lower variability.  
- **Sierra Leone** exhibits lower average irradiance due to higher humidity influence.
""")

# Download CSV button for filtered data
csv = filtered.to_csv(index=False).encode('utf-8')
st.download_button("⬇️ Download Filtered Data", csv, "filtered_data.csv", "text/csv")

# Footer
st.markdown("---")
st.caption("Developed by Muhajer Hualis | 10 Academy AI Mastery Program Week 0 Challenge")
