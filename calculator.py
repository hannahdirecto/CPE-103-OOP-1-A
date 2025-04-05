import tkinter as tk

def clear():
    entry.delete(0, tk.END)

def addition():
    entry.insert(tk.END, "+")

def subtraction():
    entry.insert(tk.END, "-")

def multiplication():
    entry.insert(tk.END, "*")

def division():
    entry.insert(tk.END, "/")

def one():
    entry.insert(tk.END, "1")

def two():
    entry.insert(tk.END, "2")

def three():
    entry.insert(tk.END, "3")

def four():
    entry.insert(tk.END, "4")

def five():
    entry.insert(tk.END, "5")

def six():
    entry.insert(tk.END, "6")

def seven():
    entry.insert(tk.END, "7")

def eight():
    entry.insert(tk.END, "8")

def nine():
    entry.insert(tk.END, "9")

def zero():
    entry.insert(tk.END, "0")

def decimal():
    current = entry.get()
    if "." not in current:
        entry.insert(tk.END, ".")

def result():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")
root.configure(bg = "#96ABCB")

#entry
entry = tk.Entry(root, font = ("Arial", 30), bd = 5, width = 15, borderwidth=10, relief="ridge", justify="right"  )
entry.grid(row=0, column=0, columnspan=4, sticky="NSEW", padx=15, pady=10)
#operations button
tk.Button(root, text="C",font=("Consolas", 15, "bold"), command=clear, width=8, height=2).grid(row=1 , column=0, columnspan=4, sticky="nsew", )
tk.Button(root, text= "+" ,font=("Consolas", 15, "bold"), command=addition, width=8, height=2).grid(row=5 , column=3, columnspan=4, sticky="nsew", )
tk.Button(root, text= "-" ,font=("Consolas", 15, "bold"), command=subtraction, width=8, height=2).grid(row=4 , column=3, columnspan=4, sticky="nsew",)
tk.Button(root, text= "*" ,font=("Consolas", 15, "bold"), command=multiplication, width=8, height=2).grid(row=3 , column=3, columnspan=4, sticky="nsew", )
tk.Button(root, text= "/" ,font=("Consolas", 15, "bold"), command=division, width=8, height=2).grid(row=2 , column=3, columnspan=4, sticky="nsew", )
#number button
tk.Button(root, text="1", font=("Consolas", 15), command=one, height=2).grid(row=2, column=0, sticky="nsew")
tk.Button(root, text="2", font=("Consolas", 15), command=two,  height=2).grid(row=2, column=1, sticky="nsew")
tk.Button(root, text="3", font=("Consolas", 15), command=three, height=2).grid(row=2, column=2, sticky="nsew")
tk.Button(root, text="4", font=("Consolas", 15), command=four,  height=2).grid(row=3, column=0, sticky="nsew")
tk.Button(root, text="5", font=("Consolas", 15), command=five, height=2).grid(row=3, column=1, sticky="nsew")
tk.Button(root, text="6", font=("Consolas", 15), command=six, height=2).grid(row=3, column=2, sticky="nsew")
tk.Button(root, text="7", font=("Consolas", 15), command=seven, height=2).grid(row=4, column=0, sticky="nsew")
tk.Button(root, text="8", font=("Consolas", 15), command=eight, height=2).grid(row=4, column=1, sticky="nsew")
tk.Button(root, text="9", font=("Consolas", 15), command=nine, height=2).grid(row=4, column=2, sticky="nsew")
tk.Button(root, text="0", font=("Consolas", 15), command=zero, height=2).grid(row=5, column=0, columnspan=2,  sticky="nsew")
tk.Button(root, text=".", font=("Consolas", 15, "bold"), command=decimal, height=2).grid(row=5, column=2, sticky="nsew")
#result button
tk.Button(root, text="=", font=("Consolas", 15, "bold"), command=result, width = 15, height=2).grid(row=6, column=0, columnspan=4, sticky="nsew")

root.mainloop()