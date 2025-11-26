"""
===============================================================================
PYTHON SETS - COMPLETE TRAINING MATERIAL
===============================================================================
Topic: Sets in Python
Level: Beginner to Intermediate
Context: General Python + ETL Testing Focus
===============================================================================
"""

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
- Elements must be immutable (strings, numbers, tuples - not lists or dicts)
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

print("=" * 80)
print("PYTHON SETS - COMPREHENSIVE TRAINING MATERIAL")
print("=" * 80)

# ==============================================================================
# SECTION 2: CREATING SETS - PROGRESSIVE EXAMPLE
# ==============================================================================

print("\n" + "=" * 80)
print("SECTION 2: CREATING SETS")
print("=" * 80)

# Let's start with a simple ETL scenario: Customer IDs from different sources

# Method 1: Using curly braces
print("\nMethod 1: Creating sets using curly braces {}")
source_customers = {101, 102, 103, 104, 105}
print(f"Source customers: {source_customers}")
print(f"Type: {type(source_customers)}")

# Method 2: Using set() constructor from list
print("\nMethod 2: Creating sets using set() constructor")
target_customers = set([101, 102, 103, 106, 107])
print(f"Target customers: {target_customers}")

# Method 3: Empty set (IMPORTANT: {} creates dict, not set!)
print("\nMethod 3: Creating empty set")
empty_set = set()  # Correct way
print(f"Empty set: {empty_set}")
print(f"Type: {type(empty_set)}")

empty_dict = {}  # This is a dictionary, not a set!
print(f"Empty dict: {empty_dict}")
print(f"Type: {type(empty_dict)}")

# Method 4: Set from string (splits into characters)
print("\nMethod 4: Set from string")
unique_chars = set("CUSTOMER")
print(f"Unique characters in 'CUSTOMER': {unique_chars}")

# Key Property: Sets automatically remove duplicates
print("\n" + "-" * 80)
print("KEY PROPERTY: Sets Remove Duplicates Automatically")
print("-" * 80)

# ETL Example: Raw data with duplicates from source system
raw_customer_ids = [101, 102, 103, 102, 101, 104, 105, 103, 106]
print(f"\nRaw customer IDs (with duplicates): {raw_customer_ids}")
print(f"Count: {len(raw_customer_ids)}")

unique_customer_ids = set(raw_customer_ids)
print(f"\nUnique customer IDs (after set conversion): {unique_customer_ids}")
print(f"Count: {len(unique_customer_ids)}")
print(f"Duplicates removed: {len(raw_customer_ids) - len(unique_customer_ids)}")

# ==============================================================================
# SECTION 3: ACCESSING SET ELEMENTS
# ==============================================================================

print("\n" + "=" * 80)
print("SECTION 3: ACCESSING SET ELEMENTS")
print("=" * 80)

# Continuing with our customer IDs example
customers = {101, 102, 103, 104, 105}

print(f"\nCustomer set: {customers}")

# Sets are UNORDERED - no indexing or slicing
print("\nIMPORTANT: Sets do NOT support indexing or slicing")
try:
    print(customers[0])  # This will raise an error
except TypeError as e:
    print(f"Error: {e}")

# How to access elements? Use iteration or membership testing
print("\nMethod 1: Check if element exists (membership testing)")
print(f"Is customer 103 in set? {103 in customers}")
print(f"Is customer 999 in set? {999 in customers}")

print("\nMethod 2: Iterate through all elements")
print("All customers:")
for customer_id in customers:
    print(f"  Customer ID: {customer_id}")

# ETL Use Case: Check if specific IDs exist in target
print("\n" + "-" * 80)
print("ETL USE CASE: Validate if expected IDs exist in target")
print("-" * 80)

target_ids = {101, 102, 103, 104, 105, 106, 107}
expected_ids = {101, 103, 105}

print(f"\nTarget IDs: {target_ids}")
print(f"Expected IDs to check: {expected_ids}")

all_present = all(exp_id in target_ids for exp_id in expected_ids)
print(f"\nAll expected IDs present in target? {all_present}")

# ==============================================================================
# SECTION 4: ADDING ELEMENTS TO SETS
# ==============================================================================

print("\n" + "=" * 80)
print("SECTION 4: ADDING ELEMENTS TO SETS")
print("=" * 80)

# Start with initial customer base
active_customers = {101, 102, 103}
print(f"\nInitial active customers: {active_customers}")

# Method 1: add() - adds single element
print("\nMethod 1: add() - Adding single customer")
active_customers.add(104)
print(f"After adding 104: {active_customers}")

# Adding duplicate has no effect
active_customers.add(102)  # Already exists
print(f"After trying to add 102 again: {active_customers} (no change)")

# Method 2: update() - adds multiple elements
print("\nMethod 2: update() - Adding multiple customers")
new_customers = [105, 106, 107]
active_customers.update(new_customers)
print(f"After adding {new_customers}: {active_customers}")

# update() can take multiple iterables
print("\nAdding from multiple sources:")
batch1 = [108, 109]
batch2 = {110, 111}
batch3 = (112, 113)
active_customers.update(batch1, batch2, batch3)
print(f"After adding multiple batches: {active_customers}")

# ETL Example: Building unique customer list from multiple sources
print("\n" + "-" * 80)
print("ETL USE CASE: Merge unique customers from multiple source systems")
print("-" * 80)

crm_customers = {101, 102, 103, 104}
erp_customers = {103, 104, 105, 106}
web_customers = {105, 106, 107, 108}

print(f"\nCRM customers: {crm_customers}")
print(f"ERP customers: {erp_customers}")
print(f"Web customers: {web_customers}")

# Merge all sources
all_unique_customers = set()
all_unique_customers.update(crm_customers, erp_customers, web_customers)
print(f"\nAll unique customers across systems: {all_unique_customers}")
print(f"Total unique customers: {len(all_unique_customers)}")

# ==============================================================================
# SECTION 5: REMOVING ELEMENTS FROM SETS
# ==============================================================================

print("\n" + "=" * 80)
print("SECTION 5: REMOVING ELEMENTS FROM SETS")
print("=" * 80)

# Start with a set of customer IDs to process
customers_to_process = {101, 102, 103, 104, 105, 106, 107, 108}
print(f"\nCustomers to process: {customers_to_process}")

# Method 1: remove() - removes element, raises error if not found
print("\nMethod 1: remove() - Removes element (raises error if not found)")
customers_to_process.remove(101)
print(f"After removing 101: {customers_to_process}")

try:
    customers_to_process.remove(999)  # Not in set
except KeyError as e:
    print(f"Error trying to remove non-existent customer: KeyError {e}")

# Method 2: discard() - removes element, no error if not found (SAFER)
print("\nMethod 2: discard() - Removes element (no error if not found)")
customers_to_process.discard(102)
print(f"After discarding 102: {customers_to_process}")

customers_to_process.discard(999)  # No error
print(f"After discarding 999 (doesn't exist): {customers_to_process} (no error)")

# Method 3: pop() - removes and returns arbitrary element
print("\nMethod 3: pop() - Removes and returns arbitrary element")
removed_customer = customers_to_process.pop()
print(f"Removed customer: {removed_customer}")
print(f"After pop: {customers_to_process}")

# Method 4: clear() - removes all elements
print("\nMethod 4: clear() - Removes all elements")
temp_set = {201, 202, 203}
print(f"Before clear: {temp_set}")
temp_set.clear()
print(f"After clear: {temp_set}")

# ETL Example: Removing processed records
print("\n" + "-" * 80)
print("ETL USE CASE: Track and remove processed customer IDs")
print("-" * 80)

pending_customers = {101, 102, 103, 104, 105, 106}
processed_customers = set()

print(f"\nPending customers: {pending_customers}")
print(f"Processed customers: {processed_customers}")

# Process customers one by one
print("\nProcessing customers...")
for i in range(3):
    if pending_customers:
        customer_id = pending_customers.pop()
        processed_customers.add(customer_id)
        print(f"  Processed customer {customer_id}")

print(f"\nPending customers: {pending_customers}")
print(f"Processed customers: {processed_customers}")

# ==============================================================================
# SECTION 6: SET OPERATIONS - THE POWER OF SETS!
# ==============================================================================

print("\n" + "=" * 80)
print("SECTION 6: SET OPERATIONS (Most Important for ETL Testing!)")
print("=" * 80)

# Let's use a realistic ETL scenario throughout this section
# Scenario: Comparing customer data between source and target databases

source_db_customers = {101, 102, 103, 104, 105, 106, 107}
target_db_customers = {103, 104, 105, 106, 107, 108, 109}

print(f"\nSource DB customers: {source_db_customers}")
print(f"Target DB customers: {target_db_customers}")

# OPERATION 1: UNION - All unique elements from both sets
print("\n" + "-" * 80)
print("OPERATION 1: UNION - Combine all unique elements")
print("-" * 80)

# Method A: Using union() method
all_customers_method = source_db_customers.union(target_db_customers)
print(f"\nUsing union() method: {all_customers_method}")

# Method B: Using | operator
all_customers_operator = source_db_customers | target_db_customers
print(f"Using | operator: {all_customers_operator}")

print(f"\nTotal unique customers across both databases: {len(all_customers_method)}")

# OPERATION 2: INTERSECTION - Common elements in both sets
print("\n" + "-" * 80)
print("OPERATION 2: INTERSECTION - Find common elements")
print("-" * 80)

# Method A: Using intersection() method
common_customers_method = source_db_customers.intersection(target_db_customers)
print(f"\nUsing intersection() method: {common_customers_method}")

# Method B: Using & operator
common_customers_operator = source_db_customers & target_db_customers
print(f"Using & operator: {common_customers_operator}")

print(f"\nCustomers present in BOTH databases: {len(common_customers_method)}")
print("ETL Insight: These customers were successfully migrated")

# OPERATION 3: DIFFERENCE - Elements in first set but not in second
print("\n" + "-" * 80)
print("OPERATION 3: DIFFERENCE - Find missing elements")
print("-" * 80)

# Method A: Using difference() method
missing_in_target_method = source_db_customers.difference(target_db_customers)
print(f"\nUsing difference() method: {missing_in_target_method}")

# Method B: Using - operator
missing_in_target_operator = source_db_customers - target_db_customers
print(f"Using - operator: {missing_in_target_operator}")

print(f"\nCustomers in SOURCE but NOT in TARGET: {missing_in_target_method}")
print("ETL Insight: These customers failed to migrate or are pending")

# Now check the other direction
extra_in_target = target_db_customers - source_db_customers
print(f"\nCustomers in TARGET but NOT in SOURCE: {extra_in_target}")
print("ETL Insight: These are new customers or data quality issues")

# OPERATION 4: SYMMETRIC DIFFERENCE - Elements in either set but not both
print("\n" + "-" * 80)
print("OPERATION 4: SYMMETRIC DIFFERENCE - Find non-matching elements")
print("-" * 80)

# Method A: Using symmetric_difference() method
mismatch_method = source_db_customers.symmetric_difference(target_db_customers)
print(f"\nUsing symmetric_difference() method: {mismatch_method}")

# Method B: Using ^ operator
mismatch_operator = source_db_customers ^ target_db_customers
print(f"Using ^ operator: {mismatch_operator}")

print(f"\nCustomers that DON'T match between databases: {mismatch_method}")
print("ETL Insight: Data reconciliation issues to investigate")

# ==============================================================================
# SECTION 7: COMPREHENSIVE ETL RECONCILIATION EXAMPLE
# ==============================================================================

print("\n" + "=" * 80)
print("SECTION 7: COMPLETE ETL RECONCILIATION EXAMPLE")
print("=" * 80)

# Realistic scenario: Daily ETL job validation
print("\nScenario: Daily Customer Data ETL Reconciliation")
print("-" * 80)

source_customers = {1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010}
target_customers = {1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011}

print(f"\nSource database: {len(source_customers)} customers")
print(f"Target database: {len(target_customers)} customers")
print(f"\nSource: {source_customers}")
print(f"Target: {target_customers}")

# Reconciliation Report
print("\n" + "=" * 40)
print("RECONCILIATION REPORT")
print("=" * 40)

# 1. Successfully migrated records
successfully_migrated = source_customers & target_customers
print(f"\n✓ Successfully migrated: {len(successfully_migrated)} customers")
print(f"  IDs: {successfully_migrated}")

# 2. Missing in target (failed migrations)
missing_in_target = source_customers - target_customers
print(f"\n❌ Missing in target: {len(missing_in_target)} customers")
print(f"  IDs: {missing_in_target}")
if missing_in_target:
    print("  ACTION REQUIRED: Investigate failed migrations")

# 3. Extra in target (orphan records)
extra_in_target = target_customers - source_customers
print(f"\n⚠ Extra in target: {len(extra_in_target)} customers")
print(f"  IDs: {extra_in_target}")
if extra_in_target:
    print("  ACTION REQUIRED: Investigate orphan records")

# 4. Overall data quality metrics
all_records = source_customers | target_customers
mismatch_records = source_customers ^ target_customers

data_accuracy = (len(successfully_migrated) / len(source_customers)) * 100
print(f"\n📊 Data Migration Accuracy: {data_accuracy:.2f}%")
print(f"📊 Total unique customers: {len(all_records)}")
print(f"📊 Mismatch count: {len(mismatch_records)}")

if len(missing_in_target) == 0 and len(extra_in_target) == 0:
    print("\n✅ ETL JOB STATUS: SUCCESS - Perfect reconciliation!")
else:
    print("\n⚠️ ETL JOB STATUS: ISSUES FOUND - Review required")

# ==============================================================================
# SECTION 8: SET COMPARISON METHODS
# ==============================================================================

print("\n" + "=" * 80)
print("SECTION 8: SET COMPARISON METHODS")
print("=" * 80)

# Using our customer sets for comparison examples
set_a = {101, 102, 103, 104, 105}
set_b = {103, 104, 105}
set_c = {101, 102, 103, 104, 105}
set_d = {201, 202, 203}

print(f"\nSet A: {set_a}")
print(f"Set B: {set_b}")
print(f"Set C: {set_c}")
print(f"Set D: {set_d}")

# 1. issubset() - Check if all elements of set are in another set
print("\n1. issubset() - Is one set contained in another?")
print(f"   Is B subset of A? {set_b.issubset(set_a)}")  # True
print(f"   Is A subset of B? {set_a.issubset(set_b)}")  # False
print(f"   Using <= operator: {set_b <= set_a}")  # True

# 2. issuperset() - Check if set contains all elements of another set
print("\n2. issuperset() - Does one set contain another?")
print(f"   Is A superset of B? {set_a.issuperset(set_b)}")  # True
print(f"   Is B superset of A? {set_b.issuperset(set_a)}")  # False
print(f"   Using >= operator: {set_a >= set_b}")  # True

