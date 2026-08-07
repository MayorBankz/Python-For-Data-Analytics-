# Task 1: iter() and Next()
# A company has four employees

employees = ["Mayowa", "Ada", "John", "Mary"]

# Create an iterator called employee_iterator
# print the first employee using next()
# print the second emploee using next()

employee_iterator = iter(employees)

print(next(employee_iterator))
print(next(employee_iterator))

# Task 2: Understanding stopIteration

# employees = ["Mayowa", "Ada", "John"]

# Create an iterator and call next() four times

#employee_iterator = iter(employees)
 
# print(next(employee_iterator))
# print(next(employee_iterator))
# print(next(employee_iterator))
# print(next(employee_iterator))

# Task 3: Manual iterator

sales = [120000, 85000, 230000, 150000]

# Create an iterator called sales_iterator
# Then use next() to print the sales one at a time.

sales_iterator = iter(sales)

print(next(sales_iterator))
print(next(sales_iterator))
print(next(sales_iterator))
print(next(sales_iterator))

# Task 4: Iterable vs Iterator 

employees = ["Mayowa", "Ada", "John"]
employee_iterator = iter(employees)

# print the results of:
# print(iter(employees))
# print(employee_iterator)

print(iter(employees))
print(employee_iterator)

# lambda
# Given:

number = 20

# create a lambda function called double that multiplies a number by 2

double = lambda number: number * 2

print(double(number))

# lambda
# create a lambda function called add_tax that adds 7.5% tax to a price

price = 10000

add_tax = lambda price: price * 0.075 + price

print(add_tax(price))

# Given

prices = [10000, 20000, 50000, 80000]

taxed_prices = map(lambda price: price * 1.075, prices)

print(list(taxed_prices))

# map() without lambda
# Given 

sales = [100000, 200000, 300000, 400000]

# The company wants to calculate a 5% commission on every sale
# Create a normal function

def calculate_commission(sale):
     return sale * 0.05 
commissions = map(calculate_commission, sales)
print(list(commissions))

# filter()
# Given

sales = [100000, 250000, 80000, 350000, 120000]

# The company wants to identify large sales of #200000 or more 
# use filter() to keep only sales >= 200000

def is_large_sale(sale):
    return sale >= 200000
large_sales = filter(is_large_sale, sales)

print(large_sales)

    
# Task 5: map()

salaries = [250000, 320000, 450000, 280000]

# The company wants to give everyone a 10% salary increase
# use map() to increase every salary by 10%


increased_salaries = map(lambda salary: salary * 1.10, salaries)

print(list(increased_salaries))

# Task 6: map() without lambda

prices = [10000, 25000, 50000, 75000]

# The company wants to add a #2,000 delivery charge to every price.
# Use map() without a lambda
# create a function
# def add_delivery(price):
    # return price + 2000
# Then use map() to produce
# [12000, 27000, 52000, 77000]

def add_delivery(price):
    return price + 2000

updated_prices = map(add_delivery, prices)
print(list(updated_prices))

# Task 7: filter()

sales = [120000, 85000, 230000, 150000, 45000, 300000]

# Use filter() to keep only sales greater than or equal to #150,000

higher_sales = filter(lambda sales: sales >= 150000, sales)

print(list(higher_sales))

# Task 8: filter() with Dictionaries

employees = [
    {"name": "Mayowa", "department": "IT", "salary": 350000},
    {"name": "Ada", "department": "Finance", "salary": 420000},
    {"name": "John", "department": "Sales", "salary": 280000},
    {"name": "Mary", "department": "HR", "salary": 310000},
    {"name": "Peter", "department": "IT", "salary": 390000}
]

# Use filter() to keep only employees who work in IT

it_employee = filter(lambda employee: employee["department"] == "IT", employees)

print(list(it_employee))

# Task 9: filter() with a normal function

employees = [
    {"name": "Mayowa", "salary": 350000},
    {"name": "Ada", "salary": 420000},
    {"name": "John", "salary": 280000},
    {"name": "Mary", "salary": 310000}
]

# create a function called high_earner that returns True when an employee's salary is #350,000
# or more, then use filter() to select those employees

def high_earner(employee):
    return employee["salary"] >= 350000

high_earners = filter(high_earner, employees)

for employee in high_earners:
    print(employee["name"])
    
# same filter(), Now with lambda
# using the same employees, create 
# high_earners = filter(__________, employees)

employees = [
    {"name": "Mayowa", "salary": 350000},
    {"name": "Ada", "salary": 420000},
    {"name": "John", "salary": 280000},
    {"name": "Mary", "salary": 310000}
]

high_earners = filter(lambda employee: employee["salary"] >= 350000, employees)

for employee in high_earners:
    print(employee["name"])
    
# Task 10: map() vs filter()
# consider

salaries = [200000, 300000, 400000, 500000]

# Give every salary a 10% increase

