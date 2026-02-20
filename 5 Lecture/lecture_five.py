# Lec: 5 Loops in python 

# Loops are used to repeat the instructions

# 1. While loop: Till when the condition is false 

# count  = 1
# while count <= 5:
#     print("hello")
#     count += 1

#break and continue statements in loops:

#break: It is used to exit the loop when a certain condition is met.

# i = 1
# while i <= 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1

#continue: It is used to skip the current iteration of the loop and move to the next iteration.

# i = 0 
# while i <= 5:
#     if(i==3):
#         i += 1
#         continue
#     print(i)
#     i += 1

#2. for loop: It is used to iterate over a sequence (like a list, tuple, string) or other iterable objects.

# num = [1,4,9,16,25,36,49,64,81,100]
# for i in num:
#     print(i)
# else:
#     print("Loop is over")


# let's understand Range Function:

# for i in range(10):
#     print(i)            #range(stop)

# for i in range(1, 11):
#     print(i)            #range(start, stop)

# for i in range(0, 10, 2):
#     print(i)            #range(start, stop, step)

#Pass statement in loops: 
# The pass statement is a null statement in Python. It is used as a placeholder when a statement is required syntactically but you do not want to execute any code.

for i in range(5):
    pass

print("This is after the loop")