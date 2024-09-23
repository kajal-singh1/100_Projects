#Poject_Treasure_Island

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")



#Iterative Coding

#Q1 Odd Or Even Exercise
# num = int(input("Enter the number = "))
# if num % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")

#Q2 BMI 2.0 Exercise
# weight = float(input("Enter the weight = "))
# height = float(input("Enter the height = "))
# BMI = round(weight / height **2)
# print("BMI = " , BMI)
# if BMI < 18.5:
#     print("underweight")
# elif  BMI < 25:
#     print("normal weight")
# elif BMI > 25 & BMI < 30:
#     print("overweight")
# elif BMI > 30 & BMI < 35:
#     print("Obese")
# else:
#     print("clinically obese")

#Q3 Leap Year Exercise
# year = int(input("Enter the year = "))
# if year % 4 == 0:
#     print("Leap Year")
# else:
#     print("Normal Year")

#Q4 Pizza Order
# print("Welcome to the pizza deliveries")
# pizza = input("What kind of Pizza do you want S , M , or L ")
# bill = 0
# if pizza == "S":
#     bill += 15
#     print(f"Price of your Pizza = ${bill}")
# elif pizza == "M":
#     bill += 20
#     print(f"Price of your Pizza = ${bill}")
# else:
#     bill += 25
#     print(f"Price of your Pizza = ${bill}")
# add_pepperoni = input("Do you want Pepperoni? Y or N ")
# if add_pepperoni == "Y":
#     if pizza == "S":
#         bill+= 2
#     else:
#         bill += 3
# extra_cheese = input("Do you want extra cheese? Y or N ")
# if extra_cheese == "Y":
#     bill += 1

# print(f"Total bill of the pizza = ${bill}")

# #Love Calculator
# print("Welcome to the love calculator!")
# name1 = input("What is your name? \n").lower()
# name2 = input("What is their name \n").lower()
 
# both_names = name1 + name2

# t = both_names.count('t')
# r = both_names.count('r')
# u = both_names.count('u')
# e = both_names.count('e')

# true = t + r + u + e

# l = both_names.count('l')
# o = both_names.count('o')
# v = both_names.count('v')
# e = both_names.count('e')

# love = l + o + v + e

# love_score = str(true) + str (love)
# print(love_score)
# ilove_score = int(love_score)

# if ilove_score < 10 or ilove_score > 90:
#     print(f"Your score is {love_score}, you go together like coke and mentos")
# elif ilove_score > 40 & ilove_score < 50:
#     print(f"Your score is {love_score}, you are alright together")
# else:
#     print(f"Your score is {love_score}")





