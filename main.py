from prettytable import PrettyTable
from sympy import symbols, solve


def evaluate_solved(lst):
    columns = [[lst[0][col_index], lst[1][col_index], lst[2][col_index]].count(0) for col_index
               in range(len(lst[0]) - 1)]
    max_zeros = max(columns)
    columns.remove(max_zeros)
    return max_zeros > 1 and max(columns) > 0


def calculate_values(lst):
    x = symbols("x")
    y = symbols("y")
    z = symbols("z")
    d = symbols("d")
    expr = 0 * x + 4 * y - 8 * z - 10 * d
    sol = solve(expr)
    print(sol)

lst = [
    [1, -2, 1, -1],
    [-2, 1, 4, -1],
    [1, 2, -7, 9]
]
lst_history = []

unsolved = True
while unsolved:
    table = PrettyTable(["x", "y", "z", "d"])
    for element in lst:
        table.add_row(element)
    print(table)
    line1_input = input("Line 1: ")
    if line1_input == "b":
        lst = lst_history[-1]
        continue
    line2_input = input("line 2: ")
    lst_history.append(lst.copy())
    line1, line1multi = int(line1_input.split("*")[0]) - 1, int(line1_input.split("*")[1])
    line2, line2multi = int(line2_input.split("*")[0]) - 1, int(line2_input.split("*")[1])
    lst[line1] = [lst[line1][i] * line1multi + lst[line2][i] * line2multi for i in range(len(lst[0]))]
    unsolved = not evaluate_solved(lst)
print("solved")
table = PrettyTable(["x", "y", "z", "d"])
for element in lst:
    table.add_row(element)
print(table)
calculate_values(lst)
