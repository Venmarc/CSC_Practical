# 3.3 Write a script that calculates the area of a circle (Control Structures context)
r = float(input("Enter radius: "))

if r < 0:
    print("Error: Radius cannot be negative.")
else:
    area = 3.14159 * r * r
    print("Area of circle:", area)
