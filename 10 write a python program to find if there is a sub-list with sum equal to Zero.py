"""
Name: Kiran G
Program: Given a list [4,2,-3,1,6] write a python program to find if there is a sub-list with sum equal to Zero.


"""

# Given list
numbers = [4, 2, -3, 1, 6]

# Initialize a set to store cumulative sums
cumulative_sums = set()
cumulative_sum = 0

# Check for sub-list with sum equal to zero
found_zero_sum_sublist = False

for num in numbers:
    cumulative_sum += num
    
    # Check if cumulative sum is zero or if it has been seen before
    if cumulative_sum == 0 or cumulative_sum in cumulative_sums:
        found_zero_sum_sublist = True
        break
    
    # Add the cumulative sum to the set
    cumulative_sums.add(cumulative_sum)

# Output the result
if found_zero_sum_sublist:
    print("There is a sub-list with sum equal to zero.")
else:
    print("There is no sub-list with sum equal to zero.")
