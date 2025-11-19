# print("Hello, Welcome to ETL Automation Labs!") # printing string
#
# a = 10
#
# print(a) # printing variable value
#
# print(10+20+30) # printing mathematical expression
#
# print("Value of a : ", a) # we are combining str with variable
#
# print("sum of 10 20 30 is", 10+20+30) # we are combining str with expression

# comment

# comment multiple lines ==> ctrl + /
# un comment multiple lines ==> ctrl + /

"this is double quote comment"
'this is single quote comment'
"""this is three double quote  comment"""
'''this three single quote is comment'''

help(print)

# a = 10
# b = 20
# c = 30
#
# print(a,b,c)
# print(a,b,c, sep = ',')
# print(a,b,c, sep = '|')
#
# print("value of a is", a, sep='|')

# a = 20
# b = 40


# print(a)
# print(b)

# print(a, end='-')
#
# print(a,b, sep='-')

# source = 10
# target = 15
#
# print("source count is",source, "target count is", target, sep=' ', end='|') # sep =' '
# print("source count is",source, "target count is", target, sep=' ')

a = 10
b = 20
print(a,b)
print(a,b, sep='-')
print(a,b, sep='-', end= '|')
print(a*b)

with open('/Users/admin/PycharmProjects/november_automation_2025/day4_12112025_python_print/output.log','w') as f:
    print("hello, Good afternoon",file=f)
    print(a, b, file=f)
    print(a, b, sep='-', file=f)
