# Topic: Number Functions for Data Analytics
# Date: 21-05-2026

---

### **Introduction**
Numbers are everywhere in data analytics ---sales figures, customer counts, percentages, averages, predictions and more.

Python provides built-in number functions and operators that help help analysts.
* Clean data
* Perform calculations
* Validate numeric values
* Generate random samples
* Round values for reporting

---

### **Number Types in Python**
Python has different numeric data

| Type      | Description     | Example        |
| --------- | --------------- | -------------- |
| `int`     | Whole numbers   | `10`, `-5`     |
| `float`   | Decimal numbers | `3.14`, `99.9` |
| `complex` | Complex numbers | `2 + 3j`       |

---

### **type()**
Used to check the data type of a value

```python
type(value)
```
--- 

### Example

```python
age = 25
price = 99.99

print(type(age))
print(type(price))
```
---

### **Output**

```python
<class 'int'>
<class 'float'>
```

---

 📌 **Analytics Use Case**

Useful when checking imported data types from CSV or databases.

---

### **int()**
Converts a value to an integer.

### Syntxax

```python
int(value)
```

---

### Example

```python
price = 45.89

print(int(price))
```
---

### **Output**

```python
45
```
---

📌 **Important Note**
int() removes the decimal part instead of rounding.

---

### **float()**
Converts a value to a decimal number

---

### Syntax

```python
float(value)
```

### Example

```python
age = 25

print(float(age))
```

---

### Output

```python
25.0
```

📌 **Analytics Use Case **
Helpful when calculations require decimal precision.

---

### **Complex()**

Creates a complex number.

### Syntax

complex(real, imaginary)

---

### Example

```python
num = complex(2, 3)

print(num)
```
---

### Output
```python
(2+3j)
```

---

📍 Complex numbers are rarely used in basic analytics but are useful in scientific computing and engineering.

---

### **Math operators**
Math operators are used for for calculations.

| Operator | Meaning             | Example  |
| -------- | ------------------- | -------- |
| `+`      | Addition            | `5 + 2`  |
| `-`      | Subtraction         | `5 - 2`  |
| `*`      | Multiplication      | `5 * 2`  |
| `/`      | Division            | `5 / 2`  |
| `//`     | Floor Division      | `5 // 2` |
| `%`      | Modulus (remainder) | `5 % 2`  |
| `**`     | Exponent (power)    | `5 ** 2` |


---

### **Addition +**
```python
sales_q1 = 5000
sales_q2 = 7000

total_sales = sales_q1 + sales_q2

print(total_sales)
```

---

### Output

```python
12000
```

---

### **Subtraction -**
```python
profit = 10000 - 2500

print(profit)
```

---

### Output

```python
7500
```

---

### **Multiplication ***

```python
price = 50
quantity = 4

total = price * quantity

print(total)
```

---

### Output
```python
200
```

---

### **Division /**

```python
print(10 / 2)
```

### Output 
```python
5.0
```

---

📍 **Important**

Division always returns a float.

---

### Floor Division //
Returns only the whole number part.

```python
print(10 // 3)
```

---

### Output
```python
3
```
---

📌 Analytics use cases

Useful when grouping data into batches.

---

### Modulus %
Returns the remainder 
```python
print(10 % 3)
```

---

### Output
```python
1
```

---
📌 Analytics use case
Helpful for checking even/odd numbers

---

### Exponent **
Raises a number to a power.
```python
print(2 ** 3)
```

---

### Output
```python
8
```

---

### **Rounding Functions**
To use some rounding functions, import the math module first.

```python
import math
```

---

### **abs()**
Returns the absolute (positive) value.

### Syntax
```python
abs(number)
```
---

### Example
```python
abs(number)
```

---


### Example

```python
print(abs(-50))
```

---

### Output
```python
50
```

---

📌 **Analytics Use Case**
Useful when measuring differences between values.

---

### **round()**
Rounds a number to the nearest value

---
### Syntax
```python
round(number, digits)
```

---

### Example
```python
print(round(4.567, 2))
```

---

### Output
```python
4.57
```

---


### **math.ceil()**
Rounds upward

---

### Syntax
```python
math.ceil(number)
```

---

### Example
```python
import math

print(math.ceil(4.2))
```

---

### Output
```python
5
```

---

📌 Analytics Use Case
Useful when estimating required inventory or staff.

---

### math.floor()
Rounds downward.

### Syntax
```python
math.floor(number)
```

---

### Example

```
import math

print(math.floor(4.9))
```

---

### Output
```python
4
```

### **math.trunc()**
Removes the decimal part.

---

### Example

```
import math

print(math.trunc(4.9))
```

---

### Output
```python
4
```

---

### **Random Numbers**
Used in simulations, testing, and sampling.

---

### **random()**
Generates a random decimal between 0 and 1.

---

### Syntax
```python
random.random()
```

---

### Example
```python
import random

print(random.random())
```

---

### Output
```python
0.4839201
```

---

### randint()
Generates a random whole number within a range.

---

### Syntax
```python
random.randint(start, end)
```

---

### Example
```python
import random

print(random.randint(1, 10))
```

---

### Output
```
7
```

---

📌 Analytics Use Case

Useful for generating sample data.

---

### **Validation Functions**
Validation helps ensure data quality.

---

### is_integer

Checks if a float is a whole number.

---

### Syntax

```python
float_value.is_integer()
```

---

### Example
```python
num = 10.0

print(num.is_integer())
```

---

### Output
```python
True
```

---

📍 **Important**
Works only on float values

---

### **isinstance**
Checks whether a value belongs to a specific data type.

### Syntax
```python
isinstance(value, datatype)
```

---

### Example
```python
age = 25

print(isinstance(age, int))
```

---

---

### Output
```python
True
```

---

📌 Analytics use case
Useful for validating imported datasets

---

### **Real-World Analytics Example**
```python
import math
import random

sales = 4589.76

# Convert to integer
sales_int = int(sales)

# Round to 2 decimal places
sales_round = round(sales, 2)

# Generate random sample ID
sample_id = random.randint(1000, 9999)

print("Sales:", sales)
print("Integer:", sales_int)
print("Rounded:", sales_round)
print("Sample ID:", sample_id)
```

---

### Top 5 Analytics Use Case
| Function           | Use Case                       |
| ------------------ | ------------------------------ |
| `round()`          | Financial reporting            |
| `int()`            | Cleaning imported numeric data |
| `isinstance()`     | Data validation                |
| `random.randint()` | Creating sample datasets       |
| `math.ceil()`      | Estimating quantities          |

---

### **Summary**
| Category       | Functions                                          |
| -------------- | -------------------------------------------------- |
| Types          | `type()`                                           |
| Conversion     | `int()`, `float()`, `complex()`                    |
| Math Operators | `+`, `-`, `*`, `/`, `//`, `%`, `**`                |
| Rounding       | `abs()`, `round()`, `ceil()`, `floor()`, `trunc()` |
| Random         | `random()`, `randint()`                            |
| Validation     | `is_integer()`, `isinstance()`                     |

---

📍 **Best Practices for Data Analytics**
* Always validate data types before calculations
* Use round() for reporting and dashboards
* Use float() when precision matters
* Use isinstance() to prevent errors in datasets.
* Import the math and random modules only when needed.
