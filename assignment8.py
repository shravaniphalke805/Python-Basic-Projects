# Q1. Creating Sets
# a) A set with 5 integers
integers = {10, 20, 30, 40, 50}

# b) A set with mixed data types (integer, string, float)
set_mixed = {100, "Python", 3.14}

# c) An empty set using the correct method
# {} creates an empty dictionary, not a set.
# Therefore, set() must be used to create an empty set.
emptyset = set()

# d) A set from the string "hello" using the set() constructor
string = set("hello")

# Printing the sets and their types
print("Set with 5 integers:", integers)
print("Type:", type(integers))
print("\nSet with mixed data types:", set_mixed)
print("Type:", type(set_mixed))
print("\nEmpty set:", emptyset)
print("Type:", type(emptyset))
print("\nSet created from 'hello':", string)
print("Type:", type(string))

# Sets automatically remove duplicate values because they store only unique elements.
# For example, in the string "hello", the letter 'l' appears twice,
# but when converted to a set, it appears only once.
# Output may look like: {'h', 'e', 'l', 'o'}


# Q2. Characteristics of Sets
# Creating a set with duplicate values
numbers = {10, 20, 30, 20, 40, 10, 50}

# Printing the set
print("Set:", numbers)

# Observe:
# Duplicate values (20 and 10) are automatically removed.
# Output will contain only unique elements.
# Demonstrating that sets are unordered
print("First print :", numbers)
print("Second print:", numbers)
print("Third print :", numbers)

# Sets are unordered, which means elements do not have fixed positions.
# The order may not be the same as the order in which elements were entered.

# Trying to access the first element using indexing
try:
    print(numbers[0])
except TypeError as e:
    print("Error:", e)

# Explanation:
# Sets do not support indexing because they are unordered collections.
# Since elements do not have positions like lists or tuples,
# numbers[0] results in:
# TypeError: 'set' object is not subscriptable


# Q3. Membership Testing
# Taking 5 colors as input from the user
colors = set()

for i in range(5):
    color = input(f"Enter color {i+1}: ")
    colors.add(color)

# Display the set of colors
print("Colors Set:", colors)

# Asking the user to enter a color to search
search_color = input("Enter a color name to check: ")

# Checking membership using 'in' and 'not in'
if search_color in colors:
    print(search_color, "is present in the set.")
else:
    print(search_color, "is not present in the set.")

# Using 'not in'
if search_color not in colors:
    print("Confirmed:", search_color, "is not in the set.")
else:
    print("Confirmed:", search_color, "is in the set.")


# Q4. Create the set
fruits = {'apple', 'banana', 'mango'}
print("set:", fruits)

# a) Add 'orange' using add()
fruits.add('orange')
print("After adding 'orange':", fruits)

# b) Add 'banana' again
fruits.add('banana')
print("After adding 'banana' again:", fruits)

# c) Remove 'mango' using remove()
fruits.remove('mango')
print("After removing 'mango':", fruits)

# d) Try to remove 'grape' using discard()
fruits.discard('grape')
print("After discarding 'grape':", fruits)


# Q5. pop() and clear()
s = {100, 200, 300, 400, 500}
print("Original set:", s)

# pop() removes and returns an arbitrary element from the set
popped_element = s.pop()
print("Popped element:", popped_element)

# Print the set after popping
print("Set after pop():", s)

# clear() removes all elements from the set
s.clear()

# Print the final empty set
print("Set after clear():", s)

# Difference between remove(), discard(), and pop():
# remove(x):
# Removes the specified element x.
# Raises a KeyError if x is not present in the set.
# discard(x):
# Removes the specified element x if it exists.
# Does NOT raise an error if x is not present.
# pop():
# Removes and returns an arbitrary element from the set.
# Raises a KeyError if the set is empty.


# Q6.update() and copy()

# Create two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}

# Make a copy of set1
set1_copy = set1.copy()

# Update set1 with elements from set2
set1.update(set2)

# Print the original copy and the updated set
print("Original copy of set1:", set1_copy)
print("Updated set1:", set1)


# Q7.Union and Intersection

# Create two sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union: Combines all unique elements from both sets
print("Union using union():", A.union(B))

# Union using | operator
print("Union using | :", A | B)

# Intersection: Returns only the elements common to both sets
print("Intersection using intersection():", A.intersection(B))

# Intersection using & operator
print("Intersection using & :", A & B)

# Q8. (Combined Methods)

# Take 6 numbers as input from the user and store them in a set
numbers = set()

for i in range(6):
    num = int(input(f"Enter number {i+1}: "))
    numbers.add(num)  # Duplicates are automatically ignored

# Add two more numbers using add()
num1 = int(input("Enter first number to add: "))
num2 = int(input("Enter second number to add: "))

numbers.add(num1)
numbers.add(num2)

# Remove one number safely using discard()
remove_num = int(input("Enter a number to remove: "))
numbers.discard(remove_num)  # No error if the number is not present

# Print the final set and its length
print("Final set:", numbers)
print("Length of the set:", len(numbers))

# Q9. (Practical Application)

# List of student scores
scores = [85, 92, 78, 92, 85, 88, 95, 78]

# Convert the list to a set to remove duplicates
unique_scores = set(scores)

# Print the unique scores
print("Unique scores:", unique_scores)

# Convert the set back to a sorted list
sorted_scores = sorted(unique_scores)

# Print the sorted list
print("Sorted unique scores:", sorted_scores)

# Print the total number of unique scores
print("Total number of unique scores:", len(unique_scores))


# Q10.Mini Project - Combined Concepts
# Unique Item Collector using Sets
# Create an empty set to store unique items
items = set()

while True:
    # Display menu
    print("\n===== Unique Item Collector =====")
    print("1. Add item")
    print("2. Remove item")
    print("3. Show all unique items")
    print("4. Check if an item exists")
    print("5. Clear all items")
    print("6. Exit")

    # Take user choice
    choice = input("Enter your choice (1-6): ")

    # Option 1: Add item
    if choice == "1":
        item = input("Enter an item to add: ")
        items.add(item)  # Duplicates are ignored automatically
        print(f"'{item}' added successfully.")

    # Option 2: Remove item safely using discard()
    elif choice == "2":
        item = input("Enter an item to remove: ")
        items.discard(item)  # No error if item does not exist
        print(f"'{item}' removed (if it existed).")

    # Option 3: Show all unique items
    elif choice == "3":
        if len(items) == 0:
            print("No items in the collection.")
        else:
            print("Unique items:", items)

    # Option 4: Check if an item exists
    elif choice == "4":
        item = input("Enter an item to check: ")
        if item in items:
            print(f"'{item}' exists in the collection.")
        else:
            print(f"'{item}' does not exist in the collection.")

    # Option 5: Clear all items
    elif choice == "5":
        items.clear()
        print("All items have been cleared.")

    # Option 6: Exit the program
    elif choice == "6":
        print("Exiting the program. Goodbye!")
        break

    # Handle invalid choices
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")