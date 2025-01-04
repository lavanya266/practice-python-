#28. Write a program to generate 10 random numbers between 1 to 100 such that there should one
# number between 1 to 10 one number between 11 to 20 etc.


import random
from turtledemo.penrose import start

ranges=[range(start,start+10) for start in range(1,100,10)]
random_numbers = [random.choice(r) for r in ranges]

print(random_numbers)