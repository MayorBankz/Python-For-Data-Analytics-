## Topic - Python Functions
## Date - 17-08-2026

---

##  **Table of Contents**
1. What is a Function?
2. Why use Functions?
3. Basic function structure
4. Parameters and Arguments
5. Parameters
6. Arguments
7. Local variable
8. Global variable
9. Global Access
10. Control Logic Globally
11. Raw Data vs Processed Data
12. Positional Arguments
13. Keyword Arguments
14. Mixed Arguments
15. Default Parameters
16. *args
17. When to use *args
18. **kwargs
19. *args vs **kwargs
20. Function Types
21. Transformation Functions
22. Validation Functions
23. Orchestrator Functions
24. How the three Function Types Work Together
25. Real-World Data Processing Example
26. Function Styling Guide
27. Good vs Poor Function Design
28. Common Mistakes
29. Function Design Checklist
30. Quick Reference
31. Key takeaways

---

## **What is a Function**

A function is a reusable block of code designed to perform a specific task.

Instead of writing the same logic repeatedly, you write it once inside a function and call it whenever you need it.

Python defines a function using the def keyword. A function definition contains the function name, parameters, and an indented body.

### **Simple Example**

```python
def greet():
    print("Hello, Mayowa")
```

Calling the function:

```python
greet()
```

### Output

Hello, Mayowa


---


## **Why Use Functions?**

Functions help us write programs that are:
* Reusable
* Easier to understand
* Easier to maintain
* Easier to test
* Easier to debug
* More organized
* Less repititive

## **Without a function**

Imagine calculating a 10% salary increase for three employees:

salary1 = 300000
new_salary1 = salary1 + (salary1 * 10 / 100)

salary2 = 400000
new_salary2 = salary2 + (salary2 * 10 / 100)

salary3 = 500000
new_salary3 = salary3 + (salary3 * 10 / 100)

There is a lot of repeated logic.

---

## **With a function**

```python
def increase_salary(salary):
    return salary + (salary * 10 / 100)
```

Now:

print(increase_salary(300000))
print(increase_salary(400000))
print(increase_salary(500000))

The logic is written once.

## **Real-world application**

A company may need to:
* Calculate salaries
* Calculate commissions
* Validate customer records
* Clean names
* Calculate sales totals
* Calculate discounts
* Validate email addresses
* Generate reports

Instead of writing these operations every time, create reusable functions.

---

## **How a Function Works?**

Consider:

```pyton
def increase_salary(salary, percentage):
    increase = salary * percentage / 100
    return salary + increase
```

When we call:

```python
result = increase_salary(300000, 10)
```

Python essentially follows this process:

1. Call the function
         ↓
2. Pass 300000 into salary
         ↓
3. Pass 10 into percentage
         ↓
4. Calculate the increase
         ↓
5. Calculate the new salary
         ↓
6. return the result
          ↓
7. Store result in result

Result:

330000.0

### **Important Idea**

The function receives inputs, performs processing, and optionally produces an **output**.

INPUT → PROCESS → OUTPUT

---

4. **Basic Function Structure**

The basic structure is:

```python
def function_name(parameters):
    # processing
    return result
```

### Example
```python
def add_numbers(a, b): 
    result = a + b 
    return result
```

Calling it:

```python
answer = add_numbers(10, 20)
print(answer)
```

### Output
30

Breakdown
def

Tells Python that we are defining a function.

add_numbers

The function name.

(a, b)

The parameters.

result = a + b

The processing logic.

return result

Sends the result back to the caller.

---

## Parameters and Arguments

This is one of the most important distinctions to understand

### Parameter 

A parameter is the name used in the function definition.

```python
def greet(name):
    print(name)
```

`name` is the parameter.

---

## **Argument**

An argument is the actual value supplied when calling the function.

greet("Mayowa")

"Mayowa" is the argument.

**Simple way to remember**

PARAMETER = placeholder

ARGUMENT = actual value

Python's documentation makes the same distinction: parameters are names defined in a function definition, while arguments are the values passed during the function call.

---

## **Parameters**

Parameters allow a function to receive information.

```python
def calculate_bonus(salary):
    return salary * 10 / 100
```

Here:

salary

is a parameter.

We can pass different values:

```python
calculate_bonus(300000)
calculate_bonus(500000)
calculate_bonus(700000)
```

