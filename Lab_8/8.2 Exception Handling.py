# 8.2 Write a program that takes numbers from a user and handles invalid input
# This is an exception Handling.
# Allow only numeric input, handle exceptions, and display result

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid number entered!")
