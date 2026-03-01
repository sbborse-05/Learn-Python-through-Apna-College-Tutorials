# Logic to calculate the sum of first n natural numbers
# The sum of first n natural numbers can be calculated using the formula n*(n+1
# We can take input from the user using the input() function and convert it to an integer using the int() function


n = int(input("Enter a number: "))
total = n*(n+1)//2
print("The sum of first", n, "natural numbers is:", total) 