The function can therefore work with different data without changing its internal logic.

---

## **Multiple parameters**

```python
def calculate_bonus(salary, percentage): 
    return salary * percentage / 100
```

Calling:

```python
calculate_bonus(300000, 10)
```

Here:

salary     → 300000
percentage → 10

---

## **Arguments**

Arguments are the values supplied to parameters.

```python
def employee_info(name, department, salary):
    print(name)
    print(department)
    print(salary)
```

Calling:

```python
employee_info("Mayowa", "IT", 350000)
```

The arguments are:

"Mayowa"
"IT"
350000

They are assigned to:

name
department
salary

Python supports different ways of supplying these arguments, including positional, keyword, and combinations of both.

---

## **Local Variables**

A variable created inside a function normally belongs to that function's local scope.

Example:

```python
def calculate_bonus(salary):
    bonus = salary * 10 / 100
    return bonus
```

bonus is a local variable.

It exists within the function while the function is executing.

```python
def calculate_bonus(salary):
    bonus = salary * 10 / 100
    return bonus
```

```
print(bonus)
```

This produces an error because bonus was created inside the function.

Think of local variables as private workspace
FUNCTION
┌─────────────────────────┐
│ salary = 300000         │
│ bonus = 30000           │
│                         │
│ These belong here       │
└─────────────────────────┘

Python creates a local symbol table for function execution. Assignments inside a function normally create local names.

---

## **Global Variables**

A global variable is created outside a function.

``` python
company = "Nigeria Distilleries Limited"

def employee_message(name):
    return f"{name} works at {company}"
```

Calling:

```python
print(employee_message("Mayowa"))
```

Output:

Mayowa works at Nigeria Distilleries Limited

The function can read the global variable.

---

## **Global Access**

A function can generally access a global variable if it does not create a local variable with the same name.

Example:

```python
company = "NDL"

def show_company():
    print(company)

show_company()
```


Output:

NDL

---

## **Local vs Global**

Consider:

company = "NDL"

```python
def change_company():
    company = "ABC"
    print(company)

change_company()

print(company)
```

Output:

ABC
NDL

Why?

Because:

company = "ABC"

inside the function creates a local variable.

It does not change the global company.

---

## **Control Logic Globally**

The phrase "control logic globally" can be understood as keeping important application-wide decisions or configuration in one place rather than scattering them throughout many functions.

For example:

SALARY_INCREASE = 10
MINIMUM_SALARY = 0

Then:

```python
def is_valid_salary(salary):
    return salary > MINIMUM_SALARY
```
And:

```python
def increase_salary(salary):
    return salary + (salary * SALARY_INCREASE / 100)
```

Now the business rules are centralized.

If the company changes the standard increase from 10% to 15%, you can change:

SALARY_INCREASE = 15

instead of searching through many functions.

Real-world application

A sales application might have:

VAT_RATE = 0.075
DISCOUNT_LIMIT = 100000
MIN_ORDER_QUANTITY = 10

Functions can use these settings.

Important

Global configuration can be useful, but avoid creating too many mutable global variables.

For most application logic, passing values into functions or returning values from functions is easier to test and maintain.

---

## **Raw Data vs Processed Data**

Functions become especially useful when working with data.

Raw Data

Raw data is data in its original or unprocessed form.

Example:

```python
customer = {
    "name": "  mayowa idowu  ",
    "country": "ng",
    "email": "mayowa@gmail.com"
}
```

The data may contain:

Extra spaces
Inconsistent capitalization
Invalid values
Missing values
Incorrect formats

---

## **Processed Data**

Processed data has been cleaned, transformed, validated, or analyzed.

For example:

```python
{
    "name": "MAYOWA IDOWU",
    "country": "NG",
    "email": "mayowa@gmail.com"
}
```
Functions can create the transformation

```python
def clean_name(name):
    return name.strip().upper()
```

Then:

raw_name = "  mayowa idowu  "

clean_name(raw_name)

Output:

MAYOWA IDOWU
Data pipeline
RAW DATA
   ↓
VALIDATION
   ↓
TRANSFORMATION
   ↓
PROCESSED DATA
   ↓
ANALYSIS

This pattern is particularly useful in data analytics and data engineering.

---

## **Positional Arguments**

Positional arguments are assigned according to their position.

```python
def employee(name, department, salary):
    print(name)
    print(department)
    print(salary)
```

