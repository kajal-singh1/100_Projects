#Debugging consist of basic 6 steps as following

#1. Describe the Problem
#Bug Code
def fn():
    for i in range(1 , 20):
        if i == 20:
            print(f"{i}, You got it")
fn()

#Debugged Code
def fn():
    for i in range(1 , 21):
        if i == 20:
            print(f"{i}, You got it")
fn()


#Reproduce the code
#Bug Code
from random import randint
dice_imgs = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣']
dice_num = randint(1 , 6)
print(dice_imgs[dice_num])

#Debugged Code
from random import randint
dice_imgs = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣']
dice_num = randint(0 , 6)
print(dice_imgs[dice_num])


#Play Computer
#Bug Code
year = int(input("what's the year of your birth?"))
if year > 1980 and year < 1994:
    print("You are millenial")
elif year > 1994:
    print("You are a Gen Z.")

#Debugged Code
year = int(input("what's the year of your birth?"))
if year > 1980 and year < 1994:
    print("You are millenial")
elif year >= 1994:
    print("You are a Gen Z.")


#Fix the Errors
#Bug Code
age = input("How old are you?")
if age > 18:
    print("You can drive at age {age}")

#Debugged Code
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}")


#Print is your friend
#Bug Code
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = input("Number of words per page:")
total_words = pages * word_per_page
print(total_words)

#Debugged Code
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page:"))
total_words = pages * word_per_page
print(total_words)


#Use a debugger
#Bug Code
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)
mutate([1, 2, 3, 4, 8, 13])

#Debugged Code
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)

        print(b_list)

mutate([1, 2, 3, 4, 8, 13])




