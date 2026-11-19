# Greedy Pseudocode

Input: Budget B and projects with an Id, integer cost, and integer benefit
Ouput: List of distinct project Ids whose total cost is at most B

1. Sort the projects from highest to lowest benefit to cost ratio
2. Set remaining budget to B and chosens Ids to an empty list
3. For each project in thhat order:
- If its cost fits the remaining budget, add its Id to chosen
- Subtract its cost from the remaining budget
- Otherwise skip and check next project
4. Return chosen Ids

# Trace from n012 file

Start with a cost of 0 and budget remaining of 232.
The first Id taken is 9 as it has the highest benefit to cost ratio. This leaves a budget of 223 and benefit of 25.
The second Id taken is 8 as it has the next highest benefit to cost ratio. This leaves a budget of 200 and benefit of 64.
The third Id taken is 1 and leaves a budget of 194 and benefit of 74 now.
The fourth Id taken is 6 which leaves a budget of 141 and benefit of 159.
The fifth Id taken is 3 and leaves a budget of 69 with a benefit of 274.
The sixth Id taken is 7 and leaves a budget of 38 and benefit of 315. 
The next highest benefit to cost is Id 0 but it exceeds the budget left so it gets skipped.
The netx following Id to get taken is 11 which leaves a budget of 1 remaining and a benefit of 355.
The rest are skipped as the budget is too small so nothing else can be taken.