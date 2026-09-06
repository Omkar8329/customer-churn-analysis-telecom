"""Customer Churn Analysis (Telecom)

Reproducible version of the exploratory workflow from the linked Colab notebook.
Expected input: data/WA_Fn-UseC_-Telco-Customer-Churn.csv
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = ROOT / "data" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
OUTPUT_PATH = ROOT / "data" / "clean_data.csv"
FIGURE_PATH = ROOT / "assets" / "churn_count.png"


def main() -> None:
    if not INPUT_PATH.exists():
        raise FileNotFoundError(
            f"Place WA_Fn-UseC_-Telco-Customer-Churn.csv at {INPUT_PATH} before running."
        )

    df = pd.read_csv(INPUT_PATH)

    print("Raw shape:", df.shape)
    print("Duplicate rows:", df.duplicated().sum())
    print("Unique customers:", df["customerID"].nunique())

    # TotalCharges is delivered as text in the source data.
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    missing_total_charges = int(df["TotalCharges"].isna().sum())
    print("Missing TotalCharges after conversion:", missing_total_charges)

    df = df.dropna(subset=["TotalCharges"]).copy()

    churn_rate = df["Churn"].value_counts(normalize=True).get("Yes", 0) * 100
    print(f"Clean shape: {df.shape}")
    print(f"Overall churn rate: {churn_rate:.2f}%")
    print("Churn counts:\n", df["Churn"].value_counts())

    # Export the analysis-ready dataset for downstream SQL/Tableau use.
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    # Save a lightweight validation figure for the repository.
    FIGURE_PATH.parent.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(6, 4))
    ax = sns.countplot(data=df, x="Churn", order=["No", "Yes"], palette=["#4E79A7", "#E15759"])
    ax.set_title("Customer Churn Count")
    ax.set_xlabel("Churn")
    ax.set_ylabel("Customers")
    plt.tight_layout()
    plt.savefig(FIGURE_PATH, dpi=160)
    plt.close()


if __name__ == "__main__":
    main()
