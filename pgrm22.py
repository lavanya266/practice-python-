# 22. Python Program to Calculate the Number of Digits and Letters in a String.

string=input("enter a string :")
digit_count=0
letter_count=0

for char in string:
    if '0' <= char <='9':
        digit_count+=1
    elif 'a'<= char <='z' or 'A'<=char<='Z':
        letter_count+=1


print(digit_count)
print(letter_count)