Calling:

```python
employee("Mayowa", "IT", 350000)
```

Python matches:

"Mayowa"  → name
"IT"      → department
350000    → salary
The order matters
employee("IT", "Mayowa", 350000)

Python will still run, but the values will be assigned incorrectly.

---

## **Keyword Arguments**

Keyword arguments explicitly specify the parameter name.

employee(
    name="Mayowa",
    department="IT",
    salary=350000
)

This is easier to read.

You can also change the order:

```python
employee(
    salary=350000,
    department="IT",
    name="Mayowa"
)
```
The names tell Python where each value belongs.

---

## **Mixed Arguments**

You can combine positional and keyword arguments.

```python
def employee(name, department, salary):
    print(name)
    print(department)
    print(salary)
```
Example:

```python
employee(
    "Mayowa",
    department="IT",
    salary=350000
)
```

This is valid.

The positional argument comes first, followed by keyword arguments.

Invalid pattern

Avoid:

```python
employee(
    name="Mayowa",
    "IT",
    350000
)
```
You cannot place positional arguments after keyword arguments.

Simple rule
POSITIONAL → first
KEYWORD    → after

---


## **Default Parameters**

A default parameter has a value that Python uses when the caller does not provide one.

Example:

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"
```
Calling:

```python
print(greet("Mayowa"))
```


Output:

Hello, Mayowa

The default value is used.

You can override it:

```python
print(greet("Mayowa", "Welcome"))
```
Output:

Welcome, Mayowa

---

## **Real-world Example**

```python
def calculate_discount(price, discount=10):
    return price - (price * discount / 100)
```
If no discount is supplied:

```python
calculate_discount(100000)
```

Python uses:

discount = 10

You can override it:

```python
calculate_discount(100000, 20)
```
Python allows default values for parameters, making some arguments optional.

---

## ***args**

*args allows a function to accept an arbitrary number of positional arguments.

Example:

```python
def add_numbers(*args):
    print(args)
```


Calling:

```python
add_numbers(10, 20, 30, 40)
```

Output:

(10, 20, 30, 40)

Inside the function, args is a tuple.

---

## **Using *args**

Using *args

```python
def add_numbers(*args):
    total = 0

    for number in args:
        total += number

    return total
```

Now:

```python
print(add_numbers(10, 20))
print(add_numbers(10, 20, 30))
print(add_numbers(10, 20, 30, 40))
```

Output:

30
60
100

---

## **When to use *args**

Use *args when:

You don't know how many positional values the function will receive.


Example: Sales totals

```python
def calculate_total_sales(*sales):
    return sum(sales)
```
Usage:

```python
calculate_total_sales(
    100000,
    250000,
    300000
)
```

Output:

650000

### **Real-world applications**

*args can be useful for:
* Adding many numbers
* Combining multiple lists
* Processing multiple sales values
* Passing an unknown number of items
* Building flexible utility functions

---

## **Kwargs**

**kwargs allows a function to accept an arbitrary number of keyword arguments.

Example:

```python
def employee_info(**employee):
    print(employee)
```
Calling:

```python
employee_info(
    name="Mayowa",
    department="IT",
    salary=350000
)
```
Output:

```python
{
    'name': 'Mayowa',
    'department': 'IT',
    'salary': 350000
}
```

Inside the function, kwargs behaves like a dictionary.

Python documents **kwargs as a variable-keyword parameter that collects arbitrary keyword arguments into a dictionary.

---

## **Accessing **kwargs**

```python
def employee_info(**employee):
    print(employee["name"])
    print(employee["department"])
    print(employee["salary"])
```
Calling:

```python
employee_info(
    name="Mayowa",
    department="IT",
    salary=350000
)
```
Output:

Mayowa
IT
350000

---

## **When to use **kwargs**

Use **kwargs when:

You don't know in advance which keyword arguments will be supplied.

For example:

```python
def create_customer(**customer):
    return customer
