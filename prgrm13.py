#13. Python Program to print the number of occurrence of a sub string in a given string.

string=input("Enter string ")
sub_string=input("enter sub string ")

res=string.count(sub_string)
print(f"The substring '{sub_string}' occurs {res} times in the string.")
