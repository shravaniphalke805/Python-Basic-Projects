# Lambda Function
# Take a number as input from the user
num = int(input("Enter a Number:"))
# Lambda function to find the square of a number
square = lambda x: x**2
# Call the lambda function and print the result
print("Lambda Function:", square(num))

# Normal Function
# Define a function named square
def square(x):
    return x * x  # Return the square of x
print("Normal Function:", square(5))

# Comparison (Student Style)
# 1. Lambda function is written in one line.
# 2. Normal function is written using the def keyword.
# 3. Lambda is useful for simple and short tasks.
# 4. Normal function is better for large and complex programs."""

#Lambda with Multiple Arguments

# Take three numbers as input from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Lambda function to add three numbers
add_three = lambda a, b, c: a + b + c

# Print the sum
print("Sum =", add_three(a, b, c))


# For Loop Revision
# A for loop is used when we know how many times we want to repeat a task.
# a) Print all numbers from 1 to 25
print("Numbers from 1 to 25:")
for i in range(1, 26):
    print(i)

# b) Print the sum of all numbers from 1 to 20
sum = 0

# Use a for loop to add numbers one by one
for i in range(1, 21):
    sum += i

print("Sum of numbers from 1 to 20 =", sum)

# c) Print the table of 5 from 1 to 10
print("Table of 5:")

# Use a for loop to generate the multiplication table
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)

# Comments:
# 1. Use a for loop when you want to repeat a task multiple times.
# 2. It is useful when the number of repetitions is known.
# 3. range() generates a sequence of numbers for the loop.
# 4. for loops help reduce repetitive code.


# While Loop Revision

# A while loop is used when we do not know in advance how many times the loop will run.

# Initialize sum to 0
total = 0

# Ask user for first input
num = int(input("Enter a positive number (0 or negative to stop): "))

# Loop will continue until user enters 0 or negative number
while num > 0:
    total += num  # add number to total
    num = int(input("Enter a positive number (0 or negative to stop): "))

# Print final total sum
print("Total Sum =", total)


# Math Module Program
# Import math module
import math
# Take input from user
num = float(input("Enter a number: "))

# Square root (works for positive numbers)
print("Square Root:", math.sqrt(num))

# Ceiling value (rounds UP to nearest integer)
print("Ceiling Value:", math.ceil(num))

# Floor value (rounds DOWN to nearest integer)
print("Floor Value:", math.floor(num))

# Factorial (only if number is a whole number and >= 0)
if num >= 0 and num == int(num):
    print("Factorial:", math.factorial(int(num)))
else:
    print("Factorial: Not defined for this input")

# Comments:
# The math module is useful because it provides ready-made mathematical functions.
# It helps in calculations like square root, factorial, rounding, etc.
# It saves time and reduces coding errors.


# Random Module Program

# Import random module
import random
# Generate and print 5 random integers between 1 and 100
print("5 Random Integers (1 to 100):")
for i in range(5):
    print(random.randint(1, 100))

# Generate one random number between 50 and 150
print("One Random Number (50 to 150):")
print(random.randint(50, 150))

# Generate a random floating point number between 0 and 1
print("Random Float (0 to 1):")
print(random.random())


# Import Methods 
# Import entire math module
import math
print("Using import math:")
print("2 to the power 4 =", math.pow(2, 4))

# Import only sqrt function from math module
from math import sqrt
print("Using from math import sqrt:")
print("Square root of 25 =", sqrt(25))

# Import math module with alias
import math as m
print("Using import math as m:")
print("Factorial of 5 =", m.factorial(5))


# Main program

import mymodule

name = input("Enter your name: ")
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

mymodule.greet(name)

print("Power Result:", mymodule.calculate_power(base, exp))


# Function definition
def greet(name):
    print("Hello", name)

# This block runs only when file is executed directly
if __name__ == "__main__":
    # Take input from user
    user_name = input("Enter your name: ")
    
    # Call the function
    greet(user_name)
    
    # Extra code that runs only in main file
    print("This program is running directly")


# Mini Project - Simple Math Utility Program

import math
import random
# Lambda function to calculate square
square = lambda x: x * x
# Normal function using math module to calculate power
def power(base, exp):
    return math.pow(base, exp)
while True:
    print("\n--- SIMPLE MATH UTILITY ---")
    print("1. Square of a number")
    print("2. Power of a number")
    print("3. Random number (1 to 100)")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # Exit condition
    if choice == 4:
        print("Exiting program... Goodbye!")
        break

    # Square using lambda
    if choice == 1:
        num = int(input("Enter a number: "))
        print("Square =", square(num))

    # Power using normal function
    elif choice == 2:
        base = int(input("Enter base: "))
        exp = int(input("Enter exponent: "))
        print("Power =", power(base, exp))

    # Random number using random module
    elif choice == 3:
        print("Random Number:", random.randint(1, 100))

    else:
        print("Invalid choice! Please try again.")


