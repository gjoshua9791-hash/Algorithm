from pathlib import Path
from statistics import mean

import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
groups = {}

for line in (HERE / "quality_results.txt").read_text().splitlines():
    parts = line.strip().split(",")
    if len(parts) == 7 and parts[0].isdigit():
        n, style, seed, budget, dp, greedy, gap = parts
        groups.setdefault((int(n), style), []).append(float(gap))

sizes = [40, 100]
realistic = [mean(groups[(n, "realistic")]) for n in sizes]
correlated = [mean(groups[(n, "correlated")]) for n in sizes]

x = range(len(sizes))
fig, ax = plt.subplots(figsize=(7, 4))

ax.bar([i - 0.18 for i in x], realistic, width=0.36, label="Realistic")
ax.bar([i + 0.18 for i in x], correlated, width=0.36, label="Correlated")

ax.set(
    title="Average benefit lost by greedy (3 datasets per group)",
    xlabel="Number of projects (n)",
    ylabel="Gap from DP optimum (%)",
    xticks=list(x),
    xticklabels=[str(n) for n in sizes],
)
ax.legend()
ax.grid(axis="y", alpha=0.3)
fig.tight_layout()

output = HERE / "quality_gap.png"
fig.savefig(output, dpi=180)
print(f"Saved {output}")