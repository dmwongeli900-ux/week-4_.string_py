# Name: DIANA MWONGELI
# Date: 20 March 2026
# Description: This program counts the frequency of each character in a string.
# It allows the user to choose case sensitivity and sorting method (by character or frequency).

# Accept user input string
input_text = input("Enter a string: ")

# Ask user if case sensitivity should be applied
case_option = input("Case sensitive? (yes/no): ").lower()

# Convert to lowercase if user selects 'no'
if case_option == "no":
    input_text = input_text.lower()

# Dictionary to store character counts
char_frequency = {}

# Count frequency of each character
# Using .get() avoids needing an if-else check
for character in input_text:
    char_frequency[character] = char_frequency.get(character, 0) + 1

# Ask user how to sort results
sort_choice = input("Sort by (char/freq): ").lower()

# Sort based on user choice
# If 'freq', sort by frequency value
# Otherwise, default to sorting by character (key)
if sort_choice == "freq":
    sorted_results = sorted(char_frequency.items(), key=lambda item: item[1])
else:
    sorted_results = sorted(char_frequency.items())

# Display results in table format
print("\nCharacter | Frequency")
print("----------------------")

for character, count in sorted_results:
    print(f"{character:^9} | {count:^9}")


# ---------------------------
# TEST CASES
# ---------------------------
# Example 1:
# Input: hello
# Case sensitive: no
# Sort: char
# Output:
# e | 1
# h | 1
# l | 2
# o | 1
