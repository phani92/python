# A game to guess the number until guessed correctly by the user

import random

numToGuess = 0
guessCnt = 0

# Saves the high score
def processWin():
    with open('files/highScore.txt') as f:
        highScore = int(f.read())

    if guessCnt < highScore:
        with open('files/highScore.txt', 'w') as f:
            f.write(str(guessCnt))

    with open('files/highScore.txt') as f:
        highScore = f.readline()
        print("High score is", highScore)

# Starts a new game
def startGame():
    numToGuess = random.randint(1, 10)
    guessCnt = 0

startGame()

while(True):
    userInp = input("Guess the number\n")
    if(userInp == 'q'):
        print("Thank you for playing the game")
        break

    try:
        if int(userInp) > numToGuess:
            print("Expected number is lower")
            guessCnt = guessCnt + 1
        elif int(userInp) < numToGuess:
            print("Expected number is higher")
            guessCnt = guessCnt + 1
        elif int(userInp) == numToGuess:
            print(f"Winner!!!!\nThe number of guesses made: {guessCnt}")
            processWin()
            startGame()
            print("Press 'q' to quit the game")

    except Exception as error:
        print("Please enter a number, there is an error {error}")
