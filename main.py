"""
===============================================================================
PYTHON DICTIONARIES - COMPLETE TRAINING MATERIAL
===============================================================================
Topic: Dictionaries in Python
Level: Beginner to Intermediate
Context: General Python + ETL Testing Focus
===============================================================================
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
- Cache lookup values for data transformation
- Store validation rules and expected results
"""

# ==============================================================================
# SECTION 2: CREATING DICTIONARIES
# ==============================================================================

print("=" * 80)
print("SECTION 2: CREATING DICTIONARIES")
print("=" * 80)

# Method 1: Using curly braces
empty_dict = {}
print(f"Empty dictionary: {empty_dict}")

# Method 2: Simple dictionary with key-value pairs
student = {
    "name": "John",
    "age": 25,
    "grade": "A"
}
print(f"\nStudent dictionary: {student}")

# Method 3: Using dict() constructor
employee = dict(emp_id=101, name="Alice", department="IT")
print(f"\nEmployee dictionary: {employee}")

# Method 4: From list of tuples
database_config = dict([("host", "localhost"), ("port", 5432), ("database", "etl_db")])
print(f"\nDatabase config: {database_config}")



# ==============================================================================
# SECTION 3: ACCESSING DICTIONARY ELEMENTS
# ==============================================================================

print("\n" + "=" * 80)
print("SECTION 3: ACCESSING DICTIONARY ELEMENTS")
print("=" * 80)

product = {
    "product_id": "P001",
    "product_name": "Laptop",
    "price": 999.99,
    "category": "Electronics"
}

# Method 1: Using square brackets []
print(f"\nProduct name: {product['product_name']}")
print(f"Price: ${product['price']}")

# Method 2: Using get() method (safer - returns None if key doesn't exist)
print(f"\nCategory: {product.get('category')}")
print(f"Discount: {product.get('discount', 'No discount available')}")  # Default value

# ETL EXAMPLE: Accessing nested configuration

# ETL EXAMPLE: Database connection configuration
db_connection = {
    "source_db": {
        "host": "source-server.com",
        "port": 3306,
        "database": "sales_db",
        "username": "etl_user",
        "password": "secure_pwd"
    },
    "target_db": {
        "host": "warehouse-server.com",
        "port": 5432,
        "database": "dw_sales",
        "username": "dw_user",
        "password": "secure_pwd"
    }
}

print(f"\nETL DB Connection Config: {db_connection}")
source_host = db_connection["source_db"]["host"]
print(f"\nSource database host: {source_host}")

# Common mistake to avoid
try:
    print(product["discount"])  # KeyError if key doesn't exist
except KeyError as e:
    print(f"\nError: Key {e} not found in dictionary")

# ==============================================================================
# SECTION 4: ADDING AND MODIFYING ELEMENTS
# ==============================================================================

print("\n" + "=" * 80)
print("SECTION 4: ADDING AND MODIFYING ELEMENTS")
print("=" * 80)

# Adding new key-value pairs
product["stock"] = 50
product["supplier"] = "TechCorp"
print(f"\nProduct after adding fields: {product}")

# Modifying existing values
product["price"] = 899.99
print(f"\nProduct after price update: {product}")

# Using update() method to add/modify multiple items
product.update({"stock": 45, "warranty": "2 years", "rating": 4.5})
print(f"\nProduct after bulk update: {product}")

# ETL EXAMPLE: Building a field mapping dictionary
field_mapping = {}
field_mapping["customer_id"] = "cust_id"
field_mapping["customer_name"] = "full_name"
field_mapping["email_address"] = "email"
field_mapping["phone_number"] = "contact_phone"
print(f"\nETL Field Mapping: {field_mapping}")

# ==============================================================================
# SECTION 5: REMOVING ELEMENTS
# ==============================================================================

print("\n" + "=" * 80)
print("SECTION 5: REMOVING ELEMENTS")
print("=" * 80)

test_dict = {
    "field1": "value1",
    "field2": "value2",
    "field3": "value3",
    "field4": "value4"
}

# Method 1: Using del keyword
del test_dict["field1"]
print(f"\nAfter del: {test_dict}")

# Method 2: Using pop() - removes and returns the value
removed_value = test_dict.pop("field2")
print(f"Removed value: {removed_value}")
print(f"After pop: {test_dict}")

# Method 3: Using pop() with default value
removed = test_dict.pop("non_existent", "Not found")
print(f"\nTrying to remove non-existent key: {removed}")

# Method 4: Using popitem() - removes and returns the last item (Python 3.7+)
last_item = test_dict.popitem()
print(f"\nLast item removed: {last_item}")
print(f"After popitem: {test_dict}")

# Method 5: Using clear() - removes all items
test_dict.clear()
print(f"After clear: {test_dict}")

# ==============================================================================
# SECTION 6: DICTIONARY METHODS
# ==============================================================================

print("\n" + "=" * 80)
print("SECTION 6: IMPORTANT DICTIONARY METHODS")
print("=" * 80)

etl_metadata = {
    "table_name": "customers",
    "record_count": 10000,
    "load_date": "2025-11-22",
    "status": "completed"
}

