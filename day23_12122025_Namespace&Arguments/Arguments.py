# ARGUMENTS

# - Arguments are the values you pass into a function when you call it.
# - They provide input so the function can do its job.
# - Think of them like ingredients you give to a recipe (the function).




# Types of Arguments in Python Functions
# 1. Positional Arguments
# • 	Values are passed in the order the parameters are defined.
# • 	Example:

def display_customer_balance(customer_name,balance):
    print(f"Hello {customer_name} , your balance for the day is {balance}")


display_customer_balance("Rakesh",1000)

display_customer_balance(1000,"Rakesh")



print("*"*100)

# 2. Keyword Arguments
# • 	You explicitly specify the parameter name when calling the function.
# • 	Order doesn’t matter since names are matched.

display_customer_balance(1000,"Rakesh")
display_customer_balance(balance=1000,customer_name="Rakesh")



print("*"*100)
# 3. Default Arguments
# • 	Parameters can have default values if no argument is provided.
# • 	Example:

def greet(name,age = 18):
    print(f"Hello My name is {name} and I am {age} years old! ")


greet("rakesh")
greet("Alice",30)

