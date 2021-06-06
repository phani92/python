# Example to use reduce and find the maximum number from the list.

import random
from functools import reduce

# Populate list with random numbers
egList = [random.randint(1,1000) for i in range(1,100)]
# Reduce the list and find the max number
print(reduce(max,egList))
