
#  Solar Data Discovery — MoonLight Energy Solutions  
**10 Academy AI Mastery Program | Week 0 Challenge**  
**Candidate**: Muhajer Hualis  
**Date**: November 2025  

---

## Executive Summary

This project supports **MoonLight Energy Solutions** in identifying the highest-potential regions for solar farm deployment across West Africa. Using minute-level environmental and solar radiation data from **Benin**, **Sierra Leone**, and **Togo**, we executed a full data engineering and analytics workflow:

1. **Task 1**: Robust Git & CI/CD setup  
2. **Task 2**: Per-country profiling, cleaning, and deep EDA  
3. **Task 3**: Cross-country statistical comparison  
4. **Bonus**: Interactive Streamlit dashboard  

**Key Recommendation**: Prioritize **Benin** for Phase 1 large-scale deployment — it delivers the highest mean GHI (240.6 W/m²), statistically significant advantage (p < 0.0001), and strong cleaning ROI (+18%).

---

## 📂 Repository Structure

```
solar-challenge-week0/
├── .github/workflows/ci.yml          # CI: pip install check
├── .gitignore                        # Ignores data/, .venv/, .ipynb_checkpoints/
├── requirements.txt                  # Python dependencies
├── README.md                         # ← You are here
│
├── notebooks/
│   ├── benin_eda.ipynb
│   ├── sierra_leone_eda.ipynb
│   ├── togo_eda.ipynb
│   └── compare_countries.ipynb
│
├── data/                             # ← Ignored in Git (never committed)
│   ├── benin_clean.csv
│   ├── sierra_leone_clean.csv
│   └── togo_clean.csv
│
├── app/
│   ├── __init__.py
│   └── main.py                       # Streamlit dashboard
│
└── dashboard_screenshots/
    └── final_dashboard.png           # Screenshot of deployed app
```

---

## Task 1: Git & Environment Setup  

### Objective  
Establish a professional development workflow with version control and CI.

