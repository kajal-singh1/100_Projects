from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    label.config(text = new_text)

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="New text")
label.grid(column=0, row=0)

#Button
button = Button(text="Click Me", command=button_clicked)

input = Entry(width=10)
print(input.get())






window.mainloop()