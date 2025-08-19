import numpy as np
import numpy_financial as npf

def project_irr(cf: np.ndarray) -> float:
    """
    Project IRR on total project cash flows (CFADS - capex - etc.).
    cf: array of cash flows starting at t0 (could be negative for capex)
    """
    return float(npf.irr(cf))

def equity_irr(equity_cf: np.ndarray) -> float:
    """
    Equity IRR on equity cash flows (negative outflows at start, positives later).
    """
    return float(npf.irr(equity_cf))
