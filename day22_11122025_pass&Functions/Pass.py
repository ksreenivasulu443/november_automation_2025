# PASS
# Pass statement can be used to do nothing and use it for future implementation or action need to take near future
from day17_03122025_Nested_IF_control_flow.nested_if import record
from day21_10122025_Continue.Continue import customers

# example
customer_ids = [101,102,103,104,105]

for customer in customer_ids:
    if customer == 103:
        # new_customer_id = customer + 200
        # print(f"processing the customer{new_customer_id}")
        pass
    else:
        new_customer_id = customer+100
        print(f"processing the customer{new_customer_id}")

records = [
    {"id": 101,  "type":"insert"},
    {"id": 102, "type": "update"},
    {"id": 103, "type": "delete"},
    {"id": 104, "type": "insert"},
]

for record in records:
    type = record["type"]
    id = record["id"]

    if type == "insert":
        print(f"Customer {id} insertion operation")
    elif type == "update":
        print(f"Customer {id} update operation")
    elif type == "delete":
        # TODO implement the delete logic
        pass
    else:
        print("unknown operation")