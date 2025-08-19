from pfmodel.debt_sculpt import sculpt_debt_by_dscr
from pfmodel.ratios import dscr_series, llcr, plcr
from pfmodel.waterfall import run_waterfall
from pfmodel.irr import project_irr, equity_irr
import numpy as np

cfads = np.array([0,120,140,160,180,180,170,160,150,140], dtype=float)
rate = 0.06
sched = sculpt_debt_by_dscr(cnads=cfads[1:], target_dscr=1.30, max_gearing=0.7, project_cost=1000.0, rate_per_period=rate)
service = sched["service"]
dscr = dscr_series(cfads[1:], service)
wf = run_waterfall(cfads[1:], service, dsra_top_up_policy_months=6, lockup_dscr=1.1)

print("Sized Debt:", round(sched["sized_debt"], 2))
print("Avg DSCR:", round(np.nanmean(dscr), 2))
print("Total Distributions:", round(wf["distributions"].sum(), 2))
print("Project IRR (toy):", round(project_irr(np.array([-1000, *cfads[1:]]))*100, 2), "%")
