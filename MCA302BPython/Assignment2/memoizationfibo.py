# Python program to display the Fibonacci sequence
# Memoization Technique
import time

memo = {}


def recur_fibo(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        value = recur_fibo(n - 1) + recur_fibo(n - 2)
    memo[n] = value
    return value


st = time.time()
term = 20

print("Fibonacci sequence of first ", +term, "terms:")
for i in range(term):
    print(recur_fibo(i))
elapse_time = time.time() - st
print("\nExecution time:", time.strftime("%H:%M:%S", time.gmtime(elapse_time)))
