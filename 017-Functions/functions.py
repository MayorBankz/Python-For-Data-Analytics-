# Task 1: Creating and calling a function
# Create a fuction called greet()
# It should simply print: Hello, welcome to python!

def greet():
    print("Hello, welcome to Python!")

greet()

# Task 2: Parameters
# Create a function called welcome_employee(name).
# It should print: Welcome Mayowa to the company!
# Test with two different names

def welcome_employee(name):
    print(f"Welcome {name} to the company!")
    
welcome_employee("Mayowa")
welcome_employee("Ada")

# Task 3: Multiple Parameters
# Create a function called: employee_info(name, department, salary)
# It should print:
# Employee: Mayowa
# Department: IT
# Salary: ₦350000

def employee_info(name, department, salary):
    print(f"Employee: {name}, Department: {department}, Salary: #{salary}")
    
employee_info("Mayowa", "IT", 350000)

# Task 4: return vs print()
# create: def calculate_total(price, quantity):
# It should return the total price instead of it 

def calculate_total(price, quantity):
    total_price = price * quantity
    return total_price
    
total_price = calculate_total(5000, 4)
print(total_price)

# Task 5: return with a calculation 
# create a function called: calculate_annual_salary(monthly_salary)
# It should: 
# Receive the employee's monthly_salary
# Multiply it by 12 
# Return the annual salary 

def calculate_annual_salary(monthly_salary):
    annual_salary = monthly_salary * 12
    return annual_salary

annual_salary = calculate_annual_salary(350000)
print(annual_salary)

# Task 6: Multiple Parameters + return 
# A company calculates an employee's net salary using:
# Net Salary = Basic Salary + Allowance - Deduction
# create: calculate_net_salary(basic_salary, allowance, deduction)
# It should return the net Salary

def calculate_net_salary(basic_salary, allowance, deduction):
    net_salary = basic_salary + allowance - deduction
    return net_salary
    
net_salary = calculate_net_salary(300000, 50000, 20000)
print(net_salary)

# Task 7: Default Parameters
# create: calculate_gross_salary(basic_salary, allowance=50000)
# It should return basic salary + allowance
# Test both
# print(calculate_gross_salary(300000, 80000))
# print(calculate_gross_salary(300000))

def calculate_gross_salary(basic_salary, allowance=50000):
    gross_salary = basic_salary + allowance
    return gross_salary
    
gross_salary = calculate_gross_salary(300000, 80000)
print(gross_salary)
gross_salary = calculate_gross_salary(300000)
print(gross_salary)

# Task 8: Keyword Arguments
# Use the function:
# def calculate_net_salary(basic_salary, allowance, deduction):
#  return basic_salary + allowance - deduction
# Then call it using keyword Argument
# Then print the result

def calculate_net_salary(basic_salary, allowance, deduction):
    net_salary = basic_salary + allowance - deduction
    return net_salary
    
net_salary = calculate_net_salary(deduction=20000, basic_salary=300000, allowance=50000)
print(net_salary)

# Task 9: Function + if/else 
# Business Requirement
# The company wants to determine whether an employee's salary is valid 
# A salary is valid if it is greater than 0.
# create: is_valid_salary(salary)
# It should return true if the salary is greater than 0.

def is_valid_salary(salary):
    if salary > 0:
        return True
    else:
        return False

print(is_valid_salary(300000))
print(is_valid_salary(-50000))
print(is_valid_salary(0))

# Task 10: Simplifying the validation Function
# Rewrite task 9 using the shorter version and test 

def is_valid_salary(salary):
    return salary > 0 
    
print(is_valid_salary(300000))
print(is_valid_salary(-50000))
print(is_valid_salary(0))

# Task 11: Validation with multiple conditions
# Business Requirement
# An employee's age is valid if:
# age is 18 or older
# and age is 65 or younger 
# create: is_valid_age(age)

def is_valid_age(age):
    return age >= 18 and age <= 65
    
print(is_valid_age(25))
print(is_valid_age(17))
print(is_valid_age(70))
print(is_valid_age(65))

# Task 12: Transformation Function 
# Business requirement 
# The company wants to give employees a 10% salary increase.
# create: increase_salary(salary)
# it should: 
# Receive the salary 
# calculate a 10% increase 
# Return the new salary 

def increase_salary(salary):
    new_salary = salary * 1.1 
    return new_salary 
    
new_salary = increase_salary(300000)
print(new_salary)

new_salary = increase_salary(500000)
print(new_salary)

