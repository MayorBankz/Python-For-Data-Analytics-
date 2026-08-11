# Topic: Lists-Sorting, Copying, Identity and Combining Lists
# Date: 26-06-2026
---

♦️ **Sorting Lists**
There are two primary ways to sort a list.

---

### **Method 1: sort()**
`sort()` sorts the original list.

Syntax
```python
list_name.sort()
```

---

### **Example**
```python

frontend = ['HTML', 'CSS']
backend = ['Python', 'sql']

full_stack = frontend + backend
 
print("full_stack:", full_stack)
print("frontend:", frontend)
print("backend:", backend)
```

---

### **Output**
```python
[34, 56, 71, 89, 92]
```
---

### 📍**Important**
```python
numbers = [3, 1, 2]

result = numbers.sort()

print(result)
```

---

### **Output**
```python
None
```

📍 Why
Because sort() modifies the original list in place and returns None.

---

### **Method 2: sorted()**
unlike sort(), sorted() creates a new sorted list.

```python
cities = ["Lagos", "Abuja", "Kano", "Ibadan"]

sorted_cities = sorted(cities)

print(cities)
print(sorted_cities)
```
---

### **output**
```python
['Lagos', 'Abuja', 'Kano', 'Ibadan']
['Abuja', 'Ibadan', 'Kano', 'Lagos']
```

---

📍 Notice: The original list did not change

---

### **Difference between sort() and sorted()**

| **sort()** | **sorted()** |
| ---------- | ------------ |
| Changes original list | Leaves original unchanged |
| Returns `None` | Returns new sorted list |
| List method | Built-in function |

---

♦️ **Copying Lists**
There are three ways.

---

### **Assignment (=)**
```python
fruits = ["apple", "banana", "orange"]

basket = fruits
```

Many beginners think this creates a copy.
It does not
Both variables point to the same list.

```python
basket[0] = "mango"

print(fruits)
print(basket)
```

---

### **Output**
```python
['mango', 'banana', 'orange']
['mango', 'banana', 'orange']
```
Changing one changes the other

---

### **Memory illustration**

fruits ───┐
          │
          ▼
['apple', 'banana', 'orange']
          ▲
          │
basket ───┘

One list. Two variable names.

---

### **Shallow Copy (.copy())**
```python
fruits = ["apple", "banana", "orange"]

basket = fruits.copy()

basket[1] = "grape"

print(fruits)
print(basket)
```

---

### **Output**
```python
['apple', 'banana', 'orange']
['apple', 'grape', 'orange']
```
Now they are different lists

---

### **Memory**
fruits ───► ['apple', 'banana', 'orange']

basket ───► ['apple', 'banana', 'orange']

Different list objects
---

🔷 **The catch**
`.copy()` only copies the outer list.
Nested lists are still shared.

---

### **Example**
```python
matrix = [
    [1, 2],
    [3, 4]
]

copy_matrix = matrix.copy()

copy_matrix[0][0] = 99

print(matrix)
print(copy_matrix)
```

---

### **Output**
```python
[[99, 2], [3, 4]]
[[99, 2], [3, 4]]
```

---

📍 **Why?**
Because the inner lists are shared.

---

### **Deep Copy**
Use:
```python
import copy
```

Then

```python
copy.deepcopy()
```

---

### **Example**
```python
import copy

matrix = [
    [1, 2],
    [3, 4]
]

copy_matrix = copy.deepcopy(matrix)

copy_matrix[0][0] = 99

print(matrix)
print(copy_matrix)
```

---

### **Output**
```python
[[1, 2], [3, 4]]
[[99, 2], [3, 4]]
```

Now every nested list is copied.

---

### **Copying Summary**

| **Method** | **Copies Outer List** | **Copies Nested List** |
| ------- | ---------------- | ------------------ |
| Assignment | ❌ | ❌ |
| `.copy()` | ✅ | ❌ |
| `deepcopy()` | ✅ | ✅ |

---

♦️ **`is` vs `==`**
This is one of the most important interview questions

---

`==`
checks whether two objects have the same value.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
```

---

### **Output**
```python
True
```

Because the contents are the same.

---

`Is`
Checks whether two variables refer to the same object

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)
```

---

### **Output**
```python
False
```

---

Different list objects.

---

### **Example**
```python
a = [1, 2, 3]

b = a

print(a == b)
print(a is b)
```

### **Output**
```python
True
True
```
Because they reference the same object.

---

### **Memory**

a ───┐
     │
     ▼
[1,2,3]
     ▲
     │
b ───┘

---

### **Quick Rule**
| Operator | Meaning |
| -------- | ------- | 
| `==` | same value? |
| `is` | same object? |

--- 

♦️ Combining Lists
Using `+`
Creates a new list.
```python
frontend = ["HTML", "CSS"]
backend = ["Python", "SQL"]

full_stack = frontend + backend

print(full_stack)
```

---

### **Output**
```python
['HTML', 'CSS', 'Python', 'SQL']
```
Original lists stay the same.

---

### Using .extend()
Modifies the existing list.

```python
frontend = ["HTML", "CSS"]
backend = ["Python", "SQL"]

frontend.extend(backend)

print(frontend)
print(backend)
```

---

### **output**
```python
['HTML', 'CSS', 'Python', 'SQL']
['Python', 'SQL']
```

---


### **Difference**
| + | .extend |
| --- | --------- |
| Creates new list | Modifies existing list |
| Original unchanged | Original changes |

---

♦️ Complete summary table
| **Operation** | **Creates New List** | **Changes Original** |
| ------------ | -------------------- | ------------------- |
| `sort()` | ❌ | ✅ |
| `sorted()` | ✅ | ❌ |
| Assignment (`=`) | ❌ | ❌ (creates another reference) |
| `.copy()` | ✅ | ❌ |
| `deepcopy()` | ✅ | ❌ |
| `+` | ✅ | ❌ |
| `.extend()` | ❌ | ✅ |

---








