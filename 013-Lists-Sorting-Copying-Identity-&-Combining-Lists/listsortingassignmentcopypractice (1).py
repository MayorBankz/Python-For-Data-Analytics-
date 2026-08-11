# Task 1: Sort Employee Salaries
# A company has recorded employee Salaries

salaries = [420000, 280000, 350000, 310000, 500000]

# sort the list in ascending order using sort()
# print the list

salaries.sort()

print(salaries)

# Task 2: Sort Product Prices (Descending)

prices = [15000, 450000, 35000, 8000, 120000]

# Sort the list from the highest to the lowest

prices.sort(reverse = True)

print(prices)

# Task 3: Keep the original list
# A manager wants to view salaries in sorted order without changing the original list

salaries = [420000, 280000, 350000, 310000]

# Create a new sorted list
# print the original list
# print the new sorted list

sorted_list = sorted(salaries)

print(f"Original: {salaries}")
print(f"Sorted: {sorted_list}")

# Task 4: Assignment Vs copy 

employees = ["Mayowa", "Ada", "John"]

# create a new variable:
# new_list = employees
# Add "Mary" to new_list

new_list = employees

new_list.append("Mary")

print(new_list)

# Task 5: Make a real copy

employees = ["Mayowa", "Ada", "John"]

# create a copy using 
# new_list = employees.copy()
# Add "Mary" to new_list

new_list = employees.copy()

new_list.append("Mary")

print(f"Original: {employees}")
print(f"Copy: {new_list}")

# Task 6: The is Operator

employees = ["Mayowa", "Ada", "John"]

list1 = employees
list2 = employees.copy()

# print the result of these expressions

print(list1 is employees)
print(list2 is employees)
print(list1 == employees)
print(list2 == employees)

# Task 7: Combining Lists
# A company has employees from three departments

it = ["Mayowa", "Peter"]
finance = ["Ada", "Grace"]
sales = ["John", "Mary"]

# Create one list called employees using the + Operator

employees = it + finance + sales

print(employees)

# Now do the same thing without +, using extend()

it.extend(finance)
it.extend(sales)


print(it)

# Task 8: Shallow Copy Vs Deep Copy (Nested Lists)

# import copy

# employees = [
#    ["Mayowa", "IT"],
#    ["Ada", "Finance"]
#]

# Create two copies 

# shallow = employees.copy()
# deep = copy.deepcopy(employees)

# change Mayowa's department in the shallow copy to "Data Engineering"

# shallow[0][1] = "Data Engineering"

# print

# print("Original:", employees)
# print("Shallow:", shallow)
# print("Deep:", deep)







