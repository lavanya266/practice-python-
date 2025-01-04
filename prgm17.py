# 17. Python Program to Count the Number of Vowels in a String.

string=input("enter string")
vowels="aeiouAEIOU"
vowel_count=0
for char in string:
    if char in vowels:
        vowel_count=vowel_count+1
print(vowel_count)