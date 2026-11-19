from pathlib import Path

import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
results = (HERE / "scaling_results.txt").read_text()
fixed_budget_text, fixed_n_text = results.split(
    "Fixed n = 100; changing only B"
)


def read_rows(section):
    rows = []
    for line in section.splitlines():
        parts = line.strip().split(",")
        if len(parts) == 4 and parts[0].isdigit():
            n, budget, seconds, cells = parts
            rows.append((int(n), int(budget), float(seconds), int(cells)))
    return rows


fixed_budget = read_rows(fixed_budget_text)
fixed_n = read_rows(fixed_n_text)

fig, (left, right) = plt.subplots(1, 2, figsize=(11, 4))

left.plot(
    [row[0] for row in fixed_budget],
    [row[2] for row in fixed_budget],
    marker="o",
)
left.set(
    title="Changing project count (B = 2,000)",
    xlabel="Number of projects (n)",
    ylabel="Median DP time (seconds)",
)

right.plot(
    [row[1] for row in fixed_n],
    [row[2] for row in fixed_n],
    marker="o",
)
right.set(
    title="Changing budget (n = 100)",
    xlabel="Budget (B)",
    ylabel="Median DP time (seconds)",
)

for chart in (left, right):
    chart.grid(True, alpha=0.3)

fig.tight_layout()
output = HERE / "dp_scaling.png"
fig.savefig(output, dpi=180)
print(f"Saved {output}")