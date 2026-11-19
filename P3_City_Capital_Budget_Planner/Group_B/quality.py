from pathlib import Path
import statistics
import sys

from my_solutions import solve_dp, solve_greedy

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "data"))
from generate_data import generate

sys.path.insert(0, str(PROJECT_ROOT / "starter"))
from problem import validate

print("n,style,seed,B,dp_benefit,greedy_benefit,gap_percent")

for n in (40, 100):
    for style in ("realistic", "correlated"):
        gaps = []

        for seed in (1, 2, 3):
            raw = generate(n, seed, style=style)
            projects = raw["projects"]
            inst = {
                "budget": raw["budget_10k"],
                "n": n,
                "cost": [p["cost_10k"] for p in projects],
                "benefit": [p["benefit"] for p in projects],
                "projects": projects,
            }

            dp_valid, dp_score, dp_message = validate(inst, solve_dp(inst))
            greedy_valid, greedy_score, greedy_message = validate(
                inst, solve_greedy(inst)
            )
            assert dp_valid, dp_message
            assert greedy_valid, greedy_message

            gap = 100 * (dp_score - greedy_score) / dp_score
            gaps.append(gap)

            print(
                f"{n},{style},{seed},{inst['budget']},"
                f"{dp_score},{greedy_score},{gap:.3f}"
            )

        print(f"Mean gap for n={n}, {style}: {statistics.mean(gaps):.3f}%")