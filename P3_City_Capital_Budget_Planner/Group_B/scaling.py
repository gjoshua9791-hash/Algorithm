from pathlib import Path
import statistics
import sys
import time

from my_solutions import solve_dp

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "data"))
from generate_data import generate

projects = generate(1000, seed=7)["projects"]
budget = 2000

print("n,B,dp_median_seconds,cells_visited")

for n in (100, 250, 500, 1000):
    selected = projects[:n]
    inst = {
        "budget": budget,
        "n": n,
        "cost": [p["cost_10k"] for p in selected],
        "benefit": [p["benefit"] for p in selected],
        "projects": selected,
    }

    times = []
    for _ in range(5):
        start = time.perf_counter()
        solve_dp(inst)
        times.append(time.perf_counter() - start)

    cells = sum(max(0, budget - cost + 1) for cost in inst["cost"])
    print(f"{n},{budget},{statistics.median(times):.8f},{cells}")




print()
print("Fixed n = 100; changing only B")
print("n,B,dp_median_seconds,cells_visited")

fixed_projects = generate(100, seed=8)["projects"]

for budget in (250, 500, 1000, 2000, 4000):
    inst = {
        "budget": budget,
        "n": 100,
        "cost": [p["cost_10k"] for p in fixed_projects],
        "benefit": [p["benefit"] for p in fixed_projects],
        "projects": fixed_projects,
    }

    times = []
    for _ in range(5):
        start = time.perf_counter()
        solve_dp(inst)
        times.append(time.perf_counter() - start)

    cells = sum(max(0, budget - cost + 1) for cost in inst["cost"])
    print(f"100,{budget},{statistics.median(times):.8f},{cells}")