from tkinter import *


def convert():
    result = round(float(miles_to_convert.get()) * 1.609344)
    km_converted.config(text=f"{result}")


window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=270, height=120)
window.config(padx=30, pady=30)

miles_to_convert = Entry(width=7)
miles_to_convert.insert(END, string="0")
miles_to_convert.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)
is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)
km_converted = Label(text="0")
km_converted.grid(column=1, row=1)
km = Label(text="Km")
km.grid(column=2, row=1)

btn_calculate = Button(text="Calculate", command=convert)
btn_calculate.grid(column=1, row=2)


window.mainloop()
