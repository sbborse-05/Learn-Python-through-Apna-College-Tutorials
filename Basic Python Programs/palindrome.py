# Program to check if a string is a palindrome or not
# A string is a palindrome if it reads the same forwards and backwards


s = input("Enter a string: ")
rev = "" 
i = len(s) - 1
while i >= 0:
    rev += s[i]
    i -= 1

if s == rev:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")