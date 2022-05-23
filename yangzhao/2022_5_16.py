import numpy as np
from typing_extensions import Self


def sum(a, b):
    return a+b


a = 3
b = 4
print(sum(a, b))


class greeter(object):
    def __init__(self, name):
        self.name = name

    def greet(self, loud=False):
        if loud:
            print("hello")
        else:
            print("HELLO")


g = greeter('yang')
print(g.name)
g.greet(True)


h = np.array([[1, 2, 3], [4, 5, 6]])
print(h)
m = np.zeros((2, 3))
print(m)
