"""
Name: Kiran G
Program: write a python program to find the first non - repeating elements in a given list of integers?

"""

# Sample list of integers
numbers = [4, 5, 1, 2, 0, 4, 5, 1, 2]

# Create a dictionary to store the count of each number
count = {}

# Count the occurrences of each number
for num in numbers:
    count[num] = count.get(num, 0) + 1

# Find the first non-repeating element
first_non_repeating = None
for num in numbers:
    if count[num] == 1:
        first_non_repeating = num
        break

# Output the result
if first_non_repeating is not None:
    print(f"The first non-repeating element is: {first_non_repeating}")
else:
    print("There are no non-repeating elements.")
