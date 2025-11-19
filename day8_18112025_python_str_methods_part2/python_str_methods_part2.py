"""
This file python_str_methods.py is created to practice python str methods part2
created by : Sreeni
Created On : 18th Nov 2025
Version : V1
Updated by:
Updated on:
"""


str1 = 'column1,column2,columns3,column4'

print("str1 is", str1, type(str1))

split_out = str1.split(sep=',', maxsplit=1) # default sep = space

print("split out", split_out, type(split_out))

str2 = "Users/admin/PycharmProjects/november_automation_2025/day8_18112025_python_str_methods_part2/python_str_methods_part2.py"

print("str2.split", str2.split(sep='/', maxsplit=1))

print("str2.split", str2.rsplit(sep='/', maxsplit=1))

print("=="*100)

str3 = 'ETL Automation labs'

print("find E ", str3.find('E'))
print("index E ", str3.index('E'))


print("find A ", str3.find('A'))
print("index A ", str3.index('A'))


print("find z ", str3.find('z')) # find will return -1 when specified character is not found
# print("index z ", str3.index('z')) # index will return error when specified character is not found



# SQl - index will start from 1


# In python index will start from 0

print("str3.find('s')", str3.find('s'))
print("str3.index('s')", str3.index('s'))
print("str3.find('a')", str3.find('a', 10))
print("str3.index('a')", str3.index('a'))

# python indexing - syntax
# str[index value - int]

print("str3[0]", str3[0])
print("str3[1]", str3[1])
print("str3[2]", str3[2])
print("str3[3]", str3[3])

print("str3[10]", str3[10])

print("str3[18]", str3[18])

# print("str3[19]", str3[19])

print("str3[-1]", str3[-1])

print("str3[-19]", str3[-19])


print("str3[6]",str3[6] )

print("str3[-17]",str3[-17] )








