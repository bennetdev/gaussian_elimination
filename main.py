from prettytable import PrettyTable
from sympy import symbols, solve
import math


def get_least_common_multiple(number1, number2):
    return number1 * number2 // math.gcd(number1, number2)


def get_columns(lst):
    return [[lst[0][col_index], lst[1][col_index], lst[2][col_index]] for col_index
            in range(len(lst[0]) - 1)]


def evaluate_solved(lst):
    columns = get_columns(lst)
    column_rows_solved = [column.count(0) for column in columns]
    print(column_rows_solved)
    max_zeros = max(column_rows_solved)
    column_rows_solved.remove(max_zeros)
    return max_zeros > 1 and max(column_rows_solved) > 0


def add_lines(line1, line2, line1multi, line2multi):
    print(line1multi, line2multi)
    if line1multi < 0:
        line1multi *= -1
    else:
        line2multi *= -1
    return [lst[line1][i] * line1multi + lst[line2][i] * line2multi for i in range(len(lst[0]))]


def decide_next_calculation(lst, col_to_solve_index, row_to_solve_index):
    row_to_solve_index = len(lst) + row_to_solve_index if row_to_solve_index < 0 else row_to_solve_index
    number_to_solve = lst[row_to_solve_index][col_to_solve_index]
    columns = get_columns(lst)
    least_common_multiple = 100
    lcm_index = 0
    for num_index, number in enumerate(columns[col_to_solve_index]):
        if num_index == row_to_solve_index:
            continue
        if number == 0:
            continue
        if col_to_solve_index != 0 and lst[num_index][col_to_solve_index - 1] != 0:
            continue
        current_lcm = get_least_common_multiple(number_to_solve, number)
        if abs(current_lcm) < least_common_multiple:
            least_common_multiple = current_lcm
            lcm_index = [col_to_solve_index, num_index]
    print(lcm_index, least_common_multiple)
    lst[row_to_solve_index] = add_lines(row_to_solve_index, lcm_index[1], least_common_multiple // number_to_solve,
              least_common_multiple // columns[col_to_solve_index][lcm_index[1]])
    print(lst)


def calculate_values(lst):
    x = symbols("x")
    y = symbols("y")
    z = symbols("z")
    d = symbols("d")
    expr = 0 * x + 4 * y - 8 * z - 10 * d
    sol = solve(expr)
    print(sol)


lst = [
    [2, -1, -1, 1],
    [0, -1, 1, 1],
    [1, 3, -1, -4]
]
lst_history = []
print(get_columns(lst))
solved = evaluate_solved(lst)
decide_next_calculation(lst, 0, -1)
print(lst)
decide_next_calculation(lst, 1, -1)
while not solved:
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
    lst[line1] = add_lines(line1, line2)
    solved = evaluate_solved(lst)
print("solved")
table = PrettyTable(["x", "y", "z", "d"])
for element in lst:
    table.add_row(element)
print(table)
calculate_values(lst)
