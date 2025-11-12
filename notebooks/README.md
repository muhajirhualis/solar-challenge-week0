# Task 2 Report - Data Profiling, Cleaning & Exploratory Data Analysis (EDA)

**Challenge:** Solar Data Discovery — MoonLight Energy Solutions  
**Candidate:** *Muhajer Hualis*  
**Week:** 0 — 10 Academy AI Mastery Program  
**Date:** November 2025  

---

## Objective

To perform **end-to-end exploratory data analysis (EDA)** on the solar radiation and environmental datasets from **Benin**, **Sierra Leone**, and **Togo**.  
The goal is to identify data quality issues, explore patterns and relationships, and generate actionable insights that support **MoonLight Energy Solutions** in making data-driven solar investment decisions.

---

## Datasets Overview

| Country | Dataset Name | Observations | Columns | Description |
|----------|-----------------|---------------|-----------|--------------|
| Benin | `benin-malanville.csv` | 525600| 18 | Solar radiation, temperature, wind, humidity |
| Sierra Leone | `sierra_leone-bumbuna.csv` | 525,600 | 18 | Meteorological and solar readings |
| Togo | `togo-dapaong.csv` | 525,600 | 18 | Time-series solar and environmental data |

Each dataset includes:
- **Solar radiation measurements:** `GHI`, `DNI`, `DHI`
- **Module performance:** `ModA`, `ModB`, `TModA`, `TModB`
- **Environmental conditions:** `Tamb`, `RH`, `BP`, `WS`, `WD`
- **Operational factors:** `Cleaning`, `Precipitation`
- **Timestamp:** Time of observation (`yyyy-mm-dd hh:mm`)

---

##  Data Profiling & Cleaning

### Data Profiling
- Loaded each dataset using `pandas` and parsed `Timestamp` as `datetime`.  
- Displayed general information (`df.info()`) and summary statistics (`df.describe()`).  
- Generated missing value reports (`df.isna().sum()`).

### Findings
- All three datasets were generally **clean and complete**.  
- Only one column (`Comments`) was **fully empty** across all datasets and was dropped.  
- No critical missing values detected in numeric columns.  
- All timestamps correctly parsed and sorted.

###  Data Cleaning
- Removed fully empty columns.  
- Verified that irradiance values (`GHI`, `DNI`, `DHI`) were non-negative.  
- Detected potential outliers using **Z-score method (|Z| > 3)** for:
- Outliers were flagged for observation, not removed, as they may represent real events (e.g., cloud edges, gusts).  
- Saved cleaned datasets as:
- `data/benin_clean.csv`
- `data/sierra_leone_clean.csv`
- `data/togo_clean.csv`

✅ Result: Datasets are clean, consistent, and analysis-ready.

---

## 📈 Exploratory Data Analysis (EDA)

### 1️. Time-Series Analysis
- Plotted **GHI, DNI, DHI, and Tamb** over time.  
- Observed clear **diurnal patterns** — solar irradiance peaks between **11:00 AM and 2:00 PM** in all three countries.
- Temperature (`Tamb`) rises in correlation with solar intensity.

**Insight:**  
Benin and Togo show strong, consistent sunlight intensity patterns. Sierra Leone shows greater variability due to coastal weather influence.

---

### 2️. Cleaning Impact
- Grouped data by `Cleaning` flag and compared average `ModA` and `ModB` readings before and after cleaning.  
- Found that post-cleaning readings were **notably higher**, confirming that regular cleaning improves module efficiency.

**Insight:**  
Cleaning has a measurable positive effect on energy yield across all locations.

---

### 3️. Correlation Analysis
- Computed and visualized correlation matrices for key features:
- **Strong positive correlation:** `GHI ↔ DNI` (r ≈ 0.9)
- **Negative correlation:** `RH ↔ GHI` and `RH ↔ Tamb`
- **Strong correlation:** `TModA/B ↔ Tamb`

**Insight:**  
High humidity reduces solar irradiance; ambient and module temperatures increase together during high irradiance periods.

---

### 4️. Wind Analysis
- Created wind rose plots using `WD` (wind direction) and `WS` (wind speed).  
- Found that:
- Winds are predominantly from **NE** and **SE**.
- Average wind speeds range between **2–4 m/s**.

**Insight:**  
Wind conditions are favorable for solar installations — minimal dust risk and low structural stress on panels.

---

### 5️. Distribution & Relationships
- Plotted histograms for `GHI`, `WS`, and `Tamb` — most distributions right-skewed.  
- Created scatter and bubble plots (e.g., `GHI vs Tamb` with bubble size = `RH`) to visualize relationships.

