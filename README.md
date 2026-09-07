# Customer Churn Analysis (Telecom)

An end-to-end telecom customer churn analysis project combining Python-based exploratory data analysis, Snowflake SQL transformation, and an interactive Tableau dashboard.

## Project Overview

Customer churn is a core retention challenge for subscription businesses. This project cleans and analyzes the IBM Telco Customer Churn dataset to understand churn behavior across contract type, tenure, internet service, and payment method. The results are presented through a Tableau dashboard designed for executive analysis.

## Project Links

| Component | Link |
|---|---|
| Tableau dashboard | [Customer Churn Overview](https://public.tableau.com/authoring/CustomerChurnOverview_17887208651510/CustomerChurnAnalysisDashboard#2) |
| Original Colab analysis | [PythonforData.ipynb](https://colab.research.google.com/drive/14_MXyQQ4GYtJF-65qDfnB6snVVR0nvT0#scrollTo=H1dY1YdLaPj7) |
| Snowflake SQL workspace | [SalesChurn.sql](https://app.snowflake.com/me-central2.gcp/do10993/#/workspaces/ws/USER%24/PUBLIC/ETL%20PIPELINE/SalesChurn.sql) |
| Repository notebook | [`customer_churn_analysis.ipynb`](./customer_churn_analysis.ipynb) |
| Author profile | [Omkar8329](https://github.com/Omkar8329) |

## Code Provenance and Versioning

The linked Colab notebook is **the original exploratory analysis authored by Omkar Karnik**. The Python script and Jupyter notebook stored in this repository are **refactored, repository-ready implementations of the same analytical workflow**. They are intentionally not presented as byte-for-byte copies of the Colab export.

| Artifact | Role | Relationship |
|---|---|---|
| Original Colab notebook | Original exploratory work and source reference | Source of the analysis sequence and initial findings |
| `customer_churn_analysis.py` | Refactored Python implementation | Adds reusable paths, validation, clean-data export, and figure generation |
| `customer_churn_analysis.ipynb` | Clean repository notebook | Reorganizes the same workflow into reproducible notebook cells |
| `sales_churn_template.sql` | Portable Snowflake SQL template | Documents the analytical SQL without exposing account-specific objects or credentials |

This distinction is intentional: reviewers can inspect your original work in Colab and use the GitHub implementation for a cleaner, reproducible project structure.

## My Contribution

I completed the project workflow end to end. I cleaned and validated the telecom customer data in Python, converted `TotalCharges` into a usable numeric field, handled incomplete records, calculated churn metrics, and prepared the analysis-ready dataset. I wrote analytical SQL for Snowflake to summarize churn overall and by contract, created and refined the Tableau dashboard for executive viewing, and documented the methodology, data dictionary, business findings, and relationship between the original Colab analysis and the refactored repository implementation.

## Executive Takeaway

| Finding | Business implication |
|---|---|
| The cleaned dataset contains 7,032 customers and the overall churn rate is 26.58%. | Churn is material enough to justify a focused retention program rather than a broad, undifferentiated campaign. |
| Month-to-month customers have approximately 42.71% churn, compared with 11.28% for one-year contracts and 2.85% for two-year contracts. | Contract commitment is the clearest observed risk signal and should guide retention prioritization. |
| Churn varies across tenure, internet service, and payment method segments. | Retention actions should be segmented by customer lifecycle and service/payment experience instead of treating all customers identically. |

Recommended actions are to prioritize month-to-month customers for targeted retention offers, design early-tenure onboarding and engagement interventions, and investigate payment-method and service-experience journeys before testing personalized campaigns. These actions should be validated with profitability, usage, complaint, and campaign-response data.

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

The repository keeps the project files at the repository root for easy access:

```text
customer-churn-analysis-telecom/
├── README.md
├── requirements.txt
├── .gitignore
├── customer_churn_analysis.py
├── customer_churn_analysis.ipynb
├── sales_churn_template.sql
├── methodology.md
├── data_dictionary.md
└── test_validation.py
```

The Python script and notebook are the refactored repository implementations. The original Colab remains linked above as the source analysis. The SQL template documents the Snowflake workflow without exposing environment-specific credentials or objects.

## Running the Python Analysis

Place the dataset at `data/WA_Fn-UseC_-Telco-Customer-Churn.csv`, install the dependencies, and run:

```bash
pip install -r requirements.txt
python customer_churn_analysis.py
```

The script writes the cleaned dataset to `data/clean_data.csv` when the input file is available.

## Validation Checks

The repository includes a lightweight `unittest` suite that validates the core cleaning behavior, churn metric calculation, required analysis columns, and the documented source benchmark. The tests use a small deterministic fixture and do not require committing the source customer data.

Run the checks from the repository root:

```bash
python -m unittest test_validation -v
```

## Data Source

The analysis is based on the commonly used IBM Telco Customer Churn dataset. The raw CSV is intentionally not committed to this repository. Add it locally under `data/` when running the refactored implementation, or open the linked Colab notebook to review the original source workflow.

## Recommended Business Actions

The results suggest prioritizing retention campaigns for month-to-month customers, investigating electronic-check payment journeys, and designing early-tenure interventions. These recommendations should be evaluated with customer-level profitability, service usage, and campaign-response data before operational rollout.

## Author

**Omkar Karnik**  
GitHub: [@Omkar8329](https://github.com/Omkar8329)

## License

This repository contains analysis code and project documentation. Dataset licensing and redistribution terms remain with the original data provider.
