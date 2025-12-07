import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")

def copy_password():
    window.clipboard_clear()
    window.clipboard_append(result_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")


window = tk.Tk()
window.title("Password Generator")
window.geometry("350x200")
window.config(bg="black")


title_label = tk.Label(window, text="Password Generator ", font=("Arial", 14), bg="black")
title_label.pack(pady=10)

length_label = tk.Label(window, text="Enter Password Length:", bg="black")
length_label.pack()

length_entry = tk.Entry(window)
length_entry.pack(pady=5)

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)

result_entry = tk.Entry(window, width=30)
result_entry.pack(pady=5)

copy_button = tk.Button(window, text="Copy", command=copy_password)
copy_button.pack(pady=5)

window.mainloop()
