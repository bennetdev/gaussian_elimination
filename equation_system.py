import math
from prettytable import PrettyTable


def get_least_common_multiple(number1, number2):
    return number1 * number2 // math.gcd(number1, number2)


class EquationSystem:
    def __init__(self, equation_system):
        self.equation_system = equation_system
        self.eqs_history = [equation_system]

    def print_eqs_as_table(self):
        table = PrettyTable(["x", "y", "z", "d"])
        for element in self.equation_system:
            table.add_row(element)
        print(table)

    def evaluate_solved(self):
        columns = self.get_columns()
        column_rows_solved = [column.count(0) for column in columns]
        max_zeros = max(column_rows_solved)
        column_rows_solved.remove(max_zeros)
        return max_zeros > 1 and max(column_rows_solved) > 0

    def add_lines(self, line1, line2, line1multi, line2multi):
        if line1multi < 0:
            line1multi *= -1
        else:
            line2multi *= -1
        return [self.equation_system[line1][i] * line1multi + self.equation_system[line2][i] * line2multi for i in
                range(len(self.equation_system[0]))]

    def get_columns(self):
        return [
            [self.equation_system[0][col_index], self.equation_system[1][col_index], self.equation_system[2][col_index]]
            for col_index
            in range(len(self.equation_system[0]) - 1)]

    def sort_eqs_by_zeros(self):
        columns_sorted = sorted(self.get_columns(), key=lambda x: x.count(0), reverse=True)
        sorted_lst = self.get_rows_by_columns(columns_sorted)
        for index, element in enumerate(sorted_lst):
            element.append(self.equation_system[index][-1])
        return sorted(sorted_lst, key=lambda x: x.count(0))

    def next_step(self):
        if self.equation_system[-2][0] != 0:
            self.decide_next_calculation(0, -2)
            self.print_eqs_as_table()
        if self.equation_system[-1][0] != 0:
            self.decide_next_calculation(0, -1)
            self.print_eqs_as_table()
        if self.equation_system[-1][1] != 0:
            self.decide_next_calculation(1, -1)

    def decide_next_calculation(self, col_to_solve_index, row_to_solve_index):
        row_to_solve_index = len(
            self.equation_system) + row_to_solve_index if row_to_solve_index < 0 else row_to_solve_index
        number_to_solve = self.equation_system[row_to_solve_index][col_to_solve_index]
        columns = self.get_columns()
        least_common_multiple = 100
        lcm_index = 0
        for num_index, number in enumerate(columns[col_to_solve_index]):
            if num_index == row_to_solve_index:
                continue
            if number == 0:
                continue
            if col_to_solve_index != 0 and self.equation_system[num_index][col_to_solve_index - 1] != 0:
                continue
            current_lcm = get_least_common_multiple(number_to_solve, number)
            if abs(current_lcm) < least_common_multiple:
                least_common_multiple = current_lcm
                lcm_index = [col_to_solve_index, num_index]
        self.equation_system[row_to_solve_index] = self.add_lines(row_to_solve_index, lcm_index[1],
                                                                  least_common_multiple // number_to_solve,
                                                                  least_common_multiple // columns[col_to_solve_index][
                                                                      lcm_index[1]])

    def get_rows_by_columns(self, columns):
        rows = []
        for i in range(len(columns[0])):
            row = []
            for column in columns:
                row.append(column[i])
            rows.append(row)
        return rows

    def solve(self):
        self.print_eqs_as_table()
        self.sort_eqs_by_zeros()
        while not self.evaluate_solved():
            self.next_step()
            self.print_eqs_as_table()