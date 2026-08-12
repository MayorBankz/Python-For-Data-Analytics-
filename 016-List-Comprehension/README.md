## Topic: List Comprehension
## Date: 12-08-2026

---

### What is Pyhton List Comprehension?

List comprehension is a simple and powerful way to create a new list from an existing iterable such as a list, tuple, string, or range().

It allows you to perform operations such as:
* Creating new lists
* Transforming data
* Filtering data
* Applying conditions
* Cleaning data
* Extracting values from lists of dictionaries

Python's official documentation describes list comprehensions as a conscise way to create lists.

---

1. **Why Learn List Comprehenion?**
   Consider this normal for loop.

 ```python
   numbers = [1, 2, 3, 4, 5]

squared_numbers = []

for number in numbers:
    squared_numbers.append(number ** 2)

print(squared_numbers)
```

---

### Output
[1, 4, 9, 16, 25]

The same operation can be written using list comprehension:

```python
numbers = [1, 2, 3, 4, 5]

squared_numbers = [number ** 2 for number in numbers]

print(squared_numbers)
```

### Output

[1, 4, 9, 16, 25]


The second operation is shorter and expresses the operation in one line.

---

2. **Basic Syntax**
   The basic structure is:

```python
[expression for item in iterable]
```

For example

```python
numbers = [1, 2, 3, 4, 5]

new_numbers = [number * 2 for number in numbers]
```

Think of it as:
  For every number in numbers, multiply the number by 2 and put the result into a new list.

### Breaking it down

```python
[number * 2 for number in numbers]
```

| **Part** | **Meaning** |
| -------- | ----------- |
| `number * 2` | What should be added to the new list |
| `for` | Start the iteration |
| `number` | current item |
| `in` | Look inside |
| `numbers` | The existing iterable |

---

3. Simple Example

```python
names = ["Mayowa", "Ada", "John", "Mary"]

uppercase_names = [name.upper() for name in names]

print(uppercase_names)
```

---

Output

['MAYOWA', 'ADA', 'JOHN', 'MARY']

The list comprehension goes through every name and applies `.upper()`. 

---

4. **List Comprehension vs For Loop**
Traditional for `loop`

```python
numbers = [1, 2, 3, 4, 5]

doubled = []

for number in numbers:
    doubled.append(number * 2)

print(doubled)
```

### List Comprehension
```python
numbers = [1, 2, 3, 4, 5]

doubled = [number * 2 for number in numbers]

print(doubled)
```

Both produce:

[2, 4, 6, 8, 10]

---

### **General Rule**
if your loop simply.
* Goes through a collection
* Performs an operation
* Adds the result to a new list
then list comprehension is often a good choice.

---

5. Filtering With List Comprehension

One of the most useful features of list comprehension is filtering.

The syntax is:

```python
[expression for item in iterable if condition]
```

Example:

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)
```

### Output

[2, 4, 6]

Read it as:
"Give me number for every number in numbers if the number is divisible by 2."

---

6. **Filtering Salaries**

This is particularly useful for data analysis.

```python
salaries = [200000, 300000, 450000, 180000, 500000]

high_salaries = [salary for salary in salaries if salary >= 300000]

print(high_salaries)
```

### Output
[300000, 450000, 500000]

The condition:

```python
if salary >= 300000
```

determines which values enter the new list.

---

7. **Transforming and filtering at the same time**

You can transform values after filtering them.

For example.

```python
salaries = [200000, 300000, 450000, 180000, 500000]

increased_salaries = [
    salary * 1.10
    for salary in salaries
    if salary >= 300000
]

print(increased_salaries)
```


### Output 
[330000.00000000006, 495000.00000000006, 550000.0]

📌 The logic is:
* look at every salary
* Keep only salaries >= 300000
* Increase those salaries by 10%
* Print the results into a new list.

---

### **Important: Expression vs Condition**
This is one of the most important things to understand.
Consider:
```python
[x * 2 for x in numbers if x > 5]
```

There are two different parts:

```python
x * 2
```

This is the expression.
It determines what goes into the list.

And.

```python
if x > 5
```

This is the condition.
It determines which items are allowed into the new list.

Think of it like this.

[WHAT TO RETURN   FOR EACH ITEM   IF CONDITION IS TRUE]

Example:

```python
[x ** 2 for x in numbers if x % 2 == 0]
```

Means:
"Square every number that is even."

---

9. **Working with strings**

List comprehension also work with strings 
```python
name = "Mayowa"

