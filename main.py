def validate_customer(customer_id,name,balance,age):
    # Check for Customer ID
    if customer_id < 0:
        print("Invalid customer ID")
        return False
    else:
        print("Valid Customer ID")

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

    print(f"All Validation for this customer:{customer_id} is passed!")
    return True



validate_customer(101,"Alice",100,25)


