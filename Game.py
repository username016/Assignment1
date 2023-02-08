#Implentation of the game data and logic

import random
import Role1 
import Role2
import App

role1_health = Role1.Health  
role2_health = Role2.Health
role1_intelligence = Role1.Intelligence
role2_Dexterity = Role2.Dexterity
role1_Strength = Role1.Strength
role2_Strength = Role2.Strength

def diceThrown():
    flag = True
    diceThrow = int(random.randrange(2,12))      # return an int,  from the range 2 of 12
    if (diceThrow in range(2,4)):
        print("Outcome: Critical Loss","(Note:) You rolled a",diceThrow)
        
        if(Role1.cop()):
           death = role1_health-role1_health
           death1 = role1_intelligence-role1_intelligence
           death2= role1_Strength-role1_Strength
           Role1.cop()
           print("You have died Health=",death, "Intelligence=",death1 ,"Strength=",death2)
           
        elif (Role2.robber()):  
            deathRole2 = role2_health - role2_health
            death1Role2= role2_Dexterity - role2_Dexterity
            death2Role2 = role2_Strength - role2_Strength
            Role2.robber()
            print("You have died Health=",deathRole2, "Dexterity=",death1Role2 ,"Strength=",death2Role2)
            
    elif (diceThrow in range(4,8)): 
        print("Outcome: Loss","(Note:) You rolled a",diceThrow)
        
        if(Role1.cop()):
           death = role1_health-role1_health
           death1 = role1_intelligence-role1_intelligence
           death2= role1_Strength-role1_Strength
           Role1.cop()
           print("You have been injured=",death, "Intelligence=",death1 ,"Strength=",death2)
           
        elif (Role2.robber()):
            deathRole2 = role2_health - 1
            death1Role2= role2_Dexterity - 1
            death2Role2 = role2_Strength - 1
            Role2.robber()
            print("You have gotten been injured Health=",deathRole2, "Dexterity=",death1Role2 ,"Strength=",death2Role2)
        
    elif (diceThrow in range(8,11)):
        print("Outcome: Win","(Note:) You rolled a", diceThrow)
        
        if(Role1.cop()):
           death = role1_health 
           death1 = role1_intelligence
           death2= role1_Strength
           Role1.cop()
           print("You have survived Health=",death, "Intelligence=",death1 ,"Strength=",death2)
           
        elif (Role2.robber()):
            deathRole2 = role2_health 
            death1Role2= role2_Dexterity 
            death2Role2 = role2_Strength
            Role2.robber() 
            print("You have survived Health=",deathRole2, "Dexterity=",death1Role2 ,"Strength=",death2Role2)
        
    else:
        print("Outcome: Critical Win","(Note:) You rolled a",diceThrow)
        
        if(Role1.cop()):
           death = role1_health + 1
           death1 = role1_intelligence + 1
           death2= role1_Strength + 1
           Role1.cop()
           print("You have gained one extra point for each attribute: Health=",death, "Intelligence=",death1 ,"Strength=",death2)
           
        elif (Role2.robber()):
            deathRole2 = role2_health + 1
            death1Role2= role2_Dexterity + 1
            death2Role2 = role2_Strength + 1
            Role2.robber()
            print("You have gained one extra point for each attribute: Health=",deathRole2, "Dexterity=",death1Role2 ,"Strength=",death2Role2)
        
diceThrown()