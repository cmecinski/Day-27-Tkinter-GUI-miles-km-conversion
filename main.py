from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=320, height=180)
window.config(padx=20, pady=20)

# Labels

miles_label = Label(text="Miles", font=("Arial", 13, "bold"))
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=("Arial", 13, "bold"))
equal_label.grid(column=0, row=1)

km_label = Label(text="Km", font=("Arial", 13, "bold"))
km_label.grid(column=2, row=1)

answer_label = Label(text="", font=("Arial", 13))
answer_label.grid(column=1, row=1)

# Input

input_miles = Entry(width=7)
input_miles.grid(column=1, row=0)


# Button

def button_calculate():
    miles_given = float(input_miles.get())
    km = miles_given * 1.60934
    answer_label.config(text=f"{km}")


calculate_button = Button(text="Calculate", command=button_calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()

