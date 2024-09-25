#The silent_auction_program
from art_silent_auction_program import logo
print(logo)

print("Welcome to the secret auction program.")

import os
def clear():
    if os.name == 'nt':
        _ = os.system('cls')

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
bids = {}
bidding_finished = False 
while not bidding_finished:  
    name = input("what is your name?: ")
    price = int(input("what's your bid?: $"))
    bids[name] = price
    another_bidder = input("Type 'yes' if other users also want to bid orelse type 'no'")
    if another_bidder == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif another_bidder == "yes":
        clear()




#Interactive Coding
#Q1 Grading Program
# student_scores = {
#     "Harry" : 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# } 

# student_grades = {}

# for student in student_scores:
#     score = student_scores[student]
    
#     if score > 90:
#         student_grades[student] = "outstanding"
#     elif score > 80:
#         student_grades[student] = "exceeds expectation"
#     elif score > 70:
#         student_grades[student] = "acceptable"
#     else:
#         student_grades[student] = "fail"

# print(student_grades)
# print(student_scores.keys())

# Travel_log = [{
#     "Telangana" : {"cities":["hyderabad","secundrabad","warangal"],"total_visits":12},
#     "banglore": ["basar","harmandi","shenai"],
# },{
#     "name":"simon",
#     "salary":"10000",
# }]

# print(Travel_log[1])

#Q2 Dictionary in list
# travel_log = [
#     {
#         "country": "bhrt",
#         "total_visits":12,
#         "cities":["hyderabad","secundrabad","warangal"],
#     },
#     {
#         "country": "india",
#         "total_visits":102,
#         "cities": ["basar","harmandi","shenai"],
#     }
# ]

# def add_new_country(country , total_visits ,cities ):
#     new_country = {}
#     new_country["country"] = country
#     new_country["total_visits"] = total_visits
#     new_country["cities"] = cities
#     travel_log.append(new_country)
# add_new_country("russia" , 2,["moscow","saint perni","columbia"])
# print(travel_log)