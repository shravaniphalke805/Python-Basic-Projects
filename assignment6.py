
# Q1. Creating Lists
# a) A list of 5 integers directly
integer = [10, 20, 30, 40, 50]

# b) Empty lists using [] and list()
empty1 = []          # Using square brackets
empty2 = list()      # Using the list() constructor

# c) A list containing mixed data types
mixed_list = [25, "Python", 3.14, True]

# d) A list of 7 zeros using repetition (*)
zero_list = [0] * 7

# Printing all lists with clear labels
print("a) List of 5 integers:", integer)

print("b1) Empty list using []:", empty1)
print("b2) Empty list using list():", empty2)

print("c) Mixed data type list:", mixed_list)

print("d) List of 7 zeros using repetition (*):", zero_list)


# Q2. Indexing and Negative Indexing

# Creating the list
fruits = ["apple", "banana", "mango", "orange", "grape"]

# Printing required items
print("First item:", fruits[0])          # Index 0
print("Third item:", fruits[2])          # Index 2
print("Last item:", fruits[-1])          # Negative index -1
print("Second last item:", fruits[-2])   # Negative index -2

# Taking index input from the user
index = int(input("Enter an index number: "))

# Basic index handling
if -len(fruits) <= index < len(fruits):
    print("Item at index", index, "is:", fruits[index])
else:
    print("Invalid index!")


# Q3. Slicing Lists

# Given list
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# a) First 4 elements
# Syntax: list[start:end]
# Starts from index 0 and goes up to index 4 (not included)
print("a) First 4 elements:", numbers[:4])

# b) Last 3 elements
# Negative slicing starts from the end of the list
print("b) Last 3 elements:", numbers[-3:])

# c) Elements from index 2 to 7
# Includes index 2 and excludes index 8
print("c) Elements from index 2 to 7:", numbers[2:8])

# d) Every second element
# Syntax: list[start:end:step]
# Step = 2 means take every second element
print("d) Every second element:", numbers[::2])

# e) Entire list in reverse order
# Step = -1 reverses the list
print("e) Entire list in reverse order:", numbers[::-1])

# Q4. Modifying Lists

# Creating the list
colors = ["red", "blue", "green", "yellow"]

# Original list
print("Original list:", colors)

# Change "blue" to "purple" using indexing
colors[1] = "purple"
print("After changing 'blue' to 'purple':", colors)

# Change the last item to "black" using negative indexing
colors[-1] = "black"
print("After changing the last item to 'black':", colors)


# Q5. append() and insert()

# Start with an empty list
cities = []

# Take user input for at least 2 cities
city1 = input("Enter first city: ")
city2 = input("Enter second city: ")

# Add cities using append()
cities.append(city1)
cities.append(city2)
cities.append("Mumbai")
cities.append("Delhi")
cities.append("Chennai")

# Display list after appending 5 cities
print("List after append operations:", cities)

# Add one more city at position 2 (index 2)
new_city = input("Enter a city to insert at position 2: ")
cities.insert(2, new_city)

# Print the final list
print("Final list after insert operation:", cities)


# Q6. remove(), pop(), and clear()

# Create the list
items = [10, 20, 30, 20, 40, 50]

print("Original list:", items)

# a) Remove the first occurrence of 20 using remove()
# remove(value) removes the first matching value from the list
items.remove(20)
print("After remove(20):", items)

# b) Remove the item at index 3 using pop()
# pop(index) removes and returns the element at the specified index
removed_item = items.pop(3)
print("Removed item at index 3:", removed_item)
print("List after pop(3):", items)

# c) Remove the last item using pop()
# pop() without an index removes and returns the last element
last_item = items.pop()
print("Removed last item:", last_item)
print("List after pop():", items)

# d) Clear the entire list using clear()
# clear() removes all elements from the list
items.clear()
print("List after clear():", items)


# Q7. index() and count()

# Create the list
scores = [85, 92, 78, 92, 65, 92, 88]

# Find and print the index of the first occurrence of 92
first_index = scores.index(92)
print("First occurrence of 92 is at index:", first_index)

# Count and print how many times 92 appears
count_92 = scores.count(92)
print("92 appears", count_92, "times in the list")

# Take a number as input from the user
num = int(input("Enter a number to search: "))

# Check if the number exists in the list
if num in scores:
    print(num, "exists in the list.")
    print("First index:", scores.index(num))
    print("Count:", scores.count(num))
else:
    print(num, "does not exist in the list.")


# Q8. sort() and reverse()

# Create the list
marks = [45, 78, 65, 90, 34, 82, 71]

print("Original list:", marks)

# Sort the list in ascending order
# sort() arranges the elements in increasing order
ascending_marks = marks.copy()  # Create a copy to preserve the original list
ascending_marks.sort()
print("Ascending order:", ascending_marks)

# Sort the list in descending order
# sort(reverse=True) arranges the elements in decreasing order
descending_marks = marks.copy()
descending_marks.sort(reverse=True)
print("Descending order:", descending_marks)

# Reverse the original list (without sorting)
# reverse() only changes the order of elements as they currently appear
reversed_marks = marks.copy()
reversed_marks.reverse()
print("Reversed original list:", reversed_marks)


# Q9. extend() vs append()

# Create two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# a) Using extend() to add list2 to list1
# extend() adds each element of list2 individually to list1
list_extend = list1.copy()
list_extend.extend(list2)

print("Result using extend():", list_extend)

# b) Using append() to add list2 to a copy of list1
# append() adds list2 as a single element at the end of the list
list_append = list1.copy()
list_append.append(list2)

print("Result using append():", list_append)


# Q10. Mini Project - Student Marks Manager

# Create an empty list to store marks
marks = []

# Take 5 subject marks as input from the user
for i in range(5):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

# Print the list of marks
print("\nMarks entered:", marks)

# Add one more subject mark using append()
extra_mark = float(input("Enter marks for an additional subject: "))
marks.append(extra_mark)

# Print updated list
print("Updated marks list:", marks)

# Find and print the highest and lowest marks
highest_mark = max(marks)
lowest_mark = min(marks)

print("Highest mark:", highest_mark)
print("Lowest mark:", lowest_mark)

# Sort the marks in descending order
marks.sort(reverse=True)
print("Marks sorted in descending order:", marks)

# Calculate and print the average marks
average_marks = sum(marks) / len(marks)
print("Average marks:", average_marks)

# Display total number of subjects
print("Total number of subjects:", len(marks))



