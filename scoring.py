import pandas as pd
import numpy as np

from check_constraints import compute_allocations, check_constraints


def load_inputs(inputs_path, config_path, alloc_path, demand_path):
    """Load all input files for one dataset."""
    inputs = pd.read_csv(inputs_path)
    box_configs = pd.read_csv(config_path)
    box_allocs = pd.read_csv(alloc_path)
    demand = pd.read_csv(demand_path)

    constraints = dict(zip(inputs["Parameter"], inputs["Value"]))
    return box_configs, box_allocs, demand, constraints


def compute_score(inputs_path, config_path, alloc_path, demand_path):
    """
    Computes final score = total_sales - (box_penalty_weight * total_boxes)
    Returns final_score
    """
    configs, allocs, demand, constraints = load_inputs(inputs_path, config_path, alloc_path, demand_path)
    units_per_store = compute_allocations(configs, allocs)

    if units_per_store is None:
        return -1e9  # invalid shape

    feasible = check_constraints(configs, allocs, units_per_store, constraints)
    if not feasible:
        return -1e9  # heavy penalty for infeasible solution

    # --- Compute total realized sales ---
    demand_matrix = demand.iloc[:, 1:].values if "Store_ID" in demand.columns else demand.values
    total_sales = np.sum(np.minimum(units_per_store, demand_matrix))

    # --- Compute box penalty ---
    total_boxes = allocs.iloc[:, 1:].sum().sum()
    box_penalty_weight = 1
    penalty = box_penalty_weight * total_boxes

    final_score = total_sales - penalty
    return final_score
