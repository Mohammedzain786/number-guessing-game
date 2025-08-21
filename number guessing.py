
import tkinter as tk
from tkinter import ttk, messagebox
import random

def start_game():
    global secret_number, attempts, game_active
    secret_number = random.randint(1, 100)
    attempts = 0
    game_active = True
    entry.config(state="normal")
    entry.delete(0, tk.END)
    result_label.config(text="", fg="white", bg="black")
    attempts_label.config(text="Attempts: 0")
    messagebox.showinfo("Game Started!", "I have chosen a number between 1 and 100.\nTry to guess it!")

def check_guess():
    global attempts, game_active
    if not game_active:
        return

    try:
        guess = int(entry.get())
        attempts += 1
        attempts_label.config(text=f"Attempts: {attempts}", foreground="orange")

        if guess < secret_number:
            result_label.config(text="Too low! ❄️", fg="skyblue")
        elif guess > secret_number:
            result_label.config(text="Too high! 🔥", fg="red")
        else:
            result_label.config(text=f"🎉 Correct! You guessed it in {attempts} attempts.", fg="lime")
            messagebox.showinfo("🎉 You Win!", f"Correct! You guessed it in {attempts} attempts.")
            entry.config(state="disabled")
            game_active = False
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number.")

# GUI setup
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("450x350")
root.configure(bg="black")

# ----- ttk Styles -----
style = ttk.Style()
style.theme_use("clam")  # needed for custom colors

style.configure("Check.TButton",
                font=("Arial", 12, "bold"),
                foreground="white",
                background="skyblue",
                padding=6)
style.map("Check.TButton",
          background=[("active", "#3399ff")],
          foreground=[("active", "white")])

style.configure("Reset.TButton",
                font=("Arial", 12, "bold"),
                foreground="white",
                background="limegreen",
                padding=6)
style.map("Reset.TButton",
          background=[("active", "green")],
          foreground=[("active", "white")])

# Title
title_label = tk.Label(root, text="🎲 Number Guessing Game 🎲", font=("Arial", 18, "bold"), bg="black", fg="gold")
title_label.pack(pady=15)

# Instructions
instruction_label = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 12), bg="black", fg="white")
instruction_label.pack(pady=5)

# Entry
entry = tk.Entry(root, font=("Arial", 16), justify="center", bg="white", fg="black")
entry.pack(pady=10)

# Buttons (styled)
check_button = ttk.Button(root, text="Check Guess", style="Check.TButton", command=check_guess)
check_button.pack(pady=5)

reset_button = ttk.Button(root, text="Restart Game", style="Reset.TButton", command=start_game)
reset_button.pack(pady=5)

# Attempts counter
attempts_label = tk.Label(root, text="Attempts: 0", font=("Arial", 12, "bold"), bg="black", fg="orange")
attempts_label.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="black", fg="white")
result_label.pack(pady=15)

# Start game
start_game()

root.mainloop()
