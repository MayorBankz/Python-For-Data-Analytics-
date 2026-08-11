# Level 1: Creating and accessing lists
# create a list called fruits: Then 
# print the entire list
# print the first item
# print the last item

fruits = ["apple", "banana", "orange", "mango"]

print(fruits)
print(fruits[0])
print(fruits[-1])

# Level 2
# Given: colors = ["red", "blue", "yellow", "black"]
# print: The first three colors
# The last two colors
# All colors except the first one

colors = ['red', 'blue', 'green', 'yellow', 'black']

print(colors[0:3])
print(colors[-2:])
print(colors[1:])

# Level 3
# Given: animals = ['cat', 'dog', 'rabbit', 'goat']
# perform the following
# change the dog to lion
# print the updated list
# print the second item in the updated list

animals = ['cat', 'dog', 'rabbit', 'goat']
animals[1] = 'lion'

print(animals)
print(animals[1])

# Level 4: Adding Items
# Given: cities = ['Lagos', 'Abuja', 'Kano']
# Do the following:
# Add "Ibadan" to the end of the list
# Add "Port Harcourt" at index 1
# print the updated list
# print the total number of cities

cities = ['Lagos', 'Abuja', 'Kano']

cities.append('Ibadan')
cities.insert(1, 'Port Harcourt')

print(cities)
print("Length:", len(cities))

# Level 5: Removing Items
# Task 5: Given: numbers [10, 20, 30, 40, 50, 60]
# Perform the following:
# Remove 30 using remove()
# Remove the last item using pop().
# Store the removed last item in a variable called "removed_num"
# print the updated list
# print the value of removed_num

numbers = [10, 20, 30, 40, 50, 60]

numbers.remove(30)
removed_num = numbers.pop()

print(numbers)
print("Removed:", removed_num)

# Level 6: Searching and checking lists
# Task 6: Given fruits = ['apple', 'banana', 'orange', 'mango', 'banana']
# Perform the following:
# Check whether 'banana' exists in the lists
# Print "Found" if it exists, otherwise print "Not found"
# print how many times "banana" appears in the list.

fruits = ['apple', 'banana', 'orange', 'mango', 'banana']

if 'banana' in fruits:
    print("Found")
else: 
    print("Not Found")

print(fruits.count('banana'))

# Level 7: Looping through lists
# Task 7: Given
# Given: scores = [85, 92, 78, 96, 88]
# Perform the following:
# Use a for loop to print each score 
# print the total score
# print the average score (rounded to 2 decimal places)

scores = [85, 92, 78, 96, 88]
total = 0

for score in scores:
    print(score)
    total += score
    
average = round(total / len(scores), 2)    
   
print("Total Score:", total)
print("Average Score:", average)

# Level 8: Finding the largest value
# Task 8: Given numbers = [14, 7, 25, 3, 19, 31, 8]
# without using max:
# Find the largest number in the list using a for loop.
# store it in a variable called largest 
# print the largest number

numbers = [14, 7, 25, 3, 19, 31, 8]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
print("Largest:", largest)

# Level 9: Accessing Nested List
# print:
# Ada
# 92
# Mary

student = [
    ['Ada', 85],
    ['John', 92],
    ['Mary', 78]
    ]

print(student[0][0])
print(student[1][1])
print(student[2][0])

# Level 10: List Unpacking
# use list unpacking to store the values in"name, age, role"
# Then print all three variables

person = ['Mayowa', 26, "Data Analyst"]

name, age, role = person

print(name)
print(age)
print(role)

# Level 11: Skipping items with "_"
# Use unpacking and "_" to 
# store the name in "name"
# skip the age
# store the role in role
# print name and role

person = ['Mayowa', 26, "Data Analyst"]

name, _, role = person

print(name)
print(role)

# Level 12: Exploring and Analyzing lists
# Explore the lists: sales = [150, 200, 120, 300, 250]
# print number of sales record
# total sales
# Highest sale
# lowest sale

sales = [150, 200, 120, 300, 250]

print("Records:", len(sales))
print("Total Sales:", sum(sales))
print("Highest Sale:", max(sales))
print("Lowest Sale:", min(sales))


# Level 13: Advanced List Unpacking (*)
# Task: Use unpacking to store:
# First country -- First
# Last country -- Last
# All countries in between -- others 

countries = ['Nigeria', 'Ghana', 'Kenya', 'South Africa', 'Egypt']

first, *others, last = countries

print(first)
print(others)
print(last)

