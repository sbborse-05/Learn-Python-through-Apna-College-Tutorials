# Logic to find factorial of a number
# Factorial of a number n is the product of all the integers from 1 to n. 
# It is denoted by n!. 
# For example, 5! = 1*2*3*4*5 = 120. 
# The factorial of 0 is defined to be 1.


n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact *= i   # fact = fact * i
print("The factorial of", n, "is", fact)