### Actions Taken  
- Initialized GitHub repo: [`github.com/muhajirhualis/solar-challenge-week0`](https://github.com/muhajirhualis/solar-challenge-week0)  
- Created branch `setup-task` and committed:  
  - `init: add .gitignore`  
  - `chore: venv setup and requirements.txt`  
  - `ci: add GitHub Actions workflow`  
- Configured `.gitignore` to exclude:
  - `data/`, `*.csv`, `.venv/`, `.ipynb_checkpoints/`
- Added CI workflow (`.github/workflows/ci.yml`) to validate environment:  
  ```yaml
  name: CI
  on: [push]
  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4
        - name: Set up Python
          uses: actions/setup-python@v5
          with: { python-version: "3.10" }
        - run: pip install -r requirements.txt
  ```

**KPI Achieved**: Dev environment reproducibility + CI validation.

---

## Task 2: Data Profiling, Cleaning & EDA  

### Objective  
Profile, clean, and explore each country’s dataset end-to-end.

### Methodology (Per Country)  
Branches: `eda-benin`, `eda-sierra-leone`, `eda-togo`  
Notebooks: `<country>_eda.ipynb`

#### 1. Data Profiling  
- Loaded `df.info()` and `df.describe()` for all 18 columns.  
- Verified no critical missing data (>5% nulls). Only `Comments` fully empty → dropped.

#### 2. Data Cleaning  
- **Clamped negative irradiance** (`GHI`, `DNI`, `DHI`) to 0 (physically impossible).  
- **Explicit median imputation** for numeric columns (robust to outliers):  
  ```python
  df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
  ```
- **Z-score outlier flagging** (`|Z| > 3`) for `ModA`, `ModB`, `WS`, `WSgust`.  
- Exported cleaned data to `data/<country>_clean.csv`.

#### 3. Exploratory Analysis  
| Analysis Type | Key Visuals | Insight |
|---------------|-------------|---------|
| **Time Series** | GHI vs Timestamp (7-day sample) | Clear diurnal peak 11 AM–2 PM; Benin most consistent |
| **Cleaning Impact** | ModA pre/post bar chart | +12% to +18% output gain after cleaning |
| **Correlation** | Heatmap (GHI, DNI, RH, Tamb) | RH ↔ GHI: r = -0.42 (humidity reduces yield) |
| **Wind** | Wind rose (WD/WS) | Dominant NE/SE flow; avg 2–3 m/s — low dust risk |
| **Distributions** | Histograms (GHI, WS), Bubble chart (GHI vs Tamb, size=RH) | Right-skewed GHI; high GHI ↔ high Temp ↔ low RH |

### Country Highlights  
| Country | Strength | Consideration |
|---------|----------|---------------|
| **Benin** | Highest GHI, stable DNI | Occasional high variability (Std = 331) |
| **Togo** | Low GHI variability (Std = 322) | Slightly lower peak irradiance |
| **Sierra Leone** | Strong cleaning ROI (+18%) | Highest humidity → lower baseline GHI |

**KPI Achieved**: Actionable insights, stats-aware visuals, self-directed learning.

---

## Task 3: Cross-Country Comparison  

### Objective  
Synthesize datasets to rank countries by solar potential.

### Approach  
Branch: `compare-countries`  
Notebook: `notebooks/compare_countries.ipynb`

#### 1. Summary Statistics (GHI in W/m²)
| Country | Mean | Median | Std Dev |
|---------|------|--------|---------|
| **Benin** | **240.56** | 1.80 | 331.13 |
| Togo | 230.56 | 2.10 | 322.53 |
| Sierra Leone | 201.96 | 0.30 | 298.50 |

#### 2. Visual Comparison  
- **Boxplots**: One clean plot per metric (`GHI`, `DNI`, `DHI`), colored by country.  
- **Bar chart**: Ranked countries by mean GHI (Benin > Togo > Sierra Leone).

#### 3. Statistical Validation  
| Test | p-value | Conclusion |
|------|---------|------------|
| One-way ANOVA | < 0.0001 | **Significant difference** in GHI |
| Kruskal–Wallis | < 0.0001 | Confirmed (non-parametric) |

#### 4. Key Observations  
- **Benin** is optimal for utility-scale farms (highest yield, +19% over Sierra Leone).  
- **Togo** offers predictable output — ideal for grid + storage systems.  
- **Sierra Leone** needs diffuse-light-optimized tech (e.g., bifacial panels).

#### Consolidated Dashboard Summary  
| Country | Avg GHI | Cleaning Gain | Strategic Fit |
|---------|---------|---------------|---------------|
| **Benin** | 240.6 | +18% | 🟢 Large-scale deployment |
| Togo | 230.6 | +15% | 🟡 Stable baseload |
| Sierra Leone | 202.0 | +12% | 🔶 Off-grid pilots |

**KPI Achieved**: All 3 countries in plots, correct p-values, actionable insights.

---

## Bonus: Interactive Dashboard  

### Objective  
Build a Streamlit app for stakeholder exploration.

### Implementation  
Branch: `dashboard-dev`  
App: `app/main.py`

#### Features  
- **Country selector** (multiselect)  
- **Dynamic boxplot** (GHI/DNI/DHI toggle)  
- **Top regions table** (ranked by mean GHI)  
- **Strategic insight card**  

#### Deployment  
✅ Deployed to Streamlit Community Cloud:  
🔗 [Click Here](https://muhajirhualis-solarchallenge-week0.streamlit.app)  
✅ Screenshot saved: `dashboard_screenshots/final_dashboard.png`

### Sample Code Snippet
```python
selected = st.sidebar.multiselect("Countries", ["Benin", "Sierra Leone", "Togo"])
metric = st.selectbox("Metric", ["GHI", "DNI", "DHI"])

fig, ax = plt.subplots()
sns.boxplot(data=df_filtered, x="Country", y=metric, hue="Country", legend=False)
st.pyplot(fig)
```

**KPI Achieved**: Usable, interactive, visually clean, deployed.

---

## How to Reproduce  

### Local Setup
```bash
git clone https://github.com/muhajirhualis/solar-challenge-week0.git
cd solar-challenge-week0
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
# .venv\Scripts\activate         # Windows
pip install -r requirements.txt
```

### Run Dashboard
```bash
streamlit run app/main.py
```

> Note: Place your cleaned CSVs in `data/` (not in Git). Dashboard reads them locally.

---

## References & Learning  
- Seaborn Boxplot Best Practices — [seaborn.pydata.org](https://seaborn.pydata.org)  
- Conventional Commits — [conventionalcommits.org](https://www.conventionalcommits.org)  
- Streamlit Docs — [docs.streamlit.io](https://docs.streamlit.io)  
- Solar Irradiance Fundamentals — NREL Handbook  

---

## Acknowledgments  
Special thanks to the 10 Academy team — **Yabebal**, **Kerod**, **Mahbubah**, and **Filimon** — for your guidance, patience, and belief in our potential. This challenge was intense, but your support made growth possible.

> — Muhajer Hualis

---
