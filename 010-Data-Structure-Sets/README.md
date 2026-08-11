## TOPIC: Data Structure (Sets)
## Date: 11-08-2026

---

### **What is a Set?**

 A set is a collection of unique values.
 The most important feture of a set is:
   A set automatically removes duplicate values.

---

### **Example**
```python
numbers = {10, 20, 30, 20, 10, 40}

print(numbers)
```

### **Output**
{10, 20, 30, 40}

The duplicate `10` and `20` were removed.

---

### **Creating a Set**

* You can create a set using curly brackets {}.

countries = {"Nigeria", "Ghana", "kenya"}

print(countries)

* You can also create a set from another collection using `set()`.

```python
countries = ["Nigeria", "Ghana", "Nigeria", "Kenya", "Ghana"]

unique_countries = set(countries)

print(unique_countries)
```

### **Output**

{'Nigeria', 'Ghana', 'Kenya'}

* This is very useful when cleaning data.

---

## 🌐 **Real-World Application of Sets**

Imagine a company has customer record:

customers = ["Mayowa", "Ada", "John", "Mayowa", "Peter", "Ada", "John"]

# The business wants to know how many unique customers exist.

unique_customers = set(customers)

print(unique_customers)

### Possible Output
{'Mayowa', 'Ada', 'John', 'Peter'}

### To count them:
print(len(unique_customers))

### Output
4

---

## **🏗️ Business Use Case**

Sets are useful for:
* Finding unique customers
* Removing duplicate records
* Finding unique products
* Finding unique locations
* Checking employee departments
* Comparing list of users
* Data cleaning
* Finding common items between datasets

---

## **Adding Items to a Set**

use .add().

departments = {"IT", "Finance", "Sales"}

departments.add("HR")

print(departments)

### Result:

{"IT", "Finance", "Sales", "HR"}


---

## **Removing Items in a Set**

Use .remove():

departments.remove("HR")

There is also .discard():
departments.discard("HR")

### Difference

departments.remove("HR")
will produce an error if "HR" does not exist.

But
departments.discard("HR") will not produce an error.

---

## **Set Operations**

This is one of the most useful feature of sets.
Suppose we have two groups of employees.

```python
it_team = {"Mayowa", "Ada", "John", "Peter"}
sales_team = {"John", "Mary", "Peter", "David"}
```

**Union**: Union gives us everything from both sets 

```python
all_employees = it_team | sales_team

print(all_employees)
```

### Output

{"Mayowa", "Ada", "John", "Peter", "Mary", "David"}

* You can also use
  ```python
  it_team.union(sales_team)
  ```
## **🌐 Real-World Use**
Find all employees belonging to either IT or Sales

---

## **Intersection**
Intersection gives items that exist in both sets.

```python
common_employees = it_team & sales_team

print(common_employees)
```

### Result:
{"John", "Peter"}

### **🌐 Real-World Use**
Suppose:

```python
monday_customers = {"Ada", "John", "Peter", "Mary"}
tuesday_customers = {"John", "Peter", "David"}
```

* To find customers who purchased on both days:

```python
repeat_customers = moonday_customers & tuesday_customers
print(repeat_customers)
```

### Result:
{"John", "Peter"}

---

## **Difference**
Difference finds items that exist in one set but not the other 

```python
it_only = it_team - sales_team 

print(it_only)
```

### Result
{"Mayowa", "Ada"}

* This means Mayowa and Ada are in IT but not Sales.

### 🌐 Real_World Use

For example:

```python
january_customers = {"Ada", "John", "Peter", "Mary"}
february_customers = {"John", "Peter", "David"}
```

Customers who purchased in January but not in February:

```python
lost_customers = january_customers - february_customers

print(lost_customers)
```

### Result

{"Ada", "Mary"}

---

## **Checking Membership**

You can check whether an item exists in a set.

```python
departments = {"IT", "Finance", "Sales", "HR"}
print("IT" in departments)
```

### Output
True

And:

```python
print("Marketing" in departments)
```

### Output:

False

This is useful for validation.

### Example

```python
approved_coutries = {"NG", "GH", "KE", "ZA"}
country = "NG"

if country in approved_countries:
    print("Country approved")
else:
    print("Country not approved")
```

---

## Important Set Characterisitics

Remember

SET
|
├── Unique values
├── Mutable
├── No indexing
├── No duplicates
└── Excellent for comparisons and membership checking

You cannot do:

```python
numbers = {10, 20, 30}

print(numbers[0])
```

This will cause an error because sets do not support indexing


  





