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

---

### **Pass Statement**
`pass` does nothing.
It acts as a placeholder for code you plan to write later.

### **Example**
```python
for number in range(5):
    if number == 2:
        pass
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

Nothing special happens because `pass` simply tells Python:
"Do nothing here."

---

### **Real Life Example**
Planning future features.
```python
if True:
    pass
```
You can return later to add the actual code.

---

### **🎯 Else in Loops**

An `else` block runs when the loop finishes normally.
If the loop stops because of `break`, the `else` block does not execute.

---

### **Exaample Without Break**
```python
for number in range(3):
    print(number)
else:
  `  print("Loop completed")
```

### **Output**
```python
0
1
2
Loop completed
```

---

### **Example With Break**
```python
for number in range(5):
    if number == 2:
        break
    print(number)
else:
    print("Loop completed")
```

---

### **Output**
```python
0
1
```

The `else` block did not run because the loop ended with `break`.

---

### **Real Life Example**
Searching for a username.

```python
users = ['John', 'Mary', 'James']
search = "David"

for user in users:
    if user == search:
        print("user found")
        break
else:
    print(""User not found)
```

---

### **🔁 Nested Loops**
A nested loop is a loop inside another loop.

---

### **Syntax**
```python
for item1 in sequence:
    for item2 in sequence:
        #code
```

---

### **Example**
```python
for row in range(3):
    for column in range(2):
        print(row, column)
```
---

### **Output**

```python
0 0
0 1
1 0
1 1
2 0
2 1
```

---

### **Real Life Applications**
Seating Arrangement
Rows and seat:
```python
for row in range(1, 4):
    for sear in range(1, 4):
        print("Row", row, "seat", seat)
```

---

### **Printing Patterns**
```python
for i in range(4):
    for j in range(i + 1):
        print("*", end = "")
    print()
```

---

### **Output**
```python
*
**
***
****
```

---

### **🔁 While Loops**
A while loop repeats as long as a condition is True.

---

### **Syntax**
```python
while condition:
    # code
```

---

### **Example**
```
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

### **Output**
```python
1
2
3
4
5
```

---

### **How it works**
Python checks:
```python
count <= 5
```

If it is `True`, the loops run.
Eventually:
```python
count = 6
```

The condition becomes false, and the loop stops

---

### **🌐 Real Life Applications of While Loops**
ATM PIN Validation
```python
pin = ""
while pin != "1234":
    pin = input("Enter PIN: ")

print("Access Granted")
```

The user keeps trying until the correct pin is entered.

---

### **Download Progress**
```python
progress = 0
while progress < 100:
    print(progress, "%")
    progress += 20
```

---

### **While True **
While True creates an infinite loop.
it runs forever until a break statement stops it.

### **Example**
```python
while True:
    name = input("Enter your name: ")
    if name == "quit":
        break
print("Hello", name)
```

---

### **Example Seesion**
Enter your name: Mayowa
Hello Mayowa

Enter your name: John
Hello John

Enter your name: quit

The loop stops when the user types:
quit

---

### Real Life Applications
Game Menus
```python
while True:
    print("1. start")
    print("2. Exit")

    choice = input("Choose: ")

if choice == "2";
    break
```

---

### **Chat Applications**
Applications continuosly wait for user input until the user exists.

---

### **Choosing the right loop**

| Loop type | Best used when |
| --------- | -------------- |
| for loop | you know how many items you want to iterate through |
| while loop | You don't know how many times the loop should run |
| while True | The program should keep running until explicitly stopped |
| Nested loops | Working with combinations, tables, grids, or patterns |

---

### **Summary**
* `Loops` help to automate repetitive tasks
* `for loops` iterate through sequences
* `continue` skips the current iteration
* `break` stops the loop immediately
* `pass` is a placeholder that does nothing
* `else` runs if the loop finishes without break
* `Nested` loops are loops inside loops
* `while` loops run as long as a condition is True
* `while True` creates an infinite loop that usually relies on `break` to stop