```
You can call:

```python
create_customer(
    name="Mayowa",
    email="mayowa@gmail.com",
    country="NG"
)
```
Or:

```python
create_customer(
    name="John",
    phone="08000000000",
    city="Lagos"
)
```

Real-world applications

**kwargs can be useful for:

* Customer records
* Employee records
* Configuration settings
* Optional properties
* API parameters
* Flexible data-processing functions

---

## ***args vs **kwargs**

| Feature | *args	| **kwargs |
| ------- | ------ | ------- |
| Accepts	| Positional arguments	| Keyword arguments |
| Stored as | Tuple |	Dictionary |
| Example | 10, 20, 30 | name="Mayowa" |
| Useful when	| Number of values varies	| Named options vary |
| Syntax	| *args	| **kwargs |

Example
```python
def example(*args, **kwargs):
    print(args)
    print(kwargs)
```
Calling:

```python
example(
    10,
    20,
    30,
    name="Mayowa",
    department="IT"
)
```

Output:

(10, 20, 30)

{
    'name': 'Mayowa',
    'department': 'IT'
}

---

## **Function Types**

Python does not have built-in categories officially named "transformation function," "validation function," and "orchestrator function." These are useful design categories for organizing application logic.

Common function categories include:

1. Built-in functions

Functions already provided by Python.

Examples:

print()
len()
sum()
max()
min()
type()
2. User-defined functions

Functions you create yourself.

```python
def calculate_salary():
    ...
```

3. Lambda functions

Small anonymous functions.

square = lambda x: x ** 2

4. Validation functions

Functions that check whether data is valid.

```python
def is_valid_salary(salary):
    return salary > 0
```

5. Transformation functions

Functions that change data.

```python
def increase_salary(salary, percentage):
    ...
```

6. Orchestrator functions

Functions that coordinate other functions.

```python
def process_salary():
    ..
```

---

## **Transformation Functions**

A transformation function takes data and changes it into another form.

Example

```python
def clean_name(name):
    return name.strip().upper()
```

Input:

"  mayowa  "

Output:

"MAYOWA"

---

## **Salary Transformation**

```python
def increase_salary(salary, percentage):
    increase = salary * percentage / 100
    return salary + increase
```

Input:

300000

Output:

330000

---

## **Real-world applications**

Transformation functions can be used to:

Clean customer names
Convert currencies
Format dates
Calculate discounts
Calculate tax
Convert units
Standardize country codes
Transform raw sales data
Calculate derived columns
Data transformation pattern
RAW VALUE
    ↓
TRANSFORMATION FUNCTION
    ↓
NEW VALUE

---

## **Validation Functions**

A validation function checks whether data meets a specific rule.

Example:

```python
def is_valid_salary(salary):
    return salary > 0
```

Testing:

```python
print(is_valid_salary(300000))
```

Output:

True

And:
```python
print(is_valid_salary(-50000))
```
Output:

False

---

## **Customer Email Validation**

def is_valid_email(email):
    return "@" in email and "." in email

Example:

print(is_valid_email("mayowa@gmail.com"))

Output:

True

---

## **Real-world applications**

Validation functions can check:

* Salary
* Email
* Phone number
* Age
* Product price
* Stock quantity
* Customer IDs
* Required fields
* Transaction amounts
* Validation pattern

RAW DATA
   ↓
VALIDATION FUNCTION
   ↓
VALID?
 ↙     ↘
YES     NO
 ↓       ↓
PROCESS  REJECT

---

## **Orchestrator Functions**

An orchestrator function coordinates multiple functions.

It does not necessarily perform all the detailed work itself.

Instead, it controls which function should run and when.

For example:

```python
def is_valid_salary(salary):
    return salary > 0


def increase_salary(salary, percentage):
    increase = salary * percentage / 100
    return salary + increase


def process_salary(salary, percentage):
    if is_valid_salary(salary):
        return increase_salary(salary, percentage)
    else:
        return "Invalid Salary"
```

Here:

is_valid_salary()
        ↓
checks the data

increase_salary()
        ↓
transforms the data

process_salary()
        ↓
coordinates the process

process_salary() is the orchestrator.

---

## **How the Three Function Types Work Together**

This is one of the most useful patterns for your Python journey.

Imagine an employee salary-processing system.

Step 1 — Validation

```python
def is_valid_salary(salary):
    return salary > 0
```

Step 2 — Transformation
```python
def increase_salary(salary, percentage):
    return salary + (salary * percentage / 100)
```

Step 3 — Orchestration

```python
def process_salary(salary, percentage):
    if is_valid_salary(salary):
        return increase_salary(salary, percentage)

    return "Invalid Salary"
