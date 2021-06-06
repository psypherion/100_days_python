import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
img = [rock, paper, scissors]
comp = random.randint(0,3)
comp_ = img[comp - 1]
user = int(input(f"1.Rock \n 2.Paper \n 3.Scissors \n "))
user_ = img[user - 1]
print(comp_)
print(user_)
if user == comp+1 :
  print("You Win")
elif comp == 1 and user == 3 :
  print("Computer Wins")
elif user < comp :
  print("Computer Wins")
elif user == comp :
  print("Draw")
