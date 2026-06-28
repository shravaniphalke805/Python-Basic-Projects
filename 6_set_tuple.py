# Sets + Tuples + Modules
# Import required modules
import random
import math

# Create an empty set to store unique numbers
numbers = set()

# Take 10 numbers as input
for i in range(10):
    while True:
        try:
            num = int(input(f"Enter number {i + 1}: "))
            numbers.add(num)  # Set stores only unique values
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
try:
    # Convert the set to a tuple
    numbers_tuple = tuple(numbers)
    print("\nUnique Numbers (Tuple):", numbers_tuple)

    # Pick and print 3 random numbers from the tuple
    if len(numbers_tuple) >= 3:
        random_numbers = random.sample(numbers_tuple, 3)
        print("3 Random Numbers:", random_numbers)
    else:
        print("Less than 3 unique numbers available.")

    # Calculate the sum of tuple elements
    total = sum(numbers_tuple)

    # Print square root of the sum
    if total >= 0:
        print("Square Root of Sum:", math.sqrt(total))
    else:
        print("Cannot calculate square root of a negative number.")

# Handle any unexpected exceptions
except Exception as e:
    print("Error:", e)
