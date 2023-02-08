#Implements the data and logic associated with the first role
import Game
Strength = 0
Health = 0 
Intelligence = 0 

def cop():
        global Strength 
        Strength=3
        global Health
        Health = 3
        global Intelligence
        Intelligence = 1
        print("Cop's Attributes:","Strength=",Strength,"Health=",Health,"Intelligence=",Intelligence)
        Game.role1_health
        Game.role1_intelligence
        Game.role1_Strength

        
