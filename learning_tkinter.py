from tkinter import *
from tkinter.ttk import *


def tkinter():
    root = Tk()
    root.title("My GUI")

    frame = Frame()
    labeltext = StringVar()
    label = Label(frame, textvariable=labeltext)
    entry = Entry(frame, width=30)
    button = Button(frame, text="My Button")
    radio1 = Radiobutton(frame, text="Alternative 1", value=1)
    radio2 = Radiobutton(frame, text="Alternative 2", value=2)
    radio3 = Radiobutton(frame, text="Alternative 3", value=3)
    checkbox1 = Checkbutton(frame, text="Option 1")
    checkbox2 = Checkbutton(frame, text="Option 2")
    labeltext.set("My Label")

    label.grid(row=0, column=0, sticky=W, padx=5)
    entry.grid(row=0, column=1, sticky=E, pady=10)
    button.grid(row=1, column=0, columnspan=2, sticky=S + E + W, padx=20, pady=5)

    radio1.grid(row=4, column=0, sticky=W, padx=5)
    radio2.grid(row=5, column=0, sticky=W, padx=5)
    radio3.grid(row=6, column=0, sticky=W, padx=5)
    checkbox1.grid(row=4, column=1, sticky=E, padx=5)
    checkbox2.grid(row=5, column=1, sticky=E, padx=5)

    frame.grid()

    root.mainloop()
