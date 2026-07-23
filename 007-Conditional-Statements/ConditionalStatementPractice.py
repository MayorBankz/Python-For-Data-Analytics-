# Task 1: Basic if
# Given:

age = 20

# Write a program that prints
# You are an adult
# Only if age is greater than or equal to 18

if age > 18:
    print("You are an adult")
    
# Task 2: if....else
# Given:

age = 16

# Write a program that:
# Print "You're an adult". if age is 18 or older
# Otherwise, print "You're a minor"

if age >= 18:
    print("You're an adult")
else:
    print("You're a minor")
    
# Task 3: if....elif...else
# Given:

score = 72

# Write a program that prints
# "Excellent" if the score is 90 or above
# "Good" if the score is 70 to 89
# "Needs improvement" if the score is below 70

if score >= 90:
    print("Excellent")
elif score >= 70 and score <90:
    print("Good")
elif score < 70:
    print("Needs Improvement")

# Task 4: Multiple Conditions (and)
# Given

age = 25
has_id = True

# Write a program that:
# Prints "Access Granted" if the person is 18 or older AND has an id
# Otherwise, prints "Access Denied"

if age >= 18 and has_id:
    print("Access Granted")
else:
    print("Access Denied")

# Task 5: Using or
# Given:

is_admin = False
is_manager = True

# Write a program that:
# Prints "Access Granted" if the user is an admin OR a is_manager

if is_admin or is_manager:
    print("Access Granted")
else:
    print("Access Denied")
    
# Task 6: Combining "and" and "not"
# Given:

is_logged_in = True
is_banned = False

# Write a program that 
# prints "Welcome!" if the user is logged in AND is not banned 
# Otherwise print "Access Restricted"

if is_logged_in and not is_banned:
    print("Welcome!")
else:
    print("Access Restricted")

# Task 7: Real-Life Scenario
# Given:

username = "Mayowa"
password = "Python123"

# Write a program that:
# print "Login Successful" if:
# Username is "Mayowa" and
# password is "Python123" 
# Otherwise, print:
# "Invalid Username or Password"

if username == "Mayowa" and password == "Python123":
    print("Login Successful")
else:
    print("Invalid Username or Password")