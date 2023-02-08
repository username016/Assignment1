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

def ChoosingCharacter():
 flag = True
 while flag:
        if (character == "cop"):
          print("Here are the benefits of being a cop")
          global cop 
          cop = Role1.cop()
          flag  = False
          
        elif (character == "robber"):
              print("Here are the benefits of being the robber") 
              global robber
              robber = print(Role2.robber())
              flag = False
        else: 
          print("Invalid Statement")
          flag = False
ChoosingCharacter()       
  
if (character == "cop"):
    print("Your fight is against the robber you fight for justice")
elif(character=="robber"):
    print("Your fight is against the cop your one fight away from freedom")
    
'''  
while True:
    age=input('Enter yes to roll again ')
    if age== ('yes'):
        break
    else:
        print('invalid') '''