# 7.2 Check for prime number using function
def is_prime(n):
    """Function to check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1): # Check divisibility up to sqrt(n)
        if n % i == 0:
            return False
    return True

# Take input from user
num = int(input("Enter a number: "))

# Check and display result
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
