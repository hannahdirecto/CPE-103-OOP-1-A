import tkinter as tk
import math

history_list = []

def update_history(expression, result_value):
    history_list.append(f"{expression} = {result_value}")
    history.set("\n".join(history_list[-10:]))

def add():
    value = float(entry1.get()) + float(entry2.get())
    result.set(value)
    update_history(f"{entry1.get()} + {entry2.get()}", value)

def subtract():
    value = float(entry1.get()) - float(entry2.get())
    result.set(value)
    update_history(f"{entry1.get()} - {entry2.get()}", value)

def multiply():
    value = float(entry1.get()) * float(entry2.get())
    result.set(value)
    update_history(f"{entry1.get()} * {entry2.get()}", value)

def divide():
    try:
        value = float(entry1.get()) / float(entry2.get())
        result.set(value)
        update_history(f"{entry1.get()} / {entry2.get()}", value)
    except ZeroDivisionError:
        result.set("Error! Division by zero.")

def square_root():
    try:
        value = math.sqrt(float(entry1.get()))
        result.set(value)
        update_history(f"squareroot{entry1.get()}", value)
    except ValueError:
        result.set("Error! Invalid input.")

def power():
    value = float(entry1.get()) ** float(entry2.get())
    result.set(value)
    update_history(f"{entry1.get()} ^ {entry2.get()}", value)

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result.set("")
    history.set("")

def calculate_trig(operation):
    try:
        angle = float(entry3.get())
        radians = math.radians(angle)

        if operation == "sin":
            value = math.sin(radians)
        elif operation == "cos":
            value = math.cos(radians)
        elif operation == "tan":
            if angle % 90 == 0 (angle / 90) % 2 == 1:
                result.set("Error! Undefined")
            value = math.tan(radians)
        else:
            result.set("Error! Invalid Operation")
            return

        result.set(value)
        update_history(f"{operation}({angle})", value)

    except ValueError:
        result.set("Error! Invalid Input.")

# Create the main window
root = tk.Tk()
root.geometry("530x330")
root.title("Simple Calculator")
root.configure(bg="#F7AFD8")

label = tk.Label(root, text="Calculator", font=("Courier", 15, "bold"), bg="#935382")
label.grid(row=0, column=0, columnspan=4, pady=10, sticky="n")

# StringVars for result and history
result = tk.StringVar()
history = tk.StringVar()

# Entry fields
tk.Label(root, text="Enter the first number:", font=("Consolas", 10, "bold"), bg="#CC7BA8").grid(row=1, column=0, sticky="ew")
entry1 = tk.Entry(root)
entry1.grid(row=1, column=1, columnspan=2, sticky="e")

tk.Label(root, text="Enter the second number:", font=("Consolas", 10, "bold"), bg="#CC7BA8").grid(row=2, column=0, sticky="ew")
entry2 = tk.Entry(root)
entry2.grid(row=2, column=1, columnspan=2, sticky="e")

tk.Label(root, text="Enter a number:", font=("Consolas", 10, "bold"), bg="#CC7BA8").grid(row=5, column=0, sticky="ew")
entry3 =tk.Entry(root)
entry3.grid(row=5, column=1, columnspan=2, stick="e" )

# History Section
tk.Label(root, text="History:", font=("Consolas", 10, "bold"), bg="white").grid(row=1, column=3, pady=5, padx=10, sticky="w")
history_label = tk.Label(root, textvariable=history, font=("Consolas", 9), justify="left",
                         bg="white", width=25, height=10, relief="solid", borderwidth=1)
history_label.grid(row=2, column=3, rowspan=6, pady=5, padx=10, sticky="n")

# Buttons
tk.Button(root, text="Add", command=add, width=10, bg="#D7BDE2").grid(row=3, column=0, pady=5, sticky="e")
tk.Button(root, text="Subtract", command=subtract, width=10, bg="#D7BDE2").grid(row=4, column=0, pady=5, sticky="e")
tk.Button(root, text="Multiply", command=multiply, width=10, bg="#D7BDE2").grid(row=4, column=1, pady=5)
tk.Button(root, text="Divide", command=divide, width=10, bg="#D7BDE2").grid(row=3, column=1, pady=5)
tk.Button(root, text="√", command=square_root, width=10, bg="#D7BDE2").grid(row=3, column=2, pady=5)
tk.Button(root, text="xʸ", command=power, width=10, bg="#D7BDE2").grid(row=4, column=2, pady=5)
 #Trigonometric Buttons
tk.Button(root, text="sin", command=lambda: calculate_trig("sin"), width=10, bg="#D7BDE2").grid(row=6, column=0, pady=5, sticky="e")
tk.Button(root, text="cos", command=lambda: calculate_trig("cos"), width=10, bg="#D7BDE2").grid(row=6, column=1, pady=5)
tk.Button(root, text="tan", command=lambda: calculate_trig("tan"), width=10, bg="#D7BDE2").grid(row=6, column=2, pady=5)

# Clear Button (Spans 3 columns)
tk.Button(root, text="Clear", command=clear, width=32, bg="#AC2E6B", fg="white").grid(row=8 , column=0, columnspan=3, pady=10)

# Result Display
tk.Label(root, text="Result:", font=("Consolas", 10, "bold"), bg="#CC7BA8").grid(row=7, column=0, pady=5, sticky="ew")
tk.Label(root, textvariable=result, font=("Consolas", 10), bg="#935382", width=20).grid(row=7, column=1, pady=5, columnspan=2, sticky="e")

# Start the main loop
root.mainloop()
