# Topic: Input() Function
## Date: 07-05-2026

---

### **What is the input() function in python?**

The input() function in python is used to collect data from a user while a program is running.
It pauses the program and waits for the user to type something using the keyboard. After the user presses **ENTER**, the enetered value is returned to the program as a string.
It is one of the most commonly used functions for creating interactive python programmes.

---

### **Why Do We Need the input() Function?**
The input() function is important because it allows programs to interact with users instead of using fixed values.
Without input() , programs would always produce the same output everytime they run.

📌 With input():
* Users can provide their own data
* Programs become dynamic and flexible
* Applications can make decisions based on user responses
* Developers can build interactive systems like login pages, calculators, quizzes and forms.

---

### **Syntax**
```python
input("prompt")
```

### Syntax of the input() Function

| Part | Meaning |
| ---- | ------- |
| input() | The function used to receive user input |
| Prompt | A message displayed to the user before typing |
| Return value | Always returns the entered value as a string |

---

### **Basic Example**

```python
name = input("Enter Your Name:")
print("Hello", name)
```

📌 **Output**

```python
Enter Your Name: Mayowa
Hello Mayowa
```

### **What Happened**

1. Python displayed the message:
     "Enter your name: "
2. The user typed:
     "Mayowa"
3. The value was stored in the variable name.
4. The program printed the greeting

---

### **Important Note: input() Returns a string**
Even if a user types a number, python still treats it as text(string)

### Example
```python
 age = input("Enter Your age: ")

print(age)
print(type(age))
```

### Output 
```python
Enter Your Age: 25
 25
<class 'str'>
```

The value 25 is treated as a string, not an integer.

---

### **Converting User Input to Other Data Types**
To perform calculations, we often convert the input into:
* int() - Integer
* float() - Decimal number

---

### Example Using Int()

```python
age = int(input(""Enter Your Age: )
print(age+5)
```

### Output
```python
Enter Your Age: 20

25
```

### **Explanation**
* input() collects "20" as a string
* int() converts into an integer
* Python can now perform arithmetic operations

---

### Multiple Examples

### **Example 1 - Collecting a User's Name**
```python
name = input("What is Your Name: ")
print("Welcome", name)
```

---

### **Example 2 - Adding Two Numbers**
```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2
print("Sum =", sum)
```

### Output

```python
Enter first num: 5
Enter second num: 7

Sum = 12
```

---

### **Example 3 - Simple Login Check**
```python
password = input("Enter Password: ")
if password == "admin123":
print("Access Granted")
else:
print("Wrong Password")
```

---

### **Top 3 Use Cases of input() Function**
1. User Registration and Login Systems

input() is commonly used to collect:

Username
Password
Email
Phone number

### Example
```python
username = input("Enter username: ")
password = input("Enter password: ")
```

---

2. **Calculator Programs**
Programs use input() to receive numbers from users for calculations.

### Example

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(num1 * num2)
```

---

3. **Interactive Applications and Games**
Games and interactive programs use input() to receive commands and choices.

### Example

```python
choice = input("Choose left or right: ")

print("You chose", choice)
```

---

### **Common Mistakes Beginners Make**
Mistake 1 — Forgetting Type Conversion

```python
num = input("Enter a number: ")

print(num + 5)
```

💡 This causes an error because num is a string.

Correct Version

```python
num = int(input("Enter a number: "))

print(num + 5)
```

---

### **Mistake 2 — Using Wrong Variable Names**
```python
name = input("Enter name: ")

print(Name)
```

💡 Python is case-sensitive.

Correct
```python
print(name)
```
---

📁 Key Points to Remember
* input() collects data from users
* It pauses execution until the user types something
* The returned value is always a string
* Use int() or float() when working with numbers
* It helps make programs interactive

---

### **Summary**
The Python input() function is used to receive information from users during program execution. It is essential for building interactive applications such as calculators, login systems, quizzes, and games.

Main Takeaways
* Syntax:
```python
input(prompt)
```
* Returns data as a string
* Can be converted using int() or float()
* Makes programs dynamic and user-friendly
  










