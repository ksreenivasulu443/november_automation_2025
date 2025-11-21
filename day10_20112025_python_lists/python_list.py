"""
This file is created to practice list methods
Author : prasanna
created date : 20th Nov 2025
Updated date :
updated Author name:
"""
import sys
from logging.config import stopListening

ls  = [] #empty list

print(ls)
print("id is",id(ls))

print("values of ls", ls)
print("type of ls", type(ls))
print("id of ls", id(ls))
print("size of ls", sys.getsizeof(ls)) # this method gives the size

print("methods of ls", dir(ls))

# Append:

ls.append(12)
print(ls)
print("id is ls", id(ls))

ls.append("etl")
print(ls)
print("id is ls", id(ls))

ls.append([1,2,3])
print(ls)
print("id is ls", id(ls))

# Mutability


# Extend

ls.extend('etl')
print(ls)

ls.extend([4,5,6])
print(ls)

# Insert
ls.insert(2,"automation")
print(ls)

print("*"*100)
print(ls)

ls.insert(0,10)
print(ls)

ls.append(["etl","auto"])
print(ls)

# Index

print(ls[2])
print(ls[10])

# POP:

print(ls.pop(2))
print(ls)

print(ls.pop(10))
print(ls)

# REMOVE:

ls.remove("automation")
print(ls)

ls.append(10)
print(ls)

ls.remove(10)
print(ls)



print("*"*100)

# SORT

ls1 = [1,2,5,4,8,9]
print("ls1 is ", ls1)

ls1.sort()
print("after sorting ",ls1)

ls1.sort(reverse=True)
print("after reverse sorting ",ls1)

# REVERSE
ls1 = [1,2,5,4,8,9]
print("ls1 is ", ls1)

ls1.reverse()
print(ls1)



# CLEAR()

# ls.clear()


# count()
print(ls)
print(ls.count(10))

# Copy
print(ls)
ls2 = ls.copy()
print(ls2)

print(id(ls))
print(id(ls2))


ls = [1,2,3,4,5,6,7,8]
tpl = (1,2,3,4,5,6,7,8)

print(ls[2:4])
print(ls[2::-1])
print(ls[2:4])
8,5,2
start = 7
stop = 0
step = -3

print("multi level list slice is",ls[7::-3])

ls1 = [1,2,3,[4,5,6,7,8],(9,6,3,6,7),23,56,78]

print("multi slice is" , ls1[3][2:4])

print("multi tuple slice is" ,ls1[4][4:1:-1])
# copy() ==shallow
# reference()

ls.sort(reverse=True)
print(ls)




