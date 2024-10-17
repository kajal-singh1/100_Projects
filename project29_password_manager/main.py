from tkinter import *

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    with open("100_Projects/project29_password_manager/data.txt",  "a") as data:
        data.write(f"{website} | {email} | {password}")
        
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
pw_button = Button(text="Generate Password")
pw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44)
add_button.grid(column=1, row=4, columnspan=2)








window.mainloop()
