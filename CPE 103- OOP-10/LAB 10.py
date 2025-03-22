#Creating tkinter window and set dimensions
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo

window = tk.Tk()
window.title('Combobox')
window.geometry('500x250')

def choice_month(event):
    month = event.widget.get()
    if month == 'February':
    print("Your birth month", month)

def choice_date(event):
    date = event.widget.get()
    print("Your birth month", date)

def choice_year(event):
    year = event.widget.get()
    print("Your birth month", year)


#label text for title
ttk.Label(window, text = "Choose your birth month",
          background ='light yellow', foreground="black",
          font=("Courier", 15 )).grid(row=0, column=1)

ttk.Label(window, text = "Choose your birth date",
          background ='light yellow', foreground="black",
          font=("Courier", 15 )).grid(row=0, column=1)

ttk.Label(window, text = "Choose your birth year",
          background ='light yellow', foreground="black",
          font=("Courier", 15 )).grid(row=0, column=1)

#setlabel
ttk.Label(window, text="Select the month of your birth:",
          font=("Courier", 12)).grid(column=0,
                                     row=5, padx=5, pady=25)
ttk.Label(window, text="Select birth date:",
          font=("Courier", 12)).grid(column=0,
                                     row=7, padx=5, pady=25)
ttk.Label(window, text="Select birth year:",
          font=("Courier", 12)).grid(column=0,
                                     row=9, padx=5, pady=25)

#Create Combobox
n = tk.StringVar()
month = ttk.Combobox(window, width=27, textvariable=n)
date = ttk.Combobox(window, width=27, textvariable=n)
year = ttk.Combobox(window, width=27, textvariable=n)

month['value'] = ( 'January',
                   'February',
                   'March',
                   'April',
                   'May',
                   'June',
                   'July',
                   'August',
                   'September',
                   'October',
                   'November',
                   'December')

month.grid(column=1, row=5)
month.current()

def choice(event):
    showinfo(
            title = "Selection",
            message = f'You selected{n.get()}')

month.bind("<<ComboboxSelected>>", choice)
window.mainloop()
