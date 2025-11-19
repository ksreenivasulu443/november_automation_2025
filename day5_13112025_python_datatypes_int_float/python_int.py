a = 10

print("value of a", a)
print("type of a", type(a)) # type function will display datatype
print("id of a", id(a)) # memory loc of a variable
print("size of a", a.__sizeof__()) #will display size
print("methods available/transformations int type", dir(a)) #display methods

# __name__ ==> dunder methods/special methods
print("=="*100)

b = 10
print("value of b", b)
print("type of b", type(b))  # type function will display datatype
print("id of b", id(b))  # memory loc of a variable
print("size of b", b.__sizeof__())  # will display size
print("methods available/transformations int type", dir(a))  # display methods

print("=="*100)
c = 11
print("value of c", c)
print("type of c", type(c))  # type function will display datatype
print("id of c", id(c))  # memory loc of a variable
print("=="*100)
d = -11
print("value of d", d)
print("type of d", type(d))  # type function will display datatype
print("id of d", id(d))  # memory loc of a variable
print("=="*100)
e = 0
print("value of e", e)
print("type of e", type(e))  # type function will display datatype
print("id of e", id(e))  # memory loc of a variable
print("=="*100)
print(a+b)
print("=="*100)
print(a.__add__(b))


print("=="*100)

k = 10
l = 0
sum1 = k +l
print("id of k", id(k))
print("id of l", id(l))
print("id of sum1", id(sum1))
print("=="*100)
m = 371258673846573416576423756473265784326576143875634371258673846573416576423756473265784326576143875634
print("value of m", m)
print("type of m", type(m))  # type function will display datatype
print("id of m", id(m))
print("size of m", m.__sizeof__())
# ETL use case
# source_count = 10
# number_of_columns = 2
# length_phone = 10
# diff = source_cnt-target_cnt

