# ACIS_Marketing_Analytics
# ACIS Marketing Analytics Project
# Project Overview
This project aims to optimize marketing strategies for AlphaCare Insurance Solutions (ACIS) by analyzing historical insurance claim data. The analysis involves understanding key metrics, testing hypotheses, and building predictive models to identify low-risk clients for premium reduction.

# Folder Structure
ACIS_Marketing_Analytics/
├── data/
│   ├── raw/                # Raw data files
│   ├── processed/          # Processed data files
│   └── .gitignore          # Exclude raw data from version control
├── src/
│   ├── eda/                # Scripts for exploratory data analysis
│   ├── hypothesis_testing/ # Scripts for statistical tests
│   ├── modeling/           # Scripts for statistical modeling
│   └── utils/              # Utility scripts
├── notebooks/              # Jupyter notebooks for analysis
├── reports/
│   └── plots/              # Plots generated during EDA
├── .dvc/                   # DVC metadata
├── requirements.txt        # Python dependencies
├── README.md               # Project overview
├── LICENSE                 # License information
├── .gitignore              # Ignored files/folders
└── dvc.yaml                # DVC pipeline configuration


# Project Tasks
# Task 1: Git and GitHub, EDA & Stats
Objectives:
Set up a GitHub repository with branches for task management.
Perform exploratory data analysis (EDA) to understand the dataset and gain insights.
Key Steps:
Summarized data using descriptive statistics.
Assessed data quality and detected outliers.
Created insightful visualizations.
Output:
Three key visualizations and an EDA summary report.

# Task 2: Data Version Control (DVC)
Objectives:
Implement DVC to track and version data files.
Store data in a local remote storage.
Key Steps:
Initialized DVC and configured local storage.
Tracked raw and processed data versions.
Pushed data to remote storage.
Output:
.dvc files for raw and processed datasets.

# Task 3: A/B Hypothesis Testing
Objectives:
Perform statistical hypothesis testing to validate business insights.
Key Steps:
Tested hypotheses on risk differences across provinces, zip codes, and genders.
Conducted chi-squared and t-tests.
Documented findings and their business implications.
Output:
Hypothesis testing scripts and result reports.

# Task 4: Statistical Modeling
Objectives:
Build predictive models to identify low-risk clients.
Key Steps:
Prepared data through cleaning, encoding, and feature engineering.
Built and evaluated models (Linear Regression, Random Forests, XGBoost).
Analyzed feature importance using SHAP.
Output:
Final model evaluation report and feature importance plots.

# Installation
Clone the Repository
  git clone https://github.com/aberamen/ACIS_Marketing_Analytics.git
cd ACIS_Marketing_Analytics
# Install Dependencies
  pip install -r requirements.txt
# Set Up DVC
  dvc init
  dvc remote add -d localstorage /path/to/local/storage
# Usage
# Run EDA

   python src/eda/eda_analysis.py
Run Hypothesis Testing

python src/hypothesis_testing/hypothesis_tests.py
Run Modeling

python src/modeling/model_building.py
View Data Versioning
Add new data to DVC:

dvc add data/raw/new_data.csv
Push data to remote:

dvc push


