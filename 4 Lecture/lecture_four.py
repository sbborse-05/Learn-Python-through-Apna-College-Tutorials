#dictionary 
# info = {
#     "key" : "value",
#     "name" : "saurabh",
#     "learning" : "Coding",
#     "age" : 21,
#     "is_adult" : True,
#     "marks" : [75,87,97,56],
#     12 : 94.4
# }
# print(info.get("name"))

# info["name"] = "Saurabhborse"
# print(type(info))
# print(info["name"])
# print(info["age"])
# print(info["marks"])

#null dictionary

# null_dict = {}
# null_dict["name"] = "saurabh"  #assingning value in null dictionary
# print(null_dict)

# info["name"] = "Saurabh"
# info["surname"] = "Borse"

# print(info)

#NESTING Dictionary
# student = {
#     "name":"Saurabh Borse",
#     "subjects" : {
#         "phy" : 97,
#         "chem" : 90,
#         "math": 98
#     }
# }
# print(student)
# print(student["subjects"])
# print(student["subjects"]["chem"])
# print(len(student))        #print length of dict
# print(student.keys())     #returns all keys
# print(len(list(student.keys())))  #typecast it in list 
# print(student.values())   #returns all values

# print(student.items())  #returns all (key,val) pairs as tuples

# print(student.get("name"))  #returns the keys according to value

# student.update({ "city": "delhi"})  #returns updated value
# print(student)

#Sets in Python

# collection = {1,2,3,4, "SAURABH", "BORSE", "BORSE"}

# print(type(collection))
# print(collection)
# print(len(collection)) #measures all values ignoring duplicates

# collection = set() #empty set; syntax
# collection.add(1)  #adds element to set
# collection.add(2)
# collection.add(1)
# collection.add(3)
# collection.add("Saurabh")
# collection.add("Borse")
# collection.add((1,4,3,5))

# # collection.remove(1)    #removes the element

# collection.clear()   #empties the set
# print(len(collection))

# collection = {"hello", "world", "saurabh", "borse", "hey"}

# print(collection.pop())  #removes a random values
# print(collection.pop())
set1 = {1,2,3}
set2 = {2,3,4,5}

print(set1.union(set2)) #union of two sets
print(set1)

print(set1.intersection(set2))  #combines common values and give new sets


 
