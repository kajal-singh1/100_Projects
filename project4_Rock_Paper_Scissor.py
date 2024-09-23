#Rock Paper Scissor
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
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")


#Interactive coding
 #Q1 Heads and Tails
# import random
# game = random.randint(0,1)

# print(game)
# if game == 1:
#     print("Heads")
# else:
#     print("Tails")

#Q2 Who Gonna Pay
# name_string = input("Give me everybody's names, seperated by comma.\n")
# names = name_string.split(",")
# data = type(names)
# print(data)
# items = len(names)
# choice = random.randint(0 , items-1)

# person_to_pay = names[choice]

# print(f"{person_to_pay} will pay the bill")

#Q3 Treasure Map Exercise
# row1 = [" " , " " , " "]
# row2 = [" " , " " , " "]
# row3 = [" " , " " , " "]
# map = [row1 , row2 , row3]
# print('map' , map)
# print(f"{row1}\n{row2}\n{row3}")
# position =input("Where do you want to put the treasure?")
# horizontal = int(position[0])
# print(horizontal)
# vertical = int(position[1])
# print(vertical)

# selected = map[vertical - 1]
# selected[horizontal - 1] = "x"

# print(f"{row1}\n{row2}\n{row3}")

