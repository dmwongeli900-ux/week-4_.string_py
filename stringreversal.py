# Name: DIANA MWONGELI
# Date: 20 March 2026
# Description: This program reverses a string using two methods:
# 1) Slicing method
# 2) Loop method

# Accept user input
input_text = input("Enter a string: ")

# Method 1: Using slicing

# [::-1] reverses the string by stepping backwards from end to start
reversed_text_slicing = input_text[::-1]

print("Reversed (Method 1 - Slicing):", reversed_text_slicing)


# -------------------------------
# Method 2: Using a loop
# -------------------------------
# Initialize empty string to store reversed result
reversed_text_loop = ""

# Loop through each character and place it at the front
# This builds the reversed string step by step
for character in input_text:
    reversed_text_loop = character + reversed_text_loop

print("Reversed (Method 2 - Loop):", reversed_text_loop)


# ---------------------------
# TEST CASES
# ---------------------------
# Example 1:
# Input: hello
# Output:
# olleh
# olleh

# Example 2:
# Input: Python
# Output:
# nohtyP
# nohtyP

# Example 3:
# Input: 12345
# Output:
# 54321
# 54321