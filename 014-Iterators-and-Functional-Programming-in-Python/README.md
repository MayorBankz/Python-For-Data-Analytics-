# Topic: Iterators and Functional Programming
# Date: 01-07-2026

---

📁 **Table of Contents**

1. Introduction
2. Iterables
3. Iterators
4. `iter()` and `next()`
5. `enumerate()`
6. `reversed()`
7. `zip()`
8. `map()`
9. `filter`
10. Lambda Functions
11. Lambda + `map()`
12. Lambda + `filter()`
13. Summary Table


---

## **INTRODUCTION**
Python provides several built-in tools that make working with collections easier and more efficient.
Instead of writing long loops, python allows you to process data using tools like:
* `enumerate()`
* `zip()`
* `map()`
* `filter`
* `lambda`

These are called iterable tools because they work with sequences such as:
* Lists
* Tuples
* Strings
* Dictionaries
* Sets

---

### **What is an Iterable?**
An iterable is any object that can be looped over.

📌 Examples include:

```python
numbers = [10, 20, 30]

for num in numbers:
    print(num)
```

---

### Output
```python
10
20
30
```

Since we can loop through the list, it is an iterable.

---

### **Common Iterables**

```python
my_list = [1, 2, 3]

my_tuple = (1,2,3)

my_string = "Python"

my_dict = {"name":"Ada"}

range(5)
```

All of these are iterable.

---

### **What is an Iterator?**

An iterator is an object that returns one item at a time. 
Think of it like a TV remote.
Instead of showing every channel at once
It shows
* Channel 1
* Press next
* Channel 2
* Press next
* Channel 3

Python does the same thing

---

### **Creating an Iterator**
Use
```python
iter()
```

---

### Example
```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator)
print(next(iterator)
print(next(iterator)
```

---

### Output
10
20
30

---

If you request another value

```python
print(next(iterator))
```

---

### **Output**
  _StopIteration_
because there are no more items.

---

🌐 **Real-Life Example**
Imagine a queue at a bank.

People enter:

A
B
C
D

The iterator serves

next()
A
next()
B
next()
C
next()
D

One customer at a time.

---

### **iter()**
Converts an iterable into an iterator.

Example
```python
names = ['Ada', 'John', 'Mary']
it = iter(names)

print(next(it))

```

---

### Output
Ada

---

### **next()**
Gets the next item from an iterator.

```python
numbers = [5,10,15]
it = iter(numbers)

print(next(it))
```

---

### Output
5
10

---

### **enumerate()**
`enumerate()` lets you loop while keeping track of the position (index).
Without enumerate
```python
students = ['Ada', 'John', 'Mary']
index = 0

for student in students:
    print(index, student)
    index += 1
```

---

### **Using enumerate**
```python
students = ['Ada', 'John', 'Mary']
for index, student in enumerate(students):
    print(index, student)
```

---

### Output
0 Ada
1 John
2 Mary

---

### **Starting From Another Number**
```python
students = ['Ada', 'John', 'Mary']

for index, student in enumerate(students, start=1):
    print(index, student)
```

---

### Output

1 Ada 
2 John
3 Mary

---

🌐 **Real-Life Example**
Imagine taking attendance.
1 Ada
2 John
3 Mary

The numbering is automatic.

---

### **reversed()**
Returns items in reverse order.

```python
numbers = [10,20,30,40]
for num in reversed(numbers):
    print(num)
```

---

### Output
40
30
20
10

---

You can also convert it back into a list.
```python
numbers = [10,20,30]
print(list(reversed(num)))
```

---

### Output
[30,20,10]

---

🌐 **Real-Life Example**
Think of reading a queue backwards.
Original 
A
B
C

Reversed
C
B
A

---

### **Zip()**
`zip()` combines multiple iterables together.

Example
```python
students = ['Ada', 'John', 'Mary']

scores = [90,85,80]

for student, score in zip(students, scores):
    print(student, score)
```

---

### Output

Ada 90
John 85
Mary 80

---

