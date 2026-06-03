# **Topic : Boolean Expressions**

# **Date: 03-06-2026**

---

### Overview

Boolean expressions in Python are expressions that evaluate to either:
* TRUE
* FALSE

They are the foundation of decision-making in python programs and are used in conditions, loops, validations, and data filtering.

---

1. **Boolean Values**
Python has two built-in Boolean values:
* True
* False

These represent truth and falsify in logical operations.

---

### Example 

```python
is_active = True
is_deleted = False

print(is_active)
print(is_deleted)
```

---

### **Output**

```python
True
False
```

---

2. **Boolean Functions**
2.1 `bool()` - converts a value into a boolean (`True` or `False`)

---

### **Example**
```python
print(bool(1))
print(bool(0))
print(bool(Hello))
print(bool("")
```

---

### **Output**
```python
True
False
True
False
```

---

2.2 `any()` - Returns `True` if at least one element in an iterable is `True`.

### Example
```python
values = [0, False, 5, ""]

print(any(values))
```

### Output
```python
True
```

---

2.3 `all()` - Returns `True` only if all elements in an iterable are `True`.

### Example
```python
Values = [1, True, "Hello"]

print(all(values))
```

---

### Output
```python
True
```

---

2.4 `isinstance()` - Checks if a value belongs to a specific data type.

Example
```python
username = 'mayowa'

print(isinstance(username, str))
print(isinstance(username, int))
```

---

### **Output**
```python
True
False
```

---

3. **Comparison Operator**
Comparison operator compares two values and return a Boolean result.
| **Operator** | **Meaning** | **Example** |
| ------------ | ----------- | ----------- |
| `==` | Equal to | `5==5` |
| `!=` | Not equal to | `5 != 3` |
| `<` | Less than | `3 < 10` |
| `>` | Greater than | `10 > 3` |
| `<=` | Less than or equal | `5 <= 5` |
| `>=` | Greater than or equal | `10 >= 8` |

---

### Example
```python
print(10 == 10)
print( 5 != 2)
print(3 < 7)
print(10 >= 20)
```

---

### **Output**
```python
True
True
True
False
```

---

4. **Logical Operators**
Logical operators combine multiple Boolean expressions.
4.1 `and`
   Returns `True` only if all conditions are true.
```python
age = 25

print(age > 18 and age < 40)
```

---

4.2 `or`
Returns `True` if at least one condition is true.
```python
age = 16

print(age < 18 or age > 60)
```

---

4.3 `not`
Reserves the Boolean value.
```python
is_logged_in = False
print(not is_logged_in)
```

---

5. **Membership Operators **
Used to check if a value exists in a sequence (list, string, tuple, etc.)
5.1 `in`
Returns `True` if value exists

```python
fruits = ["apple", "banana", "orange"]

print("banana" in fruits)
```

---

5.2 `not in` 
Returns `True` if value does NOT exist. 
```python
print("grape" not in fruits)
```

---

6. **Identity Operators**
   Used to compare memory locations (object identity), not just values.
6.1 `is`
   Returns `True` if both variables refer to the same object.
```python
x = None

print(x is None)
```

---

6.2 `is not` 
Returns `True` if both variables do NOT refer to the same object.
```python
 x = "Python"
print(x is not None)
```

---

### **Summary Table**

| Category | Operators / Functions |
| -------- | --------------------- |
| Boolean values | `True`.`False` |
| Conversion | `bool()` |
| Aggregation | `any()`. `all()` |
| Type Check | `isinstance()` |
| Comparison | `==`, `!=`, `<`, `>`, `<=`, `>=` |
| Logical | `and`, `or`, `not` |
| Membership | `in`, `not in` |
| Identity | `is`, `is not` |

---

### **Key Takeaway**

Boolean expressions are essential for controlling program flow in python. They allow you to evaluate conditions and make decisions using comparisons, logic, membership checks.

They always evaluate to either:
```python
True
```

or 

```python
False
```


