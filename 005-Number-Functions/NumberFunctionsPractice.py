# Task 1: Given
price = "250"

# Convert into an integer and print:
# The converted value
# It's data type

print(int(price))
print(type(int(price)))

# Task 2: Given

weight = "72.5"

# Convert into a float, then print:
# The converted value
# Its data type

print(float(weight))
print(type(float(weight)))

# Task 3: Given

real = 5
imaginary = 3

# Create a complex number using these values and then print:
# The complex number
# Its data type

print(complex(real, imaginary))
print(type(complex(real, imaginary)))

# Task 4: abs()
# Given:

temperature = -18


# Print: The absolute value of temperature

print(abs(temperature))

# Task 5: Round()
# Given:

price = 199.876

# Print: 
# The number rounded to 2 decimal places 
# The number rounded to the nearest whole number

print(round(price, 2))
print(round(price))

# Task 6: pow()
# Given:

base = 4
exponent = 3

# print:
# The result of raising base to the power of exponent using pow()
# The result of the same calculation using the ** operator

print(pow(base, exponent))
print(base ** exponent)

# Task 7: min(), max() and sum()
# Given:

scores = [78, 95, 84, 67, 91]

# Write code to print 
# The lowest score
# The highest score
# The total of all score

print(f"Lowest Score: {min(scores)}")
print(f"Highest Score: {max(scores)}")
print(f"Total Score: {sum(scores)}")

# Task 8: Combination of several functions in one Task
# Given:

prices = [199.99, 250.50, 149.75, 300.20, 99.99]

# Print:
# The highest price
# The lowest price
# The total price
# The total, rounded to 2 decimal places

print(f"Highest Price: {max(prices)}")
print(f"Lowest Price: {min(prices)}")
print(f"Total Price: {sum(prices)}")
print(f"Rounded Total: {round(sum(prices), 2)}")