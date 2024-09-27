############### Blackjack Project #####################
import random
from art_blackjack import logo
import os
def clear():
    if os.name == 'nt':
        _ = os.system('cls')

def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        random_cards = random.choice(cards )
        return random_cards

def calculate_score(random_cards ):
    if  sum(random_cards) == 21 and len(random_cards) == 2:
        return 0
    if 11 in random_cards and sum(random_cards) > 21:
        random_cards.remove(11)
        random_cards.append(1)
    return sum(random_cards)

def compare(user_score , computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You Lose 😭"
    elif user_score == computer_score:
        return "Draw 😑"
    elif computer_score == 0:
        return "Loose, opponent has Blackjack. 😱"
    elif user_score == 0:
        return "Win witha blackjack. 😎"
    elif user_score > 21:
        return "You went over. You Lose 😭"
    elif computer_score > 21:
        return "opponent went over, You win 😁"
    elif user_score > computer_score:
        return "You win 😍"
    else:
        return "You Loose 😶"

def play_game(): 
    print(logo)  
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score =calculate_score(computer_cards)
        print(f"Your cards: {user_cards},current score:{user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"your final hand: {user_cards} , final_score:{user_score}")
    print(f" Computer's final hand: {computer_cards} , final_score:{computer_score}")   
    print(compare(user_score , computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'y':
    clear()
    play_game()
