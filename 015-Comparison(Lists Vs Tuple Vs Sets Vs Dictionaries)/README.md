## Topic: Comparison(List Vs Tuples Vs Sets Vs Duplicates)
## Date: 11-08-2026

---

### **Quick Comparison**
Python's four major built-in collection data structures can be compared like this:

| **Data Structure** | **Example** | **Ordered?** | **Changeable?** | **Duplicates?** | **Main Purpose** |
| ------------------ | ----------- | ------------- | -------------- | ---------------- | --------------- |
| **List** | ["Sales", "IT"] | ✅ Yes | ✅ Yes | ✅ Yes | General collection of items |
| **Set** | {"IT", "Sales"} | ❌ No indexing | ✅ Yes | ❌ No | Unique values and comparisons |
| **Tuple** | ("IT", "Sales") | ✅ Yes | ❌ No | ✅ Yes | Fixed/unchanging data |
| **Dictionary** | {"dept": "IT", "salary": 350000} | ✅ Yes* | ✅ Yes | Keys ❌ | Key-value data |

📌 Dictionaries preserve insertion order in modern python

---

## **Real-World Business Example**
Imagine a company has five customers:

```python
customers = ["Mayowa", "Ada", "John", "Ada", "Mayowa"]
```

### **If the business wants to preserve every transaction/customer occurence**

use a **list**.

```python
customers = ["Mayowa", "Ada", "John", "Ada", "Mayowa"]
```

Duplicates are allowed.

---

### **If the business wants only unique customers**
use a **set**.

```python
unique_customers = set(customers)
```

Result:
{"Mayowa", "Ada", "John"}

---

### **If the business has fixed information about one customer**

A **tuple** can work

```python
customer = ("Mayowa", "Nigeria", "Active")
```

---

### **If the business wants descriptive customer information **
 A **dictionary** is better.

```python
 customer = { "name": "Mayowa",
             "country": "Nigeria", 
             "status": "Active" 
             }
```

---

### **List of Dictionaries - Very Important**
In real-world Python applications and data analytics, you will frequently combine lists and dictionaries..

For example:

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

Here:

LIST
├── Dictionary → Employee 1
│
├── Dictionary → Employee 2
│
└── Dictionary → Employee 3

This structure is extremely common when working with:
* JSON
* APIs
* Business data
* Data analytics
* Data engineering
* Web applications

---

### **Choosing the Right Data Structure**
When solving a problem, ask yourself the following questions
Question 1

Do I need an ordered collection that I can modify?

Use a:
list

Example:

```python
products = ["Product A", "Product B", "Product C"]
```

---

### Question 2
Do I need only unique values?

Use a:

set

Example:

```python
unique_products = {"Product A", "Product B", "Product C"}
```

---

### Question 3
Do I need ordered data that should not change?

Use a:

tuple

Example:

coordinates = (6.5244, 3.3792)

---


### **Question 4**
Do I need to connect names/keys to values?

Use a:

dictionary

Example:

Example:

```python
employee = { 
            "name": "Mayowa", 
            "salary": 350000
}
```

---


### **Easy way to remember**
Think of the four structures this way:

LIST = COLLECTION

"Give me a collection of items."

["Apple", "Orange", "Mango"]

---

SET = UNIQUE

"Give me the unique items."

{"Apple", "Orange", "Mango"}

---

TUPLE = FIXED

"Give me a collection that should not change."

("Apple", "Orange", "Mango")

---

DICTIONARY = INFORMATION

"Give me information with labels."

```python
{
 "name": "Mayowa",
"age": 25,
"department": "IT"
}

```



