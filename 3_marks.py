# Lists + Functions + Exception Handling
def manage_marks():
    # Create an empty list to store marks
    marks = []

    # Take input for 5 subjects
    for i in range(5):
        while True:
            try:
                mark = float(input(f"Enter marks for Subject {i + 1}: "))
                marks.append(mark)
                break  # Exit the loop if input is valid
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

    # Calculate average marks
    average = sum(marks) / len(marks)

    # Find highest and lowest marks
    highest = max(marks)
    lowest = min(marks)

    # Sort marks in descending order
    marks.sort(reverse=True)

    # Display the results
    print("\nResults")
    print("Marks:", marks)
    print("Average Marks:", average)
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)
# Call the function
manage_marks()

