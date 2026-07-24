# Task 1: Given

fruits = ["Apple", "Banana", "Orange", "Mango"]

# Write a for loop that prints each fruit on a new line.

for fruit in fruits:
    print(fruit)
    
# Task 2: Loop through a string 
# Given:

word = "Python"

# Write a for loop that prints each character on a new line 

for w in word:
    print(w)
    
# Task 3: Range()
# Given:

range(5)

# write a for loop that prints  the numbers from 0 to 4 using range(5).

for i in range(5):
    print(i)

# Task 4: range(start, stop)
# Write a for loop that prints the numbers from 5 to 10 using range()

for i in range(5, 11):
    print(i)

# Task 5: range(start, stop, step)
# Given:

range(2, 11, 2)

# Write a for loop that prints all even numbers from 2 to 10
for i in range(2, 11, 2):
    print(i)

# Task 6: Counting backwards
# write a for loop that print the numbers from 10 down to 1 

for i in range(10, 0, -1):
    print(i)
    
# Task 6: Nested Loops 
# Given

colors = ["Red", "Blue"]
fruits = ["Apple", "Banana"]

# Write a program that prints every combination of a color and fruit

for color in colors:
    for fruit in fruits:
        print(f"{color} {fruit}")
        
# Task 8: break
# Given:

numbers = [3, 7, 12, 5, 9]

# Write a program that:
# Loop through the list
# Prints each number
# stop the loop as soon as it reaches 12

for number in numbers:
    print(number)
    if number == 12:
        break
    
# Task 9: continue
# Given

numbers = [1, 2, 3, 4, 5]

# Write a program that 
# Loops through the list
# Skips the number 3
# Prints every other number

for number in numbers:
    if number == 3:
        continue
    print(number)
        
    
# Task 10: pass
# Given:

numbers = [1, 2, 3]

# Write a program that 
# Loops through the list
# If the number is 2, use pass
# print every number

for number in numbers:
    if number == 2:
        pass
    print(number)

# Task 11: for....else
# Given

numbers = [2, 4, 6]

# Write a program that:
# Prints every number
# After the loop finishes normally (without break), print 
# Loop completed successfully

for number in numbers:
    print(number)
else:
    print("Loop completed successfully")

# Task 12: Real-World Applications (Sales Report)
# Given:

sales = [120000, 85000, 230000, 150000, 98000]

# Print every sale in this format:
# Sale Amount: ₦120000
# Sale Amount: ₦85000
# Sale Amount: ₦230000
# Sale Amount: ₦150000
# Sale Amount: ₦98000

for sale in sales:
    print(f"Sale Amount: {sale}")
    
# Task 13: High Value sales
# Given:

sales = [120000, 85000, 230000, 150000, 98000]

# print only the sales that are #100,000 or more  

for sale in sales:
    if sale >= 100000:
        print(sale)
# Task 14: Customer Greeting
# Given

customers = [
    "Mayowa",
    "Ada",
    "John",
    "Mary"
]

# print
# Welcome, Mayowa!
# Welcome, Ada!
# Welcome, John!

for customer in customers:
    print(f"Welcome, {customer}!")

# Task 15: Count passed students

scores = [75, 48, 90, 66, 82, 39, 71]

# Write a program that counts how many students scored 50 or above

count = 0

for score in scores:
    if score >= 50:
        count += 1 
print(f"Passed Student: {count}")

# Task 16: Find the largest number
# Given:

numbers = [45, 87, 23, 99, 12, 76]

# Write a program that finds the largest number without using:
# max()
# sort()

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
print(f"Largest: {largest}")

# Task 17: Employee Data Cleaning
# Given:

employees = [
    "  MAYOWA IDOWU ",
    " ada obi",
    "JOHN DOE ",
    "  mary ann"
]

# print exactly
# Mayowa Idowu
# Ada Obi
# John Doe
# Mary Ann

for employee in employees:
    cleaned_employee = employee.strip().title()
    
    print(cleaned_employee)


        
        
        
    
    
