import itertools
import numpy as np

def run_sensitivity_grid(base_inputs: dict, param_grid: dict, runner_fn):
    """
    Enumerate a grid of parameter variations (holding debt fixed if runner_fn enforces it).
    Returns list of (params, results).
    - base_inputs: dict of baseline assumption values
    - param_grid: dict of lists, e.g. {"price":[90,100,110], "capex":[900,1000]}
    - runner_fn: callable(params)->metrics dict
    """
    keys = list(param_grid.keys())
    results = []
    for combo in itertools.product(*[param_grid[k] for k in keys]):
        params = base_inputs.copy()
        params.update(dict(zip(keys, combo)))
        metrics = runner_fn(params)
        results.append((params, metrics))
    return results
