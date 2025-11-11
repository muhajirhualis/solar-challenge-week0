
---

## Solar Data Dashboard Implementation Overview

###  `app/utils.py`
- Loads and combines cleaned datasets (`benin_clean.csv`, `sierra_leone_clean.csv`, `togo_clean.csv`).
- Generates summary statistics (mean, median, std) for GHI, DNI, and DHI.

### `app/main.py`
- Builds the **interactive UI** with:
  - Sidebar filters to select **countries** and **metrics (GHI/DNI/DHI)**.
  - **Side-by-side bar and box plots** for instant comparison.
  - **Summary statistics table** and **key insights** section.
- Uses Seaborn and Matplotlib for clean, publication-ready visuals.
- Includes consistent color palette across plots for readability.
- Footer credits and light visual separation using markdown lines.

---

## Dashboard Features

| Feature | Description |
|----------|--------------|
| **Country Selector** | Multiselect widget for Benin, Sierra Leone, and Togo |
| **Metric Dropdown** | Choose between GHI, DNI, or DHI |
| **Side-by-Side Plots** | Bar chart (mean values) and boxplot (distribution) shown together |
| **Summary Table** | Displays mean, median, std for each country |
| **Key Observations** | Markdown highlights major insights |
| **Consistent Color Palette** | Ensures easy country recognition |
| **Responsive Layout** | Works smoothly on desktop and mobile |
| **Optional Download Button** | Allows users to export filtered data (bonus) |

---

## Deployment

- Branch: `dashboard-dev`  
- Deployed to **Streamlit Community Cloud**  
- URL: *[https://muhajirhualis-solarchallenge-week0.streamlit.app]*  

**Deployment Steps:**
1. Pushed dashboard branch to GitHub.  
2. Configured Streamlit Cloud:  
   - Main file path → `app/main.py`  
   - Python version → `3.10`  
   - Added `requirements.txt` dependencies.  
3. Verified deployment and responsiveness on web and mobile.

---

## Key Insights Displayed

- **Benin** records the highest average solar irradiance, ideal for solar projects.  
- **Togo** shows stable irradiance and lower variability, ensuring consistent energy yield.  
- **Sierra Leone** exhibits slightly lower irradiance due to higher humidity and coastal influence.  

---

##  Technical Stack
- **Python 3.10**
- **Streamlit 1.x**
- **Seaborn / Matplotlib**
- **Pandas / NumPy**
- **Git & GitHub** (version control & CI/CD)

---

## Conclusion
The Streamlit dashboard transforms the analytical results from Tasks 2 & 3 into an **engaging, data-driven interface**.  
It enables users to explore, compare, and interpret solar potential across Benin, Sierra Leone, and Togo interactively.  
All core KPIs were met, demonstrating proficiency in **data visualization, storytelling, and web deployment**.

---

> _Prepared by **Muhajer Hualis**, 10 Academy AI Mastery Program Week 0 Challenge Participant_
