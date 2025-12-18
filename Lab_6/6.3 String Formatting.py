# 6.3 String formatting
# Using f string for formatting
name = "Samuel"
age = 25
department = "Computer Science"

print(f"My name is {name}, I am {age} years old, and I study {department}.")

name = "Ada"
score = 95.6

print("Student: {}, Score: {:.2f}".format(name, score))

# Using % Operator for formatting
name = "John"
age = 30
print("Name: %s, Age: %d" % (name, age))

print("\n--- 'in' and 'not in' operators ---")
# Print only if "free" is present:
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

# Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)

# print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
