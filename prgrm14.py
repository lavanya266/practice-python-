#14. Python program to print the lowest index in the string where substring sub is found within the string

string=input("enter string")
sub_string=input("enter sub string to find")

index=string.find(sub_string)

if(index!=-1):
    print("substring found at",index)
else:
    print("substring not found")