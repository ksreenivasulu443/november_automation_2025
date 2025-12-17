# Functions That Return Values
# When a function 'returns' something , it gives you back a result
from day16_01122025_Operators.operators import status

# def calculate_tax(amount):
#     tax = amount * 0.10
#     # print("tax",tax)
#     return tax

# tax_amount = calculate_tax(3000)
# print(tax_amount)

# print(calculate_tax(3000))







# Using the returned value elsewhere
# amount = 1000
# def calculate_tax(amount):
#     tax = amount * 0.10
#     # print("tax",tax)
#     return tax
#
# tax_amount = calculate_tax(amount)
# total_amount = amount + tax_amount
# print(total_amount)

# def calculate_total_amount(total):
#     tax_amount = calculate_tax(total)
#     final_total = total+tax_amount
#     return final_total
#
# val = calculate_total_amount(1000)
# print(val)


# example2:

# transcation1 = 1000
# transcation2 = 500

# i want to find the sum of transcation and calculate the tax of this sum of transc and come up wit a total_transcation_amount_tax

# def sum_of_transc(a,b):
#     sum = a + b
#     # print("sum is =",sum)
#     return sum
#
#
# def calculate_tax(amount):
#     tax = amount * 0.10
#     # print("tax",tax)
#     return tax

# sum_of_transcation = sum_of_transc(transcation1,transcation2)
# print("sum_of_transcation=",sum_of_transcation)
#
# tax_of_sum_transcation = calculate_tax(sum_of_transcation)
# print(f"the tax_of_sum_transcation = {tax_of_sum_transcation}")
#
# total_transcation_amount_tax = sum_of_transcation+tax_of_sum_transcation
# print(total_transcation_amount_tax)







# Return Vs Print()

# you cannot use print statement after return statement
# for a function return statement would be the last action as it comes out /exits the code








# Return Multiple Values


# def calculate_tax(amount):
#     tax = amount * 0.10
#     total_amount = amount+tax
#     # print("tax",tax)
#     return tax,total_amount

# transcation_tax,total_transcation, = calculate_tax(10000)
# print("transcation_tax =",transcation_tax)
# print("total_transcation = ",total_transcation)






# Building A VALIDATION FUNCTION

# simple validation

# check if the balance is not negetive

# def is_balance_valid(balance):
#     if balance >=0:
#         # print("valid balance")
#         return True
#     else:
#         return False
#
# print(is_balance_valid(1000))
# print(is_balance_valid(-1000))
# print(is_balance_valid(0))
#
# def validate_balance(balance):
#     if balance < 0:
#         return f"Invalid Balance and balance cannot be negetive!{balance}"
#     elif balance == 0:
#         return "Warning! your balance is Zero!"
#     else:
#         return "Good! your balance is positive"
#
# print(validate_balance(0))
# print(validate_balance(100))
# print(validate_balance(-100))

print("*"*100)
# Complete Customer Validation
# validate the customer data
# returns True if valid and False if invalid
# 1.validate the customer_id
# 2.validate name
# 3. balance
# 4. age


def validate_customer(customer_id,name,balance,age):
    # Check for Customer ID
    if customer_id < 0:
        print("Invalid customer ID")
        # return False

    else:
        print("Valid Customer")

    # check for Valid Name
    if name == "" or name is None:
        print("Name is Empty or NULL")
        return False
    else:
        print(f"{name} : Name is Valid ! ")

    # Check for balance
    if balance <=0:
        print("Balance is not valid ")
        return False
    else:
        print("Valid Balance")

    # checking for age

    if age <18:
        print("Age is Invalid, below 18")
        return False
    else:
        print(f"Age is valid {age}")

    print(f"All Validation for this {customer_id} is passed!")
    return True



print(validate_customer(101,"Alice",100,25))





print("*"*100)



# example
# create a function to validate status and use that function to validate each customer from customer list

customers_list = [
    {"id":101, "name": "John", "status": "active", "balance": 1500},
    {"id":102, "name": "Jane", "status": "inactive", "balance": 500},
    {"id":103, "name": "Bob", "status": "suspended", "balance": -2500},
    {"id":104, "name": "Alice", "status": "active", "balance": -200},
]

def validate_status(status,balance):
    if status == "active" and balance >0:
        print("active customer")
        return True
    else:
        print("Inactive Customer")
        return  False

for customer in customers_list:
    status = customer["status"]
    balance = customer["balance"]
    validate_status(status,balance)
