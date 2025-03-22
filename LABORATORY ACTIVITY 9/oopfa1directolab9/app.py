import tkinter as tk
from tkinter import messagebox

def start_timer():
    global running, time_left
    if not running:
        try:
            hours = int(hour_entry.get())
            minutes = int(min_entry.get())
            seconds = int(sec_entry.get())
            time_left = hours * 3600 + minutes * 60 + seconds
            if time_left <= 0:
                messagebox.showerror("Invalid Time", "Please enter a valid time.")
                return
            running = True
            update_timer()
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter numbers only!")

def stop_timer():
    global running
    running = False

def reset_timer():
    global time_left, running
    running = False
    time_left = 0
    update_display()
    hour_entry.delete(0, tk.END)
    min_entry.delete(0, tk.END)
    sec_entry.delete(0, tk.END)

def update_timer():
    global time_left
    if running and time_left > 0:
        time_left -= 1
        update_display()
        root.after(1000, update_timer)
    elif time_left == 0 and running:
        messagebox.showinfo("Time Over", "Time is up!")

def update_display():
    mins, secs = divmod(time_left, 60)
    hrs, mins = divmod(mins, 60)
    timer_label.config(text=f"{hrs:02}:{mins:02}:{secs:02}")

running = False
time_left = 0
root = tk.Tk()
root.title("Computer Shop Timer")
root.geometry("400x350")
root.configure(bg="white")
timer_label = tk.Label(root, text="00:00:00", font=("Arial", 24), bg="white", fg="black")
timer_label.place(relx=0.5, rely=0.2, anchor="center")

hour_entry = tk.Entry(root, width=3)
hour_entry.place(relx=0.35, rely=0.4, anchor="center")
hour_entry.insert(0, "0")

tk.Label(root, text=":", font=("Arial", 14), bg="white").place(relx=0.4, rely=0.4, anchor="center")

min_entry = tk.Entry(root, width=3)
min_entry.place(relx=0.45, rely=0.4, anchor="center")
min_entry.insert(0, "0")

tk.Label(root, text=":", font=("Arial", 14), bg="white").place(relx=0.5, rely=0.4, anchor="center")

sec_entry = tk.Entry(root, width=3)
sec_entry.place(relx=0.55, rely=0.4, anchor="center")
sec_entry.insert(0, "0")

start_button = tk.Button(root, text="Start", command=start_timer, bg="green", fg="white")
start_button.place(relx=0.3, rely=0.7, anchor="center")

stop_button = tk.Button(root, text="Stop", command=stop_timer, bg="red", fg="white")
stop_button.place(relx=0.5, rely=0.7, anchor="center")

reset_button = tk.Button(root, text="Reset", command=reset_timer, bg="gray", fg="white")
reset_button.place(relx=0.7, rely=0.7, anchor="center")
root.mainloop()
