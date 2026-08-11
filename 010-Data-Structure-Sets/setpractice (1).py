# Task 1: 

departments = {
    "IT",
    "Finance",
    "Sales",
    "HR"
}

print(departments)

# Task 2: Automatic Duplicate Removal

employees = {
    "Mayowa",
    "Ada",
    "John",
    "Ada",
    "Mayowa",
    "Peter"
}

# print the set

print(employees)

# Task 3: Adding Items to a set
departments = {
    "IT",
    "Finance",
    "Sales"
}

# Add "HR" to the set

departments.add('HR')

print(departments)

# Task 4: Adding a Duplicate

departments = {
    "IT",
    "Finance",
    "Sales"
}

# Add "IT" to the set again
# print the set

departments.add("IT")

print(departments)

# Task 5: Removing Items

departments = {
    "IT",
    "Finance",
    "Sales",
    "HR"
}

# Remove "sales" from the set
# print the updated set

departments.remove("Sales")

print(departments)

# Task 6: Membership Testing

departments = {
    "IT",
    "Finance",
    "HR",
    "Sales"
}

# print the result of these expressions

# "Finance" in departments
# "Marketing" in departments
# "HR" not in departments

print("Finance" in departments)
print("Marketing" in departments)
print("HR" not in departments)

# Task 7: Union (|)

branch_a = {
    "Mayowa",
    "Ada",
    "John"
}

branch_b = {
    "John",
    "Peter",
    "Mary"
}

# Create a new set called "all_employees" that contains everyone from both branches

all_employees = branch_a | branch_b

print(all_employees)

# Task 8: Intersection (&)

branch_a = {
    "Mayowa",
    "Ada",
    "John"
}

branch_b = {
    "John",
    "Peter",
    "Mary"
}

# Create a new set called "common_employees" that contains only the employees who are in both branches

common_employees = branch_a & branch_b

print(common_employees)

# Task 9: Difference (-)

branch_a = {
    "Mayowa",
    "Ada",
    "John"
}

branch_b = {
    "John",
    "Peter",
    "Mary"
}

# Create a new set called "ony_branch_a" that contains employees who are in Branch A but not in Branch Branch

only_branch_a = branch_a - branch_b

print(only_branch_a)

# Task 10: Symmetric Difference(^)

branch_a = {
    "Mayowa",
    "Ada",
    "John"
}

branch_b = {
    "John",
    "Peter",
    "Mary"
}

# create a new set called "unique_employees" that contains employees who are in only one branch(not both)

unique_employees = branch_a ^ branch_b

print(unique_employees)
