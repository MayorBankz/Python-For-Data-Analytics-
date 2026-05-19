# Topic: String Functions Categories
# Date: 19-05-2026

---

💠 **Data Types**
### **type()**
Used to check the data type of a value.

```python
type(variable)
```

### Example
```python
name = "Mayowa"
amount = 450000

print(type(name))
print(type(amouunt))
```

### Output
```python
<class 'str'>
<class 'int'>
```

---

📌 **Analytics Use Case**
Useful when validating imported datasets from:
* CSV files
* Excel sheets
* APIs
* SQL databases

---

### **str()**
Converts a value into a string

Syntax
```python
str(value)
```

### Example

```python
amount = 450000
print("Total Amount: " str(amount))
```

### Output 
```python
Total Amount: 450000
```

📌 **Analytics Use Case**
Useful when combining
* numbers + text
* report generation
* dashboard labels

---

💠 String Math & Measurement
### **len()** - Returns the total number of characters.

Syntax
```python
len(string)
```

### Example
```python
city = "Lagos"

print(len(city))
```

### Output 

```python
5
```

📌 Important

Spaces are counted.

```python
name = "Mayowa Idowu"

print(len(name))
```

### Output
```python
13
```

---

### **count()**
Counts how many times a value appears

### Syntax
```python
string.count(value)
```

### Example
```python
email = "mayowa@gmail.com"

print(email.count("a"))
```

### Output
```python
3
```

📌 **Analytics Use Case**
Useful for 
* detecting duplicate characters
* keyword frequency
* text analysis

---

💠 String Transformations

replace() - replaces part of a string with another value.

### Syntax

```python
string.replace(old, new)
```

### Example
```python
phone = "0813-555-9087"

print(phone.replace("-", ""))
```

### Output 
```python
08135559087
```

---

📌 **Analytics Use Case**
Useful for cleaning
* Phone numbers
* IDs
* Inconsistent formatting

---

### **Joining Strings**
Combines multiple strings together.
Using +
```python
first_name = "Mayowa"
last_name = "Idowu"

full_name = first_name + " " + last_name

print(full_name)
```

### Output
```python
Mayowa Idowu
```

### Using " ".join()
Syntax
```python
"separator".join(list)
```

### Example
```python
items = ["Laptop", "Mouse", "Keyboard"]

print(" | ".join(items))
```

### Output
```python
items = ["Laptop", "Mouse", "Keyboard"]

print(" | ".join(items))
```

---


### **f-strings**
Modern and cleaner way to combine variables inside strings.

Syntax
```python
f"text {variable}"
```

### Example
```python
name = "Mayowa"
amount = 450000

print(f"{name} spent {amount}")
```

### Output 
```python
Mayowa spent 450000
```

📌 **Analytics Use Case**
Useful for:
* automated reports
* dynamic messages
* logging

---

### **Split()**
Breaks a string into a list.

Syntax
```python
string.split(separator)
```

### Example
```python
purchase = "Laptop, Mouse, Keyboard"

print(purchase.split(", "))
```

### Output
```python
['Laptop', 'Mouse', 'Keyboard']
```

📌 **Analytics Use Case**
Useful for:
* CSV parsing
* tokenization
* separating categories

---

### String Repitition
Repeats a string multiple times.

Syntax
```python
string * number
```

### Example
```python
print("Data " * 3)
```
### Output
```python
Data Data Data
```
---

### **Data Extraction**
Extracting part of a string using indexing/slicing.

Indexing
```python
name = "Python"

print(name[0])
```

### Output
```python
P
```

---

### Slicing

Syntax
```python
string[start:end]
```

### Example
```python
email = "mayowa@gmail.com"

print(email[0:6])
```

### Output
```python
mayowa
```

---

💠 **Data Cleansing**
Whitespaces
Extra spaces often exist in raw datasets.
Example:

```python
name = "  Mayowa Idowu  "
```

---

### **lstrip()**
Removes spaces from the left side.

### Example

```python
name = "  Mayowa"

print(name.lstrip())
```

### Output
```python
Mayowa
```

---

### **rstrip()**
Removes spaces from the right side.

### Example
```python
name = "Mayowa  "

print(name.rstrip())
```

### Output
```python
Mayowa
```

---

### **strip()**
Removes spaces from both sides.

### Example
```python
name = "  Mayowa  "

print(name.strip())
```

### Output
```python
Mayowa
```

---

### **Removing Multiple Internal Spaces**

Example
```python
name = "  Mayowa   Idowu  "

clean_name = " ".join(name.split())

print(clean_name)
```

### Output 
```python
Mayowa Idowu
```

📌 **Analytics Use Case**
Very common in:
* Customer databases
* survery responses
* CRM Systems

---

### **Search Functions**
startswith()
Checks if a string starts with a value.

### Syntax
```python
string.startswith(value)
```

### Example
```python
email = "mayowa@gmail.com"

print(email.startswith("may"))
```

### Output
```python
True
```

### **endswith()**
Checks if a string ends with a value.

### Example
```python
file = "sales.csv"

print(file.endswith(".csv"))
```

### Output
```python
True
```

### **find()**
Returns the position of a value.
Syntax
```python
string.find(value)
```

### Example
```syntax
email = "mayowa@gmail.com"

print(email.find("@"))
```

### Output
```python
7
```

### **important**
Returns `-1` if not found.

---

### **in**
Checks if a value exists inside a string.

Syntax
```python
email = "mayowa@gmail.com"

print("gmail" in email)
```

### Output

```python
True
```

### **Analytics Use Cases**
Useful for:
* keyword detection
* Filtering records
* conditional logic

---

### **Validating Functions**
isalpha()
Checks if all characters are letters only.

### Example
```python
name = "Mayowa"

print(name.isalpha())
```

### Output
```python
True
```

### Example with Space
```python
name = "Mayowa Idowu"

print(name.isalpha())
```

### Output 
```python
False
```

Because spaces are not alphabet characters.

---

### **Isnumeric()**
Checks if all characters are numbers.
### Example
```python
number = "450000"

print(number.isnumeric())
```

### Output
```python
True
```

---

### Example
```python
number = "450k"

print(number.isnumeric())
```

### Output
```python
False
```

---

### **Real Analytics Workflow Example**
```python
customer_name = "  MAYOWA   IDOWU  "
email = "MAYOWA@GMAIL.COM"

clean_name = " ".join(customer_name.strip().split())
clean_email = email.lower()

print(clean_name)
print(clean_email)
```

### Output
```python
Mayowa IDOWU
mayowa@gmail.com
```

---

### Best Practices for Data Analytics
✅ Always clean whitespace
✅ Convert inconsistent text cases
✅ Validate data types
✅ Use split() for parsing
✅ Use replace() for formatting cleanup
✅Avoid hardcoded extraction indexes when possible 
✅ Prefer dynamic methods for scalable analytics









