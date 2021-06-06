# Example for enumerating a list

import random

# creates a list of 10 random numbers from 1 to 50
list1 = random.sample(range(1, 50), 10)

for index, element in enumerate(list1):
    if ((index == 4) or (index == 6) or (index == 8)):
        print(element)
