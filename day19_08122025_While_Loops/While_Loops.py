# While Loops
# The Code executes as long as the condition is true
# when the condition becomes false the loop stops

# while True:
#     print("Hello")


# keep popping the elements in list as long as the length is greater than zero

# customer_list = [101,102,103,104,105]
customer_list = []
print(customer_list)

while len(customer_list) > 0:
    popped_element = customer_list.pop()
    print("the popped element is ", popped_element)
    print("the current lenght now is ",len(customer_list))
    print("the current customer list is ",customer_list)


print("the iteratio is done now the lenght is zero")












# Counter Based While Loop :
# Retry Logic ( retry count must increase by 1 as long as the retry count equals max retries and when it does success is set to true till then false )

retry_count = 0
max_retries = 10

while retry_count <= max_retries:

    print(retry_count)
    if retry_count == max_retries:
        print("success or reached the maximun retries")
    else:
        print("failed")

    retry_count += 1
    # print(retry_count)













# Processing untill Threshold
# the processed count must increase by 1 untill total amount exceeds the threshould amount

records_to_process = [
    {"id": 101, "amount": 100},
    {"id": 102, "amount": 150},
    {"id": 103, "amount": 120},
    {"id": 104, "amount": 300},
    {"id": 105, "amount": 180},
    {"id": 106, "amount": 50}
]

threshould_amount  = 900
processed_count = 0
total_amount = 0
# record = records_to_process[processed_count]
# print(record)
print("*"*100)

while total_amount <= threshould_amount and processed_count < len(records_to_process):
    record = records_to_process[processed_count]
    id = record["id"]
    amount = record["amount"]
    print(f"processed record {record} and the id is {id} and amount is {amount} ")
    total_amount += amount
    print(f"the total amount is {total_amount}")
    processed_count += 1

print(f"exiting the loop as the condition has become false because {total_amount} exceeds the {threshould_amount}")


























