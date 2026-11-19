from pathlib import Path
import statistics
import sys
import time

from my_solutions import solve_dp, solve_greedy

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "starter"))
from problem import load_instance, validate

FILES = [
    "projects_n012.json",
    "projects_n040.json",
    "projects_n040_corr.json",
    "projects_n100.json",
    "projects_n1000.json",
]

print("file,algorithm,n,B,score,median_seconds,operations")

for filename in FILES:
    inst = load_instance(PROJECT_ROOT / "data" / filename)

    for name, solve in (("greedy", solve_greedy), ("dp", solve_dp)):
        times = []

        for _ in range(5):
            start = time.perf_counter()
            ids = solve(inst)
            times.append(time.perf_counter() - start)

        valid, score, message = validate(inst, ids)
        assert valid, message

        if name == "greedy":
            operations = inst["n"]  # Projects considered after sorting
        else:
            operations = sum(
                max(0, inst["budget"] - cost + 1)
                for cost in inst["cost"]
            )  # Budget values visited by the DP inner loop

        print(
            f"{filename},{name},{inst['n']},{inst['budget']},"
            f"{score},{statistics.median(times):.8f},{operations}"
        )