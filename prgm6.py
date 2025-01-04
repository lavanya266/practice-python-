#6. Python Program to Find the Sum of Digits in a Number.

num= int(input("enter numbers\n"))

sum=0

while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10

print("sum is",sum)