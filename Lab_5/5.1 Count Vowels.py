# 5.1 Input a sentence and count vowels
text = input("Enter text: ").lower()
vowels = "aeiou"
count = 0
for char in text:
    if char in vowels:
        count += 1
print("Vowel count:", count)
