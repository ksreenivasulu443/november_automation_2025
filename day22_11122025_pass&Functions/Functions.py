# Functions
# Functions are like receipe
#     -you give it the ingredients (inputs)
#     - it follow the steps (code)
#     -it will give you the final dish (output)


# reusable module /item which you can use it for doing something repeatable


# why do we functions?
# 1.reusability
# 2.easier to read
# 3.Easier to FIX
# 4.Easier to test

# IN the context of ETL Testing
# - Validate data
# - Transform the data
# -Reuse the validation logic across multiple tables


# Example

# def function_name():
    # code logic

# this code runs when you call the function


def greet_customer():
    print("Hello! Welcome to our Shop")
    print("abanvsbvvnlkvnlknlvk jkvbskjbdvjksvnklvd")


greet_customer()
greet_customer()
greet_customer()
print("*"*100)


# display_balance()

def display_balance():
    balance = 1000
    print(f"the Balance is {balance}")

display_balance()
display_balance()
display_balance()
display_balance()
display_balance()

# FUnctions with parameters:(input)
# with one parameter
#     parameter is a value which we pass it to the function for function to take it and utilize it in its operaition

def greet_customer_by_name(customer_name):
    print(f"Hello {customer_name}, Welcome to our shop and have a nice day !")

greet_customer_by_name("Siddhesh")
greet_customer_by_name("Rakesh")

print("*"*100)
# Functions with Two parameters
# arguements/parameters/inputs

def display_customer_balance(customer_name,balance):
    print(f"Hello {customer_name} , your balance for the day is {balance}")

display_customer_balance("rakesh",5000)
display_customer_balance(10000,"rakesh")




# Types of Arguments in Python Functions
# 1. Positional Arguments
# • 	Values are passed in the order the parameters are defined.
# • 	Example:







# 2. Keyword Arguments
# • 	You explicitly specify the parameter name when calling the function.
# • 	Order doesn’t matter since names are matched.







# 3. Default Arguments
# • 	Parameters can have default values if no argument is provided.
# • 	Example:

