# word_list = ["ardvark" , "baboon" , "camel"]
from  hangman_words import word_list

import random
Logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(Logo)

stages = ['''
  +---+
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

chosen_word = random.choice(word_list)

# print("chosen_word = " , chosen_word)
end_of_the_game = False
lives = 6

display = [ ]
for _ in range(len(chosen_word)):
    display += "_"
# print(display)

while not end_of_the_game:
    guess = input("Guess the letter: ").lower()
    
    if guess in display:
        print(f"{guess} is already in display ")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"{guess} not in the chosen_word , You loose a life")
        lives -= 1
        if lives == 0:
            end_of_the_game = True
            print(f"You Lose.\nChosen word = {chosen_word}")
        
    print(f"{' '.join(display)}")  

    if "_" not in display:
        end_of_the_game = True
        print("You Won")
    
    print(stages[lives])