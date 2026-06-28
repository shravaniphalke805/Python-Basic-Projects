# Strings + Sets + Exception Handling + Modules
# Import math module
import math
try:
    # Take sentence input from user
    sentence = input("Enter a sentence: ")
    # Check for empty input
    if sentence.strip() == "":
        raise ValueError("Sentence cannot be empty.")
    # Convert sentence into words
    words = sentence.split()
    # Store unique words using set
    unique_words = set(words)
    # Sort and display unique words
    sorted_words = sorted(unique_words)
    print("\nUnique words in sorted order:")
    for word in sorted_words:
        print(word)
    # Count total unique words
    total_unique = len(unique_words)
    # Calculate number of unique words raised to power 2
    result = math.pow(total_unique, 2)
    print("\nTotal unique words:", total_unique)
    print("Unique words count raised to power 2:", result)
# Handle errors
except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("Unexpected error occurred:", e)
