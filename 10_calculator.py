# Import required modules
import math
import random
from datetime import datetime
# Dictionary to store calculation history
history = {}
# Function for basic arithmetic operations
def basic_arithmetic():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("\nChoose Operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = int(input("Enter choice: "))
        if choice == 1:
            result = num1 + num2
            operation = "Addition"
        elif choice == 2:
            result = num1 - num2
            operation = "Subtraction"
        elif choice == 3:
            result = num1 * num2
            operation = "Multiplication"
        elif choice == 4:
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2
            operation = "Division"
        else:
            print("Invalid operation.")
            return
        print("Result:", result)
        store_result(operation, result)
    except ValueError:
        print("Invalid input! Enter numbers only.")
    except ZeroDivisionError as e:
        print(e)

# Function for scientific calculations
def scientific_calculation():
    try:
        num = float(input("Enter number: "))
        print("\nScientific Options:")
        print("1. Square Root")
        print("2. Power")
        print("3. Factorial")
        choice = int(input("Enter choice: "))
        if choice == 1:
            if num < 0:
                raise ValueError("Cannot find square root of negative number.")
            result = math.sqrt(num)
            operation = "Square Root"
        elif choice == 2:
            power = int(input("Enter power: "))
            result = math.pow(num, power)
            operation = "Power"
        elif choice == 3:
            if num < 0:
                raise ValueError("Factorial not possible for negative numbers.")
            result = math.factorial(int(num))
            operation = "Factorial"
        else:
            print("Invalid choice.")
            return
        print("Result:", result)
        store_result(operation, result)
    except ValueError as e:
        print("Error:", e)

# Function to generate random numbers
def generate_random_numbers():
    try:
        numbers = []
        for i in range(5):
            numbers.append(random.randint(1, 100))
        print("Random Numbers:", numbers)
        store_result("Random Numbers", numbers)
    except Exception as e:
        print("Error:", e)

# Function to store results in dictionary with timestamp
def store_result(operation, result):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    history[time] = {
        "Operation": operation,
        "Result": result
    }
    print("Result saved successfully.")

# Function to view history
def view_history():
    if len(history) == 0:
        print("No history available.")
    else:
        print("\nCalculation History")
        for time, data in history.items():
            print("--------------------")
            print("Time:", time)
            print("Operation:", data["Operation"])
            print("Result:", data["Result"])

# Main menu program
while True:
    print("\n===== Smart Calculator & Data Manager =====")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculations")
    print("3. Generate Random Numbers")
    print("4. Store Results in Dictionary")
    print("5. View History")
    print("6. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            basic_arithmetic()
        elif choice == 2:
            scientific_calculation()
        elif choice == 3:
            generate_random_numbers()
        elif choice == 4:
            operation = input("Enter operation name: ")
            result = input("Enter result: ")
            store_result(operation, result)
        elif choice == 5:
            view_history()
        elif choice == 6:
            print("Exiting Calculator...")
            break
        else:
            print("Invalid choice. Select between 1-6.")
    except ValueError:
        print("Please enter a valid number.")

