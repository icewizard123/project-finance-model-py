import numpy as np

def size_dsra(next_debt_service: float, months_covered: int, months_per_year: int = 12) -> float:
    """
    Basic DSRA sizing as X months of next debt service (placeholder policy).
    """
    cover_years = months_covered / months_per_year
    return next_debt_service * cover_years