```

Overall flow
                  process_salary()
                         │
                         ▼
                is_valid_salary()
                         │
                 ┌───────┴───────┐
                 │               │
               VALID           INVALID
                 │               │
                 ▼               ▼
        increase_salary()   "Invalid Salary"
                 │
                 ▼
           Processed Salary

This separation makes the program easier to understand and maintain.

---

## **Real-World Data Processing Example**

Suppose you receive this raw employee data:

```python
employees = [
    {"name": "  Mayowa  ", "salary": 300000},
    {"name": " John ", "salary": 450000},
    {"name": " Ada ", "salary": -50000}
]
```

We can create separate functions.

Transformation
```python
def clean_name(name):
    return name.strip().title()
Validation
def is_valid_salary(salary):
    return salary > 0
Transformation
def increase_salary(salary, percentage):
    return salary + (salary * percentage / 100)
```

Orchestrator
```python
def process_employee(employee):
    name = clean_name(employee["name"])
    salary = employee["salary"]

    if not is_valid_salary(salary):
        return None

    new_salary = increase_salary(salary, 10)

    return {
        "name": name,
        "salary": new_salary
    }
```

Now:

```python
for employee in employees:
    result = process_employee(employee)

    if result:
        print(result)
```

Output:

{'name': 'Mayowa', 'salary': 330000.0}
{'name': 'John', 'salary': 495000.0}

Ada is excluded because the salary is invalid.

Notice the architecture
RAW EMPLOYEE DATA
       ↓
clean_name()
       ↓
is_valid_salary()
       ↓
increase_salary()
       ↓
process_employee()
       ↓
PROCESSED EMPLOYEE DATA

This is very similar to the kind of logic you will eventually use when processing real datasets.

---

## **Function Styling Guide**

Good function style makes your code easier to read and maintain.

* Use Descriptive Names

Bad:

def f(x):
    ...

Better:

def calculate_salary(salary):
    ...

The function name should tell the reader what the function does.

---

* Use snake_case

Python convention recommends lowercase words separated by underscores for function names.

Good:

calculate_salary()
validate_customer()
clean_email()
process_sales()

Avoid:

CalculateSalary()
calculateSalary()
CALCULATESALARY()

---

* Keep Functions Focused

Good:

```python
def validate_salary(salary):
    return salary > 0
```

Good:

```python
def increase_salary(salary, percentage):
    return salary + (salary * percentage / 100)
```

Avoid creating one huge function:

```python
def process_everything():
    # clean customer
    # validate customer
    # calculate salary
    # calculate tax
    # generate report
    # send email
    # update database
```

Break large processes into smaller functions.

---

* Use return for Reusable Results

Prefer:

```python
def calculate_total(price, quantity):
    return price * quantity
```
Then:

```python
total = calculate_total(1000, 5)
```
over:
```python
def calculate_total(price, quantity):
    print(price * quantity)

return allows the calling code to decide what to do with the result.
```
---

* Keep Parameters Meaningful

Good:

```python
def increase_salary(salary, percentage):
    ...
```

Less clear:

```python
def increase_salary(x, y):
    ...
```

Meaningful names improve readability.

---

* Avoid Too Many Parameters

This:

```python
def employee(name, department, salary, age, city, country, phone, email):
    ...
```


may indicate that the function needs a better design.

Consider passing a dictionary:
```python
def process_employee(employee):
    ...
```
---

* Use Docstrings

A docstring explains what a function does.

```python
def calculate_bonus(salary, percentage):
    """
    Calculate an employee's bonus based on salary
    and the specified percentage.
    """
    return salary * percentage / 100
```

Docstrings are supported by Python and are commonly used to document functions.

---

* Avoid Unnecessary Global Variables

Instead of:

```python
salary = 300000

def increase_salary():
    global salary
    salary += 10000
```

Prefer:

```python
def increase_salary(salary):
    return salary + 10000
```

Then:

```python
salary = increase_salary(salary)
```
This makes the function easier to test and reuse.

---

* Avoid Functions That Do Too Many Things

If a function is difficult to explain in one sentence, it may be doing too much.

Good:
```python
def clean_name(name):
    ...
```

Good:

```python
def validate_salary(salary):
    ...
```

Good:

```python
def calculate_bonus(salary):
    ...
```

Then combine them with an orchestrator.

---

* Good vs Poor Function Design
Poor Design

```python
def process_employee(name, salary):
    name = name.strip().upper()

    if salary > 0:
        bonus = salary * 10 / 100
        new_salary = salary + bonus
        print(name, new_salary)
    else:
        print("Invalid salary")
