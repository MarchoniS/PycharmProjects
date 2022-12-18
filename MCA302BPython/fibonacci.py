# Python program to display the Fibonacci sequence using recursive function

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


n = int(input("Enter the number of terms : "))

# check if the number of terms is valid
if n <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(fibo(i), end=" ")