# 3. isdisjoint() - Check if sets have no common elements
print("\n3. isdisjoint() - Do sets have no common elements?")
print(f"   Are A and B disjoint? {set_a.isdisjoint(set_b)}")  # False (they overlap)
print(f"   Are A and D disjoint? {set_a.isdisjoint(set_d)}")  # True (no overlap)

# 4. Equality check
print("\n4. Equality - Are sets identical?")
print(f"   Is A equal to C? {set_a == set_c}")  # True
print(f"   Is A equal to B? {set_a == set_b}")  # False

# ETL Use Case: Validating data subsets
print("\n" + "-" * 80)
print("ETL USE CASE: Validate VIP customers are subset of all customers")
print("-" * 80)

all_customers = {101, 102, 103, 104, 105, 106, 107, 108, 109, 110}
vip_customers = {102, 105, 108, 110}
new_vip_candidates = {105, 111, 112}  # 111, 112 don't exist in all_customers

print(f"\nAll customers: {all_customers}")
print(f"VIP customers: {vip_customers}")
print(f"New VIP candidates: {new_vip_candidates}")

# Validate VIP customers are valid
if vip_customers.issubset(all_customers):
    print("\n✓ All VIP customers are valid (exist in customer database)")
else:
    print("\n❌ Some VIP customers don't exist in customer database")

# Validate new VIP candidates
if new_vip_candidates.issubset(all_customers):
    print("✓ All VIP candidates are valid")
else:
    invalid_vips = new_vip_candidates - all_customers
    print(f"❌ Invalid VIP candidates (don't exist): {invalid_vips}")

# Check for data quality: ensure no overlap issues
if all_customers.isdisjoint(set_d):
    print("✓ No overlap with external dataset D")

# ==============================================================================
# SECTION 9: MODIFYING SETS IN-PLACE
# ==============================================================================

print("\n" + "=" * 80)
print("SECTION 9: MODIFYING SETS IN-PLACE")
print("=" * 80)

# Note: Previous operations created NEW sets. These methods modify EXISTING sets.

main_customers = {101, 102, 103, 104, 105}
new_customers = {105, 106, 107}

print(f"\nMain customers: {main_customers}")
print(f"New customers: {new_customers}")

# 1. update() - Add elements (union in-place)
print("\n1. update() - Union in-place")
main_customers_copy = main_customers.copy()
main_customers_copy.update(new_customers)
print(f"   After update: {main_customers_copy}")

# Using |= operator
main_customers_copy2 = main_customers.copy()
main_customers_copy2 |= new_customers
print(f"   Using |= operator: {main_customers_copy2}")

# 2. intersection_update() - Keep only common elements
print("\n2. intersection_update() - Intersection in-place")
set_x = {101, 102, 103, 104, 105}
set_y = {103, 104, 105, 106, 107}
print(f"   Before: {set_x}")
set_x.intersection_update(set_y)
print(f"   After intersection_update: {set_x}")

# Using &= operator
set_x2 = {101, 102, 103, 104, 105}
set_x2 &= set_y
print(f"   Using &= operator: {set_x2}")

# 3. difference_update() - Remove elements that exist in other set
print("\n3. difference_update() - Difference in-place")
set_p = {101, 102, 103, 104, 105}
set_q = {103, 104, 105}
print(f"   Before: {set_p}")
set_p.difference_update(set_q)
print(f"   After difference_update: {set_p}")

# Using -= operator
set_p2 = {101, 102, 103, 104, 105}
set_p2 -= set_q
print(f"   Using -= operator: {set_p2}")

# 4. symmetric_difference_update() - Keep only non-common elements
print("\n4. symmetric_difference_update() - Symmetric difference in-place")
set_m = {101, 102, 103, 104, 105}
set_n = {103, 104, 105, 106, 107}
print(f"   Before: {set_m}")
set_m.symmetric_difference_update(set_n)
print(f"   After symmetric_difference_update: {set_m}")

# Using ^= operator
set_m2 = {101, 102, 103, 104, 105}
set_m2 ^= set_n
print(f"   Using ^= operator: {set_m2}")

# ETL Example: Maintaining processed records list
print("\n" + "-" * 80)
print("ETL USE CASE: Maintain and update processed customer list")
print("-" * 80)

processed_today = {101, 102, 103}
processed_yesterday = {103, 104, 105}
failed_processing = {102}

print(f"\nProcessed today: {processed_today}")
print(f"Processed yesterday: {processed_yesterday}")
print(f"Failed processing: {failed_processing}")

# Add all newly processed
all_processed = processed_yesterday.copy()
all_processed.update(processed_today)
print(f"\nAll processed records: {all_processed}")

# Remove failed ones
all_processed.difference_update(failed_processing)
print(f"After removing failures: {all_processed}")

# ==============================================================================
# SECTION 10: FROZEN SETS - IMMUTABLE SETS
# ==============================================================================

