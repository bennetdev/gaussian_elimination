from equation_system import EquationSystem

eq = EquationSystem([
    [1, 1, 1, 9],
    [1, -1, 1, 3],
    [1, 1, -1, 1]
])
eq.solve()
