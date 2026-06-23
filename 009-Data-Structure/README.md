## TOPIC: Python Data Structure (Lists) 
## DATE: 23-06-26

---

### What is a Data Structure?

A data structure is a way of organizing and storing data so it can be used efficiently.

Think of it like:
* A shopping basket stores groceries
* A folder stores document
* A list stores multiple values in python

---

### Example:
```python
fruits = ["Apple", "Banana", "Orange"]
```
---

Here, fruits stores multiple items in one variable.

---

### Built-in Data Structures in Python
Python provides four major built-in data structures:

---

| **Data Structure** | **Symbol** | **Ordered?** | **Changeable** |
| ------------------ | ---------- | ------------ | -------------- |
| List | [] | Yes | Yes |
| Tuple | () | Yes | No |
| Set | {} | No | Yes |
| Dictionary | {} | Yes | Yes |

---

### Example:
```python
# List
fruits = ["Apple", "Banana"]

# Tuple
coordinates = (10, 20)

# Set
colors = ("Red", "blue")

# Dictionary
student = {
          "name": "John",
          "age": 25
            }
```

For this guide, we'll focus mainly on lists

---

### What is a List?
A list is a collection of items stroed in a single variable.

### Example:
```python
fruits = ["Apple", "Banana", "orange"]
```

The list contains 3 items.

---

### **How to create lists**
**Empty Lists**
```python
fruits = []
```

--- 

### Output
```python
[]
```

---

### **List with values**
```python
fruits = ["Apple", "Banana", "Orange"]
```

---

### **List with numbers**
```
source = [90, 85, 70, 100]
```

---

### **Mixed Data Types**
```python
data = ["John", 25, True]
```

---

### Output
```python
["John". 25, true]
```

---

python lists can store different data types together.

---

### **Nested Lists**

A nested list is a list inside another list.

### Example
```python
students = [
          ["John", 90],
          ["Mary", 85]
          ["Peter", 75]
]
```

---

### Visual Representation

---

```python
[
    ["John", 90],
    ["Mary", 85],
    ["Peter", 75]
]
```

---

### Accessing Items

---

```python
print(students[0])
```

---

### Output 
```python
['John', 90]
```

---

### **Accessing Individual values**
```python
print(students[0][0])
```

---

### Output
```python
John
```

---

### **Explanation**
* First[0] - selects first list
* second[0] - selects first item inside it

---

### **Reading and Accessing Lists**
Given:
```python
fruits = ["Apple", "Banana", "Orange"]
```

---

### **First Item**
```python
print(fruits[0])
```

---

### Output
```python
Apple
```

---

### **Second Item**
```python
print(fruits[1])
```

---

### **Output:**
```python
print(fruits[1])
```

---

### **Third Item**
```python
print(fruits[2])
```

---

### **Output**
```python
Orange
```

---

### **Understanding Indexing**
Python starts counting from 0
| **Item** | **Index** |
| -------- | --------- |
| Apple | 0 |
| Banana | 1 |
| Orange | 2 |

---

```python
fruits = ["Apple", "Banana", "Orange"]
```

---

### **Negative Indexing**
Python can count backwards.

| **Item** | **Negative Index** |
| -------- | ------------------ |
| Orange | -1 |
| Banana | -2 |
| Apple | -3 |

---

### Example
```python
print(fruits[-1])
```

---

### **Output**
```python
Orange
```

---

### **Slicing Lists**
Slicing allows you to get multiple items

### Syntax:
```python
list[start:stop]
```

---

### **Example**
```python
numbers = [10, 20, 30, 40, 50]
```

---

Get first three items

```python
print(numbers[0:3]
```
---


### Output
```python
[10, 20, 30]
```

---

Get from index 1 to 4:

```python
print(numbers[1:4])
```

---

### Output:
```python
[20, 30, 40]
```

---

Get everything
```python
print(numbers[:])
```

### Output
```python
print(numbers[:])
```

---

### Output
```python
[10, 20, 30, 40, 50]
```

---

Last 2 items
```python
[10, 20, 30, 40, 50]
```

---

### Output
```python
[40, 50]
```

---

### **Unpacking Lists**

Unpacking means assigning list items into separate variables.

---

### Example

```python
fruits = ["Apple", "Banana", "Orange"]

a, b, c = fruits

print(a)
print(b)
print(c)
```

---

### Output
```python
Apple
Banana
Orange
```

---

📌 **Unpacking Rules**
Rule 1: Number of variables must match number of items 
correct:
```python
fruits = ["Apple", "Banana", "Orange"]

a, b, c = fruits
```

