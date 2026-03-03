# # CHAPTER THREE: Lists and Tuples

# marks = [23,31,23,43,12,431,231,431,42,67,5,467,43]

# print(marks)  
# print(len(marks))  #length
# print(type(marks))  #type 
# print(marks[2])     #identation
# print(marks[0])

#Lists slicing

# student = ["Saurabh", 100, 17, "Nashik"]
# print(student)
# print(student[0:2])
# print(student[-3:-1])

#List Method

list = ['w','r','t','q','p','r']
list.append('s')  #add one elememts at end 
print(list.sort())  #sorts in ascending order
print(list)
print(list.sort(reverse=True))  #sorts in descending  order
print(list)
list.reverse()     #reverse the whole list
print(list)
list.insert(0,'u')   #insert element at a specific idx
print(list)
list.pop(2)      #removes a element fron the index
print(list)
list.remove('r')
print(list)

#Tuple

# tup = (2,3,2,1)
# print(type(tup))
# print(tup[1:])    #tuple slicing 

#tuple methods

# tup = (2,1,3,1)
# print(tup.index(1))  #returns index of first occurence
# print(tup.count(1))   #counts number of occurence

