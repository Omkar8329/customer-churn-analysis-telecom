# Methodology

## Data Preparation

The source dataset is loaded with pandas. The initial quality checks inspect shape, columns, duplicate records, missing values, customer identifier uniqueness, and data types.

`TotalCharges` is converted from object/string to numeric with coercion. The conversion produces 11 missing values, corresponding to records where the field is blank or non-numeric. Those records are excluded from the analysis dataset so that downstream aggregate metrics are based on valid charge values.

## Metrics

| Metric | Definition |
|---|---|
| Total customers | Count of rows in the cleaned analysis dataset |
| Churn count | Count of records where `Churn = Yes` |
| Churn rate | Churned customers divided by total customers |
| Segment churn rate | Churned customers within a segment divided by all customers in that segment |
| Average monthly charges | Mean of `MonthlyCharges` for the relevant population |

## Analysis Dimensions

The Tableau dashboard and Snowflake SQL explore churn by contract, tenure group, internet service, and payment method. These dimensions were selected because they are directly interpretable by customer-retention and commercial teams.

## Limitations

The dataset is observational and does not establish causal relationships. The analysis does not include campaign exposure, customer profitability, service incidents, competitor activity, or time-series retention behavior. Recommendations should therefore be validated with operational data and controlled experiments.