letters = [letter for letter in name]

print(letters)
```

### Output 
['M', 'a', 'y', 'o', 'w', 'a']

You can also filter characters.

```python
name = "Mayowa"

vowels = [letter for letter in name if letter.lower() in "aeiou"]

print(vowels)
```

### Output
['a', 'o', 'a']

---

10. Cleaning Data
List comprehension can be useful when cleaning simple datasets.

For example:

```python
names = [" Mayowa ", " Ada ", " John ", " Mary "]

clean_names = [name.strip() for name in names]

print(clean_names)
```

### Output
['MAYOWA', 'ADA', 'JOHN', 'MARY']

---

11. **Working with list of dictionaries**
This is extremely important for data analysis.

Suppose we have employee data.

```python
employees = [
    {"name": "Mayowa", "department": "IT", "salary": 350000},
    {"name": "Ada", "department": "Finance", "salary": 420000},
    {"name": "John", "department": "Sales", "salary": 280000},
    {"name": "Mary", "department": "HR", "salary": 310000},
    {"name": "Peter", "department": "IT", "salary": 390000}
]
```

Get employee names.

```python
names = [employee["name"] for employee in employees]

print(names)
```

### Output 
['Mayowa', 'Ada', 'John', 'Mary', 'Peter']

---

12. **Filter Employees by department**
Suppose we only want IT employees.

```python
it_names = [
    employee["name"]
    for employee in employees
    if employee["department"] == "IT"
]

print(it_names)
```

### Output 
['Mayowa', 'Peter']

Read it as:
  "Give me the employee's name for every employee whose department is IT".

---

13. **Filter Employees by Salary**

```python
high_earners = [
    employee["name"]
    for employee in employees
    if employee["salary"] >= 350000
]

print(high_earners)
```

### Output
['Mayowa', 'Ada', 'Peter']

---

14. **Extract Speific Values**
You can extract only salaries:

```python
salaries = [employee["salary"] for employee in employees]

print(salaries)
```

### Output

[350000, 420000, 280000, 310000, 390000]

You can also extract only IT salaries:

```python
it_salaries = [
    employee["salary"]
    for employee in employees
    if employee["department"] == "IT"
]

print(it_salaries)
```

### Output
[350000, 390000]

---

15. **Conditional Expression inside List Comprehension**
There is another form where if and else are used.

Syntax:

```python
[expression_if_true if condition else expression_if_false for item in iterable]
```

Example:

```python
numbers = [1, 2, 3, 4, 5]

result = ["Even" if number % 2 == 0 else "Odd" for number in numbers]

print(result)
```

Output 

['Odd', 'Even', 'Odd', 'Even', 'Odd']

📁 Important Difference 

These two structures are different:

Filtering
```python
[x for x in numbers if x > 5]
```

This removes item that don't satisfy the condition

### **If/else transformation**

```python
["High" if x > 5 else "Low" for x in numbers]
```

This keeps every item, but changes what gets returned.

---

16. **Example With Employee Salaries**
```python
employees = [
    {"name": "Mayowa", "salary": 350000},
    {"name": "Ada", "salary": 420000},
    {"name": "John", "salary": 280000},
    {"name": "Mary", "salary": 310000}
]

salary_status = [
    "High" if employee["salary"] >= 350000 else "Low"
    for employee in employees
]

print(salary_status)
```

Output
['High', 'High', 'Low', 'Low']

---

17. **Using range()**
List comprehension works very well with range().

```python
numbers = [number for number in range(1, 6)]

print(numbers)
```

Output
[1, 2, 3, 4, 5]

You can also generate squares.

```python
squares = [number ** 2 for number in range(1, 6)]

print(squares)
```

Output:
[1, 4, 9, 16, 25]

---

18. **Even Numbers From a Range**

```python
even_numbers = [
    number
    for number in range(1, 21)
    if number % 2 == 0
]

