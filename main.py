import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import messagebox
from ttkthemes import ThemedStyle, ThemedTk

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


def combobox_constructor(frame, row, column, values):
    combobox = ttk.Combobox(frame, values=values, state='readonly')
    combobox.grid(row=row, column=column)
    return combobox


def spinbox_constructor(frame, row, column, from_, to):
    spinbox = ttk.Spinbox(frame, from_=from_, to=to)
    spinbox.grid(row=row, column=column)
    return spinbox


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
                print(widget.get())
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
    user_info_frame, 1, 0, ['', 'Mr.', 'Ms.', 'Dr.']
)

first_name_label = label_constructor(user_info_frame, 'First Name', 0, 1)
first_name_entry = entry_constructor(user_info_frame, 1, 1)

last_name_label = label_constructor(user_info_frame, 'Last Name', 0, 2)
last_name_entry = entry_constructor(user_info_frame, 1, 2)

age_label = label_constructor(user_info_frame, 'Age', 2, 0)
age_spinbox = ttk.Spinbox(
    user_info_frame, from_=18, to=110, state='readonly')
age_spinbox.grid(row=3, column=0)

nationality_label = label_constructor(user_info_frame, 'Nationality', 2, 1)
nationality_combobox = combobox_constructor(
    user_info_frame, 3, 1, ['Brazil', 'Not Brazil']
)

# put a padding in all grids
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# course frame
courses_frame = ttk.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky='news', padx=20, pady=10)

registered_label = ttk.Label(courses_frame, text='Registration Status')

reg_status_var = tkinter.StringVar(value='Not Registered')
registered_check = ttk.Checkbutton(
    courses_frame, text='Currently Registered', variable=reg_status_var, onvalue='Registered', offvalue='Not Registered'
)
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

num_courses_label = ttk.Label(courses_frame, text='# Completed Courses')
num_courses_spinbox = ttk.Spinbox(
    courses_frame, from_=0, to='infinity', state='readonly')
num_courses_label.grid(row=0, column=1)
num_courses_spinbox.grid(row=1, column=1)

num_semesters_label = ttk.Label(courses_frame, text='# Semesters')
num_semesters_spinbox = ttk.Spinbox(
    courses_frame, from_=0, to='infinity', state='readonly')
num_semesters_label.grid(row=0, column=2)
num_semesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Terms frame
terms_frame = ttk.LabelFrame(frame)
terms_frame.grid(row=2, column=0, sticky='news', padx=20, pady=10)

terms_status_var = tkinter.StringVar(value='Not Accepted')
terms_check = ttk.Checkbutton(
    terms_frame, text='I Accept the terms and conditions',
    variable=terms_status_var, onvalue='Accepted', offvalue='Not Accepted'
)
terms_check.grid(row=0, column=0)

# Button
button = ttk.Button(frame, text='Enter Data', command=enter_data)
button.grid(row=3, column=0, sticky='news', padx=20, pady=10)

window.mainloop()
