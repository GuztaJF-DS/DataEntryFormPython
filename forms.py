import tkinter
from tkinter import ttk
from tkinter import messagebox

def label_constructor(frame, text, row, column):
    label = ttk.Label(frame,  text=text)
    label.grid(row=row, column=column)
    return label


def entry_constructor(frame, row, column):
    entry = ttk.Entry(frame)
    entry.grid(row=row, column=column)
    return entry


class CustomCombobox(ttk.Combobox):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(style='Custom.TCombobox')

def combobox_constructor(frame, values, row, column):
    combobox = ttk.Combobox(frame, values=values, state='readonly')
    combobox.grid(row=row, column=column)
    return combobox


def spinbox_constructor(frame, from_, to, row, column,):
    spinbox = ttk.Spinbox(frame, from_=from_, to=to, state='readonly')
    spinbox.grid(row=row, column=column)
    return spinbox

def check_constructor(frame, text, value_variable, onvalue, offvalue, row, column,):
    checkbutton = ttk.Checkbutton(
        frame, text=text, variable=value_variable, onvalue=onvalue, offvalue=offvalue
    )
    checkbutton.grid(row=row, column=column)
    return checkbutton


def button_constructor(frame, text, command, row, column,):
    button = ttk.Button(frame, text=text, command=command)
    button.grid(row=row, column=column, sticky='news', padx=20, pady=10)
    return button