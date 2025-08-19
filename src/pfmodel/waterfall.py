import numpy as np

def run_waterfall(cnads: np.ndarray, debt_service: np.ndarray, dsra_top_up_policy_months: int = 6, lockup_dscr: float = 1.1):
    """
    Very simplified waterfall:
      1) Senior debt service
      2) DSRA top-up to X months
      3) Distributions if DSCR >= lockup; else trapped
    Returns dict with allocations and trapped cash balance.
    """
    T = len(cnads)
    alloc_debt = np.minimum(cnads, debt_service)
    rem = cnads - alloc_debt

    # DSRA target = X months of next period's debt service (approximate with current)
    dsra_target = debt_service * (dsra_top_up_policy_months / 12.0)
    dsra_bal = np.zeros(T+1)
    dsra_topup = np.zeros(T)

    distributions = np.zeros(T)
    trapped = np.zeros(T)

    # Compute period DSCR using current period debt service (simplification)
    dscr = np.where(debt_service == 0, np.inf, cnads / debt_service)

    for t in range(T):
        # Top up DSRA
        needed = max(dsra_target[t] - dsra_bal[t], 0.0)
        topup = min(rem[t], needed)
        dsra_topup[t] = topup
        dsra_bal[t+1] = dsra_bal[t] + topup
        rem[t] -= topup

        # Distribute or trap
        if dscr[t] >= lockup_dscr:
            distributions[t] = rem[t]
        else:
            trapped[t] = rem[t]

    return {
        "alloc_debt_service": alloc_debt,
        "dsra_topup": dsra_topup,
        "dsra_balance": dsra_bal,
        "distributions": distributions,
        "trapped_cash": trapped,
        "dscr": dscr
    }
