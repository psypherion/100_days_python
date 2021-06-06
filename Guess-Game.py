logo = """      
   ____     _   _ U _____ u ____    ____           ____      _      __  __  U _____ u 
U /"___|uU |"|u| |\| ___"|// __"| u/ __"| u     U /"___|uU  /"\  uU|' \/ '|u\| ___"|/ 
\| |  _ / \| |\| | |  _|" <\___ \/<\___ \/      \| |  _ / \/ _ \/ \| |\/| |/ |  _|"   
 | |_| |   | |_| | | |___  u___) | u___) |       | |_| |  / ___ \  | |  | |  | |___   
  \____|  <<\___/  |_____| |____/>>|____/>>       \____| /_/   \_\ |_|  |_|  |_____|  
  _)(|_  (__) )(   <<   >>  )(  (__))(  (__)      _)(|_   \\    >><<,-,,-.   <<   >>  
 (__)__)     (__) (__) (__)(__)    (__)          (__)__) (__)  (__)(./  \.) (__) (__) 

"""
import random
a = random.randint(0,100)
print(logo)
mode = input("Easy OR Hard").lower()
def checker(count) :
  l =False
  while l == False:
    guess = int(input("Enter Your Guess : "))
    if guess > a :
      print("Too High")
      count -= 1
    elif guess < a:
      print("Too Low")
      count -= 1
    elif guess == a :
      print("Congrats! You've Guessed Correctly.")
      l = True
    if count == 0 :
      print("Sorry, You're Out of choices.")
      l = True
if mode == 'easy':
  count = 10
  checker(count)
elif mode == 'hard':
  count = 5
  checker(count)
