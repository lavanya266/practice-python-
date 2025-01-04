# 19. Python Program to find the length of string without using any built-in functions


input_string = input("Enter a string: ")


length = 0

for char in input_string:
    length += 1

print(f"The length of the string is: {length}")
