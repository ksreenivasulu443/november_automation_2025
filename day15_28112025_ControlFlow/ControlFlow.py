# Introduction to Control Flow

# it determines the order in which the code executes
# it makes the code to take decisions and repeat the actions
# Essential for data validation , processing and testing logics

# Components covered
# 1.Conditional statements
# if , else , elseif
# 2.Loops (for , while )
# 3.Loop Control(break , continue , pass)

# why it is important etl testing
# 1. validate the quality checks
# 2.Process the records iteratively
# 3.Handle different data validation scenarios
# 4.Validate transformations


# Conditional Statements
# If Condition

# scenario: we want to validate wheather a customer is valid or not
# condition : customer_id should be grerater than zero
customer_id = -10

# if customer_id >= 0:
#     print("the cusotmer is a valid customer")

# example: check customer status
# customer_status = active /inactive
# "=" it is a assignment
#  "==" it is comparetive

customer_status = "active"

# if customer_status == "active":
#     print("customer is an active customer ")

customer_status = "inactive"

if customer_status == "active":
    print("customer is an active customer ")

# example 3
# validating a valid balance
customer_balance = -100

if customer_balance >=0:
    print("the customer balance is valid and it is postive")

# If-Else Condition :

# if condition :
#     print("")
# else:
#     print("")

# scenario : if the customer_id is greater than or equal to 100 then he is a "premium customer" otherwise "standard customer"

customer_id = 99

if customer_id >=100:
    print("customer is a premium customer")
else:
    print("customer is a standard customer")

balance = 500

if balance >= 0:
    final_balance = balance
    print(f"valid balance exist and the final balance is {final_balance} ")
else:
    final_balance = 0
    print(f"invalid balance detected, and the revised balance is {final_balance}")

#     etl count validation
source_count = 9000
target_count = 1000
tolerance = abs(source_count - target_count)
difference = 200

if tolerance >= difference:
    print("the count difference is not acceptable")
else:
    print("acceptable but needs attention")


#     if elif else condition :(multiple condition )
# balance
#
# platinum: balance > 5000
# gold: balance > 2000
# silver: balance > 1000
# bronze
balance = 500

if balance >= 5000:
    print("customer is a platinum")
elif balance >=2000:
    print("customer is a gold")
elif balance >=1000:
    print("customer is a silver")
else:
    print("cusotmer is a bronze")


