# Topic: Conditional Statements 
# Date: 05-06-2026

---

## **Conditional Statements**

Conditional statements allow your program to make decisions based on certain conditions. They help control the flow of execution by running different blocks of code depending on whether a condition is `True` or `False`.

---

### **Table of Contents**
1. Standalone `if` statements
2. Indentation
3. `else` statement
4. Multiple conditions (`elif`)
5. Branching (`elif`, `elif`....)
6. Nested `if`
7. Connecting conditions
8. Independent `if` statements
9. Ternary (inline `if`)
10. `match-case` statement

---

### 1. Standalone if statement
The `if` statement executes a block of code only when a condition is `True`.

---

### **Syntax**
```python
if condition:
    # code to execute
```

---

### Example
```python
age = 20

if age>= 18:
    print("You're an adult")
```

---

### Output 
```python
You're an adult
```

---

📌 Explanation
* python checks if `age>=18`
* Since the condition is `True`, the code inside the `if` block runs.

---

### 2. **Indentation**
Python uses indentation (spaces or tabs) to define code blocks.

--- 

### Correct Example
```python
age = 20

if age>= 18:
   print("Access granted.")
```

---

### Incorrect Example
```python
age = 20
if age >= 20:
print("Access granted.")
```

---

### Output 
```python
IndentationError
```

---

📌 Best Practice
Use 4 spaces for each indentation level.

```python
if True:
   print("Level 1")
```

---

### 3. **else Statement**
The `else` statement runs when the `if` condition is `False`

---

### Syntax
```python
if condition:
   # code is True
else:
   # code is False
```

---

### Example
```python
age = 16

if age >= 18:
    print("you can vote")
else:
   print("You cannot vote")
```

---

### Output 
```python
You cannot vote
```

---

📌 Explanation
* The condition `age >= 18` is `False`.
* Python executes the `else` block.

---

### 4. **Multiple Conditions (`elif`)**
The `elif` statement allows you to check additional conditions.

### Syntax
```python
if condition1:
   # code
elif condition2:
   # code
else:
   # code
```

---

### Example
```python
score = 75

if score >= 90:
    print("Grade A")
elif score >= 70;
    print("Grade B")
else:
    print("Grade C")
```

---

### Output
```python
Grade B
```

---

📌 Explanation
* Python checks condition from top to bottom
* The first condition that evaluates to `True` is executed.

---

### 5. Branching (elif, elif ....)
Branching allows a program to choose one path from several possibilities.

---

### Example

```python
day = 3

if day == 1:
   print("Monday")
elif day == 2:
   print("Tuesday")
elif day == 3:
   print("Wednesday")
elif day == 4:
   print("Thursday")
else:
   print("Invalid day")
```

---

### Output 
```python
Wednesday
```

---

💠 **Key Point**
Only one branch is executed, even if multiple conditions could potentially be true.

---

### Nested if
A nested `if` is an `if` statement inside another `if` statement.

---

### Example
```python
age = 25
has_id = True

if age >= 18:
  if has_id:
      print("Entry is allowed")
```

---

### Output

```python
Entry is allowed
```

---

📌 Explanation
* First condition checks age
* Second condition checks if the user has an ID.
* Both condtions must be true

---

🔷 Visual Structure
```
if condition1:
   if condition2:
        execute code
```

---

### 7. **Connecting Conditions**
You can combine multiple conditions using logical operators.
Using `and`
Both conditions must be `True`

```python
age = 20
has_id = True

if age >= 18 and has_id:
   print("Access Granted.")
```

---

### Output
```python
Access Granted.
```

---

### Using or 
At least one condition must be `True`
```python
is_admin = False
is_manager = True

if is_admin or is_manager:
    print("Access Granted.")
```

---

### Output
```python
Access if granted
```

---

### Using not
Reverses a condition.
```python
logged_in = False

if not logged_in:
   print("Please log in")
```

---

### Output
```python
Please log in
```

---

### 8. Independent if statements

Independent `if` statements are evaluated separately.

---

### Example
```python
number = 12

if number > 10:
    print("Greater than 10")

if number % 2 == 0:
    print("Even number")
```

---

### Output
```python
Greater than 10
Even number
```

---

📌 Explanation
* Each `if` statements is checked independently
* Multiple blocks can execute.

Compare with `if-elif`

```python
number = 12

if number > 10:
   print("Greater than 10")
elif number % 2 == 0:
   print("Even number")
```

---

### Output
```python
Greater than 10
```

🔷 Only the first matching condition runs

---

### 9. Ternary (inline if)
A ternary expression is a short way to write simple `if-else` statements.

---

### Syntax
```python
value_if_true if condition else value_if_false
```

---

### Example
```python
age = 20
message = "Adult" if age >= 18 else "Minor"
print(message)
```

---

### Output
```python
Adult
```

---

### Traditional Version
```python
if age >= 18:
    message = "Adult"
else:
    message = "Minor"
```

---

🔷 When to use
Use ternary expressions for simple decisions that fit on one line

---

### **10. match-case statement**
Introduced in Python 3.10, `match-case` provides a cleaner alternative to long `if-elif-else` chains.

---

### Syntax
```python
match variable:
   case value1:
        # code
   case value2:
        # code
   case_:
        # default case
```

---

### Example
```python
status_code = 404

match status_code:
    case 200:
          print("success")
    case 404:
          print("Page not found")
    case 500:
          print(""Server error)
    case_:
          print("Unknown Status")
```

---

### Output
```python
page not found
```

---

### Using Multiple values
```python
day = "saturday"

match day:
    case "Saturday" | "Sunday":
         print("Weekend")
    case _:
        print("weekday")
```

---

### Output
```python
weeekend
```

---

🔷 Default Case
The underscore (_) acts like an else statement.

```python
case_:
    print("Default option")
```

---

| Statement        | Purpose                                       |
| ---------------- | --------------------------------------------- |
| `if`             | Execute code when a condition is `True`       |
| `else`           | Execute code when a condition is `False`      |
| `elif`           | Check additional conditions                   |
| Nested `if`      | Place an `if` inside another `if`             |
| `and`            | All conditions must be `True`                 |
| `or`             | At least one condition must be `True`         |
| `not`            | Reverse a condition                           |
| Independent `if` | Evaluate multiple conditions separately       |
| Ternary `if`     | Write simple `if-else` logic in one line      |
| `match-case`     | Pattern matching and branching (Python 3.10+) |

---

### **Practice Exercises**
* Exercise 1

Check if a user is eligible to vote.

---

* Exercise 2

Check if a number is:

Positive
Negative
Zero

Using if-elif-else.

---

* Exercise 3

Check if a user can access a system when:

Age is at least 18
User has a valid ID

Use the and operator.

---

* Exercise 4

Convert the following into a ternary expression:

```python
if score >= 50:
    result = "Pass"
else:
    result = "Fail"
```

---

* Exercise 5

Use match-case to display a message for the following grades:

```python
grade = "A"
```

* A → Excellent
* B → Good
* C → Average
* Any other value → Invalid Grade
