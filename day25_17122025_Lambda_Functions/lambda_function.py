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

add = lambda x,y: x+y

sum_of_two_numbers = add(100,200)
#
# print("sum_of_two_numbers",sum_of_two_numbers)
#
# sum_two_numbers = sum_of_numbers(100,200)
# print("sum_two_numbers",sum_two_numbers)



# multiply three numbers

multiply = lambda a,b,c: a*b*c

product_of_three_numbers = multiply(23,44,660)
print("product_of_three_numbers",product_of_three_numbers)







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
# filter(function , iterable)


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






names = ["Abhishek","Abhay","Chinmay","Rahul","Sumit"]

# find the list of names which starts with A

filtered_names = list(filter(lambda x: x.startswith("S"), names))
print(filtered_names)










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

# sorted(iterable,key=function) key decides the sorting criteria or how to sort

# example 1

# sort the numbers by their squares












# sort the string by their lenghts







