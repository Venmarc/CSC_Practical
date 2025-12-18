# 4.1 Multiplication table using for loop
n = int(input("Enter number: "))
for i in range(1, 13):
    print(f"{n} x {i} = {n*i}")

# Extra examples from manual (Loops) -- separating with comments
print("\n--- While Loop Examples ---")
print("Print i as long as i is less than 6:")
i = 1
while i < 6:
    print(i)
    i += 1

print("\nExit the loop when i is 3:")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

print("\nContinue to the next iteration if i is 3:")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
