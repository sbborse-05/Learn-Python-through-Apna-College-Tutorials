# Program to demonstrate list comprehension
# This program creates a list of squares of numbers from 1 to 10 using list comprehension.
# List comprehension is a concise way to create lists in Python. 
# It consists of brackets containing an expression followed by a for clause, 
# then zero or more for or if clauses.
# The expression can be anything, meaning you can put in all kinds of objects in lists.
# The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.
# For example, the list comprehension [x**2 for x in range(1, 11)] will create a list of squares of numbers from 1 to 10.

squares = [x**3 for x in range(1, 11)]
print(squares)