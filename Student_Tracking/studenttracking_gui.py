#
# Python:       3.11.7
#
# Author:       Chris Dini
#
# Purpose:      Student Tracking Assignment. Creating a student tracking system application using Python with Tkinter and SQLite3.
#
# Tested OS:    This code was written and tested to work with Windows 10.
#


from tkinter import *
import tkinter as tk


import studenttracking_gui
import studenttracking_func


def load_gui(self):

    # Labels
    self.lbl_fname = tk.Label(self.master, text='First Name:')
    self.lbl_fname.grid(row=0, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    self.lbl_lname = tk.Label(self.master, text='Last Name:')
    self.lbl_lname.grid(row=2, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    self.lbl_phone = tk.Label(self.master, text='Phone Number:')
    self.lbl_phone.grid(row=4, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    self.lbl_email = tk.Label(self.master, text='Email Address:')
    self.lbl_email.grid(row=6, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    self.lbl_course = tk.Label(self.master, text='Current Course:')
    self.lbl_course.grid(row=8, column=0, padx=(27,0), pady=(10,0), sticky=N+W)

    self.lbl_user = tk.Label(self.master, text='User:')
    self.lbl_user.grid(row=0, column=2, padx=(0,0), pady=(10,0), sticky=N+W)

    # Textboxes
    self.txt_fname = tk.Entry(self.master, text='')
    self.txt_fname.grid(row=1, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
    self.txt_lname = tk.Entry(self.master, text='')
    self.txt_lname.grid(row=3, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
    self.txt_phone = tk.Entry(self.master, text='')
    self.txt_phone.grid(row=5, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
    self.txt_email = tk.Entry(self.master, text='')
    self.txt_email.grid(row=7, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
    self.txt_course = tk.Entry(self.master, text='')
    self.txt_course.grid(row=9, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)

    # Listbox and scroll bar
    self.scrollbar1 = Scrollbar(self.master, orient=VERTICAL)
    self.lstList1 = Listbox(self.master, exportselection=0, yscrollcommand=self.scrollbar1.set)
    self.lstList1.bind('<<ListboxSelect>>', lambda event: studenttracking_func.onSelect(self, event))
    self.scrollbar1.config(command=self.lstList1.yview)
    self.scrollbar1.grid(row=1, column=5, rowspan=9, columnspan=1, padx=(0,0), pady=(0,0), sticky=N+E+S)
    self.lstList1.grid(row=1, column=2, rowspan=9, columnspan=3, padx=(0,0), pady=(0,0), sticky=N+E+S+W)

    # Buttons
    self.btn_add = tk.Button(self.master, width=12, height=2, text='Add', command=lambda: studenttracking_func.addToList(self))
    self.btn_add.grid(row=10, column=0, padx=(100,0), pady=(45,0), sticky=W)
    self.btn_delete = tk.Button(self.master, width=12, height=2, text='Delete', command=lambda: studenttracking_func.onDelete(self))
    self.btn_delete.grid(row=10, column=2, padx=(15,0), pady=(45,0), sticky=W)
    self.btn_close = tk.Button(self.master, width=12, height=2, text='Close', command=lambda: studenttracking_func.ask_quit(self))
    self.btn_close.grid(row=10, column=4, columnspan=1, padx=(15,0), pady=(45,0), sticky=E)

    studenttracking_func.create_db(self)
    studenttracking_func.onRefresh(self)










if __name__ == "__main__":
    pass





