print(even_numbers)
```

Output 
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

---

19. **Multiple Conditions**
You can use multiple conditions.

```python
numbers = range(1, 21)

result = [
    number
    for number in numbers
    if number > 5 and number < 15
]

print(result)
```

Output:
[6, 7, 8, 9, 10, 11, 12, 13, 14]

Another example:
```python
numbers = range(1, 21)

result = [
    number
    for number in numbers
    if number % 2 == 0 and number > 10
]

print(result)
```

Output:
[12, 14, 16, 18, 20]

---

20. **Nested List Comprehension**

List comprehensions can contain multiple `for` clauses. Python's documentation also demonstrates nested list comprehensions for working with nested data structures.

### Example

```python
numbers = [[1, 2], [3, 4], [5, 6]]

flattened = [
    number
    for row in numbers
    for number in row
]

print(flattened)
```

### Output: 
[1, 2, 3, 4, 5, 6]

This can be difficult to understand initially.

The equivalent normal loop is:

```python
flattened = []

for row in numbers:
    for number in row:
        flattened.append(number)
```

so:
```pyhthon
[number for row in numbers for number in row]
```

means:
For every row, go through every number inside that row.

---

21. **Nested List Comprehension Example**
    
Imagine sales data:

```python
sales = [
    [100, 200, 300],
    [400, 500, 600],
    [700, 800, 900]
]
```

Flatten it:

```python
all_sales = [
    amount
    for row in sales
    for amount in row
]

print(all_sales)
```

Output:
[100, 200, 300, 400, 500, 600, 700, 800, 900]

--- 

22. **List Comprehension With zip()**
    
You can combine list comprehension with zip().

```python
names = ["Mayowa", "Ada", "John", "Mary"]
salaries = [350000, 420000, 280000, 310000]

employee_salaries = [
    (name, salary)
    for name, salary in zip(names, salaries)
]

print(employee_salaries)
```
### Output 
[
    ('Mayowa', 350000),
    ('Ada', 420000),
    ('John', 280000),
    ('Mary', 310000)
]

This is useful when working with columns of data.

---

23. **Common Data Analysis Pattern**
    
A very common pattern is:

```python
[transformation for item in data if condition]
```

For example:
```python
salaries = [200000, 300000, 450000, 180000, 500000]

result = [
    salary * 1.10
    for salary in salaries
    if salary >= 300000
]
```

Think of it as:

            TRANSFORM
                ↓
[ salary * 1.10
  for salary in salaries
  if salary >= 300000 ]
                 ↑
              FILTER

This pattern is extremely useful when manipulating data.

---

24. **Common Mistake #1 - Forgetting the Expression**
    
Incorrect:

```python
numbers = [1, 2, 3, 4]

result = [for number in numbers]

```

This produces a syntax error.

correct:
```python
result = [number for number in numbers]
```

You need to specify what should be specify into the new list.

---

25. **Common Mistake #2 - Putting `if` in the wrong position **
    
For filtering, this is correct:

```python
[x for x in numbers if x > 5]
```

Not:

```python
[x if x > 5 for x in numbers]
```

The second form is invalide because the `if` is being used as a filter but is placed where a conditional expression belongs.

---

26. **Common Mistake #3 - Confusing Filtering With If/Else**
    
Filtering

```python
[x for x in numbers if x > 5]
```

Output might be:
[6, 7, 8, 9, 10]

Items that don't satisfy the condition disappear.

### If/else
```python
["High" if x > 5 else "Low" for x in numbers]
```

Every item gets a result.

For example:
['Low', 'Low', 'Low', 'Low', 'Low', 'High', 'High', ...]

---

27. **When Should I use List Comprehension**
    
Use list comprehension when the operation is simple and readable
Good example:
```python
squares = [x ** 2 for x in numbers]
```

Good example:

```python
even_numbers = [x for x in numbers if x % 2 == 0]
```

Good example:
```python
names = [employee["name"] for employee in employees]
```

---

28. **When Should You Not Use It?**
    
Don't force everything into one line.
For example, this can become so difficult to understand.

```python
result = [
    x * 2 if x > 10 else x + 5
    for x in numbers
    if x % 2 == 0 and x > 3
]
```

Although valid python, a normal for loop maybe easier for another developer to understand.
Python's documentation and common Python guidance favor readability; nested or overly complex comprehensions can become difficult to follow.

### Better:
```python
result = []

