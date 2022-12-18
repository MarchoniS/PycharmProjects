# Python program to display the Fibonacci sequence
# Recursion function
import time


def recur_fibo(m):
    if m <= 1:
        return m
    else:
        return recur_fibo(m - 1) + recur_fibo(m - 2)


st = time.time()
n = 20

print("Fibonacci sequence of first ", +n, "terms:")
for i in range(n):
    print(recur_fibo(i))
elapse_time = time.time() - st
# print("\nExecution time:", time.strftime("%H:%M:%S", time.gmtime(elapse_time)))
print("Execution Time:",elapse_time," Second")
