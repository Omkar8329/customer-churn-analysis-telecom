-- Customer Churn Analysis (Telecom)
-- Update the source table reference before execution.

-- SET source_table = '<DATABASE>.<SCHEMA>.CUSTOMER';

-- Overall customer and churn summary
SELECT
    COUNT(*) AS total_customers,
    SUM(IFF(CHURN = 'Yes', 1, 0)) AS churned_customers,
    ROUND(100 * SUM(IFF(CHURN = 'Yes', 1, 0)) / NULLIF(COUNT(*), 0), 2) AS churn_rate
FROM CUSTOMER;

-- Churn rate by contract
SELECT
    CONTRACT,
    COUNT(*) AS total_customers,
    SUM(IFF(CHURN = 'Yes', 1, 0)) AS churned_customers,
    ROUND(100 * SUM(IFF(CHURN = 'Yes', 1, 0)) / NULLIF(COUNT(*), 0), 2) AS churn_rate
FROM CUSTOMER
GROUP BY CONTRACT
ORDER BY churn_rate DESC;

-- Average monthly charges among customers above the overall average
SELECT
    CUSTOMERID,
    MONTHLYCHARGES
FROM CUSTOMER
WHERE MONTHLYCHARGES > (
    SELECT AVG(MONTHLYCHARGES)
    FROM CUSTOMER
)
ORDER BY MONTHLYCHARGES DESC;

-- Average monthly charges
SELECT ROUND(AVG(MONTHLYCHARGES), 2) AS avg_monthly_charges
FROM CUSTOMER;
