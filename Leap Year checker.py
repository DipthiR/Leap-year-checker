import tkinter as tk
from tkinter import messagebox

def is_leap_year(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def check_leap_year():
    try:
        year = int(entry.get())
        if is_leap_year(year):
            result_label.config(
                text=f"✅ {year} is a Leap Year! 🎉",
                fg="green"
            )
        else:
            result_label.config(
                text=f"❌ {year} is NOT a Leap Year.",
                fg="red"
            )
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid year (number).")

# Create main window
root = tk.Tk()
root.title("🌍 Leap Year Checker")
root.geometry("400x250")
root.configure(bg="#f0f8ff")  # Light blue background

# Title label
title = tk.Label(root, text="Leap Year Checker", font=("Arial", 20, "bold"), bg="#f0f8ff", fg="#333")
title.pack(pady=10)

# Entry widget
entry_label = tk.Label(root, text="📅 Enter a Year:", font=("Arial", 14), bg="#f0f8ff")
entry_label.pack()

entry = tk.Entry(root, font=("Arial", 14), width=10, justify='center')
entry.pack(pady=5)

# Button
check_button = tk.Button(root, text="Check", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", command=check_leap_year)
check_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f0f8ff")
result_label.pack(pady=10)

# Start GUI loop
root.mainloop()
