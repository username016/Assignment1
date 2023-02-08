#Implements the data and logic associated with the second role
import Game
Strength = 0
Health = 0
Dexterity = 0

def robber():
    global Strength 
    Strength = 3
    global Health 
    Health = 3
    global Dexterity
    Dexterity = 2
    print("Robbers Attributes=","Strength=",Strength,"Health=",Health,"Dexterity=",Dexterity)
    Game.role2_Strength 
    Game.role2_Dexterity
    Game.role2_health
    