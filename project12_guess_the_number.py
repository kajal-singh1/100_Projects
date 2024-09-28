import random
from art_game_the_number import logo
print(logo)
attempts_easy = 10
attempts_hard = 5

def check_guess(guess , computer_chosen , attempts):
        if guess == computer_chosen:
            print ("Hurrey!! That's Right") 
            
        elif guess < computer_chosen:
            print("too low")
            return attempts - 1
        else:
            print("too high")
            return attempts - 1   

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return attempts_easy
    else:
        return attempts_hard

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'am thinking of a number between 1 to 100")

    computer_chosen = random.randint(1 , 100)
    attempts = set_difficulty()
    guess = 0
    while guess != computer_chosen:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess =  int(input("Make a guess: "))
        attempts = check_guess(guess , computer_chosen , attempts)
        if attempts == 0:
            print(f"you're run out of guesses , you lose. Actual_answer is {computer_chosen}")
            return
        elif guess != computer_chosen:
            print("Try Again")
play_game()