# Implementing the interactivity with the user

import re
import random
import Role1
import Role2
import Game

print("Welcome to a text-based adventure game called Beta, This game is based upon luck of the dice that being said please enter your name")
name = input("")
x = re.findall("[A-Za-z]", name)
if x:
  print("Hi",name, "oh you also need to pick a role for today's adventure :D")       
else:
  print("Please enter alphabetical letters only")

# User enters their's name

print("So {} you have to pick between a cop or a robber" .format(name))

character = input("")

while(character != "cop" or "robber"):
        if (character =="cop"):
          print("Here are the benefits of being a cop")
          print(Role1.cop())
          break
      
      
        elif (character == "robber"):
              print("Here are the benefits of being the robber") 
              print(Role2.RoleNumero2.robber())
              break
        else: 
          print("Invalid Statement")
          break
  
   
   
x = Game.diceThrown()  
        
if (character == "cop"):
  print("Stage one")
  print(x)
  
