# Logic to check if a number is even or odd
# A number is even if it is divisible by 2, otherwise it is odd
# We can use the modulus operator % to check if a number is divisible by 2
# If n % 2 == 0, then n is even, otherwise it is odd
# We can take input from the user using the input() function and convert it to an integer using the int() function


n = int(input("Enter a number: "))
if n % 2 == 0:
    print("The number is even")
else: 
    print("The number is odd")