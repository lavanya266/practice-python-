#. Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String

# Input the string
input_string = input("Enter a string: ")

# Initialize counters for uppercase and lowercase letters
upper_count = 0
lower_count = 0

# Loop through each character in the string
for char in input_string:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

# Output the result
print(f"Number of uppercase letters: {upper_count}")
print(f"Number of lowercase letters: {lower_count}")
