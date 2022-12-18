# square using lambda expression
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)
print("Square of every number in the list:")
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)
