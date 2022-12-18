# Reduce function to find smallest number from a list
from functools import reduce


def mini(a, b):
    return a if a < b else b


numbers = [34, 23, 7, 4, 20]
print("Original list", numbers)
small = reduce((lambda a, b: mini(a, b)), numbers)
print("Smallest number from the list:", small)
