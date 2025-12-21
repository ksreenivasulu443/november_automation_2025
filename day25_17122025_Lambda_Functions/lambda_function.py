# Lambda Functions

# A lambda function is a small anonymous function defined using the lambda keyword

# it can have any number of arguments but can take only one expression


# syntax:
# lambda_function_name = lambda arguments: expression

print("*"*100)

# example :

# lambda function that adds two numbers
# def sum_of_numbers(a,b):
#     sum = a+b
#     print("the sum is ",sum)
#     return sum

# add = lambda x,y: x+y

# sum_of_two_numbers = add(100,200)
#
# print("sum_of_two_numbers",sum_of_two_numbers)
#
# sum_two_numbers = sum_of_numbers(100,200)
# print("sum_two_numbers",sum_two_numbers)


print("*"*100)

# multiply three numbers

multiply = lambda a,b,c: a*b*c

product_of_three_numbers = multiply(23,44,660)
print("product_of_three_numbers",product_of_three_numbers)

print("*"*100)


# calculate tax

# def calculate_tax(amount):
#     tax = amount * 0.10
#     print("tax",tax)
#     return tax

# lambda_function_name = lambda arguments: expression
calculate_tax = lambda amount: amount*0.10

tax = calculate_tax(22000)
print(tax)


# divide two numbers

divide_two_numbers = lambda a,b: a/b

result = divide_two_numbers(220,22)
print(result)



# lambda function using filter
# syntex : filter(function , iterable)


print("*"*100)

# def even_num(x):
#     for cust in customer_list:
#         if cust%2 == 0:
#             print("even number")
#         else:
#             "odd"


customer_list = [100,101,102,103,104,105,106]
# filter this customer list for even numbers
# filter(function , iterable)


filtered_even_list = list(filter(lambda x: x%2 == 0, customer_list))

print(filtered_even_list)

filtered_odd_list = list(filter(lambda y: y%2 !=0, customer_list))
print(filtered_odd_list)


print("*"*100)


names = ["Abhishek","Abhay","Chinmay","Rahul","Sumit"]

# find the list of names which starts with A

filtered_names = list(filter(lambda x: x.startswith("A"), names))
print(filtered_names)


print("*"*100)


# find the customer with balance >0
# and active status

customers_list = [
    {"id":101, "name": "John", "status": "active", "balance": 1500},
    {"id":102, "name": "Jane", "status": "inactive", "balance": 500},
    {"id":103, "name": "Bob", "status": "active", "balance": -2500},
    {"id":104, "name": "Alice", "status": "active", "balance": 200},
]

# filter(function , iterable)

values = list(filter(lambda x: x["balance"]<0 or x["status"] == "active", customers_list))

print(values)










# Lambda with sorting

# syntex: sorted(iterable,key=function) key decides the sorting criteria or how to sort

# example 1

# sort the numbers by their squares


numbers = [5,2,9,1,7]
# print(numbers)
#
# numbers.sort(reverse=True)
# print(numbers)

# sorted(iterable, key=function)

new_numbers = sorted(numbers,key = lambda x: x**2)
print(new_numbers)

# neg_numbers = [5,-3,10,1,-11] -----[-11,-3,1,5,10]
neg_numbers = [5,-3,10,1,-11]
# ------> [1,9,25,100,122]

new_neg_numbers = sorted(neg_numbers, key= lambda y:y**2,reverse=True)
print(new_neg_numbers)








# sort the string by their lenghts
# sorted(iterable, key=function)

words = ["applesb","orange","kiwi","fig"]

sorted_words = sorted(words, key=lambda x:len(x),reverse=True)
print(sorted_words)







