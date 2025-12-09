# Nested IF condition
from pickle import PROTO

# customer_id = int(input("input the cusotmer id :"))
# balance = int(input("put the balance : "))
# status = input("what is the status ?:")

# if customer_id > 0:
#     print("valid customer ID")
#     if balance >= 0:
#         print("valid balance")
#         if status == "active":
#             print("Customer is active")
#             print("all checks are passed : Process the customer")
#         else:
#             print("Customer is not active ")
#             print("Skip Processing")
#     else:
#         print("Invalid Balance ")
#         print("Reject the Record")
# else:
#     print("Invalid Cusotmer ID ")
#     print("Reject the record")
print("/n"*50)
# example

record = {
    "customer_id": 102,
    "email": "customer@example.com",
    "balance": -2000,
    "country": "US"
}

validation_passed = False

if "customer_id" in record:
    print("record has customer id")
    if record["customer_id"] > 0:
        print("customer id is positive")
        if "email" in record and "@" in record["email"]:
            print("email is valid")
            if record["balance"] >=0:
                print("balance is positive")
                if record["country"] in ["india","UK","France","US"]:
                    validation_passed = True
                    print("Supported Country")
                    print("All Validations Passed , It is a Valid Record")
                else:
                    print("Unsupported Country")
            else:
                print("balance is negetive ")
        else:
            print("invalid email id")
    else:
        print("customer id is negetive")
else:
    print("missing customer id")

if not validation_passed:
    print("record failed ")






