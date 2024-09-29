from art_higher_lower import logo , vs
from data_higher_lower import data
import random

import os
def clear():
    if os.name == 'nt':
        _ = os.system('cls')

def randomm():
    random_acc = random.choice(data)
    return random_acc

def format(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def userguess(guess , a_guess , b_guess):
    if a_guess > b_guess:
        return guess == "a"
    else:
        return guess == "b"
    
def play_game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = randomm()
    account_b = randomm()

    while game_should_continue:
        account_a = account_b
        account_b = randomm()

        while account_a == account_b:
            account_b = randomm()

        print(f"Compare A: {format(account_a)}.")
        print(vs)
        print(f"Against B: {format(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = userguess(guess, a_follower_count, b_follower_count)

        clear()
        print(logo)
        if is_correct:
          score += 1
          print(f"You're right! Current score: {score}.")
        else:
          game_should_continue = False
          print(f"Sorry, that's wrong. Final score: {score}")

play_game()
