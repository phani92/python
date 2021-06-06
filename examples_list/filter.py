## Example to use filter. Creates a list with numbers divisible by 5

import random

egList = [random.randint(1,10) for i in range(1,10)]
filList = list(filter(lambda a : a % 5 == 0,egList))
print(filList)
