# 5.3 Simple indexing and Slicing implementation
# Define a string
text = input("Enter a text: ")

# Indexing
# Note: This assumes the input text has at least one character.
if len(text) > 0:
    print("First character:", text[0])
    print("Last character:", text[-1])

    # Slicing
    print("First 6 characters:", text[0:6])
    print("Characters from index 7 to 12:", text[7:13])
    print("Every second character:", text[::2])
    print("Reversed string:", text[::-1])
else:
    print("You entered an empty string.")
