import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo

# Creating tkinter window and set dimensions
window = tk.Tk()
window.title('Combobox')
window.geometry('420x220')
window.configure(background="#AFA9B4")

def leap_year(year):
    return (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0)

def update_days(event=None):
    month_selected = month_var.get()
    year_selected = year_var.get()

    if month_selected in ['April', 'June', 'September', 'November']:
        days = list(range(1, 31))
    elif month_selected == "February":
        if year_selected.isdigit() and leap_year(int(year_selected)):
            days = list(range(1, 30))
        else:
            days = list(range(1,29))
    else:
        days = list(range(1, 32))

    day_combobox['values'] = days
    day_combobox.current(0)

def choice():
    showinfo(
        title="Selected Birth Date",
        message=f'Your birth date: {day_var.get()} {month_var.get()} {year_var.get()}')

# LABEL FOR TITLE
ttk.Label(window, text="Choose your Birthdate",background="#E6E1F6", foreground="black",
          font=("Consolas", 12)).grid(row=0, column=0, columnspan=3, pady=15, sticky="n")

# DAY SELECTION
(ttk.Label(window, text="Select the day of your birthday:",
            font=("Consolas", 10)).grid(column=0,row=5, padx=5, pady=10))
day_var = tk.StringVar()
day_combobox = ttk.Combobox(window, width=20, textvariable=day_var,  state="readonly")
day_combobox['values'] = list(range(1, 32))
day_combobox.grid(column=1, row=5, padx=5, pady=5)
day_combobox.current(0)

# MONTH SELECTION
ttk.Label(window, text="Select the month of your birthday:",
          font=("Consolas", 10)).grid(column=0,row=6, padx=5, pady=10)
month_var = tk.StringVar()
month = ttk.Combobox(window, width=20, textvariable=month_var,  state="readonly")
month['values'] = ('January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December')
month.grid(column=1, row=6)
month.bind("<<ComboboxSelected>>", update_days)

# YEAR SELECTION
ttk.Label(window, text="Select the year of your birthday:",
          font=("Consolas", 10)).grid(column=0,row=7, padx=5, pady=10)
year_var = tk.StringVar()
year_combobox = ttk.Combobox(window, width=20, textvariable=year_var, state="readonly")
year_combobox['values'] = tuple(range(1900, 2026))  # Years 1900-2025
year_combobox.grid(column=1, row=7, padx=5, pady=5)
year_combobox.bind("<<ComboboxSelected>>", update_days)

ttk.Button(window, text= "Show", command=choice).grid(column=0, columnspan=2, row=8, pady=10)

window.mainloop()