from tkinter import Tk, Frame, StringVar, Label, Entry, Button, W, E, S


def tkinter():
    root = Tk()
    root.title("My GUI")

    frame = Frame()
    labeltext = StringVar()
    label = Label(frame, textvariable=labeltext)
    entry = Entry(frame, width=30)
    button = Button(frame, text="My Button")
    labeltext.set("My Label")

    label.grid(row=0, column=0, sticky=W, padx=5)
    entry.grid(row=0, column=1, sticky=E, pady=10)
    button.grid(row=1, column=1, sticky=S, padx=20, pady=5)
    frame.grid()

    root.mainloop()