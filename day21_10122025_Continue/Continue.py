# Continue
# Skips the rest of the current iteration and moves on with the next iteration


customers = [
    {"id": 101,"status":"active"},
{"id": 102,"status":"inactive"},
{"id": 103,"status":"active"},
{"id": 104,"status":"suspended"}
]

# for customer in customers:
#     id = customer["id"]
#     status = customer["status"]
#     if customer["status"] != 'active':
#         print(f"we are skipping this customer {id} and his status is {status}")
#         continue
#     print(f"processing the customer{id}")


# Print the odd numbers from 1 to 10 using the while loop and continue
num = 1
while num <=10:
    if num % 2 == 0:
        print(f"im skipping this number{num} because it is even number")
        num += 1
        continue

    print("printing the odd number",num)
    num+= 1