salary_increase = map(lambda salary: salary * 0.1 + salary, salaries)

print(list(salary_increase))

# From the original salaries, keep only salaries of #350,000 or more

higher_salary = filter(lambda salary: salary >= 350000, salaries)

print(list(higher_salary))

# Task 11: Real-World Employee Data

employees = [
    {"name": "Mayowa", "department": "IT", "salary": 350000},
    {"name": "Ada", "department": "Finance", "salary": 420000},
    {"name": "John", "department": "Sales", "salary": 280000},
    {"name": "Mary", "department": "HR", "salary": 310000},
    {"name": "Peter", "department": "IT", "salary": 390000}
]

# use filter() + lambda to select only IT employees

it_employees = filter(lambda employee: employee["department"] == "IT", employees)

for employee in it_employees:
    print(employee["name"])
    
# Now use map() + lambda on the original employees list to extract only the employee names

extract = map(lambda employee: employee["name"], employees)

print(list(extract))

# Task 12: map() + filter() together 
# using the same employee data:

employees = [
    {"name": "Mayowa", "department": "IT", "salary": 350000},
    {"name": "Ada", "department": "Finance", "salary": 420000},
    {"name": "John", "department": "Sales", "salary": 280000},
    {"name": "Mary", "department": "HR", "salary": 310000},
    {"name": "Peter", "department": "IT", "salary": 390000}
]

# Business requirement 
# The company wants the name of IT employees who earn #350,000 or more

it_higher_earners = filter(lambda employee: employee["salary"] >= 350000 and employee["department"] == "IT", employees)

names = map(lambda employee: employee["name"], it_higher_earners)

print(list(names))

# Task 13: A more realistic data Task

products = [
    {"name": "Laptop", "category": "Electronics", "price": 450000},
    {"name": "Mouse", "category": "Accessories", "price": 15000},
    {"name": "Monitor", "category": "Electronics", "price": 120000},
    {"name": "Keyboard", "category": "Accessories", "price": 35000},
    {"name": "Phone", "category": "Electronics", "price": 300000}
]

# Business requirement
# The company wants the names of Electronnics products costing #100,000 or more

electronic_products = filter(lambda product: product["price"] >= 100000
                                    and product["category"] == "Electronics", products)
names = map(lambda product: product["name"], electronic_products)
print(list(names))

# Task 14: zip()
# Given

names = ["Mayowa", "Ada", "John", "Mary"]
salaries = [350000, 420000, 280000, 310000]

# Use zip() to combine them, then loop through the result

combined = list(zip(names, salaries))

for name, salary in combined:
    print(f"{name} earns #{salary}")
    
# Task 15: zip() + Dictionary

names = ["Mayowa", "Ada", "John", "Mary"]
departments = ["IT", "Finance", "Sales", "HR"]
salaries = [350000, 420000, 280000, 310000]

# create a list of dictionaries containing:
# [
#    {"name": "Mayowa", "department": "IT", "salary": 350000},
#     {"name": "Ada", "department": "Finance", "salary": 420000},
#     {"name": "John", "department": "Sales", "salary": 280000},
 #   {"name": "Mary", "department": "HR", "salary": 310000}
# ]

employees = []

for name, department, salary in zip(names, departments, salaries):
    employee = {
        "name": name,
        "department": department,
        "salary": salary
        }
    employees.append(employee)
print(employees)

# Task 16: enumerate()
# Given:

products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

# The company wants to number the product starting from 1.
# Use enumerate to produce this output

for index, product in enumerate(products, start=1):
    print(f"{index}. {product}")

# Task 17: enumerate() + condition
# You have a list of sales

sales = [120000, 85000, 230000, 150000, 300000]

# The company wants to identify sales of #200,000 or more and display their transaction number

for index, sale in enumerate(sales, start=1):
    if sale > 200000:
        print(f"Transaction {index}: #{sale}")
    
# Task 18: reversed()
# Given:

products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

# The warehouse wants to process the products from the last item to first
# Use a reversed() and a for loop.


for product in list(reversed(products)):
    print(product)
    
# Task 19: reversed() + enumerate()
# Given 

departments = ["IT", "Finance", "Sales", "HR"]

# The company wants to display the departments in reverse order, while still numbering them from 19

for index, department in enumerate(reversed(departments), start=1):
    print(f"{index}.{department}")
    
# Task 20: Sort employees by salary
# Given:

employees = [
    {"name": "Mayowa", "salary": 350000},
    {"name": "Ada", "salary": 420000},
    {"name": "John", "salary": 280000},
    {"name": "Mary", "salary": 310000}
]

# sort employees by salary then 
# loop through the result and print:
# John - ₦280000
# Mary - ₦310000
# Mayowa - ₦350000
# Ada - ₦420000
 
sorted_employees = sorted(employees, key=lambda employee: employee["salary"])
 
for employee in sorted_employees:
     print(f"{employee['name']} - #{employee['salary']}")
     
