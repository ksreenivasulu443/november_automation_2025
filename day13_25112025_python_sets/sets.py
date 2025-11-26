"""
===============================================================================
PYTHON SETS - COMPLETE TRAINING MATERIAL
===============================================================================
Topic: Sets in Python
Level: Beginner to Intermediate
Context: General Python + ETL Testing Focus
===============================================================================
"""
from main import unique_customer_ids, batch3

# ==============================================================================
# SECTION 1: INTRODUCTION TO SETS
# ==============================================================================

"""
What is a Set?
--------------
- A set is an unordered collection of unique elements
- No duplicate values allowed
- Unordered (no indexing, no slicing)
- Mutable (can add/remove elements after creation)
- Elements must be immutable (strings, numbers, tuples - not lists or dicts )
- Denoted by curly braces {} or set() function
- Based on mathematical set theory

WHY USE SETS IN ETL TESTING?
- Remove duplicate records from data
- Find unique values in columns
- Compare data between source and target (missing records, extra records)
- Validate referential integrity
- Check for intersection of data sets
- Identify orphan records
- Performance: O(1) lookup time (very fast!)
"""
# ==============================================================================
# SECTION 2: CREATING SETS
# ==============================================================================
print('\n'*100)

set1 = {1,2,3,4,5}
print(type(set1))

set1 = {}
print(type(set1))

set2 = set()
print(set2)
print(type(set2))

set1 = {1,2,3,3,4,3,4,5,5}
print(set1)

string1 = "hellollo"
set2 = set(string1)
print(set2)

# set1 = {1,2,3,4,5}
# print(set1[0:2])

# set1 = {1,2,3,4,5,{2:3}}
# print(set1)

a = 1
print(id(a))
a = a+1
print(id(a))

# immutable in nature : fundamental/collection datatype ex: numbers , string , tuple
# mutable in nature : dict , list

set2 = {1,2,3,4}
print(set2)

set2.add(6)
print(set2)

# Accessing the elements of the sets()

set2 = {1,2,3,4}

# method1: Membership testing

print("do we have 1 in set1?:",{1 in set2})

print("do we have 2 in set2?:",{2 in set2})

print("do we have 6 in set2?:",{6 in set2})

# method2: iterations

for i in set2:
    print(i)


        # Adding the elements into set()
# method1: Add()
set2 = {1,2,3,4}

set2.add(5)
print(set2)

# set2.add(5,6)
# print(set2)

# Update()

set2.update([6,7,8,9])
print(set2)

set2.update((6,7,8,9,9))
print(set2)

batch1 = [1,2,3,4]
batch2 = (5,6,7)
batch3 = {8,9,10}

set4 = set()

set4.update(batch1,batch2,batch3)
print("the set4 is ",set4)

# Removing the elements
# method1: Remove()
print(set4)

set4.remove(10)
print(set4)

# method2: Discard()
set4.discard(9)
print(set4)

# method3: POP()

set4.pop()
print(set4)

set4.pop()
print(set4)

set4.pop()
print(set4)

# method4 : clear()

set4.clear()
print(set4)

# Set Operations :
# Method: UNION

set1 = {1,2,3}
set2 = {3,4,5}
union_of_set = set1.union(set2)
print("the union of set is ",union_of_set)

# using | operator
union_of_set = set1|set2
print("the union of set is ",union_of_set)

union_of_set = set2|set1
print("the union of set is ",union_of_set)

# method: Intersection

intersec_of_sets = set1.intersection(set2)
print("intersection of sets is ", intersec_of_sets)

intersec_of_sets = set2.intersection(set1)
print("intersection of sets is ", intersec_of_sets)

intersec_of_sets = set2 & set1
print("intersection of sets is ", intersec_of_sets)

# Method: Difference

print("set1 is",set1)
print("set1 is",set2)

difference_of_1_minus_2 = set1.difference(set2)
print("difference_of_1_minus_2", difference_of_1_minus_2)

difference_of_1_minus_2 = set1 - set2
print("difference_of_1_minus_2", difference_of_1_minus_2)

difference_of_1_minus_2 = set2.difference(set1)
print("difference_of_1_minus_2", difference_of_1_minus_2)

difference_of_2_minus_1 = set2 - set1
print("difference_of_2_minus_1", difference_of_2_minus_1)

# Symentic difference

symmentic_diff = set1.symmetric_difference(set2)
print("symmentic_diff is :", symmentic_diff)

symmentic_diff = set2.symmetric_difference(set1)
print("symmentic_diff is :", symmentic_diff)

set1.add(10)
set2.add(11)
set1.add(9)
set2.add(9)

symmentic_diff = set1.symmetric_difference(set2)
print("symmentic_diff is :", symmentic_diff)

symmentic_diff = set2.symmetric_difference(set1)
print("symmentic_diff is :", symmentic_diff)

symmentic_diff = set1^set2
print("symmentic_diff is :", symmentic_diff)

symmentic_diff = set2^set1
print("symmentic_diff is :", symmentic_diff)