**Insight:**  
- Higher temperatures are generally associated with high GHI and low humidity.
- Outliers correspond to rare weather fluctuations (gusts or heavy cloud cover).

---

## Country-Specific Highlights

| Country | Key Observations |
|----------|------------------|
| **Benin** | Strong and consistent irradiance patterns; moderate humidity; excellent solar potential. |
| **Sierra Leone** | Higher humidity; more variability in GHI and DNI; cleaning improves performance significantly. |
| **Togo** | Stable irradiance and wind; balanced environmental factors; strong daily solar yield. |

---

## Visualizations Summary

| Visualization Type | Purpose |
|--------------------|----------|
| Time-series plots | Track GHI, DNI, DHI, and Tamb variations |
| Correlation heatmap | Examine relationships among variables |
| Cleaning impact bar chart | Show effect of cleaning on ModA/ModB |
| Wind rose plot | Display wind direction and strength |
| Histograms & scatter plots | Understand distributions and variable relationships |

---

## Key Insights

1. **Solar Radiation Trends:**  
 All countries exhibit strong midday peaks, confirming consistent sunlight exposure.
2. **Cleaning Impact:**  
 Regular cleaning significantly improves irradiance and efficiency.
3. **Humidity Effect:**  
 Higher humidity correlates with lower GHI and DNI values.
4. **Wind Behavior:**  
 Winds are moderate and beneficial for reducing soiling.
5. **Country Ranking:**  
 **Benin and Togo** demonstrate the highest and most stable solar potential.

---


# **Task 3: Cross-Country Comparison**

This task synthesizes cleaned solar datasets from **Benin**, **Sierra Leone**, and **Togo** to identify high-potential regions for MoonLight Energy Solutions’ solar investments.

####  Approach
- Loaded cleaned CSVs (`benin_clean.csv`, `sierraleone_clean.csv`, `togo_clean.csv`) generated from Task 2.
- Computed summary statistics (mean, median, std) for key irradiance metrics: **GHI**, **DNI**, **DHI**.
- Visualized distributions using **separate boxplots per metric**, colored by country for clear comparison.
- Conducted **one-way ANOVA and Kruskal–Wallis tests** on GHI to assess statistical significance (p < 0.0001 → highly significant).
- Ranked countries by average GHI and summarized insights in a consolidated dashboard-style table.

####  Key Findings
| Country      | Avg GHI (W/m²) | Std Dev | Interpretation |
|--------------|----------------|---------|----------------|
| **Benin**    | **240.6**      | 331.1   | Highest solar potential; ideal for large-scale deployment |
| Togo         | 230.5          | 322.5   | Slightly lower yield but more stable output (lower variability) |
| Sierra Leone | 202.0          | 298.5   | Lowest GHI — likely due to higher humidity/cloud cover; better suited for pilot or off-grid use |

- **Statistical validation**: Both ANOVA and Kruskal–Wallis confirm **significant differences** in GHI across countries (p < 0.0001).
- **Actionable insight**: Prioritize **Benin** for Phase 1 utility-scale farms; consider **Togo** for reliability-focused projects.

#### Outputs
- Notebook: [`notebooks/compare_countries.ipynb`](notebooks/compare_countries.ipynb)
- Visuals: Boxplots (GHI/DNI/DHI), GHI ranking bar chart, summary table
- Statistical evidence: p-values reported and interpreted

---


## Tools & Libraries Used

- **Python:** pandas, numpy, matplotlib, seaborn, scipy  
- **Environment:** Jupyter Notebook  
- **Version Control:** Git & GitHub  
- **Automation:** GitHub Actions (CI/CD)

---

## Challenges Encountered

- Large time-series data required optimized memory usage.  
- Distinguishing real irradiance peaks from sensor noise.  
- Ensuring consistent scaling and readability across multiple plots.

---

## Lessons Learned

- Practical application of EDA workflow on real-world environmental datasets.  
- Data validation, cleaning, and outlier management techniques.  
- Importance of data visualization for trend discovery.  
- Strengthened Git workflow and CI/CD understanding.

---

## Conclusion

All three solar datasets were successfully profiled, cleaned, and analyzed.  
The exploratory analysis revealed key insights into solar patterns, environmental factors, and the operational impact of maintenance activities.  

**Benin and Togo** show the strongest potential for solar energy projects due to high irradiance consistency and low environmental interference, while **Sierra Leone** exhibits slightly higher variability linked to humidity and coastal conditions.  

These findings prepare the foundation for **Task 3: Cross-Country Comparison** and **Task 4: Interactive Dashboard** development.


---

> _Prepared by **Muhajer Hualis**, 10 Academy AI Mastery Week 0 Challenge Participant_
