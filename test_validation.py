import importlib.util
import sys
import unittest
from pathlib import Path

import pandas as pd


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "customer_churn_analysis.py"
spec = importlib.util.spec_from_file_location("customer_churn_analysis", SCRIPT_PATH)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class TestCustomerChurnValidation(unittest.TestCase):
    def setUp(self) -> None:
        self.raw = pd.DataFrame(
            {
                "customerID": ["A", "B", "C", "D"],
                "TotalCharges": ["100.00", "", "240.00", "300.00"],
                "Churn": ["No", "Yes", "Yes", "No"],
            }
        )

    def test_cleaning_converts_total_charges_and_removes_invalid_rows(self):
        cleaned = module.clean_customer_data(self.raw)
        self.assertEqual(len(cleaned), 3)
        self.assertEqual(str(cleaned["TotalCharges"].dtype), "float64")
        self.assertFalse(cleaned["TotalCharges"].isna().any())

    def test_metric_calculation(self):
        cleaned = module.clean_customer_data(self.raw)
        metrics = module.calculate_metrics(cleaned)
        self.assertEqual(metrics["total_customers"], 3)
        self.assertEqual(metrics["churned_customers"], 1)
        self.assertEqual(metrics["churn_rate"], 33.33)

    def test_cleaned_dataset_has_expected_analysis_columns(self):
        cleaned = module.clean_customer_data(self.raw)
        self.assertTrue({"customerID", "TotalCharges", "Churn"}.issubset(cleaned.columns))

    def test_documented_source_benchmark(self):
        # Benchmark from the linked Colab workflow: 1,869 churned / 7,032 cleaned customers.
        self.assertEqual(round(100 * 1869 / 7032, 2), 26.58)


if __name__ == "__main__":
    unittest.main()
