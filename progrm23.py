#23. Python Program to check whether a full pattern (not sub string) is present in the given sentence.

sentence=input("enter the sentence")
pattern=input("enter pattern")

if sentence.strip()==pattern.strip():
    print("matches")
else:
    print("not matched")

#exrea spaces from front and end are removed
