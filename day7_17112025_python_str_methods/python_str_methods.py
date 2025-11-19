"""
This file python_str_methods.py is created to practice python str methods
created by : Sreeni
Created On : 17th Nov 2025
Version : V1
Updated by:
Updated on:
"""

str1 = 'ETL Automation labs'

print("str1.lower()", str1.lower())
print( "str1.upper()", str1.upper())
print( "str1.capitalize()", str1.capitalize())
print( "str1.title()", str1.title())
print( "str1.casefold()", str1.casefold())
print( "str1.swapcase()", str1.swapcase())

str2 = 'Hanuman Tech solutions'
print("str2.lower()", str2.lower())
print( "str2.casefold()", str2.casefold())

print("=="*100)
text = "Straße"
print("text.lower()", text.lower())
print("text.casefold()",text.casefold())
# str3 = 'ईटी L'
# print("str3.lower()", str3.lower())
# print( "str3.casefold()", str3.casefold())

print("=="*100)


str4 = ' ETL Automation Labs         '

print("str4, len(str4)", str4, len(str4))

print("str4.lstrip", str4.lstrip(),len(str4.lstrip()) )
print("str4.rstrip", str4.rstrip(),len(str4.rstrip()) )
print("str4.strip", str4.strip(),len(str4.strip()) )


print("=="*100)
str5 = '   42313333333 ET@L 456@!'
print("str5.lstrip : ", str5.lstrip('1234 ') )
print("str5.rstrip", str5.rstrip('456'), )
print("str5.strip", str5.strip('123456@! ') )


str6 = 'ETL Automation labs labs labs'

print("count of E", str6.count('E'))
print("count of o", str6.count('o'))
print("count of a", str6.count('a'))
print("count of A", str6.count('A'))
str7 = str6.lower()
print("str7 is", str7)
print("count of A/a", str7.count('a'))
print("count of A/a", str6.lower().count('a'))

print("count of labs", str6.count('labs'))


str8 = 'Etlautomationlabs@Gmail.Com'

print("str8.endswith('in')", str8.endswith('in')) # validation function

print("str8.startwith('etl')", str8.startswith('etl'))


print("str8.islower()", str8.islower())

print("str8.isupper()", str8.isupper())
print("str8.istitle()", str8.istitle())


str9 = 'Hanuman1'

print("str9.isalpha()", str9.isalpha())
print("str9.isalnum()", str9.isalnum())

str10 = '10.3'
print(str10.isnumeric())




