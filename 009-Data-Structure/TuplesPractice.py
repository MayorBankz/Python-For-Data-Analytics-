# Task 1: Creating a tuple

offices = (
    "Lagos",
    "Abuja",
    "Port Harcourt",
    "Ibadan"
)

# print the entire tuple

print(offices)

# Task 2: Indexing

offices = (
    "Lagos",
    "Abuja",
    "Port Harcourt",
    "Ibadan"
)

# print
# Lagos
# Ibadan

print(offices[0])
print(offices[-1])

# Task 3: Tuple Slicing

offices = (
    "Lagos",
    "Abuja",
    "Port Harcourt",
    "Ibadan"
)

# print exactly
# ('Abuja', 'Port Harcourt')

print(offices[1:3])

# Task 4: Membership Testing

offices = (
    "Lagos",
    "Abuja",
    "Port Harcourt",
    "Ibadan"
)

# print the result of these expressions
# "Lagos" in offices
# "Kano" in offices

print("Lagos" in offices)
print("Kano" in offices)

# Task 5: Tuple Unpacking
employee = (
    "EMP001",
    "Mayowa",
    "IT",
    350000
)

# unpack the tuple into 
# emp_id
# name
# department
# salary
# Then print
# Mayowa
# IT
# 350000

emp_id, name, department, salary = employee

print(name)
print(department)
print(salary)

# Task 6: Rest collector with tuple

months = (
    "January",
    "February",
    "March",
    "April",
    "May"
)

# unpack into:
# first
# *middle
# last 
# Then print 
# January
# ['February', 'March', 'April']
# May

first, *middle, last = months

print(first)
print(middle)
print(last)

# Task 7: Exploring Tuples
sales = (
    120000,
    85000,
    230000,
    150000,
    98000
)

# print
# Total number of sales
# Highest sale
# Lowest sale
# Total of all sales
# average sale

print(f"Total Sales Record: {len(sales)}")
print(f"Highest Sale: {max(sales)}")
print(f"Lowest Sale: {min(sales)}")
print(f"Total: {sum(sales)}")
print(f"Average Sale: {sum(sales) / len(sales)}")

# Task 8: count() and index()
departments = (
    "IT",
    "Finance",
    "Sales",
    "IT",
    "HR"
)

# print:
# How many times "IT" appears.
# The index of sales 

print(f"IT appears: {departments.count('IT')}")
print(f"Sales index: {departments.index('Sales')}")

# Task 9: Understanding Immutability

departments = (
    "IT",
    "Finance",
    "Sales"
)

# Try to change Finance to Marketing
departments[1] = "Marketing"

print(departments)