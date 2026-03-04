# Program to calculate simple interest

p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time in years: "))

interest = (p*r*t)/100

print("Simple Interest is: ", interest)
