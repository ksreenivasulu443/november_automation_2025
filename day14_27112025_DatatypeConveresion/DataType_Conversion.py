# INT
from logging.config import stopListening
from tkinter import PanedWindow

from pandas import Flags

a = 100
print(type(a))

# Float

b= 101.233

print(type(b))

# Complex

c = 10+3j
print(type(c))
print(c.real)
print(c.imag)

# Bool
flag = True
flag1 = False
print(type(flag))
print(type(flag1))

# STR

name = "Hello"
print(type(name))

# LIST

list1 = [1,2,3,4]

# Tuple
# COncatenation
Tpl1 = (1,2,3)
Tpl2 = (4,5,6)
Tpl3 = Tpl1 +Tpl2
print(Tpl3)

tpl = (1,2,3)

times_3_tpl = tpl*3
print(times_3_tpl)

# membership testing

print("is 1 is there in tuple?:",1 in tpl)

print("is 10 is there in tuple?:",10 in tpl)

# LEngth
print(tpl)
print(len(tpl))

# Iteration
for i in tpl:
    print(i)


# Frozenset

set1 = {1,2,3,4}
print(type(set1))

frozen_set = frozenset(set1)
print(frozen_set)
print(type(frozen_set))

# frozen_set.add(5)
# print(frozen_set)

# frozen_set.update(5)
# print(frozen_set)

# frozen_set.clear()
# print(frozen_set)

# Indexing and Slicing

list = [11,22,33,44,55]
       # 0  1  2  3  4

first_value = list[0]
print(first_value)

last_value = list[4]
print(last_value)

# SLicing
print(list[0:2])

list = [11,22,33,44,55]
# 11,33,55
# start: 0
# stop: 5
# step: 2

print(list[0:5:2])

# Type casting

# Converting one datype into another datatype


int_val = 100
float_val = 101.234
str_val = "Hello"
str_val1 = "120"
bool_val = True
complex_val = 10+5j

# int convertion

print(type(int(float_val)))
print(type(int(str_val1)))
print(type(int(bool_val)))
# print(type(int(complex_val)))

print("*"*100)

# Str COnvertion

print(type(str(float_val)))
print(type(str(int_val)))
print(type(str(bool_val)))
print(type(str(complex_val)))

# Float Convertion
print("*"*100)
print(type(float(int_val)))
print(type(float(str_val1)))
# print(type(float(complex_val)))
print(type(float(bool_val)))

print("*"*100)
# Bool COnvertion

print(type(bool(int_val)))
print(type(bool(float_val)))
print(type(bool(complex_val)))
print(type(bool(str_val)))

# complex conversion
print("*"*100)
print(type(complex(int_val)))
print(type(complex(float_val)))
print(type(complex(bool_val)))
print(type(complex(str_val1)))