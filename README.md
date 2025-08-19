# Project Finance Model (Python)

A clean, testable project finance modeling toolkit in Python. It demonstrates:
- Cash flow waterfall
- Debt sculpting & sizing (DSCR / max gearing constraints)
- IRR (Project & Equity)
- Ratios: DSCR, LLCR, PLCR
- Reserve accounts (DSRA, MMRA, Seasonality)
- Financial covenant monitoring (distribution lock-ups)
- Funding schedules (equity-first / pro-rata / equity-last)
- Equity instruments (share capital, SHL, equity bridge loan)
- Sensitivity analysis (assumptions change while debt fixed)
- Cash tax vs accounting tax
- Depreciation schedules

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
python examples/run_quickstart.py
```

## Repo layout
```
src/
  pfmodel/
    __init__.py
    irr.py
    ratios.py
    depreciation.py
    taxes.py
    reserves.py
    debt_sculpt.py
    waterfall.py
    funding.py
    sensitivity.py
examples/
  inputs_minimal.yaml
  run_quickstart.py
tests/
  test_irr.py
  test_ratios.py
  test_debt_sculpt.py
```

## Notes
- This is education-oriented. For production-grade banking models you'd add logging, more rigorous tests, and validation.
- No circularity copy-paste hacks: we use deterministic functions or controlled iteration where needed.