# Task 13: Transformation with a parameter 
# Business requirement 
# Instead of always giving a 10% increase, the company wants to specify the percentage
# create: calculate_salary_increase(salary, percentage)
# It should:
# Receive salary 
# Receive percentage 
# Calculate the increase
# Add it to the original salary 
# Return the new salary 

def calculate_salary_increase(salary, percentage):
    increase = salary * percentage / 100
    new_salary = salary + increase 
    return new_salary
    
new_salary = calculate_salary_increase(300000, 10)
print(new_salary)
new_salary = calculate_salary_increase(300000, 20)
print(new_salary)
new_salary = calculate_salary_increase(500000, 15)
print(new_salary)

# Task 14: Function calling another Function
# We already have 

def is_valid_salary(salary):
    return salary > 0

# and

def calculate_salary_increase(salary, percentage):
    increase = salary * percentage / 100
    new_salary = salary + increase
    return new_salary 
    
# Now create a third function called:process_salary(salary, percentage):
# It should check whether the salary is_valid_salary
# If the salary is valid, calculate the salary increase using calculate_salary_increase().
# If the salary is invalid, return "Invalid salary"

def process_salary(salary, percentage):
    if is_valid_salary(salary):
        return calculate_salary_increase(salary, percentage)
    else:
        return "Invalid Salary"
        

print(process_salary(300000, 10))
print(process_salary(-50000, 10))

# Task 15: Function + Default Parameters 
# Create a function: def calculate_gross_salary(basic_salary, allowance=50000):
# It should return: basic_salary + allowance
# Test it two ways 
# print(calculate_gross_salary(300000, 80000))
# print(calculate_gross_salary(300000))

def calculate_gross_salary(basic_salary, allowance=50000):
    gross_salary = basic_salary + allowance
    return gross_salary
    
gross_salary = calculate_gross_salary(30000, 80000)
print(gross_salary)
gross_salary = calculate_gross_salary(30000)
print(gross_salary)

# Task 16: Keyword Arguments + Default parameters 
# create: def calculate_gross_salary(basic_salary, allowance=50000):
# Then call it using keyword argument 

def calculate_gross_salary(basic_salary, allowance=50000):
    gross_salary = basic_salary + allowance 
    return gross_salary
    
gross_salary = calculate_gross_salary(allowance = 80000, basic_salary=300000)
print(gross_salary)

# Task 17: Validation Function with multiple conditions 
# Business requirement 
# An employee's salary increase percentage is valid if:
# It is greater than 0 
# It is not more than 50%
# create: is_valid_increase(percentage)

def is_valid_increase(percentage):
    return percentage > 0 and percentage <= 50 

print(is_valid_increase(10))
print(is_valid_increase(50))
print(is_valid_increase(0))
print(is_valid_increase(60))
print(is_valid_increase(-10))

# Task 18: Validation + Transformation 
# Business requirement 
# The company wants to increase an employee's salary.
# However, salary must be greater than 0.
# Increase percentage must be between 1% and 50% 
# If both are valid - calculate the new salary 
# Otherwise - return "Invalid Input"
# calculate_salary(salary, percentage)

def calculate_salary(salary, percentage):
    if salary > 0 and percentage > 0 and percentage <= 50:
        increase = salary * percentage / 100
        new_salary = salary + increase
        return new_salary
    else:
        return "Invalid Input"
        
print(calculate_salary(300000, 10))
print(calculate_salary(300000, 50))
print(calculate_salary(-50000, 10))
print(calculate_salary(300000, 60))

# Task 19: *args 
# create: def calculate_total_sales(*sales):
# It should return the total sales

def calculate_total_sales(*sales):
    return sum(sales)

print(calculate_total_sales(100000, 200000, 150000))
print(calculate_total_sales(100000, 200000, 150000, 50000, 300000))

# Task 20: Understanding args*
# create:
# def display_sales(*sales):
# Inside the function, print:
# The sales variable
# The type of sales
# The number of sales received

def display_sales(*sales):
    print(sales)
    print(len(sales))
    print(type(sales))
    
display_sales(10000, 50000, 70000)

# Task 21: **Kwargs
# create def employee_info(**employee):
# Inside the function, print:
# employee
# type(employee)
# len(employee)

def employee_info(**employees):
    print(employees)
    print(type(employees))
    print(len(employees))
    
employee_info(name="Mayowa", department="IT", salary=35000)

# Task 22: Accessing **Kwargs
# create def employee_info(**employee):
# The function should print
# Name: Mayowa
# Department: IT
# Salary: ₦350000

