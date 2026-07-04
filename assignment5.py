
# 1) String Indexing
# Take string input from the user
text = input("Enter a string: ")

# Positive indexing starts from 0 (left to right)
print("First character:", text[0])

# Negative indexing starts from -1 (right to left)
print("Last character:", text[-1])

# 3rd character from the start
# Index 2 because indexing begins at 0
print("3rd character from the start:", text[2])

# 2nd character from the end
# Index -2 because -1 is the last character
print("2nd character from the end:", text[-2])


# 2) String Slicing
# Take string input from the user
text = input("Enter a string: ")

# Slicing syntax: [start:end:step]
# start -> index where slicing begins
# end   -> index where slicing stops (not included)
# step  -> how many positions to move each time

# a) First 5 characters
print("First 5 characters:", text[:5])
# b) Last 4 characters
print("Last 4 characters:", text[-4:])

# c) String in reverse order
# step = -1 means move backwards
print("Reversed string:", text[::-1])

# d) Every 2nd character
# step = 2 means take every second character
print("Every 2nd character:", text[::2])


# 3) String Membership
# Take input from the user
main_string = input("Enter the main string: ")
substring = input("Enter the substring to search: ")

# Check if the substring is present in the main string
if substring in main_string:
    print("Substring found!")
else:
    print("Substring not found!")

# Demonstrating 'not in'
if substring not in main_string:
    print("The substring is not present in the main string.")
else:
    print("The substring is present in the main string.")


# 4) len() function
# Take a string input from the user
text = input("Enter a string: ")

# Find the length of the string
length = len(text)

# Print the length
print("Length of the string:", length)

# Print the last character using len()
print("Last character:", text[length - 1])

# Print the middle character if the length is odd
if length % 2 != 0:
    middle_index = length // 2
    print("Middle character:", text[middle_index])
else:
    print("The string length is even, so there is no single middle character.")

# Common mistakes with len():
# 1. Using text[len(text)] -> Error! Index out of range.
#    Last valid index is len(text) - 1.
# 2. Forgetting that indexing starts at 0.
# 3. Using len without parentheses:
#    len(text) is correct, but len is just the function name.

# 5) range()
# a) Print numbers from 0 to 10
print("Numbers from 0 to 10:")
for i in range(11):  # 0 to 10
    print(i, end=" ")

print("\n")

# b) Print numbers from 5 to 15
print("Numbers from 5 to 15:")
for i in range(5, 16):  # 5 to 15
    print(i, end=" ")

print("\n")

# c) Print odd numbers from 1 to 21
print("Odd numbers from 1 to 21:")
for i in range(1, 22, 2):  # Start at 1, step by 2
    print(i, end=" ")

# range(stop)
# Starts from 0 and goes up to (stop - 1)
# range(start, stop)
# Starts from 'start' and goes up to (stop - 1)
# range(start, stop, step)
# Starts from 'start', increases by 'step',
# and goes up to (stop - 1)

# 6) range() with a negative step

# Numbers from 20 down to 10
print("Numbers from 20 down to 10:")
for i in range(20, 9, -1):  # Start at 20, stop before 9, decrease by 1
    print(i, end=" ")

print("\n")

# Numbers from 15 down to 1 in steps of 2
print("Numbers from 15 down to 1 in steps of 2:")
for i in range(15, 0, -2):  # Start at 15, stop before 0, decrease by 2
    print(i, end=" ")


# 7) Strings + range() + len()

# Take a string input from the user
text = input("Enter a string: ")

# Print each character with its index
print("\nCharacters with their indices:")
for i in range(len(text)):
    print("Index", i, ":", text[i])

# Print the string in reverse order using range() with a negative step
print("\nString in reverse order:")
for i in range(len(text) - 1, -1, -1):
    print(text[i], end="")

# 8) membership in ranges

# Take a number as input from the user
num = int(input("Enter a number: "))

# Check if the number is present in range(1, 51)
if num in range(1, 51):
    print(f"{num} is present in range(1, 51).")
else:
    print(f"{num} is NOT present in range(1, 51).")

# Check if the number is present in range(10, 100, 5)
if num in range(10, 100, 5):
    print(f"{num} is present in range(10, 100, 5).")
else:
    print(f"{num} is NOT present in range(10, 100, 5).")


# 9) Slicing + range()
# 1) First 10 even numbers (2 to 20)
# Even numbers start from 2 and increase by 2
print("First 10 even numbers (2 to 20):")
for i in range(2, 21, 2):
    print(i, end=" ")

print("\n")

# 2) Numbers from 1 to 30 in steps of 3
# range(start, stop, step)
print("Numbers from 1 to 30 in steps of 3:")
for i in range(1, 31, 3):
    print(i, end=" ")

print("\n")

# 3) String slicing operations
text = "PythonProgramming"
print("Original string:", text)

# "Python" → first 6 characters
print("First word (Python):", text[:6])

# "Programming" → remaining part after index 6
print("Second word (Programming):", text[6:])

# Reverse the string using slicing
print("Reversed string:", text[::-1])


# 10) Mini Project: String Analyzer Program
# Take input from the user
text = input("Enter a string: ")

# Convert string to lowercase for case-insensitive search
lower_text = text.lower()

print("\n--- STRING ANALYSIS REPORT ---")

# 1. Length of the string
length = len(text)
print("1. Length of the string:", length)

# 2. First half and second half using slicing
mid = length // 2

# If length is odd, second half will include the middle character
first_half = text[:mid]
second_half = text[mid:]

print("2. First half:", first_half)
print("   Second half:", second_half)

# 3. Check if "python" is present (case-insensitive)
if "python" in lower_text:
    print("3. The word 'python' is present in the string.")
else:
    print("3. The word 'python' is NOT present in the string.")

# 4. Print characters with positive and negative indices using range()
print("\n4. Characters with indices:")
for i in range(length):
    print("Char:", text[i], "| Positive index:", i, "| Negative index:", i - length)

# 5. Print string in reverse
reversed_text = text[::-1]
print("\n5. Reversed string:", reversed_text)