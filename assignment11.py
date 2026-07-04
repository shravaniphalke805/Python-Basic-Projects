#1
#simple try example
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = num1 / num2
    print("Division result:", result)

except ValueError:
    print("Error: Please enter valid numeric values.")

#2
#Handling ZeroDivisionError
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = num1 / num2
    print("Division result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid numeric values.")

#3
try:
    # Convert string to integer
    num = int(input("Enter an integer: "))

    # Perform division
    divisor = int(input("Enter a divisor: "))
    result = num / divisor

    print("Division result:", result)

except ValueError:
    print("Error: Invalid input. Please enter valid integers.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

#4
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = num1 / num2
    print("Division result:", result)

except ValueError:
    print("Error: Please enter valid numeric values.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

else:
    print("Division performed successfully!")

#5
try:
    # Take input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform division
    result = num1 / num2
    print("Division result:", result)

except ValueError:
    print("Error: Please enter valid numeric values.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

else:
    print("Division performed successfully!")

finally:
    # The finally block always executes, whether an exception occurs or not.
    # It is commonly used for cleanup tasks such as closing files,
    # releasing resources, or displaying a final message.
    print("Program execution completed.")

#6
try:
    # Take input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform division
    result = num1 / num2
    print("Division result:", result)

except ValueError:
    print("Error: Please enter valid numeric values.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

else:
    # Executes only if no exception occurs
    print("Division performed successfully!")

finally:
    # Executes whether an exception occurs or not
    print("Thank you for using the division program!")

#7
try:
    # Take age as input and convert it to an integer
    age = int(input("Enter your age: "))

    # Check if age is negative
    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Your age is:", age)

except ValueError as e:
    print("Error:", e)


#8
try:
    # Take input from the user
    num = int(input("Enter a number: "))

    # Divide 100 by the entered number
    result = 100 / num

    print("Result:", result)

except (ValueError, ZeroDivisionError):
    print("Error: Please enter a valid non-zero number.")

#9
try:
    # Take input from the user and convert it to an integer
    num = int(input("Enter a number: "))

    # Divide 100 by the entered number
    result = 100 / num

    # Display the result
    print("Result:", result)

except ValueError:
    # Handles non-numeric input
    print("Please enter a valid number.")

except ZeroDivisionError:
    # Handles division by zero
    print("Error: Division by zero is not allowed.")

except Exception as e:
    # Handles any other unexpected errors
    print("Some error occurred:", e)


#10
while True:
    print("\nSimple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    try:
        choice = int(input("Enter your choice (1-5): "))
        if choice == 5:
            print("Exiting calculator. Thank you!")
            break
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        try:
            if choice == 1:
                result = num1 + num2
                print("Result:", result)
            elif choice == 2:
                result = num1 - num2
                print("Result:", result)
            elif choice == 3:
                result = num1 * num2
                print("Result:", result)
            elif choice == 4:
                result = num1 / num2
                print("Result:", result)
            else:
                print("Invalid choice. Please select between 1 and 5.")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")

        finally:
            # This block always executes after every calculation attempt
            print("Operation attempted.")

    except ValueError:
        # Handles invalid menu choices and non-numeric inputs
        print("Error: Please enter valid numeric input.")