```

This function:

* Cleans data
* Validates data
* Transforms data
* Displays output

Everything is mixed together.

Better Design

```python
def clean_name(name):
    return name.strip().upper()


def is_valid_salary(salary):
    return salary > 0


def calculate_bonus(salary):
    return salary * 10 / 100


def process_employee(name, salary):
    name = clean_name(name)

    if not is_valid_salary(salary):
        return "Invalid salary"

    bonus = calculate_bonus(salary)

    return {
        "name": name,
        "salary": salary + bonus
    }
```
Now each function has a clear responsibility.

---

* **Common Mistakes**
Mistake 1 — Forgetting to Call the Function
def greet():
    print("Hello")

Nothing happens until:

greet()
Mistake 2 — Forgetting return

Incorrect:

def add(a, b):
    result = a + b

Correct:

def add(a, b):
    result = a + b
    return result
Mistake 3 — Confusing print() and return
def add(a, b):
    print(a + b)

This displays the value.

But:

def add(a, b):
    return a + b

returns the value so other code can use it.

Mistake 4 — Incorrect Argument Order

```python
def employee(name, department):
    ...
```

Then:

employee("IT", "Mayowa")

Python will assign:

name       → IT
department → Mayowa

The code may run, but the data is wrong.

Mistake 5 — Using global Unnecessarily

Avoid:

global salary

unless you genuinely need to modify the global variable.

Mistake 6 — Using *args and `**kwargs Without a Reason

Don't use:

```python
def calculate_salary(*args, **kwargs):
    ...
```

just because you can.

Use them when the function genuinely needs flexible numbers of positional or keyword arguments.

---

* **Function Design Checklist**

Before creating a function, ask:

1. What does this function do?

Example:

Validate salary
2. What input does it need?
salary
3. What should it return?
True / False
4. Does it have one clear responsibility?

If not, split it.

5. Should the values be parameters?

If the function needs external data, usually yes.

6. Should it return a value?

If another part of the program needs the result, usually yes.

7. Am I using global variables unnecessarily?

If yes, consider passing values as parameters.

8. Is the function name descriptive?

Prefer:

calculate_total_sales()

over:

process()
Do I really need *args or **kwargs?

Only use them when they solve a real problem.

* **Quick Reference**

Basic Function
```python
def greet():
    print("Hello")
```

Function with Parameter
```python
def greet(name):
    return f"Hello {name}"
```

Multiple Parameters

```python
def add(a, b):
    return a + b
```


Positional Arguments
add(10, 20)

Keyword Arguments
add(a=10, b=20)

Mixed Arguments
```python
def employee(name, department, salary):
    ...
```

```python
employee(
    "Mayowa",
    department="IT",
    salary=350000
)
```

Default Parameter
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"
```

*args
```python
def total(*numbers):
    return sum(numbers)
```

args → tuple

**kwargs
```python
def employee(**details):
    return details
```

kwargs → dictionary

Validation Function

```python
def is_valid_salary(salary):
    return salary > 0
```

Transformation Function
```python
def increase_salary(salary, percentage):
    return salary + (salary * percentage / 100)
```

Orchestrator Function
```python
def process_salary(salary, percentage):
    if is_valid_salary(salary):
        return increase_salary(salary, percentage)

    return "Invalid Salary"
```

---

**Key Takeaways

**The most important concepts to remember are:

Function

A reusable block of code that performs a specific task.

Parameter

A variable defined in a function definition.

Argument

The actual value passed to a function.

Local Variable

A variable created inside a function and normally available within that function's scope.

Global Variable

A variable defined outside functions at module/global scope.

Positional Argument

An argument matched according to its position.

Keyword Argument

An argument matched using the parameter name.

Default Parameter

A parameter with a value used when the caller doesn't provide one.

*args

Collects an arbitrary number of positional arguments into a tuple.

**kwargs

Collects an arbitrary number of keyword arguments into a dictionary.

Transformation Function

Changes data from one form to another.

Validation Function

Checks whether data satisfies a rule.

Orchestrator Function

Coordinates multiple functions to complete a larger process.



.

Return a new processed dataset

That is the point where your understanding of functions starts becoming practical Python programming for analytics, rather than just knowing Python syntax.
