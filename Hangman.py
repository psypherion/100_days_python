import random
stages = [
'''  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

win = ['''
  +---+
  |   |
      |
 \O/  |
  |   |
 / \  |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = word_list[random.randint(0,len(word_list)-1)]
print('''
          Rules : 
                  NO. Of Lives is : 6
                  So, You can make 6 wrong Choices only.
''')
display = []
for i in range(0,len(chosen_word)):
    display.append("_")
print(f"The Length Of The Word You Have to Guess is : {len(chosen_word)}")
lives = 6
while "_"  in display :
  guess = input("Guess A Letter : ").lower()
  for i in range(0,len(chosen_word)):
    if guess == chosen_word[i]:
      display[i] = guess
  if guess  not in chosen_word:
    lives -= 1
    if lives == 0 :
      print("Game Over")
      break 
  if "_" not in display:
    end_of_game = True
    print("You win.")
    print(win[0])
    break
  print(f"{' '.join(display)}")
  print(stages[lives])
