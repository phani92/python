# A game to guess the number until guessed correctly by the user

import random

def genRandomNum():
    return random.randint(1, 10)


numToGuess = genRandomNum()
guess = False
guessCnt = 1
userInp = int(input("Guess the number\n"))

while(guess != True):
    if userInp > numToGuess:
        userInp = int(input("Guess a lower number please\n"))
        guessCnt = guessCnt + 1
    elif userInp < numToGuess:
        userInp = int(input("Guess a higher number please\n"))
        guessCnt = guessCnt + 1
    else:
        print(f"Winner!!!!\nThe number of guesses made: {guessCnt}")
        guess = True


## Saves the high score
with open('files/highScore.txt') as f:
    highScore = int(f.read())

if guessCnt < highScore:
    with open('files/highScore.txt', 'w') as f:
      f.write(str(guessCnt))

with open('files/highScore.txt') as f:
  highScore = f.readline()
  print("High score is", highScore)
