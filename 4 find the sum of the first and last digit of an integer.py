"""
Name: Kiran G
Program: Write a python program to find the sum of the first and last digit of an integer?

"""

# Given integer
number = 12345  # You can change this to any integer

# Convert the number to a string to easily access digits
number_str = str(number)

# Get the first digit
first_digit = int(number_str[0])

# Get the last digit
last_digit = int(number_str[-1])

# Calculate the sum
digit_sum = first_digit + last_digit

# Output the result
print("Sum of the first and last digit:", digit_sum)
