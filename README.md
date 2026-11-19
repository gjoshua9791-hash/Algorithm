# P3 City Capital Budget Planner — Joshua Garcia

I finifhsed Group B which was greedy benefit per cost and
0/1 knapsack dynamic programming.

## What the program does

Given a budget and projects with costs and benefits, each
algorithm returns project Ids to fund. The goal is to get the best total
benefit without exceeding the budget.

## How to run

Open a terminal in this repository and run:

    cd P3_City_Capital_Budget_Planner
    python3 starter/run_checks.py Group_B/my_solutions.py --only dp,greedy
    python3 Group_B/edge_cases.py

The first command runs the course-provided checker. The second runs my
five edge-case tests.

To repeat my experiment scripts:

    python3 Group_B/benchmark.py
    python3 Group_B/scaling.py
    python3 Group_B/quality.py

The saved results are in the corresponding `*_results.txt` files.

## Graphs

The graphs are saved as `Group_B/dp_scaling.png` and
`Group_B/quality_gap.png`. To regenerate them, install Matplotlib in a
Python environment, then run:

    python3 Group_B/plot_scaling.py
    python3 Group_B/plot_quality.py

## Where to find my work

- `Group_B/my_solutions.py` — both algorithms
- `Group_B/pseudocode.md` — pseudocode and worked examples
- `Group_B/edge_cases.py` — edge-case tests
- `Group_B/report.md` — results, complexity, and recommendation
- `Group_B/*_results.txt` and `Group_B/*.png` — experiment results and graphs

## Data sources and help received

The project brief, starter code, sample data, and data generator. I also used ChatGPT for debugging, milestone planning, and help to create the tests as well as plot graphs. I did check the algorithms and ran the tests myself and had Chat help me understand the results from the terminal to be able explain them but I did find that tracing the algorithm by hand a quite a bit easier. 