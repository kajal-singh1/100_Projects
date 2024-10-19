from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

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
    new_data = {
        website:{
        "email": email,
        "password": password
        }
    }

    if len(website)== 0 or len(password) == 0:
          messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:    
            with open("100_Projects/project30_Upgraded_Password_Manager/data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("100_Projects/project30_Upgraded_Password_Manager/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("100_Projects/project30_Upgraded_Password_Manager/data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

#################################### FIND PASSWORD ####################################

def find_password():
    website = website_entry.get()
    try:
        with open("100_Projects/project30_Upgraded_Password_Manager/data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:              
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}\n Password:{password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for{website} exists")

#################################### UI SECTION ####################################

#Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Lock Canvas
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file = "100_Projects/project30_Upgraded_Password_Manager/logo.png")
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
website_entry = Entry(width=34)
website_entry.focus()
website_entry.grid(column=1, row= 1)

email_entry = Entry(width=53)
email_entry.grid(column=1, row= 2, columnspan=2)
email_entry.insert(0, "dummy@gmail.com")

password_entry = Entry(width=34)
password_entry.grid(column=1, row= 3)

#Buttons 
pw_button = Button(text="Generate Password", command=generate_pw)
pw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Serach", width=15, command=find_password)
search_button.grid(column=2, row=1)



window.mainloop()
