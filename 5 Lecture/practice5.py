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

# x = (1,4,9,16,25,36,49,64,81,100)

# y = 100
# i = 0
# while i < len(x):
#     if(x[i] == y):
#         print("Foundt at index", i)
#     i += 1

#print the elements of the following list uiding a for loop:
# [1,4,9,16,25,36,49,64,81,100]

# num = [1,4,9,16,25,36,49,64,81,100]
# for i in num:
#     print(i)
# else:
#     print("Loop End")

# search for a number a in this tuple
# x = (1,4,9,16,25,36,49,64,81,100)
 
# x = (1,4,9,16,25,36,49,64,81,100)
# y = 100
# idx = 0
# for el in x:
#     if(el == y):
#         print("Found at idx", idx)
#         break
#     idx +=1

#Practice range function:

#print numbers from 1 to 100:

# for i in range(1, 101):
#     print(i)

#print numbers from 100 to 1:

# for i in range(100,0, -1):
#     print(i)

# print the multiplication table of number n:

# n = int(input("Enter N : "))

# for i in range(1,11):
#     if i <= 10:
#         print(n*i)

#practice

#WAP to find the sum of first n numbers using while loop::

# n = int(input("Enter n: "))
# i = 1
# sum = 0
# while i <= n:
#     sum += i
#     i += 1
# print("The sum of first n numbers is: ", sum)


#WAP to find the factorial of first n numbers using while loop:

# n = int(input("Enter n: "))
# i = 1
# fact = 1
# while i <= n:
#     fact *= i
#     i += 1
# print("The factorial of first n numbers is: ", fact)

#WAP to find the factorial of first n numbers using for loop:

n = int(input("Enter n: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("The factorial of first n numbers is: ", fact)



