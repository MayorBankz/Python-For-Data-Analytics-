# Task 1: Ask the user for their first name
# store it in a variable called first_name
# Then print the value

first_name = input("What is your first name? ")

print(first_name)

# Task 2
# Ask the user for their last name and their country
# store them in: last_name and country
# Then print them on a separate line

last_name = input("What is your last name? ")
country = input("Which country are you from? ")

print(last_name)
print(country)

# Task 3: Write a program that asks the user for:
# Their favorite programming language
# Store it in a variable called 'language'
# Then print 'your favorite programming language is python'

language = input('What is your favorite programming language? ')

print(f"Your favorite programming language is {language}" )
print(language)

# Task 4: Write a program that asks the user for:
# their first name, last name
# Then print exactly this:
# Full Name:
# Mayowa Idowu

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

print("Full Name:")
print(first_name + ' ' + last_name)

# Task 5: Write a program that asks the user for four pieces of information:
# First Name
# Last Name
# City
# country
# Then display the result like this:
# PERSONAL PROFILE
# ----------------
# Name:
# Mayowa Idowu

# City:
# Lagos

# Country:
# Nigeria

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
city = input("Which city are you from? ")
country = input("Which country are you from? ")

print("PERSONAL PROFILE")
print('-' * 16)
print("Name:")
print(first_name, last_name)

print("City:")
print(city)

print("Country:")
print(country)

# Task 6: Write a program that asks the user for:
# favorite food
# favorite drink
# favorite color
# Then display exactly:
# FAVORITES
# ----------
# Food:
# Pizza

# Drink:
# Water

# Color:
# Blue


food = input("What is your favorite food? ")
drink = input("What is your favorite drink? ")
color = input("What is your favorite color? ")

print("FAVORITES")
print("-" * 9)

print("Food:")
print(food)

print("Drink:")
print(drink)

print("Color:")
print(color)

# Task 7: Write a program that:
# Asks the user for their language
# Stores in a variable called age.
# Use int(input())
# print the variable

age = int(input("Enter your age: "))

print(age)

# Task 8: Write a program that:
# Asks the user for their height
# Stores it in a variable called height
# Uses float(input())
# print the variable

height = float(input("Enter your height: "))

print(height)

# Task 9: Write a program that:
# Asks the user for the first number using int(input())
# Asks the user for the second number using int(input())
# store them in: num1, num2
# print both numbers on separate 

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

print(num1)
print(num2)

# Task 10: Write a program that:
# Asks the user for two numbers using int(input())
# store them in: num1 num2
# Create a third variable called total: total
# Store the sum of the two numbers in total 
# print total: 35

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
total = num1 + num2

print("Total:", total)

# Task 11: Substraction operator
# Write a program that:
# Asks the user for: first number, second number
# Stores them in: num1, num2
# create a variable called difference
# print difference

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
difference = num1 - num2

print("Difference:", difference)

# Task 12: Multiplication operator
# Asks the user for two numbering int(input())
# Store them in:
# num1 num2
# Create a variable called: product
# print product

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
product = num1 * num2

print("Product:", product)

# Task 13: Division operator
# Ask the user for:
# first num
# second number
# store the result in a variable called: quotient
# print quotient

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
quotient = num1 / num2

print("quotient:", quotient)

# Task 14: Write a program that:
# Ask the users for two integers.
# Store them in: num1 num2
# Create these variables
# sum result
# difference
# product
# quotient
# print the result

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

print("sum:", sum)
print("difference:", difference)
print("product:", product)
print("quotient:", quotient)

