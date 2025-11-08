import numpy as np


def compute_allocations(box_configs, box_allocs):
    pack_matrix = box_configs.iloc[:, 1:].values  # exclude Pack_ID
    alloc_matrix = box_allocs.iloc[:, 1:].values  # exclude Store_ID

    # Check matrix dimensions first
    if alloc_matrix.shape[1] != pack_matrix.shape[0]:
        print(f"Matrix Dimension Check: Violated "
              f"(alloc_matrix has {alloc_matrix.shape[1]} columns, "
              f"pack_matrix has {pack_matrix.shape[0]} rows)")
        return None

    print("✅ Matrix Dimension Check: OK")
    return alloc_matrix @ pack_matrix


def check_constraints(configs, allocs, units_per_store, constraints):
    """Run all constraint checks and print results."""
    results = {}

    # Integer check
    int_ok = (np.issubdtype(configs.iloc[:, 1:].values.dtype, np.integer) and
              np.issubdtype(allocs.iloc[:, 1:].values.dtype, np.integer))
    results["Integer Check"] = int_ok

    # Unpack constraints
    total_units_cap = constraints["Total Allocation Units"]
    max_pack_size = constraints["Maximum Pack Size"]
    min_pack_size = constraints["Minimum Pack Size"]
    impression_min = constraints["Impression Minimum"]
    max_packs_per_loc = constraints["Maximum Packs per Location"]
    min_units_per_size = constraints["Minimum Units per Size per Location"]
    max_box_configs = constraints.get("Maximum Box Configurations", np.inf)

    # Compute derived totals
    configs["Pack_Total"] = configs.iloc[:, 1:].sum(axis=1)
    results["Pack Size Check"] = (configs["Pack_Total"].max() <= max_pack_size) and (configs["Pack_Total"].min() >= min_pack_size)
    results["Total Allocation Check"] = units_per_store.sum() <= total_units_cap
    results["Impression Minimum Check"] = (units_per_store.sum(axis=1) >= impression_min).all()
    results["Max Packs per Location Check"] = (allocs.iloc[:, 1:].sum(axis=1) <= max_packs_per_loc).all()
    results["Min Units per Size Check"] = (units_per_store.min(axis=0) >= min_units_per_size).all()
    results["Max Box Configurations Check"] = len(configs) <= max_box_configs

    # Print results
    for k, v in results.items():
        print(f"✅ {k}: {'OK' if v else 'Violated'}")

    return all(results.values())