print("\n" + "=" * 80)
print("SECTION 10: FROZEN SETS (Immutable Sets)")
print("=" * 80)

print("\nFrozenset: Immutable version of set")
print("Use cases: Dictionary keys, set elements, constant reference data")

# Create frozenset
regular_set = {101, 102, 103}
frozen_customers = frozenset([101, 102, 103, 104, 105])

print(f"\nRegular set: {regular_set}")
print(f"Frozen set: {frozen_customers}")

# Frozensets cannot be modified
print("\nTrying to modify frozenset:")
try:
    frozen_customers.add(106)
except AttributeError as e:
    print(f"  Error: {e}")

# But all query operations work
print(f"\nIs 103 in frozen set? {103 in frozen_customers}")
print(f"Union with regular set: {frozen_customers | regular_set}")

# Use case: Frozenset as dictionary key
print("\n" + "-" * 80)
print("ETL USE CASE: Using frozenset as dictionary key for lookup tables")
print("-" * 80)

# Store validation rules for different customer segments
customer_segments = {
    frozenset([101, 102, 103]): "Premium",
    frozenset([104, 105]): "Standard",
    frozenset([106, 107, 108]): "Basic"
}

print("\nCustomer segment mapping:")
for segment_ids, segment_name in customer_segments.items():
    print(f"  {segment_name}: {segment_ids}")

# Lookup segment for a specific group
lookup_group = frozenset([101, 102, 103])
segment = customer_segments.get(lookup_group)
print(f"\nSegment for {lookup_group}: {segment}")

# ==============================================================================
# SECTION 11: SET METHODS SUMMARY
# ==============================================================================

print("\n" + "=" * 80)
print("SECTION 11: ALL SET METHODS - QUICK REFERENCE")
print("=" * 80)

reference_set = {101, 102, 103, 104, 105}
print(f"\nReference set: {reference_set}")

print("\nADDING ELEMENTS:")
print("  .add(element)              - Add single element")
print("  .update(iterable)          - Add multiple elements")

print("\nREMOVING ELEMENTS:")
print("  .remove(element)           - Remove element (raises error if not found)")
print("  .discard(element)          - Remove element (no error if not found)")
print("  .pop()                     - Remove and return arbitrary element")
print("  .clear()                   - Remove all elements")

print("\nSET OPERATIONS (Create new set):")
print("  .union(other)              - A | B   - All elements from both")
print("  .intersection(other)       - A & B   - Common elements")
print("  .difference(other)         - A - B   - Elements in A but not B")
print("  .symmetric_difference(other) - A ^ B - Elements in either but not both")

print("\nSET OPERATIONS (Modify in-place):")
print("  .update(other)             - A |= B  - Add elements from B to A")
print("  .intersection_update(other) - A &= B - Keep only common elements")
print("  .difference_update(other)  - A -= B  - Remove B's elements from A")
print("  .symmetric_difference_update(other) - A ^= B")

print("\nCOMPARISON METHODS:")
print("  .issubset(other)           - A <= B  - Is A contained in B?")
print("  .issuperset(other)         - A >= B  - Does A contain B?")
print("  .isdisjoint(other)         - No common elements?")

print("\nOTHER METHODS:")
print("  .copy()                    - Create shallow copy")
print("  len(set)                   - Number of elements")
print("  element in set             - Membership test")

# ==============================================================================
# SECTION 12: PRACTICAL ETL TESTING FUNCTIONS
# ==============================================================================

print("\n" + "=" * 80)
print("SECTION 12: PRACTICAL ETL TESTING FUNCTIONS")
print("=" * 80)

# Function 1: Comprehensive reconciliation function
def reconcile_datasets(source_ids, target_ids, dataset_name="Dataset"):
    """
    Comprehensive reconciliation between source and target datasets

    Args:
        source_ids: Set of IDs from source system
        target_ids: Set of IDs from target system
        dataset_name: Name of dataset for reporting

    Returns:
        Dictionary with reconciliation metrics
    """
    results = {
        "dataset_name": dataset_name,
        "source_count": len(source_ids),
        "target_count": len(target_ids),
        "matched": source_ids & target_ids,
        "missing_in_target": source_ids - target_ids,
        "extra_in_target": target_ids - source_ids,
        "all_unique": source_ids | target_ids,
        "accuracy_percent": 0.0,
        "status": "FAIL"
    }

    # Calculate accuracy
    if len(source_ids) > 0:
        results["accuracy_percent"] = (len(results["matched"]) / len(source_ids)) * 100

    # Determine status
    if len(results["missing_in_target"]) == 0 and len(results["extra_in_target"]) == 0:
        results["status"] = "PASS"

    return results

# Function 2: Find duplicate records
def find_duplicates(record_list, key_field):
    """
    Find duplicate records based on key field

    Args:
        record_list: List of dictionaries (records)
        key_field: Field name to check for duplicates

    Returns:
        Set of duplicate values
    """
    seen = set()
    duplicates = set()

    for record in record_list:
        value = record.get(key_field)
        if value in seen:
            duplicates.add(value)
        else:
            seen.add(value)

    return duplicates

