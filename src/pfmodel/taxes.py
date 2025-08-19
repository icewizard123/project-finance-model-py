import numpy as np

def cash_tax_schedule(taxable_income: np.ndarray, tax_rate: float) -> np.ndarray:
    """
    Simple cash tax = max(taxable_income, 0) * tax_rate.
    """
    return np.maximum(taxable_income, 0.0) * tax_rate
