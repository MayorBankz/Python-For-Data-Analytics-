## Topic: Data Structure (Dictionaries)
## Date: 11-08-2026

---

## What is a Dictionary?
A dictionary stores information as:

KEY → VALUE

It uses curly brackets `{}`.

### Example:

```python
employee = { "name": "Mayowa", "department": "IT", "salary": 350000 }
```
Here:

Key     Value
name → Mayowa
department → IT
salary → 350000

---

### **Why Are Dictionaries Important?**
Dictionaries are one of the most important python data structures for data analytics and real-world programming.
They are useful because you can give meaningful names to your data.
Instead of:
employee = ["Mayowa", "IT", 350000]

you can write:
```python
  employee = { "name": "Mayowa",
                "department": "IT",  
                "salary": 350000 
              }
```
The second version is much easier to understand.

---

### **Accessing Dictionary Values**
Use the key.

```python
employee = { "name": "Mayowa", 
              "department": "IT", 
              "salary": 350000 
              }
print(employee["name"])
```

# Output: Mayowa

---

You can also access:

print(employee["department"])
print(employee["salary"])

---

### Adding a New Dictionary Item
Simply assign a new key.

```python
employee["location"] = "Lagos"
```

The dictionary contains :
name
department
salary 
location

---

### **Updating a Dictionary Value**
Suppose the employee receives a salary increase.

employee['salary'] = 400000

The old value:
350000 becomes 400000

---

### **Removing a dictionary Item**
You can use del:

del employee["location"]

or 

Or .pop():

employee.pop("location")

---

### **Checking whether a Key Exists**
You can use in.

```python
if "salary" in employee:
    print("Salary information exists")
```

This is useful when working with incomplete datasets.

---

### **Dictionary Methods**
Some important dictionary methods are 
* keys()
* values()
* items()
* get()
* pop()
* update()

---

### **Keys()**
Returns all keys.

```python
employee.keys()
```

Example result:

dict_keys(['name', 'department', 'salary'])

---

### **Values()**
Returns all values

employee.values()

---

### **items()**
Returns key-value pairs.
employee.items()

You will frequently use .items() with loops.

```python
for key, value in employee.items():
    print(key, value)
```

### Output
name Mayowa 
department IT 
salary 350000

---

### **Using .get()**
Instead of:
```python
print(employee["age"])
```

which produces an error if "age" doesn't exist, you can use:

```python
print(employee.get("age"))
```
Output:

None

You can also provide a default value:

```python
print(employee.get("age", 0))
```
Output:
0

📌 This is very useful when dealing with real-world datasets where some information may be missing.

### **Dictionaries in Business Data**

Suppose a company has employees:

```python
employees = [
    {
        "name": "Mayowa",
        "department": "IT",
        "salary": 350000
    },
    {
        "name": "Ada",
        "department": "Finance",
        "salary": 420000
    },
    {
        "name": "John",
        "department": "Sales",
        "salary": 280000
    }
]
```

This is a list of dictionaries.

This structure is extremely common in Python.

Each dictionary represents one employee.

The list represents all employees.

---

### **Looping Through a List of Dictionaries**
```python
for employee in employees:
    print(employee["name"])
```
Output:

Mayowa
Ada
John

You can also access salary:

```python
for employee in employees:
    print(employee["name"], employee["salary"])
```

---

### **Filtering Dictionary Data**
Suppose the business wants employees earning ₦350,000 or more.

```python
high_earners = [
    employee
    for employee in employees
    if employee["salary"] >= 350000
]
```
This produces:


[
    {"name": "Mayowa", "department": "IT", "salary": 350000},
    {"name": "Ada", "department": "Finance", "salary": 420000}
]

This type of operation is very important in data analytics.

---

### **Dictionary Comprehension**

You can also create a dictionary using a comprehension.
```python
high_earners =
 {
    employee["name"]: employee["salary"]
    for employee in employees
    if employee["salary"] >= 350000
}
```
Result:

{
    "Mayowa": 350000,
    "Ada": 420000
}

This means:

Employee Name → Salary

---

### **Real-World Use Case: Product Prices**

Imagine a company has products:

```python
product_prices = {
    "Gold Label": 25000,
    "Smirnoff": 18000,
    "McDowell's": 15000
}
```
You can easily find a price:

print(product_prices["Gold Label"])

Output:

25000

Update a price:
```python
product_prices["Gold Label"] = 27000
```
Add a new product:

```python
product_prices["Another Product"] = 12000
```
This is much easier than searching through a list.
---

### **Real-World Use Case: Sales Data**

A sales transaction can be represented as:
```python
sale = {
    "customer": "Mayowa",
    "product": "Gold Label",
    "quantity": 10,
    "price": 25000
}

```


You can calculate the total:

```python
total = sale["quantity"] * sale["price"]

print(total)
```
Output:

250000

---

### **Real-World Use Case: Configuration**
Dictionaries are also useful for storing settings.

```python
company_settings = {
    "company_name": "ABC Limited",
    "currency": "NGN",
    "tax_rate": 0.1,
    "country": "Nigeria"
}
```


The program can retrieve these values whenever needed.


---

### **Real-World Use Case: API/JSON Data**

When working with APIs, you will frequently encounter data that looks like dictionaries.

Example:
```python
customer = {

    "id": 101,
    "name": "Mayowa",
    "email": "mayowa@example.com",
    "active": True
}
```

You can access:

customer["name"]
customer["email"]
customer["active"]

This is one reason dictionaries are extremely important for data analytics and data engineering.
