import random

# Enumeration for options
class options:
  Rock = 'r'
  Paper = 'p'
  Scissor = 's'

def game(comp, player):
    if(comp == player):
        return "Tie"
    elif(comp == 'r'):
        if (player == 's'):
            return "You Loose :("
        elif(player == 'p'):
            return "You win :D"
    elif(comp == 'p'):
        if (player == 'r'):
            return "You Loose :("
        elif(player == 's'):
            return "You win :D"
    elif(comp == 's'):
        if (player == 'p'):
            return "You Loose :("
        elif(player == 'r'):
            return "You win :D"


# Generates a random choice for comp
randomNo = random.randint(1, 3)
if randomNo == 1:
    comp = options.Rock
elif randomNo == 2:
    comp = options.Paper
elif randomNo == 3:
    comp = options.Scissor

# Take user input
while(True):
    p1 = str(input("Enter choice: Rock(r) Paper(p) or Scissor(s) ?\n"))
    if (p1 == 's') | (p1 == 'r') | (p1 == 'p'):
        break

print("Comp choice:", comp)
print("Your choice:", p1)
print(game(comp, p1))
