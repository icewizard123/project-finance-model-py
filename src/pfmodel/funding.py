import numpy as np

def make_funding_schedule(cash_need: np.ndarray, equity_first=True, pro_rata=False, equity_share: float = 0.3):
    """
    Returns (equity_draws, debt_draws) per period to meet cash_need given policy.
    - equity_first: use equity until equity budget exhausted, then debt
    - pro_rata: use equity_share each period; overrides equity_first/last toggle
    - equity_last: set equity_first=False and pro_rata=False
    """
    T = len(cash_need)
    equity_draws = np.zeros(T)
    debt_draws = np.zeros(T)

    total_equity_budget = equity_share * cash_need.sum()

    if pro_rata:
        equity_draws = cash_need * equity_share
        debt_draws = cash_need - equity_draws
        return equity_draws, debt_draws

    if equity_first:
        for t in range(T):
            d = min(total_equity_budget, cash_need[t])
            equity_draws[t] = d
            debt_draws[t] = cash_need[t] - d
            total_equity_budget -= d
    else:
        # equity last
        for t in range(T):
            debt_draws[t] = min(cash_need[t], (1.0 - equity_share) * cash_need.sum())
        equity_draws = cash_need - debt_draws

    return equity_draws, debt_draws
