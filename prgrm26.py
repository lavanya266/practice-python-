# 26. Write a program to generate 10 random integers between 1 to 20 (both inclusive).

import random

random_number=[random.randint(1,20) for i in range(10)]
print(random_number)