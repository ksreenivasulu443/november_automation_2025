"""
This file is created to practice list methods
Author : prasanna
created date : 20th Nov 2025
Updated date :
updated Author name:
"""
import sys
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
