#7. Python Program to Find the Smallest Divisor of an Integer.
num=int(input(("enter number\n")))
for i in range(2,20):
    if num%i==0:
        print(i)
        break