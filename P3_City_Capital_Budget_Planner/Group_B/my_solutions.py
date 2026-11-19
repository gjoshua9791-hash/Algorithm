"""
my_solutions.py - starter file for Project P3: City Capital Budget Planner (0/1 knapsack)

Implement the TWO techniques assigned to you (the keys are listed in TECHNIQUES below). Delete or ignore the others.
Every function receives the loaded instance (a dict; its fields are described at the top of problem.py)
and must return: a list of project ids to fund, e.g. [0, 4, 7].

Test your work from this folder:
    python run_checks.py my_solutions.py --only <key>[,<key>]      e.g.  --only bf,dnc
Rules: write the algorithms under study yourself (see the project brief for which library helpers are allowed).
"""

def solve_bf(inst):
    """Brute force (all 2^n subsets).

    Return: a list of project ids to fund, e.g. [0, 4, 7].
    """
    raise NotImplementedError("write the bf technique here")


def solve_dnc(inst):
    """Divide-and-conquer (meet in the middle).

    Return: a list of project ids to fund, e.g. [0, 4, 7].
    """
    raise NotImplementedError("write the dnc technique here")


def solve_dp(inst):
    budget = inst["budget"]
    best = [0] * (budget + 1)
    took = []

    for i in range(inst["n"]):
        cost = inst["cost"][i]
        benefit = inst["benefit"][i]
        row = bytearray(budget+1)

        for w in range(budget, cost - 1, -1):
            candidate = best[w - cost] + benefit
            if candidate > best[w]:
                best[w] = candidate
                row[w] =1

        took.append(row)

    remaining = budget
    chosen = []

    for i in range(inst["n"] - 1, -1, -1):
        if took[i][remaining]:
            chosen.append(inst["projects"][i]["id"])
            remaining -= inst["cost"][i]

    chosen.reverse()
    return chosen
    

def solve_greedy(inst):
    budget = inst["budget"]
    costs = inst ["cost"]
    benefits = inst["benefit"]

    order = sorted(range(inst["n"]), key=lambda i: float("inf") if costs[i] == 0
                   else benefits[i] / costs[i], reverse=True,)
    chosen = []
    for i in order:
        if costs[i] <= budget:
            chosen.append(inst["projects"][i]["id"])
            budget -= costs[i]

    return chosen



TECHNIQUES = {
    "bf": solve_bf,
    "dnc": solve_dnc,
    "dp": solve_dp,
    "greedy": solve_greedy,
}
