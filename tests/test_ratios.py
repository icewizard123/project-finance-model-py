import numpy as np
from pfmodel.ratios import dscr_series, llcr, plcr

def test_dscr_basic():
    cfads = np.array([100, 150, 200], dtype=float)
    service = np.array([50, 100, 100], dtype=float)
    dscr = dscr_series(cfads, service)
    assert dscr.tolist() == [2.0, 1.5, 2.0]

def test_llcr_plcr_positive():
    cfads = np.array([100, 100, 100], dtype=float)
    assert 0.0 < llcr(cfads, 0.1, 200.0) < 2.0
    assert 0.0 < plcr(cfads, 0.1, 200.0) < 2.0
