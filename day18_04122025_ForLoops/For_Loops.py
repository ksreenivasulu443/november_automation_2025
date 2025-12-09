# Looping

list1 = [1,2,3,4,5]

# 1.for loops
# 2.while loops

# FOR LOOP

# for list_items in list1: 1,2
#     print("HEllo WOrld")

# Range
# 1,2,3,4,5,6,7,8,9
# for i in range(1,1000):
#     print(i)

customer_ids = [97,98,99,100]

for i in range(1,100):
    # print(100+i)
    customer_ids.append(100+i)

print(customer_ids)

# ENUMERATE
# enumerate() is a built in function inpython that adds an index to the items which we are iterating
# default index start 0, argument start = desired value
# it returns the index, value
customer_ids = [97,98,99,100]

for index,i in enumerate(customer_ids,start=100):
    print(index,i)

list_of_statuses = ["active","inactive","suspended","inactive"]

for index,i in enumerate(list_of_statuses,start=101):
    print(index,i)

print("*"*1000)

customers_list = [
    {"id":101, "name": "John", "status": "active", "balance": 1500},
    {"id":102, "name": "Jane", "status": "inactive", "balance": 500},
    {"id":103, "name": "Bob", "status": "active", "balance": 2500},
    {"id":104, "name": "Alice", "status": "active", "balance": 1200},
]

for customer in customers_list:
    print(customer)
    customer_id = customer["id"]
    print(customer_id)
    customer_name = customer["name"]
    print(customer_name)
    customer_balance = customer["balance"]
    print(customer_balance)

    if customer_balance > 1000:
        print("elite customer")


print("*"*100)
# count the number of valid and invalid customers  based on balance (balance > =0)

records = [
    {"id": 101,"balance": 1000},
    {"id": 102,"balance": -500},
    {"id": 103,"balance": 2000},
    {"id": 104,"balance": -200},
    {"id": 105,"balance": 1500}
]

valid_count = 0
invalid_count = 0
for record in records:
    print(record)
    record_balance = record["balance"]
    print(record_balance)
    if record_balance >= 0:
        valid_count = valid_count+1
    else:
        invalid_count = invalid_count +1

print("valid_count is =",valid_count)
print(f"The invalid count is {invalid_count}")





# FOR LOOPS with multiple If Statements

# calculating high value customers with high balance( "status" == "active" , balance >=1000)

customers_list = [
    {"id":101, "name": "John", "status": "active", "balance": 1500},
    {"id":102, "name": "Jane", "status": "inactive", "balance": 500},
    {"id":103, "name": "Bob", "status": "active", "balance": 2500},
    {"id":104, "name": "Alice", "status": "active", "balance": 200},
]

high_value_customer = []

for customer in customers_list:
    customer_status = customer["status"]
    customer_balance = customer["balance"]
    customer_id = customer["id"]

    if customer_status == "active":
        if customer_balance >= 1000:
            high_value_customer.append(customer_id)


print("the high_value_customers are = ",high_value_customer)



# Multiple categories
# calculate premium customer count (status = active and balance >=2000)
# standard customer count (status == active and balance >= 1000)
# inactive customer count (status == inactive)

customers_list = [
    {"id":101, "name": "John", "status": "active", "balance": 1500},
    {"id":102, "name": "Jane", "status": "inactive", "balance": 500},
    {"id":103, "name": "Bob", "status": "active", "balance": 2500},
    {"id":104, "name": "Alice", "status": "active", "balance": 200},
]

premium_customer_count = 0
standard_customer_count = 0
inactive_customer_count = 0

for customer in customers_list:
    customer_status = customer["status"]
    customer_balance = customer["balance"]
    customer_id = customer["id"]
    if customer_status == "active" and customer_balance >=2000:
        premium_customer_count += 1
        # premium_customer_count = premium_customer_count + 1
    elif customer_status == "active" and customer_balance >=1000:
        standard_customer_count += 1
    else:
        inactive_customer_count += 1

print("the count of premium_customer_count is = ",premium_customer_count)
print("the count of standard_customer_count is = ",standard_customer_count)
print("the count of inactive_customer_count is = ",inactive_customer_count)


print("*"*100)

# Nested for Loops (One loop inside another loop)

# simple example

# for i in range(1,4):     -----------1           2        3
#     print(f"the outer loop is: {i}")
#     for j in range(1,4):
#         print(f"the inner loop is = {j}") --------------1,2,3          1,2,3     1,2,3

for i in range(1,4):
    print(f"the outer loop is: {i}")
    for j in range(1,4):
        print(f"the inner loop is = {j}")







print("*"*100)
# Finding Matching records between source and target

source_ids = [101,102,103,104,105]
target_ids = [103,104,105,106,107]
matching_count=0

# for i in source_ids:
#     for j in target_ids:
#         if i == j:
#             print("matching value found")
#             matching_count += 1
#         else:
#             print("it is not matching")
# print(matching_count)




print("*"*100)


# I want to calculate the count of orders placed by each customer

customer_orders = [
    {"customer_id": 101,"customer_name" :'John',"orders" : [1001,1002,1003]},
    {"customer_id": 102,"customer_name" :'Joe',"orders" : [1004,1005,1006,87,88,900]},
    {"customer_id": 103,"customer_name" :'Jack',"orders" : [1007,1008,1009]},
    {"customer_id": 104,"customer_name" :'Andy',"orders" : [1010,1011,1012]}
]

for customer_order in customer_orders:
    count = 0
    customer_id = customer_order["customer_id"]
    customer_original_order = customer_order["orders"]
    customer_name = customer_order["customer_name"]
    # print(customer_order)
    # print(customer_id)
    # print(customer_name)
    # print(customer_original_order)

    for i in customer_original_order:
        count += 1
    print(f"{customer_id} is {customer_name} and his order count is {count}")