---

Wrong:
```python
fruits = ["Apple", "Banana", "Orange"]

a, b = fruits
```

---


### Output
```python
ValueError
```
Because python expected 2 variables but found 3 items.

---

### using * (Star Expression)

```python
numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers

print(first)
print(middle)
print(last)
```

### Output
```python
1
[2, 3, 4]
5
```

---

### Skipping items using "_"
Use underscore _ when you don't need a value.

### Example
```python
fruits = [ "Apple", "Banana", "Orange"]

first, _, third = fruits

print(first)
print(third)
```

---

### Output
```python
Apple
Orange
```
The value "banana" is ignored.

---

### Another example:
```python
data = ["John", 25, "Lagos"]

name, _, city = data

print(name)
print(city)
```

---

### Output
```python
John
Lagos
```

---

### **Exploring and Analyzing Lists**
Length of List

```python
fruits = ["Apple", "Banana", "Orange"]

print(len(fruits))
```

---

### Output
```python
3
```

---

### **Find Maximum Value**
```python
scores = [50, 90, 70]

print(max(scores))
```

---

### Output
```python
90
```

---

### Find Minimum Value
```python
print(min(scores))
```

---

### Output
```python
50
```

---

### **Sum Values**
```python
print(sum(scores))
```

---

### Output
```python
210
```

---

### **Average**
```python
average = sum(scores) / len(scores)

print(average)
```

---

### Output
```python
70.0
```

---

### **Check if item exist**
```python
fruits = ["Apple", "Banana", "Orange"]

print("Banana" in fruits)
```

---

### Output
```python
True
```

---

### **Changing Lists**
Lists are mutable (changeable).

### **Example**
```python
fruits = ["Apple", "Banana", "Orange"]

fruits[1] = "Mango"

print(fruits)
```

---

### Output
```python
['Apple', 'Mango', 'Orange']
```

---

### **Adding Items**
append()
Adds one item at the end

```python
fruits = ["Apple", "Banana"]

fruits.append("Orange")

print(fruits)
```

---

### Output
```python
['Apple', 'Banana', 'Orange']
```

### Insert()
Adds an item at a specific position
```python
fruits.insert(1, "Mango")
```

---

### Output
```python
['Apple', 'Mango', 'Banana']
```

---

### extend()
Adds multiple items.

```python
fruits = ["Apple"]

fruits.extend(["Banana", "Orange"])
```

---

### Output
```python
['Apple', 'Banana', 'Orange']
```

---

### **Removing Items**
remove()

Removes a specific value.
```python
fruits = ["Apple", "Banana", "Orange"]

fruits.remove("Banana")

print(fruits)
```

---


### Output
```python
['Apple', 'Orange']
```

---

### **POP()**
Removes by index

```python
fruits = ["Apple", "Banana", "Orange"]

fruits.pop(1)

print(fruits)
```

---

### Output
```python
['Apple', 'Orange']
```

---

without an index:
```python
fruits.pop()
```

Removes the last item.

---

### **del**
Delete an item or entire list

```python
fruits = ["Apple", "Banana", "Orange"]

del fruits[1]

print(fruits)
```

---

### Output
```python
['Apple', 'Orange']
```

---

### **clear()**
Removes all items
```python
fruits = ["Apple", "Banana", "Orange"]

fruits.clear()

print(fruits)
```

---

### Output
```python
[]
```

---

### **Real-Life Example**
Imagine a classroom attendance list.

```python
students = ["John", "Mary", "Peter"]

# New student joins
students.append("Ada")

# Peter leaves
students.remove("Peter")

print(students)
```

---

### Output
```python
['John', 'Mary', 'Ada']
```

📌 This is exactly how lists are used in real applications such as:
* Student management systems
* Employee databases
* Shopping carts
* Contact lists
* Banking applications
* Inventory Systems

---

### **Quick Summary**
| **Operation** | **Example** |
| ------------ | ------------ |
| Create list | `items = []` |
| Access item |   `items[0]` | 
| Slice list | `items[1:4]` |
| Length | `len(items)` |
| Add item | `append()` |
| Insert item | `insert()` |
| Add many items | `extend` |
| Remove items | `remove()` |
| Remove by index | `pop` |
| Delete | `del` |
| Empty List | `clear()` |
| Unpack | `a, b, c = items` |
| skip item | `a, _, c = item` |
| Check existence | `"Apple" in items"` |
| Maximum value | `max(numbers)` |
| Minimum value | `min(numbers)` |
| Sum values | `sum(numbers)` |



