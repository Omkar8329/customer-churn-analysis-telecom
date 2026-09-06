# Customer Churn Analysis (Telecom)

An end-to-end telecom customer churn analysis project combining Python-based exploratory data analysis, Snowflake SQL transformation, and an interactive Tableau dashboard.

## Project Overview

Customer churn is a core retention challenge for subscription businesses. This project cleans and analyzes the IBM Telco Customer Churn dataset to understand churn behavior across contract type, tenure, internet service, and payment method. The results are presented through a Tableau dashboard designed for executive analysis.

## Project Links

| Component | Link |
|---|---|
| Tableau dashboard | [Customer Churn Overview](https://public.tableau.com/authoring/CustomerChurnOverview_17887208651510/CustomerChurnAnalysisDashboard#2) |
| Colab analysis notebook | [PythonforData.ipynb](https://colab.research.google.com/drive/14_MXyQQ4GYtJF-65qDfnB6snVVR0nvT0#scrollTo=H1dY1YdLaPj7) |
| Snowflake SQL workspace | [SalesChurn.sql](https://app.snowflake.com/me-central2.gcp/do10993/#/workspaces/ws/USER%24/PUBLIC/ETL%20PIPELINE/SalesChurn.sql) |
| Author profile | [Omkar8329](https://github.com/Omkar8329) |

## Workflow

1. Load the raw `WA_Fn-UseC_-Telco-Customer-Churn.csv` dataset.
2. Inspect schema, missing values, duplicates, cardinality, and data types.
3. Convert `TotalCharges` from text to numeric values.
4. Remove the 11 records with missing `TotalCharges` values.
5. Calculate churn counts and the overall churn rate.
6. Prepare analysis-ready data for SQL and Tableau reporting.
7. Compare churn rates across contract, tenure, internet service, and payment method segments.

## Key Findings

The analysis contains **7,043 raw customer records** and **21 columns**. After converting `TotalCharges` to numeric format and removing 11 rows with missing values, the analysis dataset contains **7,032 customers**.

The overall churn rate is approximately **26.58%**. Contract type is a major differentiator: month-to-month customers show substantially higher churn than customers on one-year or two-year contracts. The Snowflake results also show contract-level churn rates of approximately **42.71% for month-to-month**, **11.28% for one-year**, and **2.85% for two-year** customers.

The dashboard further explores churn by internet service, payment method, and tenure group to support targeted retention actions.

## Repository Contents

The GitHub web upload keeps the initial project files at the repository root for easy access:

```text
customer-churn-analysis-telecom/
├── README.md
├── requirements.txt
├── .gitignore
├── customer_churn_analysis.py
├── customer_churn_analysis.ipynb
├── sales_churn_template.sql
├── methodology.md
└── data_dictionary.md
```

The Python script and notebook are the reproducible analysis assets. The SQL template documents the Snowflake workflow without exposing environment-specific credentials or objects.

## Running the Python Analysis

Place the dataset at `data/WA_Fn-UseC_-Telco-Customer-Churn.csv`, install the dependencies, and run:

```bash
pip install -r requirements.txt
python customer_churn_analysis.py
```

The script writes the cleaned dataset to `data/clean_data.csv` when the input file is available.

## Data Source

The analysis is based on the commonly used IBM Telco Customer Churn dataset. The raw CSV is intentionally not committed to this repository; add it locally under `data/` or use the linked Colab notebook as the source environment.

## Recommended Business Actions

The results suggest prioritizing retention campaigns for month-to-month customers, investigating electronic-check payment journeys, and designing early-tenure interventions. These recommendations should be evaluated with customer-level profitability, service usage, and campaign-response data before operational rollout.

## Author

**Omkar Karnik**  
GitHub: [@Omkar8329](https://github.com/Omkar8329)

## License

This repository contains analysis code and project documentation. Dataset licensing and redistribution terms remain with the original data provider.
