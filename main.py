from prettytable import PrettyTable

lst = [
    [1, -2, 1, -1],
    [-2, 1, 4, -1],
    [1, 2, -7, 9]
]

while True:
    table = PrettyTable(["a", "b", "c", "Ergebnis"])
    for element in lst:
        table.add_row(element)
    print(table)
    line1 = int(input("Line 1: ")) - 1
    line2 = int(input("line 2: ")) - 1
    line1multi = int(input("line 1 mutliplikator: "))
    line2multi = int(input("line 2 mutliplikator: "))
    lst[line1] = [lst[line1][i] * line1multi + lst[line2][i] * line2multi for i in range(len(lst[0]))]