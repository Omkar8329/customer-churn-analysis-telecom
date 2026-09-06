# Data Dictionary

The project uses the IBM Telco Customer Churn dataset. The following fields are central to the analysis.

| Field | Description | Usage |
|---|---|---|
| `customerID` | Unique customer identifier | Customer-level uniqueness checks |
| `tenure` | Number of months the customer has stayed | Tenure segmentation |
| `MonthlyCharges` | Current monthly charge | KPI and pricing analysis |
| `TotalCharges` | Total amount charged to the customer | Cleaning and value analysis |
| `Contract` | Contract term | Primary churn segmentation |
| `InternetService` | Internet service category | Service-level churn comparison |
| `PaymentMethod` | Payment method used by the customer | Payment-level churn comparison |
| `Churn` | Whether the customer left the service | Target variable |

The complete source dataset contains 21 columns. The cleaned analysis dataset contains 7,032 rows after removing 11 records with missing numeric `TotalCharges` values.
