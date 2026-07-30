# Task 1: Creating a dictionary

employee = {
    "id": "EMP001",
    "name": "Mayowa",
    "department": "IT",
    "salary": 350000
}

# print the entire dictionary

print(employee)

# Task 2: Accessing Values

employee = {
    "id": "EMP001",
    "name": "Mayowa",
    "department": "IT",
    "salary": 350000
}

# print exactly
# Mayowa
# IT
# 350000

print(employee["name"])
print(employee["department"])
print(employee["salary"])

# Task 3: Updating Values

employee = {
    "id": "EMP001",
    "name": "Mayowa",
    "department": "IT",
    "salary": 350000
}

# update the "department" from "IT" to "Data Analytics"
# print the entire dictionary

employee["department"] = "Data Analytics"

print(employee)



# Task 4: Adding a New Key-value pair

employee = {
    "id": "EMP001",
    "name": "Mayowa",
    "department": "Data Analytics",
    "salary": 350000
}

# add a new key called "email"
# Give it the value: mayowa@company.com
# print the updated dictionary

employee["email"] = "mayowa@company.com"

print(employee)

# Task 5: Removing a Key-value pair

employee = {
    "id": "EMP001",
    "name": "Mayowa",
    "department": "Data Analytics",
    "salary": 350000,
    "email": "mayowa@company.com"
}

# Remove the email Key
# print the updated dictionary

employee.pop("email")

print(employee)

# Task 6: Checking if a key exists

employee = {
    "id": "EMP001",
    "name": "Mayowa",
    "department": "Data Analytics",
    "salary": 350000
}

# print the result of these expressions
# "name" in employee
# "email" in employee
# "salary" in employee

print("name" in employee)
print("email" in employee)
print("salary" in employee)

# Task 7: Looping through a dictionary

employee = {
    "id": "EMP001",
    "name": "Mayowa",
    "department": "Data Analytics",
    "salary": 350000
}

# Loop through the dictionary and print each key and it value in this format:
# id: EMP001
# name: Mayowa
# department: Data Analytics
# salary: 350000

for key, value in employee.items():
    print(f"{key}: {value}")
    
# Task 8: Loop through keys only

employee = {
    "id": "EMP001",
    "name": "Mayowa",
    "department": "Data Analytics",
    "salary": 350000
}

# Loop through the dictionary and print only the keys

for key in employee:
    print(key)
    
# Task 9: Loop through values only

employee = {
    "id": "EMP001",
    "name": "Mayowa",
    "department": "Data Analytics",
    "salary": 350000
}

# Loop through the dictionary and print only the values

for value in employee.values():
    print(value)
    
# Task 10: Real-World Dictionary Practice

employee = {
    "id": "EMP001",
    "name": "Mayowa",
    "department": "Data Analytics",
    "salary": 350000
}

# Add a new key: email - "mayowa@company.com"
# update: salary - 400000
# Remove: "department"
# Loop through the dictionary using .items()
# print each key-value pair in this format:
# id: EMP001
# name: Mayowa
# salary: 400000
# email: mayowa@company.com

employee["email"] = "mayowa@company.com"
employee["salary"] = 400000
employee.pop("department")


for key, value in employee.items():
    print(f"{key}: {value}")
    
# Task 11: Nested dictionary

employee = {
    "id": "EMP001",
    "name": "Mayowa",
    "job": {
        "department": "Data Analytics",
        "salary": 400000
    }
}

# print exactly 

# Mayowa
# Data Analytics
# 400000

print(employee["name"])
print(employee["job"]["department"])
print(employee["job"]["salary"])

# Task 12: Update a Nested dictionary
# An employee has been promoted

employee = {
    "id": "EMP001",
    "name": "Mayowa",
    "job": {
        "department": "Data Analytics",
        "salary": 400000
    }
}

# Update the department to: Data Engineering
# Update the salary to: 550000
# print the entire dictionary

employee["job"]["department"] = "Data Engineering"
employee["job"]["salary"] = 550000

print(employee)

# Task 13: List of Dictionaries

employees = [
    {
        "id": "EMP001",
        "name": "Mayowa",
        "department": "IT"
    },
    {
        "id": "EMP002",
        "name": "Ada",
        "department": "Finance"
    },
    {
        "id": "EMP003",
        "name": "John",
        "department": "Sales"
    }
]

# loop through the list and print exactly: 
# Mayowa works in IT
# Ada works in Finance
# John works in Sales

for employee in employees:
    print(f"{employee['name']} works in {employee['department']}")

# Task 14: Filter Records (SQL WHERE Equivalent)

employees = [
    {"id": "EMP001", "name": "Mayowa", "department": "IT", "salary": 350000},
    {"id": "EMP002", "name": "Ada", "department": "Finance", "salary": 420000},
    {"id": "EMP003", "name": "John", "department": "Sales", "salary": 280000},
    {"id": "EMP004", "name": "Mary", "department": "HR", "salary": 310000}
]

# Loop through the list and print only employees whose salary is #300,000 or more 

for employee in employees:
    if employee["salary"] >= 300000:
        print(f"{employee['name']} - #{employee['salary']}")
        
# Task 15: Find the highest salary (without max())
# This challenge combines loops, dictionaries, and comparison logic.

employees = [
    {"id": "EMP001", "name": "Mayowa", "salary": 350000},
    {"id": "EMP002", "name": "Ada", "salary": 420000},
    {"id": "EMP003", "name": "John", "salary": 280000},
    {"id": "EMP004", "name": "Mary", "salary": 310000}
]

# find the employee with the highest salary without using:
# max()
# sort()

# Then print
# Highest Paid: Ada
# Salary: #420000

highest_paid = employees[0]

for employee in employees:
    if employee['salary'] > highest_paid['salary']:
        highest_paid = employee
    
print(f"Highest Paid: {highest_paid['name']}")
print(f"Salary: #{highest_paid['salary']}")    


        
    