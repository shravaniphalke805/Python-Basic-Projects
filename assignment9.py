# Q1. Creating Dictionaries

# a) Empty dictionary using two different ways
# Method 1: Using {}
dict1 = {}

# Method 2: Using dict() constructor
dict2 = dict()

print("Empty Dictionary 1:", dict1)
print("Type:", type(dict1))

print("Empty Dictionary 2:", dict2)
print("Type:", type(dict2))

print()

# b) Dictionary with string keys (name, city, course)
# Syntax: {key: value, key: value, ...}
student = {
    "name": "Shravani Dipak Phalke",
    "city": "Pune",
    "course": "Python"}
print("Dictionary with String Keys:", student)
print("Type:", type(student))
print()

# c) Dictionary with integer keys
# Integer values are used as keys
numbers = {
    1: "One",
    2: "Two",
    3: "Three"}
print("Dictionary with Integer Keys:", numbers)
print("Type:", type(numbers))
print()

# d) Mixed data type dictionary
# Keys and values can have different data types
mixed_dict = {
    "name": "Shravani Dipak Phalke", # string value
    "age": 21,          # integer value
    "percentage": 88.5  # float value 
}
print("Mixed Data Type Dictionary:", mixed_dict)
print("Type:", type(mixed_dict))


# Q2. Accessing and Modifying Elements

# Create the dictionary
student = {
    "name": "Shravani Dipak Phalke",
    "age": 18,
    "city": "Pune",
    "marks": 80
}

# Print the value of "name" using square brackets
print("Name:", student["name"])

# Update the "marks" to 92
student["marks"] = 92

# Add a new key "grade" with value "A"
student["grade"] = "A"

# Print the updated dictionary
print("Updated Dictionary:", student)



# Q3. get(), keys(), values(), items()

# Create the dictionary
person = {
    "name": "Shravani Phalke",
    "age": 21,
    "profession": "Engineer"
}
# a) Using get() to access "age" and a non-existing key "salary"
print("Age:", person.get("age"))

# get() with a default value for a non-existing key
print("Salary:", person.get("salary", "Not Available"))

print()

# b) Print all keys using keys()
print("Keys:", person.keys())

print()

# c) Print all values using values()
print("Values:", person.values())

print()

# d) Print all key-value pairs using items()
print("Key-Value Pairs:", person.items())


# Q4. Nested Dictionary

# Create a nested dictionary
students = {
    "s1": {
        "name": "Rahul",
        "age": 20,
        "marks": 88
    },
    "s2": {
        "name": "Sneha",
        "age": 21,
        "marks": 95
    }
}
# Print the details of the first student
print("Details of First Student:")
print(students["s1"])

# Print the marks of the second student
print("Marks of Second Student:", students["s2"]["marks"])

# Add a new subject "math" with marks 90 for the first student
students["s1"]["math"] = 90

# Print the updated details of the first student
print("Updated First Student Details:")
print(students["s1"])


# Q5. update() and pop()

# Create the dictionary
info = {
    "brand": "Samsung",
    "model": "A52",
    "price": 25000
}

# Update the dictionary with new information
info.update({
    "color": "Black",
    "price": 24000
})

# Remove the key "model" using pop()
removed_value = info.pop("model")

# Print the removed value
print("Removed Value:", removed_value)

# Print the final dictionary
print("Final Dictionary:", info)


# Q6. popitem() and clear()

# Create a dictionary with 5 key-value pairs
student = {
    "name": "Shravani Phalke",
    "age": 20,
    "city": "Pune",
    "course": "Python",
    "marks": 88
}
print("Original Dictionary:", student)
# popitem() removes and returns the last inserted key-value pair
removed_item1 = student.popitem()
print("First Removed Item:", removed_item1)
# Remove another item using popitem()
removed_item2 = student.popitem()
print("Second Removed Item:", removed_item2)
print("Dictionary after popitem() twice:", student)
# Clear the entire dictionary
student.clear()
# Print the final result
print("Dictionary after clear():", student)
# Difference between pop() and popitem():
# pop(key) -> Removes a specific key and returns its value.
# Example: student.pop("age")
#
# popitem() -> Removes and returns the last inserted
# key-value pair as a tuple.
# Example: student.popitem()


