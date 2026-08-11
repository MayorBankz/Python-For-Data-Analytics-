## Topic: Data Structure (Tuples)
## Date: 11-08-2026

---

### **What is a Tuple?**
A tuple is an ordered collection of values that cannot be changed after creation.
Tuples use parentheses:

```python
employee = ("Mayowa", "IT", 350000)

print(employee)
```

### Result 
("Mayowa", "IT", 350000)

The three values are:
Mayowa
IT 
350000

---

### Why Use a Tuple?
The main reason to use a tuple is when the data should remain fixed.

For example:

coordinates = (6.5244, 3.3792)

These coordinates represent a location.
You probably don't want other parts of your program accidentally changing them.

Another example:
date_of_birth = (15, 5, 2000)

---

## **Tuple indexing**

Tuples are ordered, so you can access values using indexes.

```python
employee = ("Mayowa", "IT", 350000)

print(employee[0])
print(employee[1])
print(employee[2])
```

### Output
Mayowa
IT
350000

📍 Remember that python starts counting from 0.

| **Index** | **Value** |
| --------- | --------- |
| 0 | Mayowa |
| 1 | IT |
| 2 | 350000 |

---

### **Tuple cannot be changed**
Consider: 

```python
employee = ("Mayowa", "IT", 350000)
`
employee[2] = 400000
```

This will not work because tuples are immutable.

Immutable means once contents is created, they cannot be changed.

---

## 🌐**Real-World Tuple Application**
Example 1 - **Coordinates**
lagos_location = (6.5244, 3.3792)

latitude and longitude are naturally represented as a pair.

---

Example 2: Product Information
product = ("SKU001", "Gold Label", 25000)

The tuple contains:
Product ID
Product name
Price

---

Example 3: Employee Information
employee = ("Mayowa", "IT", 350000)

This could represent:

Name
department
Salary

📌 However, for employee records where you frequently access fields by name, a dictionary is usually better.

---

### **Tuple Unpacking**
One very useful feature of tuple is unpacking.

```python
employee = ("Mayowa", "IT", 350000)

name, department, salary = employee

print(name)
print(department)
print(salary)
```

### Output
Mayowa
IT
350000

This is extremely useful when working with data.

---

## Tuple and Functions
Functions can return multiple values using a tuple

```python
def calculate_salary(salary):
    tax = salary * 0.1
    net_salary = salary - tax

    return salary, tax, net_salary

# Then:
salary, tax, net_salary = calculate_salary(350000)

print(salary)
print(tax)
print(net_salary)
```

The function effectively returns: (350000, 35000, 315000)

---

### **Tuple Characteristics**
Remember:

TUPLE
|
├── Ordered
├── Immutable
├── Allows duplicates
├── Supports indexing
├── Supports unpacking
└── Useful for fixed data

🤔 Think: Tuple = data that should stay together and should not change.



