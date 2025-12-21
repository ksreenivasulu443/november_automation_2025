# tuple comprehensions
# dictionary comrpehensions
# List Comprehensions
# list comprehensions is a concise way to create lists
# syntex: [expression for item in iterable if condition]


# example
customer_ids = [100,101,102,103,104]
# create a list with prefix cust to the ids
new_list = []

[new_list.append(f"cust_{id}") for id in customer_ids]
print(new_list)

# categorize the given list as even_customer and odd_customer
# syntex: [expression for item in iterable if condition]

customer_types = [f"Even:{id}" if id % 2== 0 else f"odd:{id}" for id in customer_ids]
print(customer_types)


# create a list of dictionaries for each customer id with status active if id is even
customer_ids = [100,101,102,103,104]
print(customer_ids)
# syntex: [expression for item in iterable if condition]

customer_dict = [{"customer_id":id,"status":"active"} for id in customer_ids if id % 2 ==0]

print(customer_dict)

customer_new_dict = [{"customer_id":id,"status":"active" if id%2 == 0 else "inactive"} for id in customer_ids]
print(customer_new_dict)

# customer_new_dict1 = [{"customer_id":id,"status":"active" if id%2 == 0 else "inactive"} for id in range(1,100)]
# print(customer_new_dict1)

# ETL example
# Apply buiseness rule during transformation
balances = [500,1000,1500,3000,1200,50]
# Categorize(high,medium,low) this list based on balanace

categories = ["High" if bal > 2000 else "Medium" if bal >=1000 else "Low" for bal in balances]
print(categories)











