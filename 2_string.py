# Strings + Loops + Functions
def analyze_string(s):
    # Print length
    print("Length of the string:", len(s))

    # Print reverse of the string
    print("Reversed string:", s[::-1])

    # Count vowels (case insensitive)
    vowels = "aeiou"
    count = 0

    for char in s.lower():
        if char in vowels:
            count += 1

    print("Number of vowels:", count)

    # Print each character with positive and negative index
    print("\nCharacter Indexes:")
    for i in range(len(s)):
        print(f"Character: {s[i]}, Positive Index: {i}, Negative Index: {i - len(s)}")


# Take input from the user
text = input("Enter a string: ")

# Handle empty string case
if text == "":
    print("String cannot be empty.")
else:
    analyze_string(text)
