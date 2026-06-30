import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(entry_length.get())

        if length <= 0:
            messagebox.showerror("Error", "Please enter a positive number")
            return

        characters = ""

        if var_upper.get():
            characters += string.ascii_uppercase
        if var_lower.get():
            characters += string.ascii_lowercase
        if var_digits.get():
            characters += string.digits
        if var_symbols.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Select at least one character type")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        result_var.set(password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")

# Create window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Title Label
tk.Label(root, text="Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

# Length input
tk.Label(root, text="Enter Password Length:").pack()
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

# Options
var_upper = tk.BooleanVar()
var_lower = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_symbols = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=var_upper).pack(anchor='w', padx=50)
tk.Checkbutton(root, text="Include Lowercase (a-z)", variable=var_lower).pack(anchor='w', padx=50)
tk.Checkbutton(root, text="Include Numbers (0-9)", variable=var_digits).pack(anchor='w', padx=50)
tk.Checkbutton(root, text="Include Symbols (!@#...)", variable=var_symbols).pack(anchor='w', padx=50)

# Generate button
tk.Button(root, text="Generate Password", command=generate_password, bg="blue", fg="white").pack(pady=10)

# Output field
result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, font=("Arial", 12), width=30, justify='center').pack(pady=10)

# Run app
root.mainloop()