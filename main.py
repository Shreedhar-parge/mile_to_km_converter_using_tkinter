from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    cal = round(float(new_text) * 1.609)
    zero.config(text=f"{cal}")

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=300, height=150)
window.config(padx=50, pady=50)

#Label
miles = Label(text="Miles")
miles.grid(column=2, row=0)

km = Label(text="Km")
km.grid(column=2, row=1)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

zero = Label(text="0")
zero.grid(column=1, row=1)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

















window.mainloop()