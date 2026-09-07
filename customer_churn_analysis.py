"""Customer Churn Analysis (Telecom).

Refactored, reproducible implementation of the exploratory workflow from the
linked Colab notebook.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = ROOT / "data" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
OUTPUT_PATH = ROOT / "data" / "clean_data.csv"
FIGURE_PATH = ROOT / "assets" / "churn_count.png"


def clean_customer_data(df: pd.DataFrame) -> pd.DataFrame:
    """Convert charge fields and remove rows without valid total charges."""
    cleaned = df.copy()
    cleaned["TotalCharges"] = pd.to_numeric(cleaned["TotalCharges"], errors="coerce")
    return cleaned.dropna(subset=["TotalCharges"]).copy()


def calculate_metrics(df: pd.DataFrame) -> dict[str, float | int]:
    """Return core portfolio metrics for a cleaned customer dataset."""
    churned = int((df["Churn"] == "Yes").sum())
    total = int(len(df))
    return {
        "total_customers": total,
        "churned_customers": churned,
        "churn_rate": round(100 * churned / total, 2) if total else 0.0,
    }


def main() -> None:
    if not INPUT_PATH.exists():
        raise FileNotFoundError(
            f"Place WA_Fn-UseC_-Telco-Customer-Churn.csv at {INPUT_PATH} before running."
        )

    raw = pd.read_csv(INPUT_PATH)
    print("Raw shape:", raw.shape)
    print("Duplicate rows:", raw.duplicated().sum())
    print("Unique customers:", raw["customerID"].nunique())

    missing_before_cleaning = int(
        pd.to_numeric(raw["TotalCharges"], errors="coerce").isna().sum()
    )
    print("Missing TotalCharges after conversion:", missing_before_cleaning)

    df = clean_customer_data(raw)
    metrics = calculate_metrics(df)
    print("Clean shape:", df.shape)
    print(f"Overall churn rate: {metrics['churn_rate']:.2f}%")
    print("Churn counts:\n", df["Churn"].value_counts())

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    FIGURE_PATH.parent.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(6, 4))
    ax = sns.countplot(
        data=df,
        x="Churn",
        order=["No", "Yes"],
        hue="Churn",
        palette=["#4E79A7", "#E15759"],
        legend=False,
    )
    ax.set_title("Customer Churn Count")
    ax.set_xlabel("Churn")
    ax.set_ylabel("Customers")
    plt.tight_layout()
    plt.savefig(FIGURE_PATH, dpi=160)
    plt.close()


if __name__ == "__main__":
    main()
