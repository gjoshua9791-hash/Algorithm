from my_solutions import solve_dp, solve_greedy

def make_instance(budget, costs, benefits):
    return { "budget": budget, "n": len(costs), "cost": costs,
            "benefit": benefits,"projects": [{"id": i} for i in range(len(costs))],}

def check(name, inst, greedy_expected, dp_expected):
    for solve, expected in ((solve_greedy, greedy_expected), (solve_dp, dp_expected), ):
        ids = solve(inst)
        assert len(ids) == len(set(ids)), f"{name}: repeated ID"
        assert all(0 <= i < inst["n"] for i in ids), f"{name}: unknown ID"
        assert sum(inst["cost"][i] for i in ids) <= inst["budget"], f"{name}: over budget"
        assert sum(inst["benefit"][i] for i in ids) == expected, f"{name}: wrong benefit"
    print(f"PASS: {name}")

check("no projects", make_instance(0, [], []), 0, 0)
check("nothing fits", make_instance(2, [3, 5], [7, 9]), 0, 0)
check("greedy misses optimum", make_instance(10, [6, 5, 5], [12, 9, 9]), 12, 18)
check("project used once", make_instance(6, [3], [5]), 5, 5)
check("free project", make_instance(0, [0, 2], [4, 9]), 4, 4)