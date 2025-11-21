# sort in list

ls = [9,8,5,4,34,56]

ls.sort(reverse=True)

print(ls)



# types of copy() method in lists
# 1.referencial copy():
# A referential copy in python means when you assign one list to another , both variables will point to the same list object iin memory
# change made to the one variable will be reflected in the other

ls = [1,2,3,4,5]

ls1 = ls

print("the value of ls", ls)
print("the value of ls1", ls1)

print("the location of ls", id(ls))
print("the location of ls1", id(ls1))

ls.append(6)

print("the value of ls", ls)
print("the value of ls1", ls1)

print("the location of ls", id(ls))
print("the location of ls1", id(ls1))

ls1.remove(1)

print("the value of ls", ls)
print("the value of ls1", ls1)

print("the location of ls", id(ls))
print("the location of ls1", id(ls1))



# COpy() (shallow copy)

ls2 = ls.copy()

print("the value of ls", ls)
print("the value of ls2", ls2)

print("the location of ls", id(ls))
print("the location of ls2", id(ls2))

ls.append(100)
print("the value of ls", ls)
print("the value of ls2", ls2)
#
# print("the location of ls", id(ls))
# print("the location of ls2", id(ls2)







# Tuples

tpl = (1,2,3)
        # 0 1 2
print(dir(tpl))

print(tpl.count(1))

print(tpl[1:3:])

# start : 1
# stop : 3
# step : 0


# Slicing

ls = [1,2,3,4,5,6,7,8]

print(" 3 and 4 slice is ", ls[2:4:1])

print("7 and 6 slice is ",ls[6:4:-1])

print("8,5,2 slice is ",ls[7:0:-3])

print("1,4,7 slice is ", ls[0:7:3])

lst = (23,34,56,78)

print("slice of 23,78",lst[0:4:3])

# Multi level slicing

ls = (1,2,(3,4,5),45,65)

print("the slice of tuple(1,2,(3,4,5),45,65) is ", ls[2][0:2])


# Difference between list and tuples

# tuple is defined using paranthesis() whereas list is defined inside the brackets[]
# Tuple is immutable whereas list mutable in nature
# performance of tuple is greater than list because immutability



