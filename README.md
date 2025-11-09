# solar-challenge-week0
KAIM8 Week 0 Technical Challenge

This project analyzes solar radiation and environmental data to identify high-potential regions for solar installation.

## Setup Instructions
1. Clone this repository
2. Create and activate a virtual environment
3. Install dependencies:
   ```bash
   pip install -r requirements.txt

---


##  Task 1: Git & Environment Setup

###  Objective
To establish a reproducible and collaborative environment for analyzing multi-country solar datasets.

###  Steps Completed

1. **Repository Setup**
   - Created GitHub repository: `solar-challenge-week0`
   - Cloned locally and configured Python virtual environment.

2. **Branching & Version Control**
   - Created and merged feature branches for setup and EDA work:
     - `setup-task`
     - `eda-benin`
     - `eda-sierra-leone`
     - `eda-togo`
   - Followed **conventional commit** style:
     - `init: add .gitignore`
     - `ci: add GitHub Actions workflow`
     - `feat: complete EDA for Benin`

3. **Continuous Integration (CI)**
   - Configured `.github/workflows/ci.yml` to automatically install dependencies and validate environment setup.

     ```yaml
     name: CI
     on: [push]
     jobs:
       build:
         runs-on: ubuntu-latest
         steps:
           - uses: actions/checkout@v3
           - name: Setup Python
             uses: actions/setup-python@v3
             with:
               python-version: '3.10'
           - run: pip install -r requirements.txt
           - run: python --version
     ```

4. **.gitignore and Project Structure**

   ```bash
   ├── .github/workflows/ci.yml
   ├── data/
   ├── notebooks/
   │   ├── benin_eda.ipynb
   │   ├── sierra_leone_eda.ipynb
   │   └── togo_eda.ipynb
   ├── requirements.txt
   ├── README.md
   └── .gitignore
