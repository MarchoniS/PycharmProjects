# Python code to filter even values from a list

integers = [1, 2, 3, 4, 5, 8, 20]
print("Original List:", integers)


def is_even(x): return x % 2 == 0


even = list(filter(is_even, integers))

print("Even numbers from the list:", even)
