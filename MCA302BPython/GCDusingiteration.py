# GCD using iteration method
l = int(input("Enter the Smaller Number: "))
m = int(input("Enter the Larger Number: "))
r = 1
d = int(l)
while r != 0:
    q = m / d
    r = m % d
    d = r
print("The GCD is : ", q)
