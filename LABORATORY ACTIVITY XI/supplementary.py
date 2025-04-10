import tkinter as tk
import math

# --- Function Definitions ---
def clear():
    entry.delete(0, tk.END)

def one(): entry.insert(tk.END, "1")
def two(): entry.insert(tk.END, "2")
def three(): entry.insert(tk.END, "3")
def four(): entry.insert(tk.END, "4")
def five(): entry.insert(tk.END, "5")
def six(): entry.insert(tk.END, "6")
def seven(): entry.insert(tk.END, "7")
def eight(): entry.insert(tk.END, "8")
def nine(): entry.insert(tk.END, "9")
def zero(): entry.insert(tk.END, "0")

def addition(): entry.insert(tk.END, "+")
def subtraction(): entry.insert(tk.END, "-")
def multiplication(): entry.insert(tk.END, "*")
def division(): entry.insert(tk.END, "/")

def decimal():
    current = entry.get()
    if "." not in current:
        entry.insert(tk.END, ".")

def result():
    try:
        expression = entry.get()
        answer = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(answer)[:15])
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def sin():
    try:
        value = float(entry.get())
        res = math.sin(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(round(res, 10))[:15])
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def cos():
    try:
        value = float(entry.get())
        res = math.cos(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(round(res, 10))[:15])
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def tan():
    try:
        value = float(entry.get())
        res = math.tan(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(round(res, 10))[:15])
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def exp():
    entry.insert(tk.END, "**")

# --- UI Setup ---
root = tk.Tk()
root.title("Calculator")
root.configure(bg="#37373A")

# Entry Display
entry = tk.Entry(root, font=("Arial", 30), bd=5, width=15, borderwidth=10, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="NSEW", padx=15, pady=10)

# Row 1 - Equal Button Full Row
tk.Button(root, text="=", font=("Consolas", 15, "bold"), bg="#ACACB8", command=result, height=2).grid(row=1, column=0, columnspan=4, sticky="nsew")

# Row 2 - Clear + Trig Functions
tk.Button(root, text="sin", font=("Consolas", 15, "bold"), bg="#ACACB8", command=sin, height=2).grid(row=2, column=0, sticky="nsew")
tk.Button(root, text="cos", font=("Consolas", 15, "bold"), bg="#ACACB8", command=cos, height=2).grid(row=2, column=1, sticky="nsew")
tk.Button(root, text="tan", font=("Consolas", 15, "bold"), bg="#ACACB8", command=tan, height=2).grid(row=2, column=2, sticky="nsew")
tk.Button(root, text="Clear", font=("Consolas", 15, "bold"), bg="#ACACB8", command=clear, height=2).grid(row=2, column=3, sticky="nsew")

# Row 3 - Numbers and Division
tk.Button(root, text="1", font=("Consolas", 15), bg="#7A7B96", command=one, height=2).grid(row=3, column=0, sticky="nsew")
tk.Button(root, text="2", font=("Consolas", 15), bg="#7A7B96", command=two, height=2).grid(row=3, column=1, sticky="nsew")
tk.Button(root, text="3", font=("Consolas", 15), bg="#7A7B96", command=three, height=2).grid(row=3, column=2, sticky="nsew")
tk.Button(root, text="/", font=("Consolas", 15, "bold"), bg="#ACACB8", command=division, height=2).grid(row=3, column=3, sticky="nsew")

# Row 4 - Numbers and Multiplication
tk.Button(root, text="4", font=("Consolas", 15), bg="#7A7B96", command=four, height=2).grid(row=4, column=0, sticky="nsew")
tk.Button(root, text="5", font=("Consolas", 15), bg="#7A7B96", command=five, height=2).grid(row=4, column=1, sticky="nsew")
tk.Button(root, text="6", font=("Consolas", 15), bg="#7A7B96", command=six, height=2).grid(row=4, column=2, sticky="nsew")
tk.Button(root, text="*", font=("Consolas", 15, "bold"), bg="#ACACB8", command=multiplication, height=2).grid(row=4, column=3, sticky="nsew")

# Row 5 - Numbers and Subtraction
tk.Button(root, text="7", font=("Consolas", 15), bg="#7A7B96", command=seven, height=2).grid(row=5, column=0, sticky="nsew")
tk.Button(root, text="8", font=("Consolas", 15), bg="#7A7B96", command=eight, height=2).grid(row=5, column=1, sticky="nsew")
tk.Button(root, text="9", font=("Consolas", 15), bg="#7A7B96", command=nine, height=2).grid(row=5, column=2, sticky="nsew")
tk.Button(root, text="-", font=("Consolas", 15, "bold"), bg="#ACACB8", command=subtraction, height=2).grid(row=5, column=3, sticky="nsew")

# Row 6 - Numbers and Operators
tk.Button(root, text="0", font=("Consolas", 12, "bold"), bg="#7A7B96", command=zero, height=2).grid(row=6, column=0, sticky="nsew")
tk.Button(root, text=".", font=("Consolas", 15, "bold"), bg="#ACACB8", command=decimal, height=2).grid(row=6, column=1, sticky="nsew")
tk.Button(root, text="x^", font=("Consolas", 15, "bold"), bg="#ACACB8", command=exp, height=2).grid(row=6, column=2, sticky="nsew")
tk.Button(root, text="+", font=("Consolas", 15, "bold"), bg="#ACACB8", command=addition, height=2).grid(row=6, column=3, sticky="nsew")

# Run the app
root.mainloop()
