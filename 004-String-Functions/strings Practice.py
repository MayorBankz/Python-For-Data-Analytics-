# Level 1:
# Task 1: replace()
# Replace Java with Python

sentence = "I love Java"

print(sentence.replace("Java", "Python"))

# Task 2 - type()
# Create the following variables 
# age = 25
# height = 1.75
# country = "Nigeria"
# Then print the data type of each variable using type()

age = 25
height = 1.75
country = 'Nigeria'

print(type(age))
print(type(height))
print(type(country))

# Task 3 - Join()
# Given the list

languages = ['Python', 'SQL', 'HTML', 'CSS']

# Use join() to produce this exact output: Python, SQL, HTML, CSS

language_join = ",".join(languages)

print(language_join)

# task 4: join()
# Given

first_name = "Mayowa"
last_name = "Idowu"

# without using + or an f-string, use join to produce: Mayowa Idowu

full_name = " ".join([first_name, last_name])

print(full_name)

# Task 5: Given the string 

sentence = "Python SQL HTML CSS"

# Use split to convert into this list: ['Python', 'SQL', 'HTML', 'CSS']

cleaned_sentence = sentence.split(",")

print(cleaned_sentence)

# Task 5: Split()
# Given the string

sentence = "Python SQL HTML CSS"

# Use split to convert into this list: ['Python', 'SQL', 'HTML', 'CSS']

splitted_sentence = sentence.split()

print(splitted_sentence)

# Task 6: Split() + indexing

full_name = "Mayowa Idowu"

# Use split() to separate the names, then print:
# The first_name
# The last_name

split = full_name.split()

print(split[0])
print(split[1])

# Task 7: f-string
# Given:

name = "Mayowa"
course = "Python"
score = 95

# Use an f-string to print exactly: Mayowa scored 95 in Python

print(f"{name} scored {score} in {course}")

# Task 8 - f-string + string methods
# Given:
first_name = "mayowa".title()
last_name = "idowu".title()
role = "python developer".title()

# Use string methods and an f-string to print exactly: Mayowa Idowu is a Python developer

print(f"{first_name} {last_name} is a {role}.")

# Task 9: Sring Repetition (*) + Extraction 
# Given:

word = "Python"

# Without typing the letter "P" manually
# Extract the first character from word
# Repeat that character 5 times
# Print the result

print(word[0] * 5)

# Task 10 - Extraction + Slicing
# Given:

website = "www.python.org"

website_extract = website[4:10]

# print the following without typing "python" manually

print(website_extract)

# Task 11 - Data Cleansing + Strip()
# Given:

username = "  Mayowa  "

# print the following: Mayowa

username_cleaned = username.strip()

print(username_cleaned)

# Task 12: lstrip() + rstrip()
# Given:

product = "    Laptop    "

# write code to print three lines:
# Using lstrip()
# using rstrip()
# using strip()

print(product.lstrip())
print(product.rstrip())
print(product.strip())

# Task 13 - startswith()
# Given: 

website = "www.python.org"

# write code to check whether the string starts with "www"
# Print the result

print(website.startswith("www"))
print(website.startswith("https"))

# Task 14 - endswith()
# Given: 

filename = "report.pdf"

# Write code to:
# Check whether the filename ends with ".pdf"
# Check whether it ends with ".docx"
# Print both results

print(filename.endswith(".pdf"))
print(filename.endswith(".docx"))

# Task 15 - find()
# Given:

email = "mayowa.idowu@gmail.com"

# Write code to:
# Find the position of the "@" character.
# Find the position of the first "." character
# Print both positions

print(email.find("@"))
print(email.find("."))

# Task 16 - find() 
# Given:

filename = "sales_report_2026.xlsx"

# Write code to:
# Find the position of the first underscore ("_")
# Find the position of the ".xlsx"
# Print both positions

print(filename.find("_"))
print(filename.find(".xlsx"))

# Task 17 - isalpha()

name1 = "Mayowa"
name2 = "Mayowa123"
name3 = "Mayowa Idowu"

# print whether each string contains only alphabetic characters using isalpha()

print(name1.isalpha())
print(name2.isalpha())
print(name3.isalpha())

# Task 18 - isnumeric()
# Given:
value1 = "2026"
value2 = "20.26"
value3 = "Python2026"
value4 = "500000"

# print the result of isnumeric() for each value

print(value1.isnumeric())
print(value2.isnumeric())
print(value3.isnumeric())
print(value4.isnumeric())

# Task 18 - Clean a username
# Given:

username = "   mayowa idowu   "

# Produce this exact output: Mayowa idowu

cleaned_username = username.strip().title()

print(cleaned_username)

# Task 19 - Basic Email Validation
# Given:

email1 = "mayowa@gmail.com"
email2 = "mayowagmail.com"
email3 = "john@yahoo"

# For each email, print True only if it:
# contains "@" and ends with ".com", otherwise print False

print("@" in email1 and email1.endswith(".com"))
print("@" in email2 and email2.endswith(".com"))
print("@" in email3 and email3.endswith(".com"))

# Task 20 - Given

customers = [
    "  mayowa idowu  ",
    "  ada obi ",
    " john DOE ",
    "mARY ann "
]

# Produce this exact output
# Mayowa Idowu
# Ada Obi
# John Doe
# Mary Ann

for customer in customers:
    
    print(customer.strip().title())

# Task 21 - Generate Company Email Addresses
# Given:
employees = [
    "  Mayowa Idowu  ",
    "Ada Obi",
    " JOHN DOE ",
    "mary ann"
]

suffix = "@company.com"
# Generate company email addressed in this format:
# mayowa.idowu@company.com
# ada.obi@company.com
# john.doe@company.com
# mary.ann@company.com

for employee in employees:
    cleaned_employee = employee.strip().lower().replace(" ", ".")
    
    print(f"{cleaned_employee}{suffix}")


    