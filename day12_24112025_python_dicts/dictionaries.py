"""
This file is created to practice dict methods
Author : prasanna
created date : 24th Nov 2025
Updated date :
updated Author name:
"""

# ==============================================================================
# SECTION 1: INTRODUCTION TO DICTIONARIES
# ==============================================================================

"""
What is a Dictionary?
---------------------
- A dictionary is a collection of key-value pairs
- Unordered (before Python 3.7), ordered (Python 3.7+)
- Mutable (can be changed after creation)
- Keys must be unique and immutable (strings, numbers, tuples)
- Values can be of any data type
- Denoted by curly braces {}

WHY USE DICTIONARIES IN ETL TESTING?
- Store database connection parameters
- Map source to target field names
- Store test data configurations
- Store validation rules and expected results
"""
# ==============================================================================
# SECTION 2: CREATING DICTIONARIES
# ==============================================================================

# METHOD1: Using Curly braces
empty_dict = {}
print("the empty dict ", empty_dict)

# Method 2: Simple dict with key-vaue pairs

student = {
    "name": "John",
    "age": 25,
    "grade": "A"
}

print(f"the student dict {student}")

# Method3: dict() constructor

employee = dict(emp_id = 101,name="alice",departement = "IT")
print("the employee dict is ",employee)

# Method4 : from the list of tuples
database_config1 = dict([("host","localhost"),("port",5453),("host1","localhost")])
database_config = dict([("host","localhost"),("port",5453),("host","localhost2")])
print("dict using list of tuples ", database_config1)
print("dict using list of tuples ", database_config)

# Accessing the dictionary elements

products = {
    "product_id": "P001",
    "product_name": "laptop",
    "price": 999,
    "category": "electronics"
}

# Method1: Using square brackets

product_id = products["product_id"]
print(product_id)

prod_name = products["product_name"]
print(prod_name)

# Method2:Using get () method

price = products.get("price")
print(price)

store_name = products.get("store","store name is not available")
print(store_name)

# Nested Dictionary
db_connection = {
    "source_db":{
        "host_name": "source.server.com",
        "port": 5454,
        "database_name": "sales_db",
        "usernam": "user123",
        "password": 1234
    },
    "target_db":{
        "host_name": "target.server.com",
        "port": 5452,
        "database_name": "sales_target_db",
        "usernam": "user123",
        "password": 1234
    }
}

source_db_host_name = db_connection["source_db"]["host_name"]
print(source_db_host_name)

target_DB_password = db_connection["target_db"]["password"]
print(target_DB_password)

source_db_host_name = db_connection.get("source_db").get("host_name")
print(source_db_host_name)
target_DB_password = db_connection.get("target_db").get("password")
print(target_DB_password)

# Adding and modifying the elements


products = {
    "product_id": "P001",
    "product_name": "laptop",
    "price": 999,
    "category": "electronics"
}
print("dict before ",products)

products["product_id"] = "P002"

print("dict after ", products)

print("dict before ",products)

products["price"] = 1000

print("dict after ", products)

products["sales"] = 2000

print(products)

# UPDATE()

products.update({"product_name": "TV","warranty": "2 years"})
print(products)

# REMOVING ELEMENTS
# METHOD1: del keyword

del products["warranty"]
print(products)

# METHOD2 POP()
print(products.pop("sales"))
print(products)
# print(removed_items)

# METHOD POPITEMS()
print(products)
pop_item_removal = products.popitem()
print(products)
print(pop_item_removal)

# CLEAR()
products.clear()
print(products)

products = {
    "product_id": ["P001","P002","P003"],
    "product_name": "laptop",
    "price": 999,
    "category": "electronics"
}

print(products)