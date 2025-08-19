import numpy as np
from pfmodel.debt_sculpt import sculpt_debt_by_dscr

def test_sculpt_outputs_shapes():
    cfads = np.array([120,140,160,180], dtype=float)
    out = sculpt_debt_by_dscr(cfads, target_dscr=1.3, max_gearing=0.7, project_cost=1000.0, rate_per_period=0.06)
    assert set(out.keys()) >= {"opening_balance","interest","principal","closing_balance","service","sized_debt"}
    T = len(cfads)
    assert len(out["interest"]) == T
