#Implentation of the game data and logic

import random
#import Role1
#import Role2
#import App
def diceThrown():
    diceThrow = int(random.randrange(2,12))      # return an int,  from the range 2 of 12
    if (diceThrow in range(2,4)):
        print("Outcome: Critical Loss","(Note:) You rolled a",diceThrow)
    elif (diceThrow in range(4,8)): 
        print("Outcome: Loss","(Note:) You rolled a",diceThrow)
    elif (diceThrow in range(8,11)): 
        print("Outcome: Win","(Note:) You rolled a", diceThrow)
    else:
        print("Outcome: Critical Win","(Note:) You rolled a",diceThrow)
diceThrown()