for x in numbers:
    if x % 2 == 0 and x > 3:
        if x > 10:
            result.append(x * 2)
        else:
            result.append(x + 5)
```

Rule:
If the list comprehension becomes difficult to read, use a normal for loop.

---

29. **List Comprehension Clean Sheet**
    
Create a new list
```python
[x for x in numbers]
```

### Transform values
```python
[x * 2 for x in numbers]
```

### Square Values
```python
[x ** 2 for x in numbers]
```

### Filter values
```python
[x for x in numbers if x > 10]
```

### Filter even numbers
```python
[x for x in numbers if x % 2 == 0]
```

### Convert strings to uppercase
```python
[x.upper() for x in names]
```

### Strip Whitespace
```python
[x.strip() for x in names]
```

### Extract dicitonary values
```python
[x.strip() for x in names]
```
### Filter dictionaries
```python
[
    employee["name"]
    for employee in employees
    if employee["department"] == "IT"
]
```

### If/else

```python
["Pass" if score >= 50 else "Fail" for score in scores]
```

### Nested comprehension
```python
["Pass" if score >= 50 else "Fail" for score in scores]
```

---

30. **The Three Patterns You Should Memorize**
    
If you're learning Python for data analytics, focus heavily on these three patterns.

### Pattern 1 — Transformation
```python
[expression for item in data]
```

Example:
```python
[x * 2 for x in numbers]
```

Meaning:
Transform every item.

---

### Pattern 2 - Filtering
```python
[item for item in data if condition]
```

Example:
```python
[x for x in numbers if x > 100]
```

Meaning: 
  Keep only items that meet the condition.

---

### Pattern 3 - Filter + Transformation
```python
[expression for item in data if condition]
```

Example

```python
[x * 1.10 for x in salaries if x >= 300000]
```

Meaning:
  Find items that meet the condition, then transform them.
This third pattern is particularly useful in data analysis.

---

31. **Real-World Data Analysis Example**
    
Suppose you have employee records.

```python
employees = [
    {"name": "Mayowa", "department": "IT", "salary": 350000},
    {"name": "Ada", "department": "Finance", "salary": 420000},
    {"name": "John", "department": "Sales", "salary": 280000},
    {"name": "Mary", "department": "HR", "salary": 310000},
    {"name": "Peter", "department": "IT", "salary": 390000}
]
```

Requirement
  Find the names of IT employee at least #350,000

Solution

```python
result = [
            employee["name"]
            for employee in employees
            if employee["department"] == "IT" 
            and employee["salary"] > 350000
            ]
```

Output:
['Mayowa', 'Peter']

Notice how the comprehension combines:
* Dictionary access
* Filtering
* Multiple conditions
* Creating a new list

This is the type of pattern you will frequently encounter when working with structured data.

---

32. **List Comprehension vs map() and filter()**
    
List comprehensions can often replace simple uses of map() and filter().

For example:

```python
numbers = [1, 2, 3, 4, 5]
```
using map():
```python
result = list(map(lambda x: x * 2, numbers))
```

Using list comprehension:
```python
result = [x * 2 for x in numbers]
```

The list comprehension is often easier for beginners to read.

Similarly, filtering
```python
result = list(filter(lambda x: x > 2, numbers))
```

can be written as:

```python
result = [x for x in numbers if x > 2]
```

---

### **Key Takeaways**
Remember these points:
1. List comprehension creates a new list.
2. It usually works with an existing iterable
3. The basic syntax is:

```python
[expression for item in iterable]
```

4. You can filter with:
```python
[expression for item in iterable if condition]
```

5. You can use if/else to transform values
```python
[value_if_true if condition else value_if_false for item in iterable]
```

6. List comprehensions are especially useful for:
  * Data cleaning
  * Filtering
  * Transformation
  * Extracting values
  * Working with list of dictionaries
  * Preparing data for analysis
7. Don't sacrifice readability just to make code shorter.
