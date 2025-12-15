# what is a Namespace
from pickle import GLOBAL

from pytz.reference import Local

# keeps tracks of the names (identifiers) and they refer to the object that you have created

# think of it like a dictionary

# key = variable/function
# value = the actual object which you create

# Namespace prevent the name conflicts

# types of namespace

# 1. Built in NameSpace

# example : len(),pop(),print(),TypeError

#2 Global Namspace

# Names will be defined at the top level of a function or module or code itself

x = 100

def show_global():
    print("The Global X is ",x)

show_global()

y = x+200
print(y)


# LOCAL Namespace
x = 100

def show_local():
    x = 50
    print("The Local X is ",x)

show_local()

y = 100+x
print(y)

print("*"*100)
# Enclosing Namespace

# The Names in outer functions when you have Nested functions
z = 500
def outer():
    z = 300
    def inner():

        print("the enclosing z:",z)
    inner()

outer()


# LEGB RULE

# L -Local
# E- Enclosing
# G- GLOBAL
# B- Built -in

# name = "rakesh"
# print(len(name))

# len = "Alice"

print(len)


# Global Variable
# Local variable

# z = 500 ------Global
# def outer():
#     z = 300 ------ Local
#     def inner():
#
#         print("the enclosing z:",z)
#     inner()
#
# outer()