# Q7. copy() and setdefault()

# Create a dictionary
d = {"a": 1, "b": 2}

# Make a copy of the dictionary
copy_d = d.copy()

# Use setdefault() to add key "c" with value 3
# It will add the key only if it does not already exist
d.setdefault("c", 3)

# Use setdefault() for an existing key "a"
# Since "a" already exists, its value will not be changed
d.setdefault("a", 100)

# Print the original and copied dictionaries
print("Original Dictionary:", d)
print("Copied Dictionary:", copy_d)


# Q8. fromkeys() and Membership

# Create a dictionary with keys and default value None
keys = ["name", "age", "city"]
person = dict.fromkeys(keys, None)

print("Initial Dictionary:", person)

# Take user input to fill the keys
person["name"] = input("Enter your name: ")
person["age"] = int(input("Enter your age: "))
person["city"] = input("Enter your city: ")

print("\nUpdated Dictionary:", person)

# Check if a given key exists using the in operator
check_key = input("\nEnter a key to check: ")

if check_key in person:
    print(f"Key '{check_key}' exists in the dictionary.")
else:
    print(f"Key '{check_key}' does not exist in the dictionary.")


# Q9. Practical Application - Contact Management using Dictionary

# Create an empty dictionary to store contacts
contacts = {}
# Take contact details as input
name = input("Enter Name: ")
phone = input("Enter Phone Number: ")
email = input("Enter Email: ")
# Store contact information with name as the key
contacts[name] = {
    "Phone": phone,
    "Email": email
} 
# Search for a contact using get()
search_name = input("\nEnter the name to search: ")
contact = contacts.get(search_name)
if contact:
    print("\nContact Found:")
    print("Phone:", contact["Phone"])
    print("Email:", contact["Email"])
else:
    print("\nContact not found.")
# Print all contacts using items()
print("\nAll Contacts:")
for name, details in contacts.items():
    print(f"Name: {name}")
    print(f"Phone: {details['Phone']}")
    print(f"Email: {details['Email']}")
    print("-" * 20)


# Q10. Mini Project - Student Management System

# Dictionary to store student records
students = {}

while True:
    print("\nStudent Management System")
    print("1. Add New Student")
    print("2. Update Marks of a Student")
    print("3. Search Student by Roll Number")
    print("4. Display All Students")
    print("5. Remove a Student")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    # 1. Add New Student
    if choice == "1":
        roll_no = input("Enter Roll Number: ")

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))

        students[roll_no] = {
            "name": name,
            "age": age,
            "marks": marks
        }

        print("Student added successfully!")
    # 2. Update Marks
    elif choice == "2":
        roll_no = input("Enter Roll Number: ")

        if roll_no in students:
            new_marks = float(input("Enter New Marks: "))
            students[roll_no]["marks"] = new_marks
            print("Marks updated successfully!")
        else:
            print("Student not found.")
    # 3. Search Student
    elif choice == "3":
        roll_no = input("Enter Roll Number to Search: ")

        student = students.get(roll_no)

        if student:
            print("\nStudent Details:")
            print("Name :", student["name"])
            print("Age  :", student["age"])
            print("Marks:", student["marks"])
        else:
            print("Student not found.")

    # 4. Display All Students
    elif choice == "4":
        if students:
            print("\nAll Student Records:")
            for roll_no, details in students.items():
                print(f"\nRoll No: {roll_no}")
                print(f"Name   : {details['name']}")
                print(f"Age    : {details['age']}")
                print(f"Marks  : {details['marks']}")
        else:
            print("No student records available.")

    # 5. Remove Student
    elif choice == "5":
        roll_no = input("Enter Roll Number to Remove: ")

        removed_student = students.pop(roll_no, None)

        if removed_student:
            print("Student removed successfully!")
        else:
            print("Student not found.")

    # 6. Exit
    elif choice == "6":
        print("Exiting Student Management System...")
        break

    # Invalid Choice
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")