import numpy as np
from pfmodel.irr import project_irr, equity_irr

def test_project_irr_sanity():
    cf = np.array([-100, 60, 60, 60], dtype=float)
    irr = project_irr(cf)
    assert 0.15 < irr < 0.25  # rough check

def test_equity_irr_equals_project_when_same_cf():
    cf = np.array([-100, 60, 60, 60], dtype=float)
    assert abs(project_irr(cf) - equity_irr(cf)) < 1e-9
