import numpy as np

def straight_line(cost: float, salvage: float, life: int) -> np.ndarray:
    """
    Straight-line depreciation over `life` periods.
    """
    base = max(cost - salvage, 0.0)
    return np.full(life, base / life)
