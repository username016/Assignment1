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
          Role1.cop()
          flag  = False
          
        elif (character == "robber"):
              print("Here are the benefits of being the robber") 
              print(Role2.robber())
              flag = False
              
        else: 
          print("Invalid Statement")
          flag = False
ChoosingCharacter()       
  


 
def chracterchosen():
        
  if (character == "cop"):
    print("Your fight is against the robber you fight for justice")
  elif(character=="robber"):
    print("Your fight is against the cop your one fight away from freedom")
chracterchosen()


  
while True:
    age=input('Enter yes to roll again ')
    if age== ('yes'):
        break
    else:
        print('invalid')

def Stage1():
  
  if(character == "cop"):
    print(Game.diceThrown())
    #print("1")
  elif(character == "robber"):
    print(Game.diceThrown())
    #print("2")
    
while True:
    age=input('Enter yes to roll again ')
    if age== ('yes'):
        break
    else:
        print('invalid')
        
def Stage2():
  if(character == "cop"):
    print(Game.diceThrown())
    #print("3")
  elif(character == "robber"):
    print(Game.diceThrown())
    #print("4")
    
  while True:
    age=input('Enter yes to roll again ')
    if age== ('yes'):
        break
    else:
        print('invalid')
        
def Stage3():
  if(character == "cop"):
    print(Game.diceThrown())
    #print("5")
  elif(character == "robber"):
    print(Game.diceThrown())
    #print("6")