"""
This file python_str_methods.py is created to practice python str slicing
created by : Sreeni
Created On : 19th Nov 2025
Version : V1
Updated by:
Updated on:
"""

str1 = 'ETL AUTOMATION'

print("str1 is", str1)

print("str1[0]", str1[0])
print("str1[13]", str1[13])

# Slicing means extracting a part (substring) of a string by giving a range of positions.
# slicing is not just for string, we can also slice list, tuple, dict, set, frozenset, range, pandas, numpy array, series

#  string[start:stop:step] # start, stop and step are integer
#  **start**: The index of the first character to include in the slice (default is 0).
#  **stop**: The index where slicing stops (exclusive).
#  **step**: The interval between characters in the slice (default is 1).


print("str1[:]", str1[:])
print("str1[4:]", str1[4:])
print("str1[:4]", str1[:4], len(str1[:4]))

print("str1[:]", str1[0:3], len(str1[0:3]))


print("str1[:]", str1[0:3], len(str1[0:3]))

print("str1[0:15]", str1[0:15]) # this is slicing if end is not in index of str then it will print what ever is available

#print("str1[15]", str1[15]) # index if index is not availble we will get  IndexError: string index out of range


print("str1[0:12:1]",str1[0:12:1] )

print("str1[0:12:2]",str1[0:12:2] )

print("str1[0:10:3]",str1[0:10:3] )


print("str1[0:10:-1]",str1[0:10:-1] )

print("str1[::-1]",str1[::-1] ) #


madam  == madam

1221
141
121