# keys() - returns all keys
print(f"\nAll keys: {etl_metadata.keys()}")
print(f"Keys as list: {list(etl_metadata.keys())}")

# values() - returns all values
print(f"\nAll values: {etl_metadata.values()}")
print(f"Values as list: {list(etl_metadata.values())}")

# items() - returns all key-value pairs as tuples
print(f"\nAll items: {etl_metadata.items()}")
print(f"Items as list: {list(etl_metadata.items())}")

# copy() - creates a shallow copy
metadata_backup = etl_metadata.copy()
print(f"\nCopied dictionary: {metadata_backup}")

# fromkeys() - creates dictionary from keys with same value
test_results = dict.fromkeys(["test1", "test2", "test3"], "PASS")
print(f"\nTest results: {test_results}")

# setdefault() - returns value if key exists, otherwise sets and returns default
etl_metadata.setdefault("error_count", 0)
print(f"\nAfter setdefault: {etl_metadata}")

# ==============================================================================
# SECTION 7: LOOPING THROUGH DICTIONARIES
# ==============================================================================

print("\n" + "=" * 80)
print("SECTION 7: LOOPING THROUGH DICTIONARIES")
print("=" * 80)

data_quality_checks = {
    "null_check": "PASS",
    "duplicate_check": "PASS",
    "format_check": "FAIL",
    "range_check": "PASS"
}

# Loop through keys only
print("\nLooping through keys:")
for check in data_quality_checks:
    print(f"  {check}")

# Loop through values only
print("\nLooping through values:")
for result in data_quality_checks.values():
    print(f"  {result}")

# Loop through both keys and values
print("\nLooping through key-value pairs:")
for check, result in data_quality_checks.items():
    print(f"  {check}: {result}")

# ETL EXAMPLE: Validating test results
print("\nValidation Report:")
failed_checks = []
for check_name, status in data_quality_checks.items():
    if status == "FAIL":
        failed_checks.append(check_name)
        print(f"  ❌ {check_name}: {status}")
    else:
        print(f"  ✓ {check_name}: {status}")

if failed_checks:
    print(f"\nFailed checks: {', '.join(failed_checks)}")

# ==============================================================================
# SECTION 8: NESTED DICTIONARIES
# ==============================================================================

print("\n" + "=" * 80)
print("SECTION 8: NESTED DICTIONARIES")
print("=" * 80)

# ETL EXAMPLE: Test data for multiple environments
etl_environments = {
    "dev": {
        "source_db": "dev_source",
        "target_db": "dev_target",
        "etl_server": "dev-etl-01",
        "active": True
    },
    "test": {
        "source_db": "test_source",
        "target_db": "test_target",
        "etl_server": "test-etl-01",
        "active": True
    },
    "prod": {
        "source_db": "prod_source",
        "target_db": "prod_target",
        "etl_server": "prod-etl-01",
        "active": True
    }
}

print("\nETL Environments Configuration:")
for env, config in etl_environments.items():
    print(f"\n{env.upper()} Environment:")
    for key, value in config.items():
        print(f"  {key}: {value}")

# Accessing nested values
print(f"\nProduction ETL Server: {etl_environments['prod']['etl_server']}")

# ETL EXAMPLE: Complex data transformation mapping
transformation_rules = {
    "customer_table": {
        "source_columns": ["cust_id", "first_name", "last_name", "email"],
        "target_columns": ["customer_id", "full_name", "contact_email"],
        "transformations": {
            "full_name": "CONCAT(first_name, ' ', last_name)",
            "contact_email": "LOWER(email)"
        }
    },
    "order_table": {
        "source_columns": ["order_id", "order_date", "amount"],
        "target_columns": ["order_id", "order_date", "order_amount"],
        "transformations": {
            "order_amount": "ROUND(amount, 2)"
        }
    }
}

print("\n\nTransformation Rules:")
for table, rules in transformation_rules.items():
    print(f"\n{table}:")
    print(f"  Source: {rules['source_columns']}")
    print(f"  Target: {rules['target_columns']}")
    print(f"  Transformations: {rules['transformations']}")

# ==============================================================================
# SECTION 9: DICTIONARY COMPREHENSION
# ==============================================================================

print("\n" + "=" * 80)
print("SECTION 9: DICTIONARY COMPREHENSION")
print("=" * 80)

# Basic dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"\nSquares: {squares}")

# With condition
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"\nEven squares: {even_squares}")

# ETL EXAMPLE: Creating field mapping from lists
source_fields = ["cust_id", "prod_id", "order_id", "amount"]
target_fields = ["customer_id", "product_id", "order_id", "order_amount"]

field_map = {source: target for source, target in zip(source_fields, target_fields)}
print(f"\nField mapping: {field_map}")

# ETL EXAMPLE: Creating default test status for all tables
tables = ["customers", "products", "orders", "shipments"]
test_status = {table: "NOT_TESTED" for table in tables}
print(f"\nInitial test status: {test_status}")