Three lists
```python
students = ['Ada', 'John', 'Mary']

courses = ['Python', 'SQL', 'Html']

scores = [90,85,80]

for student, course, score in zip(students, courses, scores):
    print(student, course, score)
```

---

### Output
Ada Python 90
John SQL 85
Mary Html 80

---

📌 **Important**
zip() stops when the shortest iterable ends.
```python
a = [1,2,3]
b = [10]

print(list(zip(a,b)))
```
---

### Output
[(1,10)]

---

### **Real-Life Example**
Imagine matching
Student

↓

Course

↓

Score

into one complete record

---

### **map()**
`map()` applies the same function to every item.

without map

```python
prices = [100,200,300]

new_prices = []

for price in prices:
    new_prices.append(price + 20)
print(new_prices)
```

---

### **using map()**
```python
def add_tax(price):
    return price + 20

prices = [100,200,300]
new_prices = map(add_tax, prices)
print(list(new_prices)
```

---

### Output
[120,220,320]

---

### **Real-Life Example**
Imagine adding VAT to every product price automatically.

---

### **filter()**
`filter` keeps only items that satisfy a condition.

### Example
```python
numbers = [5,10,15,20]

def greater_than_10(num):
    return num > 10
result = filter(greater_than_10, numbers)
print(list(result))
```

---

### Output
[15,20]

---

🌐 **Real-Life Example**
Imagine filtering job applicants
Keep only applicants older than 18.

---

### **Lambda Functions**
A lambda function is a small anonymous function written in one line.
Normal function
```python
def square(x):
    return x*x
print(square(4))
```

---

### Output
16

---

### Using Lambda
```python
square: lambda x: x*x
print(square(4))
```
---

### Output
16

---

### **General Syntax**
```python
lambda parameters: expression
```

---

**Multiple parameters**
```python
multiply = lambda a,b: a*b
print(multiply(3,4))
```

---

### Output
12

---

🌐 Real-Life Example
If a function is needed only once, a lambda keeps the code short and readable.

---

**Lambda + map()**
Instead of creating a separate function.

Normal
```python
def square(x):
    return x*x
numbers = [1,2,3,4]
result = map(lambda x: x*x, numbers)
print(list(result))
```

---

### Output
[1,4,9,16]

---

### **Another example**
```python
prices = [100,200,300]
new_prices = map(lambda price: price+20, prices)
print(list(new_prices))
```

---

### **Output**
[120,220,320)

---

### **Lambda + Filter**
Normal
```python
def even(num):
    return num % 2 == 0

numbers = [1,2,3,4,5,6]

result = filter(even, numbers)

print(list(result))
```

---

Using lambda
```python
numbers = [1,2,3,4,5,6]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))
```

---

### Output
[2,4,6]

---

### Another example
Keep students whose names start with M
```python
students = [["Maria",85],
            ["Kumar",90],
            ["Max",60]]

result = filter(lambda student: student[0].startswith("M"), students)

print(list(result))
```

---

### output
[['Maria', 85], ['Max', 60]]

---

### **Summary Table**
| Function      | Purpose                            | Returns                      |
| ------------- | ---------------------------------- | ---------------------------- |
| `iter()`      | Creates an iterator                | Iterator                     |
| `next()`      | Gets next item                     | One item                     |
| `enumerate()` | Adds index while looping           | Iterator of `(index, value)` |
| `reversed()`  | Reverses iterable                  | Reverse iterator             |
| `zip()`       | Combines iterables                 | Iterator of tuples           |
| `map()`       | Applies a function to every item   | Map object                   |
| `filter()`    | Keeps matching items               | Filter object                |
| `lambda`      | Creates a small anonymous function | Function                     |

---

### **When should you use each?**
| Situation                   | Best Tool     |
| --------------------------- | ------------- |
| Need the item number        | `enumerate()` |
| Reverse a sequence          | `reversed()`  |
| Combine two or more lists   | `zip()`       |
| Transform every item        | `map()`       |
| Keep only matching items    | `filter()`    |
| Short one-time function     | `lambda`      |
| Process items one at a time | `iterator`    |

---

