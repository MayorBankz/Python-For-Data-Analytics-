## Topic: Python Loops Documentation
## Date: 17-06-26

---

## Table of Contents
---

* What are Loops?
* Real-Life applications of For Loops
* Continue Statement
* break statement
* else in Loops
* Nested Loops
* While Loops
* While True
* Choosing the right loop
* Summary

---

### What are Loops?
Loops allow a program to repeat a block of code multiple times without writing the same code repeatedly.
Imagine telling someone:
  "Print 'Hello' 100 times."

Instead of writing:
```python
print("Hello")
print("Hello")
print("Hello")
...
```
📍 You can use a loop

---

💠 **For Loops**
A for loop is used to iterate over a sequence such as:
* Lists
* Strings
* Tuples
* Dictionaries
* Ranges

---

### **Syntax**
```python
for variable in sequence:
   # code to execute
```

---

### **Example 1: Loop through a list**
```python
fruits = ['Apple', 'Banana', 'Orange']

for fruit in fruits:
    print(fruit)
```

---

### **Output**
```python
Apple
Banana
Orange
```

---

📍 **How it works**
Python takes each item from the list one at a time:

| **Iteration** | **fruit** |
| -------- | -------- |
| 1 | Apple |
| 2 | Banana |
| 3 | Orange |

---

### **Example 2: Using `range()`**
```python
for number in range(5):
   print(number)
```

---

### **Output**
```python
0
1
2
3
4
```

---

`range(5)` means:
   Start from 0 and stop before 5.

---

### **Example 3: Multiplication Table**
```python
for i in range(1, 11):
   print("7 x", i, =, 7 * i)
```

---

### **Output**

```python
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

---

🌐 **Real-Life Applications of For Loops**
1. Sending Emails

```python
customers = ['John', 'Maria', 'Mayowa', 'Idowu']

for customer in customers:
    print("Sending email to", customer)
```

---

### **Real Life**
A company can automatically send newsletters to thousands of customers.

---

2. Grading Students
```python

scores = [80, 65, 92, 74]

for score in scores:
    print("score:", score)
```

---

### **Real Life**
Teachers can process student results automatically

---

3. Checking Files

```python
files = ['report.pdf', 'data.xlsx', 'image.png']

for file in files:
    print("Scanning", file)
```

### **Real Life **
Antivirus software scans files one by one.

---

4. Online Shopping
```python
cart = [2000, 3500, 1500]

total = 0

for price in cart:
  total += price

print(total)
```

---

### **Real Life**
E-commerce websites calculate the total cost of items in your cart.

---

### **⏭️ Continue Statement**
The continue statement skips the current iteration and moves to the next one.

### Example
```python
for number in range(1, 6):
    if number == 3:
        continue
print(number)
```
---

### **Output**
```python
1
2
4
5
```

---

### **What Happened?**
When python reaches `3`:

```python
continue
```
It skips printing `3`.

---

### **Real Life Example**
Skipping absent student during attendance

```python

students = ['Mayowa', 'Michael', 'Olamide', 'Absent', 'Praise']

for student in students:
    if student == 'Absent':
        continue
    print("Present:", student)
```

---

### Output
```python
Present: Mayowa
Present: Michael
Present: Olamide
Present: praise
```

---

### **🔴 Break Statement**
break immediately stops the loop.

---

### **Example**
```python
for number in range(1, 6)
    if number == 4:
        break
    print(number)
```

---

### **Output**
```python
1
2
3
```

---

📍 The loop stops completely when it reaches 4

---

### **Real Life Example**
Stopping a search once an item is found.

```python
products = ["phone", "Laptop", "Headset"]

for product in products:
    if product == "Laptop":
        print("Product found!)
        break
```

---

### **Output**
```python
Product found!
```