# ETL EXAMPLE: Filter records based on condition
records = {
    "rec1": {"amount": 100, "status": "valid"},
    "rec2": {"amount": 0, "status": "invalid"},
    "rec3": {"amount": 250, "status": "valid"},
    "rec4": {"amount": -50, "status": "invalid"}
}

valid_records = {k: v for k, v in records.items() if v["status"] == "valid"}
print(f"\nValid records only: {valid_records}")

# ==============================================================================
# SECTION 10: COMMON OPERATIONS AND FUNCTIONS
# ==============================================================================

print("\n" + "=" * 80)
print("SECTION 10: COMMON OPERATIONS AND FUNCTIONS")
print("=" * 80)

etl_stats = {
    "records_processed": 10000,
    "records_inserted": 9500,
    "records_updated": 400,
    "records_rejected": 100
}

# len() - number of key-value pairs
print(f"\nNumber of statistics: {len(etl_stats)}")

# in operator - check if key exists
print(f"\n'records_processed' in dictionary: {'records_processed' in etl_stats}")
print(f"'records_deleted' in dictionary: {'records_deleted' in etl_stats}")

# not in operator
print(f"\n'records_deleted' not in dictionary: {'records_deleted' not in etl_stats}")

# min() and max() on keys
sample_data = {10: "ten", 5: "five", 20: "twenty", 15: "fifteen"}
print(f"\nSample data: {sample_data}")
print(f"Minimum key: {min(sample_data)}")
print(f"Maximum key: {max(sample_data)}")

# sorted() - returns sorted keys
print(f"Sorted keys: {sorted(sample_data)}")
print(f"Sorted keys (descending): {sorted(sample_data, reverse=True)}")

# any() and all()
test_results_bool = {
    "test1": True,
    "test2": True,
    "test3": False,
    "test4": True
}
print(f"\nAll tests passed: {all(test_results_bool.values())}")
print(f"Any test passed: {any(test_results_bool.values())}")

# ==============================================================================
# SECTION 11: MERGING DICTIONARIES
# ==============================================================================

print("\n" + "=" * 80)
print("SECTION 11: MERGING DICTIONARIES")
print("=" * 80)

# Method 1: Using update()
source_config = {"host": "source.com", "port": 3306}
additional_config = {"username": "user", "password": "pass"}
source_config.update(additional_config)
print(f"\nMerged using update(): {source_config}")

# Method 2: Using ** unpacking (Python 3.5+)
config1 = {"host": "server1.com", "port": 5432}
config2 = {"database": "mydb", "schema": "public"}
merged_config = {**config1, **config2}
print(f"\nMerged using unpacking: {merged_config}")

# Method 3: Using | operator (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2
print(f"\nMerged using | operator: {merged}")

# ETL EXAMPLE: Merging default and custom configurations
default_etl_config = {
    "batch_size": 1000,
    "timeout": 300,
    "retry_count": 3,
    "log_level": "INFO"
}

custom_config = {
    "batch_size": 5000,  # Override
    "parallel_jobs": 4   # New setting
}

final_config = {**default_etl_config, **custom_config}
print(f"\nFinal ETL Config: {final_config}")

# ==============================================================================
# SECTION 12: DICTIONARY USE CASES IN ETL TESTING
# ==============================================================================

print("\n" + "=" * 80)
print("SECTION 12: ETL TESTING USE CASES")
print("=" * 80)

# USE CASE 1: Storing expected vs actual counts
print("\nUSE CASE 1: Record Count Validation")
count_validation = {
    "customers": {"expected": 10000, "actual": 10000, "status": "PASS"},
    "products": {"expected": 500, "actual": 498, "status": "FAIL"},
    "orders": {"expected": 50000, "actual": 50000, "status": "PASS"}
}

for table, counts in count_validation.items():
    status_symbol = "✓" if counts["status"] == "PASS" else "❌"
    print(f"  {status_symbol} {table}: Expected={counts['expected']}, "
          f"Actual={counts['actual']}, Status={counts['status']}")

# USE CASE 2: Data type validation
print("\nUSE CASE 2: Data Type Validation")
expected_data_types = {
    "customer_id": "INTEGER",
    "customer_name": "VARCHAR",
    "email": "VARCHAR",
    "registration_date": "DATE",
    "is_active": "BOOLEAN",
    "balance": "DECIMAL"
}

print("  Expected data types:")
for column, dtype in expected_data_types.items():
    print(f"    {column}: {dtype}")

# USE CASE 3: Test execution tracking
print("\nUSE CASE 3: Test Execution Tracking")
test_suite = {
    "TC001": {
        "name": "Null value check",
        "status": "PASS",
        "duration": 2.5,
        "timestamp": "2025-11-22 10:00:00"
    },
    "TC002": {
        "name": "Duplicate check",
        "status": "PASS",
        "duration": 5.2,
        "timestamp": "2025-11-22 10:02:30"
    },
    "TC003": {
        "name": "Data transformation",
        "status": "FAIL",
        "duration": 3.8,
        "timestamp": "2025-11-22 10:07:45",
        "error": "Transformation rule mismatch"
    }
}
...

