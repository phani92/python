# Example to read and write a file

import random


def getScore():
    return random.randint(1, 1000)


# Take user input
score = getScore()
with open('files/highScore.txt') as f:
    highScore = int(f.read())

if score > highScore:
    with open('files/highScore.txt', 'w') as f:
      f.write(str(score))

with open('files/highScore.txt') as f:
  highScore = f.readline()
  print("High score is", highScore)
