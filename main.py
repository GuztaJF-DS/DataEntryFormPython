import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import messagebox
from ttkthemes import ThemedStyle


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

def enter_data():
    terms_status = terms_status_var.get()
    if (terms_status == 'Accepted'):
        # User Info
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        title = title_combobox.get()
        age = age_spinbox.get()
        nationality = nationality_combobox.get()

        # Course Info
        reg_status = reg_status_var.get()
        num_courses = num_courses_spinbox.get()
        num_semesters = num_semesters_spinbox.get()

        # check if the widgets are null
        for widget in user_info_frame.winfo_children():
            if not isinstance(widget, ttk.Label):
                if (widget.get() == ''):
                    messagebox.showerror(
                        title="Error", message="There are missing fields")
                    return

        if (int(age) < 18 or int(age) > 110):
            messagebox.showerror(
                title="Error", message="Invalid Age")
            return

        print('title:', title, 'First Name:',
              first_name, ' Last Name:', last_name)
        print('age:', age, 'nationality:', nationality)
        print('# Courses:', num_courses, '# Semesters:', num_semesters)
        print('Registration Status:', reg_status)
        print('-------------------------------------------------------------------')
    else:
        messagebox.showerror(
            title="Error", message="you have not accepted the terms and conditions")


window = tkinter.Tk()
window.title('Data entry form')

frame = ttk.Frame(window)
frame.pack()

style = ThemedStyle(frame)
style.set_theme("clearlooks") 

# Save user Info
user_info_frame = ttk.LabelFrame(frame, text='User Info')
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

title_label = label_constructor(user_info_frame, 'Title', 0, 0)
title_combobox = combobox_constructor(
    user_info_frame, ['', 'Mr.', 'Ms.', 'Dr.'], 1, 0,
)

first_name_label = label_constructor(user_info_frame, 'First Name', 0, 1)
first_name_entry = entry_constructor(user_info_frame, 1, 1)

last_name_label = label_constructor(user_info_frame, 'Last Name', 0, 2)
last_name_entry = entry_constructor(user_info_frame, 1, 2)

age_label = label_constructor(user_info_frame, 'Age', 2, 0)
age_spinbox = spinbox_constructor(user_info_frame, 18, 110, 3, 0)

nationality_label = label_constructor(user_info_frame, 'Nationality', 2, 1)
nationality_combobox = combobox_constructor(
    user_info_frame,['Brazil', 'Not Brazil'] ,3, 1
)

# put a padding in all grids
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# course frame
courses_frame = ttk.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky='news', padx=20, pady=10)

registered_label = label_constructor(courses_frame, 'Registration Status',0,0)

reg_status_var = tkinter.StringVar(value='Not Registered')
registered_check = check_constructor(
    courses_frame, 'Currently Registered', reg_status_var, 'Registered', 'Not Registered', 1, 0
)

num_courses_label = label_constructor(courses_frame, '# Completed Courses',0,1)
num_courses_spinbox = spinbox_constructor(
    courses_frame,0,'infinity',1,1)
num_courses_spinbox.grid(row=1, column=1)

num_semesters_label = label_constructor(courses_frame, '# Semesters',0,2)
num_semesters_spinbox = spinbox_constructor(courses_frame, 0, 'infinity',1,2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Terms frame
terms_frame = ttk.LabelFrame(frame)
terms_frame.grid(row=2, column=0, sticky='news', padx=20, pady=10)

terms_status_var = tkinter.StringVar(value='Not Accepted')
terms_check = check_constructor(
    terms_frame, 'I Accept the terms and conditions',
    terms_status_var, 'Accepted', 'Not Accepted',0,0
)

# Button
button = button_constructor(frame, 'Enter Data', enter_data,3,0)


window.mainloop()
