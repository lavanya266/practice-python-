#20. Python Program to Take in Two Strings and Display the Larger String without Using Built-in
#Functions.

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

length1 = 0
length2 = 0

for char in string1:
    length1 += 1

for char in string2:
    length2 += 1

if length1 > length2:
    print(f"The larger string is: {string1}")
elif length2 > length1:
    print(f"The larger string is: {string2}")
else:
    print("Both strings are of equal length.")
