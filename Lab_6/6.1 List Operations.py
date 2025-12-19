# 6.1 Write code to Add and remove elements in a list
# Part 1: Modify a list
user_input = input("Enter list items separated by space (e.g., apple banana): ")
my_list = user_input.split()

print(f"Current list: {my_list}")

item_to_add = input("Enter an item to add: ")
my_list.append(item_to_add)
print(f"List after adding '{item_to_add}': {my_list}")

item_to_remove = input("Enter an item to remove: ")
if item_to_remove in my_list:
    my_list.remove(item_to_remove)
    print(f"List after removing '{item_to_remove}': {my_list}")
else:
    print(f"Item '{item_to_remove}' not found in the list.")

print("-" * 20)

# Part 2: Remove duplicates
nums_input = input("Enter numbers with duplicates separated by space: ")
nums = nums_input.split() 
unique = list(set(nums))
print("Unique list:", unique)