# Function 3: Validate referential integrity
def validate_referential_integrity(child_ids, parent_ids, relationship_name):
    """
    Validate that all child IDs have corresponding parent IDs

    Args:
        child_ids: Set of foreign key values
        parent_ids: Set of primary key values
        relationship_name: Name of the relationship for reporting

    Returns:
        Dictionary with validation results
    """
    orphan_records = child_ids - parent_ids
    valid_records = child_ids & parent_ids

    is_valid = len(orphan_records) == 0

    return {
        "relationship": relationship_name,
        "is_valid": is_valid,
        "total_child_records": len(child_ids),
        "valid_references": len(valid_records),
        "orphan_records": orphan_records,
        "orphan_count": len(orphan_records)
    }

# Test the functions
print("\nFUNCTION 1: Reconciliation Function Test")
print("-" * 80)

source = {1001, 1002, 1003, 1004, 1005}
target = {1002, 1003, 1004, 1005, 1006}

recon_result = reconcile_datasets(source, target, "Customer Data")

print(f"\nDataset: {recon_result['dataset_name']}")
print(f"Source count: {recon_result['source_count']}")
print(f"Target count: {recon_result['target_count']}")
print(f"Matched: {len(recon_result['matched'])} records")
print(f"Missing in target: {recon_result['missing_in_target']}")
print(f"Extra in target: {recon_result['extra_in_target']}")
print(f"Accuracy: {recon_result['accuracy_percent']:.2f}%")
print(f"Status: {recon_result['status']}")

print("\nFUNCTION 2: Duplicate Detection Test")
print("-" * 80)

customer_records = [
    {"customer_id": 101, "name": "John"},
    {"customer_id": 102, "name": "Jane"},
    {"customer_id": 101, "name": "John Duplicate"},
    {"customer_id": 103, "name": "Bob"},
    {"customer_id": 102, "name": "Jane Duplicate"}
]

duplicates = find_duplicates(customer_records, "customer_id")
print(f"\nTotal records: {len(customer_records)}")
print(f"Duplicate customer IDs: {duplicates}")
print(f"Duplicate count: {len(duplicates)}")

print("\nFUNCTION 3: Referential Integrity Validation Test")
print("-" * 80)

order_customer_ids = {101, 102, 103, 104, 999}  # 999 is orphan
existing_customer_ids = {101, 102, 103, 104, 105}

ref_result = validate_referential_integrity(
    order_customer_ids,
    existing_customer_ids,
    "Orders -> Customers"
)

print(f"\nRelationship: {ref_result['relationship']}")
print(f"Is valid: {ref_result['is_valid']}")
print(f"Total child records: {ref_result['total_child_records']}")
print(f"Valid references: {ref_result['valid_references']}")
print(f"Orphan records: {ref_result['orphan_records']}")
print(f"Orphan count: {ref_result['orphan_count']}")

if not ref_result['is_valid']:
    print(f"\n⚠️ WARNING: Found {ref_result['orphan_count']} orphan records!")
    print(f"   Order(s) exist for non-existent customer(s): {ref_result['orphan_records']}")

# ==============================================================================
# SECTION 13: PERFORMANCE AND BEST PRACTICES
# ==============================================================================

print("\n" + "=" * 80)
print("SECTION 13: PERFORMANCE AND BEST PRACTICES")
print("=" * 80)

print("""
PERFORMANCE CHARACTERISTICS:
---------------------------
1. Membership testing: O(1) - Very fast!
   - "element in set" is much faster than "element in list"
   
2. Add/Remove: O(1) - Very fast!
   - Adding and removing elements is constant time
   
3. Set operations: O(len(set))
   - Union, intersection, difference are fast
   
4. Memory usage: Sets use more memory than lists
   - Trade memory for speed

WHEN TO USE SETS:
----------------
✓ Need to store unique values only
✓ Need fast membership testing (checking if element exists)
✓ Need to find common/different elements between datasets
✓ Need to remove duplicates
✓ Need mathematical set operations
✓ Order doesn't matter

WHEN NOT TO USE SETS:
--------------------
✗ Need to maintain order (use list or OrderedDict)
✗ Need to access elements by index
✗ Need to store duplicate values
✗ Elements are mutable (lists, dicts)
✗ Need to count occurrences (use Counter instead)

ETL TESTING BEST PRACTICES:
---------------------------
1. Use sets for ID-based reconciliation
2. Find missing/extra records with set operations
3. Validate referential integrity with sets
4. Remove duplicates efficiently
5. Check for unique constraints violations
6. Perform data quality checks
7. Compare data between environments
8. Track processed records
9. Maintain exclusion/inclusion lists
10. Cache lookup values for performance

COMMON MISTAKES TO AVOID:
------------------------
1. Using {} instead of set() for empty set
2. Trying to add mutable objects (lists, dicts) to sets
3. Expecting sets to maintain order (though Python 3.7+ preserves insertion order)
4. Using sets when duplicates are meaningful
5. Modifying set while iterating over it
6. Forgetting that set operations create new sets (unless using in-place versions)
7. Using sets for small datasets where overhead isn't worth it
8. Not considering memory usage for very large sets

CODE STYLE TIPS:
---------------
✓ Use descriptive variable names: "active_customers" not "s1"
✓ Use set operations instead of loops when possible
✓ Prefer in-place operations for large sets to save memory
✓ Use frozensets for constants and dictionary keys
✓ Document the purpose of sets in complex logic
✓ Use type hints: def process(ids: set) -> set:
✓ Validate input before set operations
✓ Handle empty sets gracefully
""")

