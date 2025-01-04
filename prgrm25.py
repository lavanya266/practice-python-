#25. Write a program to generate 10 random integers.

import  random

random_integers=[random.randint(1,100) for i in range(10)]
print(random_integers)

# random_number = random.randint(1, 100)
# print(f"Random number: {random_number}")
