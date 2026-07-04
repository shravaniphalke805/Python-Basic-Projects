# Q1. Creating Tuples
# a) A tuple with 5 numbers using parentheses
numbers = (10, 20, 30, 40, 50)
# b) A mixed tuple containing integer, string, float, and boolean
mixed = (25, "Python", 3.14, True)
# c) An empty tuple using two different ways
empty1 = ()
empty2 = tuple()

# d) A single-element tuple with the value 99
# Rule: A comma is required after the element.
# Without the comma, Python treats it as an integer, not a tuple.
single_element = (99,)

# Printing tuples and their types
print("Tuple with 5 numbers:", numbers)
print("Type:", type(numbers))

print("\nMixed Tuple:", mixed)
print("Type:", type(mixed))

print("\nEmpty Tuple 1:", empty1)
print("Type:", type(empty1))

print("\nEmpty Tuple 2:", empty2)
print("Type:", type(empty2))

print("\nSingle-element Tuple:", single_element)
print("Type:", type(single_element))


# Q2. Tuple Packing

# Creating a tuple without using parentheses (tuple packing)
person = "Shravani",18, "Pune"

# Printing the tuple and its type
print("Packed Tuple:", person)
print("Type:", type(person))

# Unpacking the tuple into separate variables
name, age, city = person

# Printing individual values
print("\nName:", name)
print("Age:", age)
print("City:", city)


# Q3. Indexing and Negative Indexing

# Creating the tuple
colors = ('red', 'green', 'blue', 'yellow', 'purple', 'orange')

# Printing required elements
print("First element:", colors[0])
print("Third element:", colors[2])
print("Last element:", colors[-1])
print("Second last element:", colors[-2])

# Taking index input from the user
index = int(input("Enter an index number: "))

# Printing the element at the given index
print("Element at index", index, "is:", colors[index])


# Q4. Slicing Tuples
# Creating the tuple
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Slicing Syntax:
# tuple[start : stop : step]
# start -> starting index (included)
# stop  -> ending index (excluded)
# step  -> increment/decrement value

# a) Elements from index 2 to 7
# Index 2 is included, index 8 is excluded
print("a) Elements from index 2 to 7:", numbers[2:8])

# b) First 5 elements
# Starts from the beginning and goes up to index 4
print("b) First 5 elements:", numbers[:5])

# c) Last 4 elements
# Starts 4 positions from the end
print("c) Last 4 elements:", numbers[-4:])

# d) Every second element
# Step value is 2
print("d) Every second element:", numbers[::2])

# e) The entire tuple in reverse order
# Step value -1 reverses the tuple
print("e) Tuple in reverse order:", numbers[::-1])


# Q5. Nested Tuples

# Creating a nested tuple (3x3 matrix)
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# Printing the first row
print("First row:", matrix[0])

# Printing the element at second row, third column
# Row index = 1, Column index = 2
print("Element at second row, third column:", matrix[1][2])

# Printing the element at third row, first column
# Row index = 2, Column index = 0
print("Element at third row, first column:", matrix[2][0])


# Q6. Iterating and Unpacking

# Creating the tuple
student = ('Shravani', 18, 'AIML', 'A')

# a) Iterate through the tuple using a for loop
print("Items in the tuple:")
for item in student:
    print(item)

# b) Unpack the tuple into four variables
name, age, branch, grade = student

# Print the unpacked values with descriptive messages
print("\nStudent Details:")
print("Name:", name)
print("Age:", age)
print("Branch:", branch)
print("Grade:", grade)

# Q7. count() Method

# Creating the tuple
grades = ('A', 'B', 'A', 'C', 'A', 'B', 'D', 'A', 'B')

# Counting occurrences of 'A'
print("Number of times 'A' appears:", grades.count('A'))

# Counting occurrences of 'B'
print("Number of times 'B' appears:", grades.count('B'))

# Taking a grade as input from the user
grade = input("Enter a grade: ")

# Counting and printing its occurrences
print("Number of times", grade, "appears:", grades.count(grade))


# Q8. index() Method

# Creating the tuple
fruits = ('apple', 'banana', 'cherry', 'banana', 'mango', 'apple')

# Finding the first index of 'banana'
print("First index of 'banana':", fruits.index('banana'))

# Finding the first index of 'banana' starting from index 2
print("First index of 'banana' from index 2:", fruits.index('banana', 2))

# Using try-except to safely find 'kiwi'
try:
    kiwi_index = fruits.index('kiwi')
    print("Index of 'kiwi':", kiwi_index)
except ValueError:
    print("Not found")


# Q9. Immutability of Tuples
# Creating the tuple
coordinates = (10, 20)
print("Original Tuple:", coordinates)

# Attempt 1: Change the first element
# Tuples are immutable, so this will cause an error.
# coordinates[0] = 100
# Error:
# TypeError: 'tuple' object does not support item assignment
# Attempt 2: Add a new element using append()
# Tuples do not have an append() method.
# coordinates.append(30)
# Error:
# AttributeError: 'tuple' object has no attribute 'append'
# Correct Way: Convert tuple to list, modify, and
# convert back to tuple
# Convert tuple to list
coord_list = list(coordinates)

# Modify the first element
coord_list[0] = 100

# Add a new element
coord_list.append(30)

# Convert back to tuple
coordinates = tuple(coord_list)
print("Modified Tuple:", coordinates)


# Q10. Mini Project - Student Record Program Using Tuples

# Taking input for Student 1
name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))

mark1 = int(input("Enter Subject 1 marks: "))
mark2 = int(input("Enter Subject 2 marks: "))
mark3 = int(input("Enter Subject 3 marks: "))

# Tuple Packing
# Stores all student information in a tuple

student_record = (name, roll_no, mark1, mark2, mark3)

# Printing the complete record

print("\nStudent Record")
print(student_record)

# Tuple Unpacking
name, roll_no, mark1, mark2, mark3 = student_record
print("\nUnpacked Record")
print("Name       :", name)
print("Roll No    :", roll_no)
print("Subject 1  :", mark1)
print("Subject 2  :", mark2)
print("Subject 3  :", mark3)

# Using count() method
# Check how many times a particular mark appears
search_mark = int(input("\nEnter a mark to count: "))
print("The mark", search_mark, "appears",
      student_record.count(search_mark), "time(s).")

# Creating another student record
student2 = ("Priya", 102, 88, 92, 88)
# Nested Tuple
# Stores multiple student records
students = (student_record,student2)

# Printing all student records
print("\nAll Student Records")
for student in students:
    print(student)

# Accessing specific values from nested tuple
print("\nAccessing Specific Values")
# First student's name
print("First Student Name:", students[0][0])
# First student's second subject marks
print("First Student Subject 2 Marks:", students[0][3])
# Second student's name
print("Second Student Name:", students[1][0])

# Second student's third subject marks
print("Second Student Subject 3 Marks:", students[1][4])


