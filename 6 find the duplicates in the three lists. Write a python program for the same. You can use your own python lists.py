"""

Name: Kiran G
Program: you have been given three lists. 
your task is to find the duplicates in the three lists. Write a python program for the same. You can use your own python lists?

"""

# Given lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [5, 8, 9, 10]

# Combine the lists
combined_list = list1 + list2 + list3

# Find duplicates
duplicates = set()
seen = set()

for item in combined_list:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

# Output the result
print("Duplicates in the three lists:", list(duplicates))
