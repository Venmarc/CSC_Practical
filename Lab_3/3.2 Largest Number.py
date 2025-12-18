# 3.2 Write a program to find the largest of three numbers
# Method 1: Using if-elif-else
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Determine the Largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("The largest number is:", largest)

# Method 2: Using max() function (Alternative logic mentioned in manual)
# a = int(input("A: "))
# b = int(input("B: "))
# c = int(input("C: "))
# print("Largest:", max(a, b, c))
