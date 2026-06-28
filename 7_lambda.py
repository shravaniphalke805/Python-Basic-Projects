# Lambda + range() + Lists + Exception Handling
try:
    # Lambda function to calculate square of a number
    square = lambda x: x ** 2

    # Generate numbers from 1 to 20 using range()
    numbers = range(1, 21)

    # Store squares in a list using lambda function
    squares = []

    for num in numbers:
        squares.append(square(num))

    # Print all squares
    print("Squares of numbers 1 to 20:")
    print(squares)

    # Print only even squares
    even_squares = []

    for value in squares:
        if value % 2 == 0:
            even_squares.append(value)

    print("\nEven Squares:")
    print(even_squares)

except Exception as e:
    print("An error occurred:", e)
