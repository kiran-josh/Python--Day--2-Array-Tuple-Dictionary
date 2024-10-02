"""

Name: Kiran G
Program: You have been given a list of N integers which represents the number of mangoes in a bag. 
Each bag has a variable number of mangoes. There are M students in a Guvi class, 
your task is to distribute the Mangoes in such a way that each students gets one Bag. 
The difference between the number of Mangoes in a bag with maximum Mangoes and Bag with minimum Mangoes given to the student is minimum?

"""




# Given list of mangoes in bags
mangoes = [12, 34, 67, 90, 45, 23, 78, 56]  # Example list
M = 4  # Number of students (bags to be selected)

# Sort the list of mangoes
mangoes.sort()

# Initialize minimum difference to a large value
min_diff = float('inf')

# Loop through the sorted list to find the minimum difference
for i in range(len(mangoes) - M + 1):
    # Current difference between max and min in the window of size M
    current_diff = mangoes[i + M - 1] - mangoes[i]
    # Update minimum difference
    if current_diff < min_diff:
        min_diff = current_diff

# Output the result
print("Minimum difference between max and min mangoes in bags:", min_diff)
