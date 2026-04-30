## Topic: 🐍 Python Basics: print() Function and Variables
## Date: 30-04-2026

---
### **📌 Overview**

This project introduces two fundamental concepts in pyhon;
* The print() function(used for output)
* Variables (used for storing data)

---

🔷 **The print() Function**
✅ This project introduces two fundamental concepts in python:
* The print() function is used to display output the console.

---

### **Syntax**
```python
print(object(s), sep=' ', end='\n')
```

---

### Examples

```python
print("Hello, World!")
print(10)
print("The result is:", 5 + 3)
```

### **Common Parameters**
* sep → separates multiple values (default is space)
* end → what to print at the end (default is new line)

```python
print("A", "B", "C", sep="-")   # Output: A-B-C
print("Hello", end=" ")
print("World")                  # Output: Hello World
```

---

🔷 **Variables in python**

✅ What is a Variable?

A variable is a container used to store data values

### Syntax

```python
name = "Mayowa"
age = 25
price = 99.99
```
---

🔄 Dynamic Typing
Python automatically determines the data tupe:

```python
x = 10       # int
x = "Ten"    # now it's a string
```

---

🔷 **Using Variables with print()**
```python
name = "Mayowa"
age = 25

print("Name:", name)
print("Age:", age)
```

🧠 f-Strings (Recommended)

```python
print(f"My name is {name} and I am {age} years old.")
```

---

### **Best practices**
* use meaningful variables names (user_name instead of x)
* Avoid reserved keywords (print, if, class, etc.)
* Follow snake_case naming convention

---

### **Example Program**
```python
# simple program demonstrating variables and print()

name = "Mayowa"
score = 85

print("Student Name:", name)
print("Score:", score))
print(f"{name} scored {score} in the test".)
```

---

### **Practice Exercises**
🟢 Beginner
1. Print your name, age, and favorite color using print()
2. Create variables for:
  * Your name
  * Your country
  * Your hobby
Then print them in one sentence

### Solution
```python
name = "Mayowa"
country = "Nigeria"
hobby = "Football"

print(f"My name is {name}, I'm from {country}. I love {hobby}")
```