# Task 21: Highest Salary first
# using the same employees list, sort employees from highest salary to lowest salary

employees = [
    {"name": "Mayowa", "salary": 350000},
    {"name": "Ada", "salary": 420000},
    {"name": "John", "salary": 280000},
    {"name": "Mary", "salary": 310000}
]


sorted_employee = sorted(employees, key=lambda employee: employee['salary'], reverse=True)

for employee in sorted_employee:
    print(f"{employee['name']} - #{employee['salary']}")
    
# Task 22: Sort by name

employees = [
    {"name": "Mayowa", "salary": 350000},
    {"name": "Ada", "salary": 420000},
    {"name": "John", "salary": 280000},
    {"name": "Mary", "salary": 310000}
]

# sort the emmployees alphabetically by name

sorted_employees = sorted(employees, key=lambda employee: employee['name'])

for employee in sorted_employees:
    print(f"{employee["name"]} - #{employee["salary"]}")

# Task 21: Sort by Multiple Conditions

employees = [
    {"name": "Mayowa", "department": "IT", "salary": 350000},
    {"name": "Ada", "department": "Finance", "salary": 420000},
    {"name": "John", "department": "IT", "salary": 280000},
    {"name": "Mary", "department": "Finance", "salary": 310000},
    {"name": "Peter", "department": "IT", "salary": 350000}
]

# Business requirement
# sort employees by:
# Department alphabetically
# within each department, sort by salary from highest to lowest

sorted_employees = sorted(employees, key=lambda employee: (employee["department"], -employee["salary"]))

for employee in sorted_employees:
    print(f"{employee['name']} - {employee['department']} - #{employee['salary']}")
    
# Task 22: min() and max()

employees = [
    {"name": "Mayowa", "salary": 350000},
    {"name": "Ada", "salary": 420000},
    {"name": "John", "salary": 280000},
    {"name": "Mary", "salary": 310000}
]

# Find the employee with the highest salary using: max() and key= lambda

highest_paid = max(employees, key=lambda employee: employee['salary'])

print(f"Highest Paid: {highest_paid['name']}")
print(f"Salary: {highest_paid['salary']}")

# Task 23: Find the lowest paid employee
# using the same employees list, find the employee with the lowest salary using
# min()
# key=
# lambda

employees = [
    {"name": "Mayowa", "salary": 350000},
    {"name": "Ada", "salary": 420000},
    {"name": "John", "salary": 280000},
    {"name": "Mary", "salary": 310000}
]

lowest_paid = min(employees, key=lambda employee: employee["salary"])

print(f"Lowest Paid: {lowest_paid['name']}")
print(f"Salary: #{lowest_paid['salary']}")

# Task 24: Basic List Comprehension
# Given:

numbers = [1, 2, 3, 4, 5]

# create a new list called squared numbers containing the square of every number

squared_numbers = [number ** 2 for number in numbers]

print(squared_numbers)

# Task 25: List Comprehension + if

salaries = [200000, 300000, 450000, 180000, 500000]

# The company wants a new list containing only salaries of #300,000 or more

high_salaries = [salary for salary in salaries if salary > 300000]

print(high_salaries)

# Task 26: Transform + filter
# Given:

salaries = [200000, 300000, 450000, 180000, 500000]

# The company wants to:
# select salaries #300,000 or more
# Give those salaries a 10% increase
# store the result in increased_high_salaries

increased_high_salaries = [round(salary * 1.1) for salary in salaries if salary >= 300000]

print(increased_high_salaries)

# Task 27

employees = [
    {"name": "Mayowa", "department": "IT", "salary": 350000},
    {"name": "Ada", "department": "Finance", "salary": 420000},
    {"name": "John", "department": "Sales", "salary": 280000},
    {"name": "Mary", "department": "HR", "salary": 310000},
    {"name": "Peter", "department": "IT", "salary": 390000}
]


# Business requirement
# Create a list called it_names containing the names of IT employees only

it_employees = [employee["name"] for employee in employees if employee["department"] == "IT"]

print(it_employees)

# Task 28: Dictionary Comprehension
# Given

names = ["Mayowa", "Ada", "John", "Mary"]
salaries = [350000, 420000, 280000, 310000]

# create a dictionary called employee_salaries:

employee_salaries = {name: salary for name, salary in zip(names, salaries)}

print(employee_salaries)

# Task 29: Dictionary Comprehension + Condition
# Given 

employees = [
    {"name": "Mayowa", "salary": 350000},
    {"name": "Ada", "salary": 420000},
    {"name": "John", "salary": 280000},
    {"name": "Mary", "salary": 310000},
    {"name": "Peter", "salary": 390000}
]

# Business requirement 
# Create a dictionary called high_earners containing: employee name - salary but only
# employees earning #350,000 or more

high_earners = {employee["name"]: employee["salary"] for employee in employees if employee["salary"] >= 350000}

print(high_earners)




