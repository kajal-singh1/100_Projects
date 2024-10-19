#Exercise1
# fruits = ["Apple","Pear","Orange"]


# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("fruit pie")
#     else:
#         print(fruit + "pie")

# make_pie(4)


#exercise2
# facebook_posts = [
#     {'Likes':21, 'Comments': 2},
#     {'Likes':13, 'Comments': 2, 'Shares':1},
#     {'Likes':33, 'Comments': 8, 'Shares':3},
#     {'Comments': 4, 'Shares':2},
#     {'Comments': 1, 'Shares':1},
#     {'Likes':19, 'Comments': 3}
# ]
# total_likes = 0

# for post in facebook_posts:
#         try:
#             total_likes = total_likes + post['Likes']
#         except KeyError:
#             pass

# print(total_likes)


#exercise3
import pandas as pd

data = pd.read_csv("100_Projects/project30/nato_phonetic_alphabet.csv")
new_value = {row.letter:row.code for (index,row) in data.iterrows()}
# print(new_value)

def generate():
    word = input("Enter a word: ").upper()
    try:
        output_list = [new_value[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate()
    else:
        print(output_list)

generate()
