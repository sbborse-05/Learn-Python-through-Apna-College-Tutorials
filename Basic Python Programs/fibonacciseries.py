# Program to print Fibonacci series up to n terms
# The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding

n = int(input("Enter number of terms: "))

a, b = 0, 1

for i in range(n):
    print(a)
    a, b = b, a + b