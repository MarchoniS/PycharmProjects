# Prime numbers from a list using filter function
import math

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("Original List:", numbers)


def prime(x):
    # checking for negative numbers
    # if x <= 1:
    #    return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True


print("Prime numbers from the List:")
print(list(filter(prime, numbers)))
