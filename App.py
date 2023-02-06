# Implementing the interactivity with the user

import re

print("Welcome to a text-based adventure game called Beta, please enter your name")
name = input("")
x = re.findall("[A-Za-z]", name)
if x:
  print("Hi",name)       
else:
  print("Enter letters only !!")

# User enters their's name

