#
# Python:       3.11.7
#
# Author:       Chris Dini
#
# Purpose:      Phonebook Demo. Demonstrating OOP, Tkinter GUI module, using Tkinter Parent and Child relationships.
#
# Tested OS:    This code was written and tested to work with Windows 10.


from tkinter import *
import tkinter as tk


# Be sure to import our other modules so we can have access to them
import phonebook_gui
import phonebook_func


# Frame is the TKinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define our master frame configuration
        self.master = master
        self.master.minsize(500,300) # (Height, Width)
        self.master.maxsize(500,300)
        # This CenterWindow method will center our app on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if the user clicks the upper corner, 'X' on Windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # Load in the GUI widgets from a seperate module, keeping your code compartmentalized and clutter free
        phonebook_gui.load_gui(self)



















if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