# ==============================================================================
# SECTION 14: REAL-WORLD ETL TESTING SCENARIOS
# ==============================================================================

print("=" * 80)
print("SECTION 14: REAL-WORLD ETL TESTING SCENARIOS")
print("=" * 80)

# SCENARIO 1: Daily incremental load validation
print("\nSCENARIO 1: Daily Incremental Load Validation")
print("-" * 80)

yesterday_customers = {101, 102, 103, 104, 105, 106, 107, 108, 109, 110}
today_customers = {101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112}

new_customers_today = today_customers - yesterday_customers
churned_customers = yesterday_customers - today_customers

print(f"Yesterday's customers: {len(yesterday_customers)}")
print(f"Today's customers: {len(today_customers)}")
print(f"New customers added: {new_customers_today}")
print(f"Customers removed: {churned_customers}")
print(f"Net change: +{len(new_customers_today) - len(churned_customers)}")

# SCENARIO 2: Multi-source data deduplication
print("\nSCENARIO 2: Multi-Source Data Deduplication")
print("-" * 80)

source_a = {101, 102, 103, 104, 105}
source_b = {104, 105, 106, 107, 108}
source_c = {103, 105, 107, 109, 110}

print(f"Source A: {source_a}")
print(f"Source B: {source_b}")
print(f"Source C: {source_c}")

all_sources_combined = source_a | source_b | source_c
common_across_all = source_a & source_b & source_c
duplicates_found = (len(source_a) + len(source_b) + len(source_c)) - len(all_sources_combined)

print(f"\nTotal unique IDs: {len(all_sources_combined)}")
print(f"IDs in all three sources: {common_across_all}")
print(f"Duplicate IDs removed: {duplicates_found}")

# SCENARIO 3: Data quality - Check for invalid references
print("\nSCENARIO 3: Data Quality - Invalid Reference Detection")
print("-" * 80)

valid_country_codes = {"US", "UK", "CA", "IN", "AU", "DE", "FR"}
customer_countries = {"US", "UK", "XX", "CA", "YY", "IN", "ZZ"}

invalid_codes = customer_countries - valid_country_codes
valid_codes = customer_countries & valid_country_codes

print(f"Valid country codes: {valid_country_codes}")
print(f"Customer countries: {customer_countries}")
print(f"Invalid codes found: {invalid_codes}")
print(f"Valid codes: {valid_codes}")

if invalid_codes:
    print(f"\n⚠️ Data Quality Issue: {len(invalid_codes)} invalid country code(s)")
    print(f"   Action: Clean or reject records with codes: {invalid_codes}")

# SCENARIO 4: Environment comparison (DEV vs PROD)
print("\nSCENARIO 4: Environment Comparison (DEV vs PROD)")
print("-" * 80)

dev_tables = {"customers", "orders", "products", "inventory", "test_data"}
prod_tables = {"customers", "orders", "products", "inventory", "shipments"}

tables_in_both = dev_tables & prod_tables
dev_only = dev_tables - prod_tables
prod_only = prod_tables - dev_tables

print(f"DEV tables: {dev_tables}")
print(f"PROD tables: {prod_tables}")
print(f"\nTables in both: {tables_in_both}")
print(f"DEV only: {dev_only}")
print(f"PROD only: {prod_only}")

if dev_only:
    print(f"\n⚠️ Tables in DEV not in PROD: {dev_only}")
if prod_only:
    print(f"⚠️ Tables in PROD not in DEV: {prod_only}")

# ==============================================================================
# SECTION 15: PRACTICE EXERCISES
# ==============================================================================

print("\n" + "=" * 80)
print("SECTION 15: PRACTICE EXERCISES")
print("=" * 80)