def employee_info(**employee):
    print(f"Name: {employee['Name']}")
    print(f"Department: {employee['Department']}")
    print(f"Salary: {employee['Salary']}")

employee_info(Name="Mayowa", Department="IT", Salary=350000)

# Task 23: *args + **kwargs together
# create a function: def employee_profile(*skills, **employee):
# The function should receive 
# Positional arguments - skills
# "Python"
# "SQL"
# "Excel"
# Keyword arguments - employee information
# name="Mayowa"
# department="Data Analytics"
# Then print:
# Name: Mayowa
# Department: Data Analytics
# Skills: ('Python', 'SQL', 'Excel')

def employee_profile(*skills, **employee):
    print(f"Name: {employee['Name']}")
    print(f"Department: {employee['Department']}")
    print(skills)
   
    
employee_profile('Python', 'SQL', 'Excel', Name="Mayowa", Department="Data Analytics")

# Task 24: *args + calculation
# Business requirement
# A sales manager may enter any number of daily sales
# create: def calculate_average_sales(*sales):
# The function should:
# Accept any number of sales 
# Calculate the total sales 
# Calculate the average sales
# Return the average 

def calculate_average_sales(*sales):
    total_sales = sum(sales)
    average_sales = total_sales / len(sales)
    return average_sales 
    
average_sales = calculate_average_sales(100000, 200000, 150000, 50000)

print(average_sales)

# Task 25: **kwargs + Business Logic 
# Business requirement
# The company wants a function that receives employee information and determines whether the 
# employee is a high earner 
# create: def check_high_earner(**employee)
# The function will receive
# check_high_earner(
#    name="Mayowa",
#    department="IT",
#    salary=350000
# )

def check_high_earner(**employee):
    if employee['salary'] >= 350000:
        return f"{employee['name']} is a high earner"
    else:
        return f"{employee['name']} is not a high earner"
    
print(check_high_earner(name="Mayowa", department="IT", salary=350000))
print(check_high_earner(name="John", department="Sales", salary=280000))

# Task 27: Combining **kwargs with validation
# Business requirement 
# create: def validate_employee(**employee):
# The employee is valid only if:
# name exists
# department exists
# salary is greater than 0 
# if everything is valid: return "Employee is valid"
# otherwise return: "Invalid employee data"

def validate_employee(**employee):
    if employee['name'] and employee['department'] and employee['salary'] > 0:
        return "Employee is valid"
    else:
        return "Invalid employee data"
        
print(validate_employee(name = "Mayowa", department="IT", salary=350000))
print(validate_employee(name="John", department="Sales", salary=-50000))

# Task 27: Local Variables
# create: def calculate_bonus(salary):
# Inside the function:
# Create a local vriable called bonus 
# calculate a 10% bonus 
# Return the bonus 

def calculate_bonus(salary):
    bonus = salary * 0.1 
    return bonus 

bonus = calculate_bonus(300000)
print(bonus)

# Task 28: Global vs Local Variable 
# create: company_name = "Nigeria Distilleries Limited"
# Then create def employee_message(name):
# Inside the function, create a local variable: message
# The message should say:
# Welcome Mayowa to Nigeria Distilleries Limited
# Then return the message 

company_name = "Nigeria Distilleries Limited"

def employee_message(name):
    message = f"Welcome {name} to {company_name}"
    return message
    
message = employee_message("Mayowa")
print(message)
message = employee_message("Ada")

# Task 29: Global Variable 
# Business Requirement 
# The company currently has: company_name = "Nigeria Distilleries Limited"
# Create a function called: change_company()
# Inside the function:
# Use the global keyword
# Change company_name to "ABC Limited"
# Then run:
# print(company_name)

# change_company()

# print(company_name)

company_name = "Nigeria Distilleries Limited"

def change_company():
    global company_name
    company_name = "ABC Limited"
    
print(company_name)
change_company()
print(company_name)

# Task 30: Orchestrator function
# We have two functions 
# Validation Function
def is_valid_salary(salary):
    return salary > 0 

# Transformation Function

def increase_salary(salary, percentage):
    increase = salary * percentage / 100
    new_salary = salary + increase 
    return new_salary 

def process_salary(salary, percentage):
    if is_valid_salary(salary):
        return increase_salary(salary, percentage)
    else:
        return "Invalid Salary"
        
print(process_salary(300000, 10))
print(process_salary(500000, 20))
print(process_salary(-50000, 10))
    
