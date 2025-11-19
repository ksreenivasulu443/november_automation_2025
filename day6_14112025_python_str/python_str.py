"""

This file python_str.py is created to practice python str datatype
created by : Sreeni
Created On : 14th Nov 2025
Version : V1
Updated by: Chandra
Updated on: 1st Jan 2026

"""
# a = 10
# b = 10.
# c = '10'

# str1 = 'ETL Automation labs'
# print("value of str1 is", str1)
# print("type of str1 is",type(str1) )
# print("id of str1 is",id(str1) )
# print("methods str1 is",dir(str1) )
# print("=="*100)
# str2 = 'ETL Automation labs'
# print("value of str2 is", str2)
# print("type of str2 is",type(str2) )
# print("id of str2 is",id(str2) )
# print("methods str2 is",dir(str2) )
#
# c = '10'
# d = "10"
# e = """10"""
# f = '''10'''
#
# # any value if we enclose within single quote, double quote, 3 time single quote, 3 time double
# print("=="*100)
# print("information about c", c, type(c), id(c))
# print("information about d", d, type(d), id(d))
# print("information about e", e, type(e), id(e))
# print("information about f", f, type(f), id(f))
# print("=="*100)
# str3 =  "It's raining outside" # when we have single quote in the actual string use double quotes to create string
#
# print("information about str3", str3, type(str3), id(str3))
# print("=="*100)
# str4 = 'It"s raining outside'
# print("information about str4", str4, type(str4), id(str4))


str5 = "I don't play cricket"

print(str5)

str6 =  ' Reena said, "She plays cricket" '
print(str6)


str7 = """ETL (Extract, Transform, Load) testing is the process of verifying data accuracy, completeness, and integrity '
        as it moves from source systems to a target system like a data warehouse"""

str8 = '''ETL (Extract, Transform, Load) testing" is the process of verifying data accuracy, completeness, and integrity '
        as it moves from source systems to a target system like a data warehouse '''

# documentation string""""""

def add():
    """doc string"""

# str type  - ETL Usecases


query1 = 'select * from table_name'

query2 = "select * from table_name where name='ETL' "

query3 = """select * from table_name 
          "where name='ETL' """

pkey = 'cutomer_id'

null_cols = 'customer_name'

host = '10.5.2.1'

username = 'nov2025'

print("methods on str",dir('etl') )


print("username.capitalize", username.capitalize())
print("username.upper", username.upper())



