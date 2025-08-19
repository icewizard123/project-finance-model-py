import numpy as np

def sculpt_debt_by_dscr(cnads: np.ndarray, target_dscr: float, max_gearing: float, project_cost: float, rate_per_period: float) -> dict:
    """
    Return a simple sculpted debt schedule sized to maintain target DSCR,
    capped by max gearing (Debt <= max_gearing * project_cost).
    Assumes interest-only draw period (t0) and amort from t1..T.
    """
    T = len(cnads)
    # DSCR-driven maximum debt service each period:
    max_service = cnads / target_dscr
    # For a level-payment approximation, take the min of average service and gearing cap
    level_service = np.nanmin([np.nanmean(max_service), np.inf])
    # Size debt backwards from level service
    # Pmt formula: service = debt * annuity(rate, T)
    if rate_per_period == 0:
        annuity = 1.0 / T
    else:
        annuity = (rate_per_period) / (1 - (1 + rate_per_period) ** (-T))
    sized_debt = level_service / annuity
    sized_debt = min(sized_debt, max_gearing * project_cost)

    # Build schedule
    debt = np.zeros(T+1)
    interest = np.zeros(T)
    principal = np.zeros(T)
    debt[0] = sized_debt
    for t in range(T):
        interest[t] = debt[t] * rate_per_period
        principal[t] = max(level_service - interest[t], 0.0)
        debt[t+1] = max(debt[t] - principal[t], 0.0)

    return {
        "opening_balance": debt[:-1],
        "interest": interest,
        "principal": principal,
        "closing_balance": debt[1:],
        "service": interest + principal,
        "sized_debt": sized_debt
    }
