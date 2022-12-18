# Reduce function to find Sum
from functools import reduce


def Sum(a, b):
    # print(f"a={a}, b={b}, {a} + {b} ={a+b}")
    return a + b


L = [75, 65, 80, 95, 50]
print("Original List:", L)
total = reduce(Sum, L)
print("Sum of numbers present in the List:", total)
