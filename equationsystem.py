def join_list(lst):
    joined_list = []
    for element in lst:
        joined_list.extend(element)
    return joined_list


class EquationSystem:
    def __init__(self, table, brain):
        self.table = table
        self.start_sum = sum([sum(i) for i in self.table])
        self.brain = brain
        self.fitness = 0
        self.solved = False
        self.moves = 0

    def add_lines(self, line1, line2):
        self.table[line1] = [self.table[line1][index] + self.table[line2][index] for index in range(len(self.table[line1]))]

    def eveluate_solved(self):
        columns = [[self.table[0][col_index], self.table[1][col_index], self.table[2][col_index]].count(0) for col_index
                   in range(len(self.table[0]) - 1)]
        max_zeros = max(columns)
        columns.remove(max_zeros)
        return max_zeros > 1 and max(columns) > 0

    def update(self):
        if not self.solved:
            output = self.brain.query(join_list(self.table))
            print(output)
            if output[0] == max(output):
                self.add_lines(0, 1)
            elif output[1] == max(output):
                self.add_lines(1, 0)
            elif output[2] == max(output):
                self.add_lines(1, 2)
            elif output[3] == max(output):
                self.add_lines(2, 1)
            elif output[4] == max(output):
                self.add_lines(0, 2)
            elif output[5] == max(output):
                self.add_lines(2, 0)
            print(self.table)
            self.moves += 1
