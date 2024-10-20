from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
to_learn = {}

try:
    data = pandas.read_csv("angela yu/100_Projects/project31_Flash_Cards/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("angela yu/100_Projects/project31_Flash_Cards/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def change_word():
    global current_word, flip_timer
    windows.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    canvas.itemconfig(card_title, text= "French", fill="black")
    canvas.itemconfig(card_word, text = current_word["French"], fill="black")
    canvas.itemconfig(card_background, image = card_front_image)
    flip_timer = windows.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text= "English",fill="white" )
    canvas.itemconfig(card_word, text = current_word["English"],fill="white")
    canvas.itemconfig(card_background, image= card_back_image)

def is_known():
    to_learn.remove(current_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("angela yu/100_Projects/project31_Flash_Cards/data/words_to_learn.csv", index=False)

    change_word()

windows = Tk()
windows.title("Flashy")
windows.config( padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = windows.after(3000, func=flip_card)

card_back_image = PhotoImage(file = "angela yu/100_Projects/project31_Flash_Cards/images/card_back.png")
card_front_image = PhotoImage(file = "angela yu/100_Projects/project31_Flash_Cards/images/card_front.png")
checkmark_image = PhotoImage(file = "angela yu/100_Projects/project31_Flash_Cards/images/right.png")
crossmark_image = PhotoImage(file = "angela yu/100_Projects/project31_Flash_Cards/images/wrong.png")

canvas = Canvas(width=800, height=526)
card_foreground = canvas.create_image(400,263, image= card_back_image)
card_background= canvas.create_image(400,263, image= card_front_image)
card_title = canvas.create_text(400,150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,263, text="Text", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR , highlightthickness=0)

checkmark_button = Button(image=checkmark_image, highlightthickness=0 , command=change_word)
checkmark_button.grid(row=1, column=0)

crossmark_button = Button(image=crossmark_image, highlightthickness=0, command=is_known)
crossmark_button.grid(row=1, column=1)

change_word()

windows.mainloop()