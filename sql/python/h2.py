# Store a short paragraph using a multiline string
paragraph = """
Python is a powerful programming language. This Python course helps beginners
learn Python with hands-on examples and clear explanations.
"""

# 1. Display the length of the paragraph (number of characters)
length = len(paragraph)
print("Length of paragraph:", length)

# 2. Display the first and last characters
print("First character:", paragraph[0])
print("Last character:", paragraph[-1])

# 3. Slice and print a short preview (first 50 characters)
preview = paragraph[:50]
print("Preview:", preview)

# 4. Replace all occurrences of "Python" with "PYTHON"
replaced_text = paragraph.replace("Python", "PYTHON")
print("\nReplaced text:\n", replaced_text)

# 5. Convert to lowercase
lower_text = paragraph.lower()
print("\nLowercase text:\n", lower_text)

# 6. Remove extra whitespaces from start or end
trimmed_text = paragraph.strip()
print("\nTrimmed paragraph:\n", trimmed_text)

# 7. Split into individual words
word_list = trimmed_text.split()
print("\nList of words:", word_list)

# 8. Check if the word "course" exists
if "course" in trimmed_text.lower():
    print("\nThe word 'course' exists in the paragraph.")
else:
    print("\nThe word 'course' does NOT exist in the paragraph.")

# 9. Display final formatted message
final_message = "The course description is {} characters long and has {} words.".format(
    len(trimmed_text), len(word_list)
)
print("\n" + final_message)