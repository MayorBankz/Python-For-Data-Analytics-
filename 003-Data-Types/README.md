# Topic: Data Types
## Date: 12-05-26

---

## Overview
Data types in python define the kind of a value a variable can store.
Python automatically detects the data type when you assign a value to a variable.

Understanding data types is important because they determine:
* What operations can be performed
* How data is stored
* How programs behave
---

1. **Numeric data type**
Used for storing numbers.
Integer (init)
Stores whole number

```python
age = 25
year = 2026

printy(type(age))
```
### Output
```python
<class 'int'>
```
---

### **Float** (float)

stored decimal numbers

```python
price = 99.99
temperature = 36.5

printy(type(price))
```

### Output
```python
<class 'float'>
```

---

### Complex (complex)

Stores complex number

```python
number - 3 + 5j

print(type(number))
```

### Output

```python
<class 'complex'>
```

---

2. **String Data Types**

Str
ing (str)
Stores text
```python
name = 'Mayowa'
Message = 'Welcome to Python'

print(type(name))
```

### Output
```python
<class 'str'>
```

---

### **Common String Operations**

```python
text = "Python"

print(text.upper())
print(text.lower())
print(len(text))
```

---

3. **Boolean Data type **
Boolean (bool)
stores only
* True
* False

```python
is_logged_in = True
is_admin = False

print(type(is_logged_in)
```

### Output

```python
<class 'bool'>
```

---

4. **Sequence Data Types**
Sequence types stores multiple values

List (list) 
Ordered and changeable collection

```python
fruits = {"apple", "banana", "orange"}

print(fruits)
print(type(fruits))
```

📌 **Features**
* Ordered
* Mutable (can be changed)
* Allows duplicates

### Example 
```python
fruits.append("mango")

print(fruits)
```

---

### Tuple (tuple)
Ordered but cannot be changed.
```python
coordinates = (10, 20)
print(type(coordinates))
```

📌 Features
* Ordered
* Immutable
* Faster than lists

---

### Range (range)
Generate a sequence of numbers
```python
numbers = range(5)
for i in numbers;
print(i)
```

### Output
```python
0
1
2
3
4
```
---

5. **Set Data Types**

Set(set)
Unordered collection of unique numbers
```python
numbers = {1, 2, 3, 4}
print(type(numbers))
```

📌 Features
* No duplicates
* Unordered
* Mutable

### Example
```python
numbers.add(5)
print(numbers)
```
---

**Frozen Set (frozenset)**

Immutable version of a set.

```python
data = frozenset([1, 2, 3])

print(type(data))
```

---

6. Dictionary Data Type
Dictionary (dict)

Stores data in key-value pairs.

```python
student = {
    "name": "Mayowa",
    "age": 25,
    "course": "Python"
}

print(type(student))
```
Accessing Values
```python
print(student["name"])
print(student["age"])
```

📌 Features
* Key-value structure
* Mutable
* Fast data lookup

---

7. **Binary Data Types**

Used for storing binary data.

Bytes (bytes)

```python
data = b"Hello"

print(type(data))
```

---

Bytearray (bytearray)
```python
data = bytearray(5)

print(type(data))
```

---

Memoryview (memoryview)

```python
data = memoryview(bytes(5))

print(type(data))
```

---

Checking Data Types

Use the type() function.

```python
name = "Python"

print(type(name))
```

---

Type Conversion in Python

Python allows conversion from one data type to another.

Convert Integer to Float
```python
num = 10

converted = float(num)

print(converted)
```

---

Convert Float to Integer
```python
price = 19.99

converted = int(price)

print(converted)
```

---
Convert num to string
```python
age = 25

converted = str(age)

print(converted)
```

---

### **Summary Table**
| Data Type | Example   | Description                  |
| --------- | --------- | ---------------------------- |
| int       | `10`      | Whole numbers                |
| float     | `10.5`    | Decimal numbers              |
| complex   | `2+3j`    | Complex numbers              |
| str       | `"Hello"` | Text                         |
| bool      | `True`    | True or False                |
| list      | `[1,2,3]` | Ordered mutable collection   |
| tuple     | `(1,2,3)` | Ordered immutable collection |
| set       | `{1,2,3}` | Unique unordered values      |
| dict      | `{"a":1}` | Key-value pairs              |
| bytes     | `b"Hi"`   | Binary data                  |

---

### **Top Use Cases of Python Data Types**
1. Storing User Information
```python
user = {
    "name": "Mayowa",
    "email": "mayowa@email.com"
}
```

---

2. **Performing Calculations**
```python
price = 1500
quantity = 3

total = price * quantity

print(total)
```
---

3. **Managing Collections of Data**
```python
students = ["John", "Mary", "David"]

for student in students:
    print(student)
```

---

### Best Practices
* Use meaningful variable names
* Choose the correct data type
* Use lists for changeable data
* Use tuples for fixed data
* Use dictionaries for structured information

---

### **CONCLUSION**
Python data types are the foundation of Python programming.
They help organize, store, and manipulate data efficiently.

