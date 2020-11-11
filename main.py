from prettytable import PrettyTable
from equationsystem import EquationSystem
from nn import NeuralNetwork

lst = [
    [2, -1, -1, 1],
    [0, -1, 1, 1],
    [0, 3, -1, -4]
]

brain = NeuralNetwork(12, 20, 6, 0.1)

es = EquationSystem(lst, brain)
print(es.eveluate_solved())
print(lst)
es.update()