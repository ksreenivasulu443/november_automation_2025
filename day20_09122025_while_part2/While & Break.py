from random import randint

from day18_04122025_ForLoops.For_Loops import customers_list

# Game:
# guess the secret number game
# a number to guess
# a secret number to compare it with
# if guess is less than secret print lower
# if greater print greater
# print the number of attempts

# secret_number = randint(1,9)
# print("The secret Number is ",secret_number)
# guess = None
#
# attempts = 0
#
# while guess != secret_number:
#     guess = int(input("Please Guess the Number:"))
#     attempts +=1
#     if guess < secret_number:
#         print("Guessed Number is lower")
#     elif guess > secret_number:
#         print("Guess number is Greater")
#
# print(f"Yeahh, You have guessed the exact number {guess}")
# print(f"You have taken {attempts} attempts!")



# Break Statement:
# it immediately exits the loop regardless of the loop condition
# its commonly used inside for and while loops when you want to stop looping early

# why its important ?
# it prevents unneccesary iterations
# helps optimize the performance
print("*"*100)
# breaking out of for loop

# we have a customer list and we want to break out /stop when id becomes or equal to 104

customers_list = [101,102,103,104,105,106,107]

for customer in customers_list:
    if customer == 104:
        print(f"Error occured at customer{customer}")
        break
    print("the customers are ", customer)













# ETL use case : find the first match

# find the first invalid email record

records = [
    {"id": 101,"email":"john@example.com"},
    {"id": 102,"email":"sam@example.com"},
    # {"id": 103,"email":"invalid_.com"},
    {"id": 104,"email":"bob@example.com"},
    {"id": 105,"email":"jack@example.com"}
]
invalid_record = None
for record in records:
    # print(f"record is {record}")
    if "@" not in record["email"]:
        print("invalid email ID")
        invalid_record = record
        break

if invalid_record:
    print(f"{invalid_record['id']} Invalid record ")
else:
    print("all the records validated succesfully")







# break with while loop
# customer count must increase by 1 untill equals or exceeds 5 once hits should break  and aslo if it hits max_count 10

