
# 1)Basic Function 
# Define a function named welcome
def welcome():
     # Print a welcome message
     print('Welcome to Python Programming!')
# Call the function
welcome()
 
# 2)Function with Parameter
def greet(name):
     print("Hello",name +"!", "Welcome back")
greet("Shravani")
greet("Shreya")
greet("Arya")
greet("Ganesh")
greet("Shruti")

# 3)Default Parameter
# Function with a default parameter
def show_message(message="Hello"):
    print(message)

# Call the function without passing an argument
show_message()

# Call the function with a different message
show_message("Welcome to Python Programming!")

# Benefit of default parameters:
# They allow a function to work even when no argument is provided,
# making the function more flexible and reducing the need to pass
# common values every time it is called.

# 4)Function with Multiple Parameters & Return

# Function definition
def calculate_sum(a, b):
    return a + b
# Function call and storing result
result = calculate_sum(10, 20)
# Printing result
print("Sum =", result)

# Same Program using print() inside function
def calculate_sum(a, b):
    print("Sum =", a + b)
result = calculate_sum(10, 20)
print("Returned value:", result)

# 5)Positional vs Keyword Arguments
# Function that takes two parameters and prints student information
def student_info(name, age):
    print("Name:", name)
    print("Age:", age)
    print()

# 1. Using positional arguments
# (Values are passed in order)
student_info("Amit", 20)

# 2. Using keyword arguments
# (Values are passed using parameter names)
student_info(age=22, name="Shravani")

# 6)Function with Return Value
# Function to calculate square
def square(num):
    return num * num

# Function to calculate cube
def cube(num):
    return num * num * num

# Main program
# Taking input from user
num = int(input("Enter a number: "))

# Calling functions and storing results
sq = square(num)
cb = cube(num)

# Printing results
print("Square =", sq)
print("Cube =", cb)

# 7)Recursion - Basic
# Recursive function to print countdown from n to 1
def countdown(n):
    # Base case (stopping condition)
    if n == 0:
        return
    # Print current number
    print(n)
    # Recursive call (function calls itself with smaller value)
    countdown(n - 1)
# Calling the function
countdown(10)

# 8)Recursion - Factorial
# Recursive function to calculate factorial
def factorial(n):
    # Base case: factorial of 0 or 1 is 1 (stopping condition)
    if n == 0 or n == 1:
        return 1
    
    # Recursive case
    return n * factorial(n - 1)

# Taking input from user
num = int(input("Enter a number: "))

# Calling function and storing result
result = factorial(num)

# Printing result
print("Factorial =", result)

# 9)Scope - Local vs Global
# Global variable
total = 0

# Function to modify global variable
def add_value(x):
    global total   # accessing global variable
    total = total + x
    print("Total after adding", x, "=", total)

# Calling function multiple times
add_value(10)
add_value(20)
add_value(5)

# Local variable example
def demo():
    local_var = 100
    print("Inside function local_var =", local_var)
demo()

# Trying to access local variable outside function 
# print(local_var)

# 10)Mini Project - All Concepts

# Function to take input from user
def get_number():
    return int(input("Enter a number (0 to stop): "))
# Function to check even or odd
def is_even(num):
    return num % 2 == 0
# Function to calculate power (default exponent = 2)
def power(base, exp=2):
    return base ** exp
# Function to display result
def show_result(num):
    if is_even(num):
        print(num, "is Even")
    else:
        print(num, "is Odd")
    print("Square =", power(num))  # default exponent used as 2
    print()
# Main program (loop until user enters 0)
while True:
    num = get_number()
    # stop condition
    if num == 0:
        print("Program stopped.")
        break  
    show_result(num)