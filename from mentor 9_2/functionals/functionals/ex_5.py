# functools.reduce(function, sequence, initial)
from functools import reduce

def add(x, y):
    return x * y


numbers = [2, 3, 4, 5]

result = reduce(add, numbers, 3)
print(result)

# (((2*3)*4)*5)