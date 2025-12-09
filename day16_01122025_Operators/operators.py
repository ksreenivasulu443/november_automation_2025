# what are operators?
from traceback import print_tb

# operators are special symbols that perform operations on variables nad values
# it supports different types for different operations
# it is very important for testing validation and manipulation and logic testing

# Types of operators
# 1. Arithmetic operators
# 2. Comparision/Relational Operators
# 3. Logical operatos
# 4. Assignment Operatos
# 5. Bitwise operator
# 6. Membership Operators
# 7.Identity Operatos

# why it is important ?

# data metrics and aggregations
# compare source vs target
# validation on data conditions
# applying filters and transform the data
# perform data quality checks
# Building the complex validation logic


# 1. Arithmetic operators

transcation_1_amount = 1000
transcation_2_amount = 250

# 1a) Addition

sum_amount = transcation_1_amount + transcation_2_amount
print(sum_amount)


# 2 Subtraction (-)

difference_amount = transcation_1_amount - transcation_2_amount
print(difference_amount)

difference_amount = transcation_2_amount - transcation_1_amount
print(difference_amount)

# 3. Multiplication(*)

multiply_value = 0.05
value = transcation_2_amount * multiply_value
print(value)

# 4. Division(/)

average = (transcation_1_amount + transcation_2_amount)/2
print(average)

# 5. Floor Division(//) rounds down to the lower whole number

print(999/500)
print(999//500)

print(999/300)
print(999//300)

# Modulus (%) returns the remainder

print(999%500)
print(1000%500)

# Exponential (**)

print(10**2)
print(10**3)


# Comparision Operators

# Basically used for comparing two values and returns the result in boolean values (True/False)

customer1_balance = 1500
customer2_balance = 2500
customer3_balance = 2500
minimun_balance = 1000

# 1. Equal to (==)

is_equal = customer1_balance == customer2_balance
print(is_equal)

is_equal = customer3_balance == customer2_balance
print(is_equal)

# 2. Not equal to (!=)
not_equal = customer1_balance != customer2_balance
print(not_equal)

is_equal = customer3_balance != customer2_balance
print(is_equal)

# 3. Greater than (>):
customer1_balance = 1500
customer2_balance = 2500
customer3_balance = 2500
minimun_balance = 1000

is_greater = customer1_balance > customer2_balance

print("is_greater ouput is =",is_greater)

is_greater = customer2_balance > customer1_balance

print("is_greater ouput is =",is_greater)


# 4. Lesser than (>):

is_lesser = customer1_balance < customer2_balance

print("is_lesser ouput is =",is_lesser)

is_lesser = customer2_balance < customer1_balance

print("is_lesser ouput is =",is_lesser)

# 4. Greater than or equal to (>=)

customer1_balance = 1500
customer2_balance = 2500
customer3_balance = 2500
minimun_balance = 1000

meets_minimum = customer1_balance >= minimun_balance
print(meets_minimum)

# 5. lesser than or equal to (<=)

meets_minimum = customer1_balance <= minimun_balance
print(meets_minimum)


# LOGICAL OPERATORS

customer_id = -101
balance = 2500
status = "inactive"
age = 30

# 1. AND operator
condition1 = customer_id > 0
condition2 = balance > 1000
condition3 = status == "active"
condition4 = age > 18

# False and True = False

print("condition1 and condition2 = " , condition1 and condition2)

# False and false = false
print("condition1 and condition3=",condition1 and condition3)

# True and False = False

print("condition3 and condition1=",condition3 and condition1)

# True and true = true

print("condition2 and condition4=",condition2 and condition4)

print("*"*100)

# 1. OR operator
customer_id = -101
balance = 2500
status = "inactive"
age = 12
height = 180

condition1 = customer_id > 0
condition2 = balance > 1000
condition3 = status == "active"
condition4 = age > 18
condition4 = height > 140

# False and True = True

print("condition1 and condition2 = " , condition4 or condition2)

# False and false = false
print("condition1 and condition3=",condition1 or condition3)

# True and False = True

print("condition4 and condition1=",condition4 or condition1)

# True and true = true

print("condition2 and condition4=",condition2 or condition4)

# Not Operator
print("*"*100)

is_suspended = False

print(not is_suspended)

is_suspended = True

print(not is_suspended)

# complex logical expressions

# eligible cusomters condition1 (balance >=2000 and status = "active") or age >=40
print("*"*100)

customer_id = 101
balance = 2500
status = "inactive"
age = 15
height = 180

eligibility = (balance >=2000 and status == "active") or (age >=40)
                    # True and False = False or False = False
print(eligibility)

# Assignment Operators

# 1.equal to (=)

balance = 1000
balance1 = 1000
print(balance)
# 2. add and assign (+=)

balance = balance +500
print(balance)

balance1 += 500
balance = balance +500
print(balance1)

debt = 350

debt += 200
print("debt is ",debt)
# debt = debt+200
debt = 350 +200

print("*"*100)
# 2.substarct and assign ( -=)
print(balance)

balance -= 200
# balance = balance -200

print(balance)
print("*"*100)
# 3 Multiply and assign ( *= )
factor = 2.5
print(balance)

balance *= 2.5
balance = balance*2.5

print(balance)
print("*"*100)
# 4 divide and assign ( /=)
print(balance)

balance /= 2
# balance = balance /2
print(balance)

# 5. Floor divide and assign (//=)
print("*"*100)
records = 1000

records //= 3
# records = records // 3

print(records)

# 6. modulus and assign ( %=)
print("*"*100)

records = 999
print(records)

records %= 500

print(records)

# 7. exponential and assign (**=)

sqaure = 100

sqaure **= 3

print(sqaure)

# BIT WISE OPERATORS
print("*"*100)
# 1 = True
# 0 = False

read_permission = 2
write_permission = 1

# 1. BITWISE_AND ( &)

print(5 & 3)

print(bin(5))
print(bin(3))

print(int("001",2))

customerid = 101
cust_balance = 2500


eligibil = (customerid > 100) and (cust_balance > 1000)
print("eligibility is ",eligibil)

eligibil = (customerid > 100) & (cust_balance > 1000)
print("eligibility is ",eligibil)

# 2.BITWISE_OR ( | )

print( 5 | 4)

# 3 Bitwise XOR (^)
# false output for same combination and true for different combination

print( 5 ^ 4)
print(bin(5))

# Bitwise NOT(~): inverts all the bits
print(~5)

# Membership Operator
# also gives you the output in boolean (True and false)
countries = ["india","UK","USA"]

# IN operator
print("india" in countries )
print("india in conutries=","india" in countries )
print("srilanka" in countries)

# 2. NOT IN
# tests wheather the value does not exist in the sequence
print("srilanka" not in countries)

print("india in conutries=","india" not in countries )

# IDENTITY OPERATOR : tests if two variables point to the same object or memory location
# IS

a = [101,102,103]
b = a
c = [101,102,103]

print( "is a is b=" , a is b)
print("is a is c = ", a is c)

print("id of a is :",id(a))
print("id of b is :",id(b))
print("id of c is :",id(c))

# IS NOT

a = [101,102,103]
b = a
c = [101,102,103]

print(a is not c)
print(a is not b)

name = "Tommy"
print(f"the name is {name}")