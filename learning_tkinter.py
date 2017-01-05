from tkinter import *
from tkinter.ttk import *

# manually, because it's not mentiones in __all__ and therefore not imported by 'from tkinter import *'
from tkinter import messagebox


def tkinter():
    def checkbox_changed():
        str = ""
        if checkbox1_value.get():
            str += "(Option 1)"
        if checkbox2_value.get():
            str += "(Option 2)"

        messagebox.showinfo("Option Clicked", "Selected Options: " + str)

    # Opens a message box when called
    def show_about(event=None):
        messagebox.showwarning(
            "About",
            "This Awesome Program was Made in 2016"
        )

    def exit_app(event=None):
        root.quit()

    root = Tk()
    root.title("My Test-GUI")

    frame = Frame(root)
    # frame.master.maxsize(800,600)
    # frame.master.minsize(800, 600)
    frame.master.geometry("800x600+100+50")
    frame.master.resizable(0, 0)

    labeltext = StringVar()
    label = Label(frame, textvariable=labeltext)
    entry = Entry(frame, width=30)
    button = Button(frame, text="Exit")
    button.bind("<Button-1>", exit_app)
    radio1 = Radiobutton(frame, text="Alternative 1", value=1)
    radio2 = Radiobutton(frame, text="Alternative 2", value=2)
    radio3 = Radiobutton(frame, text="Alternative 3", value=3)

    checkbox1_value = BooleanVar()
    checkbox2_value = BooleanVar()

    checkbox1_value.set(True)
    checkbox2_value.set(False)

    checkbox1 = Checkbutton(frame, text="Option 1", variable=checkbox1_value, command=checkbox_changed)
    checkbox2 = Checkbutton(frame, text="Option 2", variable=checkbox2_value, command=checkbox_changed)
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

    # Create the menu object
    the_menu = Menu(root)

    # ----- FILE MENU -----

    # Create a pull down menu that can't be removed
    file_menu = Menu(the_menu, tearoff=0)

    # Add items to the menu that show when clicked
    # compound allows you to add an image
    file_menu.add_command(label="Open")
    file_menu.add_command(label="Save")

    # Add a horizontal bar to group similar commands
    file_menu.add_separator()

    # Call for the function to execute when clicked
    file_menu.add_command(label="Quit", accelerator="Alt-X", command=exit_app)

    # Add the pull down menu to the menu bar
    the_menu.add_cascade(label="File", menu=file_menu)

    # ----- FONT MENU FOR VIEW MENU -----

    # Stores font chosen and will update based on menu
    # selection
    text_font = StringVar()
    text_font.set("Times")

    # Outputs font changes
    def change_font(event=None):
        print("Font Picked :", text_font.get())

    # Define font drop down that will be attached to view
    font_menu = Menu(the_menu, tearoff=0)

    # Define radio button options for fonts
    font_menu.add_radiobutton(label="Times",
                              variable=text_font,
                              command=change_font)

    font_menu.add_radiobutton(label="Courier",
                              variable=text_font,
                              command=change_font)

    font_menu.add_radiobutton(label="Ariel",
                              variable=text_font,
                              command=change_font)

    # ----- VIEW MENU -----
    view_menu = Menu(the_menu, tearoff=0)

    # Variable changes when line numbers is checked
    # or unchecked
    line_numbers = IntVar()
    line_numbers.set(1)

    # Bind the checking of the line number option
    # to variable line_numbers
    view_menu.add_checkbutton(label="Line Numbers",
                              variable=line_numbers)

    view_menu.add_cascade(label="Fonts", menu=font_menu)

    # Add the pull down menu to the menu bar
    the_menu.add_cascade(label="View", menu=view_menu)

    # ----- HELP MENU -----
    help_menu = Menu(the_menu, tearoff=0)

    # accelerator is used to show a shortcut
    # OSX, Windows and Linux use the following options
    # Command-O, Shift+Ctrl+S, Command-Option-Q with the
    # modifiers Control, Ctrl, Option, Opt, Alt, Shift,
    # and Command
    help_menu.add_command(label="About",
                          accelerator="Ctrl-A",
                          command=show_about)

    the_menu.add_cascade(label="Help", menu=help_menu)

    # Bind the shortcut to the function
    root.bind('<Control-A>', show_about)
    root.bind('<Control-a>', show_about)
    root.bind('<Alt-X>', exit_app)
    root.bind('<Alt-x>', exit_app)

    # Display the menu bar
    root.config(menu=the_menu)

    # disable resizing of application window
    root.resizable(0, 0)
    root.mainloop()