print("""
BEGINNER EXERCISES (Using our customer ID examples):
---------------------------------------------------
1. Create a set of customer IDs: {101, 102, 103, 104, 105}
2. Add customer ID 106 to the set
3. Try to add customer ID 103 again (observe duplicate handling)
4. Check if customer 104 exists in the set
5. Remove customer 102 from the set

INTERMEDIATE EXERCISES (Building on examples):
---------------------------------------------
1. Create two sets: source_ids = {101, 102, 103, 104} and 
   target_ids = {103, 104, 105, 106}
2. Find customers in source but not in target
3. Find customers in target but not in source
4. Find common customers
5. Find all unique customers across both sets

ADVANCED EXERCISES (ETL Testing Focus):
--------------------------------------
1. Write a function to detect duplicate customer IDs in a list
2. Create a function that validates all order customer IDs exist in customer table
3. Build a reconciliation report comparing source vs target counts
4. Implement a function to find orphan records across related tables
5. Create a data quality checker that validates:
   - All IDs are unique
   - All foreign keys have valid references
   - No invalid status codes exist
   
CHALLENGE EXERCISES:
-------------------
1. Build a complete ETL validation framework using sets for:
   - Record count reconciliation
   - Duplicate detection
   - Referential integrity checks
   - Data quality validation
   
2. Create a performance comparison: set vs list for membership testing
   with 10,000 elements

3. Implement a function that tracks daily changes (new, modified, deleted records)
   using sets to compare yesterday's and today's data

4. Build a multi-environment comparison tool that identifies differences
   between DEV, TEST, and PROD databases

5. Create a data profiling tool that uses sets to find:
   - Unique values in each column
   - Common values across related tables
   - Data inconsistencies

PRACTICAL PROJECT:
-----------------
Build a mini ETL testing framework with these functions:
- reconcile_counts(source, target)
- find_missing_records(source, target)
- find_extra_records(source, target)
- validate_references(child_table, parent_table)
- detect_duplicates(data_list, key_field)
- generate_reconciliation_report(source, target)
""")

# ==============================================================================
# SECTION 16: SUMMARY AND CHEAT SHEET
# ==============================================================================

print("\n" + "=" * 80)
print("SECTION 16: SETS CHEAT SHEET")
print("=" * 80)

print("""
CREATING SETS:
-------------
my_set = {1, 2, 3}                    # Using braces
my_set = set([1, 2, 3])               # From list
empty_set = set()                     # Empty set (NOT {})
frozen_set = frozenset([1, 2, 3])     # Immutable set

ADDING/REMOVING:
---------------
my_set.add(4)                         # Add single element
my_set.update([5, 6])                 # Add multiple elements
my_set.remove(4)                      # Remove (raises error if not found)
my_set.discard(4)                     # Remove (no error if not found)
my_set.pop()                          # Remove arbitrary element
my_set.clear()                        # Remove all elements

SET OPERATIONS:
--------------
a | b  or  a.union(b)                 # Union (all elements)
a & b  or  a.intersection(b)          # Intersection (common elements)
a - b  or  a.difference(b)            # Difference (in a, not in b)
a ^ b  or  a.symmetric_difference(b)  # Symmetric difference (in either, not both)

IN-PLACE OPERATIONS:
-------------------
a |= b  or  a.update(b)               # Add elements from b
a &= b  or  a.intersection_update(b)  # Keep only common
a -= b  or  a.difference_update(b)    # Remove b's elements
a ^= b  or  a.symmetric_difference_update(b)  # Keep only non-common

COMPARISONS:
-----------
a <= b  or  a.issubset(b)             # Is a subset of b?
a >= b  or  a.issuperset(b)           # Is a superset of b?
a.isdisjoint(b)                       # No common elements?
a == b                                # Are sets equal?

COMMON OPERATIONS:
-----------------
len(my_set)                           # Number of elements
element in my_set                     # Membership test
element not in my_set                 # Negative membership test
for item in my_set:                   # Iterate through set

ETL TESTING QUICK REFERENCE:
---------------------------
# Find missing records
missing = source_ids - target_ids

# Find extra records
extra = target_ids - source_ids

# Find common records
common = source_ids & target_ids

# Get all unique records
all_records = source_ids | target_ids

# Check referential integrity
orphans = child_ids - parent_ids

# Remove duplicates
unique_ids = set(id_list)

# Check if subset (validation)
is_valid = test_ids.issubset(valid_ids)

KEY TAKEAWAYS:
-------------
✓ Sets store unique, unordered elements
✓ O(1) membership testing (very fast!)
✓ Perfect for ETL reconciliation
✓ Use set operations instead of loops
✓ Great for finding duplicates, missing data
✓ Essential for data quality validation
✓ Remember: {} is dict, set() is empty set
✓ Elements must be immutable (no lists/dicts)

NEXT STEPS:
----------
1. Practice all exercises above
2. Apply sets to your ETL testing scripts
3. Build reusable reconciliation functions
4. Compare performance: sets vs lists
5. Explore real-world ETL frameworks
6. Create your own testing utilities
7. Master set comprehensions
8. Learn about collections.Counter for counting
""")

print("\n" + "=" * 80)
print("END OF SETS TRAINING MATERIAL")
print("=" * 80)
print("\n🎓 Congratulations on completing the Sets training!")
print("📚 Practice with the exercises to master sets")
print("🚀 Apply these concepts to your ETL testing projects")
print("\nFor more information:")
print("https://docs.python.org/3/tutorial/datastructures.html#sets")
