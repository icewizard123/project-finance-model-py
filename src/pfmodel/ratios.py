import numpy as np

def dscr_series(cnads: np.ndarray, debt_service: np.ndarray) -> np.ndarray:
    """Debt Service Coverage Ratio per period = CFADS / Debt Service (P+I)."""
    denom = np.where(debt_service == 0.0, np.nan, debt_service)
    return cnads / denom

def llcr(cnads: np.ndarray, discount_rate: float, outstanding_debt: float) -> float:
    """
    Loan Life Coverage Ratio = NPV(CFADS over loan life, discounted at r) / outstanding debt.
    """
    t = np.arange(len(cnads))
    npv = np.sum(cnads / np.power(1+discount_rate, t+1))
    return float(npv / outstanding_debt) if outstanding_debt else np.inf

def plcr(cnads: np.ndarray, discount_rate: float, total_debt: float) -> float:
    """
    Project Life Coverage Ratio = NPV(CFADS over project life) / total debt.
    """
    t = np.arange(len(cnads))
    npv = np.sum(cnads / np.power(1+discount_rate, t+1))
    return float(npv / total_debt) if total_debt else np.inf
