from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

#################################### PASSWORD GENERATOR ####################################
def generate_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

#################################### SAVE PASSWORD ####################################

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website)== 0 or len(password) == 0:
          messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email:{email} \nPassword:{password}\n Is it ok to save?" )


        if is_ok:
            with open("100_Projects/project29_password_manager/data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    
#################################### UI SECTION ####################################
#Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Lock Canvas
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file = "100_Projects/project29_password_manager/logo.png")
canvas.create_image(100, 100, image = lock_image)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text = "Website:")
website_label.grid(column=0, row=1)

email_label = Label(text = "Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text = "Password:")
password_label.grid(column=0, row=3)

#Entries
website_entry = Entry(width=52)
website_entry.focus()
website_entry.grid(column=1, row= 1, columnspan=2)

email_entry = Entry(width=52)
email_entry.grid(column=1, row= 2, columnspan=2)
email_entry.insert(0, "dummy@gmail.com")

password_entry = Entry(width=34)
password_entry.grid(column=1, row= 3)

#Buttons 
pw_button = Button(text="Generate Password", command=generate_pw)
pw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)








window.mainloop()
