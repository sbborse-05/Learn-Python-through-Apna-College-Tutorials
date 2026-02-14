# Lec: 5 Loops in python 

# Loops are used to repeat the instructions

# 1. While loop: Till when the condition is false 

# count  = 1
# while count <= 5:
#     print("hello")
#     count += 1

#Practice while loops:

# Print numbers from 1 to 100:

# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# Print numbers from 100 to 1 

# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# Print the multiplication table of number n 

# n = int(input("Enter the number: "))

# i = 1
# while i <= 10:
#     print(n*i)
#     i += 1

# Print the elements of following list using loop:
# [1,4,9,16,25,36,49,64,81,100]

# num = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i < len(num):
#     print(num[i])
#     i += 1

# Search for number x in this tuple using loop:
# [1,4,9,16,25,36,49,64,81,100]

x = (1,4,9,16,25,36,49,64,81,100)

y = 36
i = 0
while i < len(x):
    if(x[i] == y):
        print("Foundt at index", i)
    i += 1
