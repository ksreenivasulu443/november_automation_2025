a = 'etl'

print(type(a))

print(dir(a))
print("1)a memory ", id(a))

a = 'auto'

print(dir(a))
print("2)a memory ", id(a))

print("3) a memory", id(a.upper()))
# print("upper value at line5", a.upper())
#
# print("a value at line 7", a)

# print("a memory before updating", id(a))
# a = a.upper()
# print("a memory after updating", id(a))

# int
# float
# str
# bool
# complex
# None

# once a variable created using fundamental datatypes int, float, str, bool, complex, None
# we can't change value in it if you want to change new memory will be created(immutable)
# All fundamental datatypes are immutable in nature

b = 10
print(b,id(b))
c = 20
print(c,id(c))
b = c
c = 40

print(b,id(b))
print(c,id(c))
