# 8.1 Read & Write content of file and display

# Open a file in write mode ('w')
with open("example.txt", "w") as file:
    file.write("Hello, this is my first file in Python!\n")
    file.write("Python makes file handling easy.\n")

print("Write to File: Try it yourself (Done)")

# Read from file
# Open file in read mode ('r')
with open("example.txt", "r") as file:
    content = file.read()

print("File content:")
print(content)

# Reading Line by Line
print("\nReading Line by Line:")
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip()) # strip() removes newline characters

# Appending to a File
print("\nAppending to a File:")
with open("example.txt", "a") as file:
    file.write("This line was appended later.\n")

# Verify append
with open("example.txt", "r") as file:
    print(file.read())
