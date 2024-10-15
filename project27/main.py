from tkinter import *

def miles_to_km():
    miles = float(input.get())
    km = miles * 1.609
    Km_result_label.config(text=f"{km}")

#Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=300, height=200)
window.config(padx=20,pady=20)

input = Entry( width=10)
input.grid(column=1, row=0)

#Labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

Km_result_label = Label(text="0")
Km_result_label.grid(column=1, row=1)

km_label = Label(text="kilometer")
km_label.grid(column=2, row=1)

#Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1,row=2)











window.mainloop()