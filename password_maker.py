import tkinter as tk
from tkextrafont import Font
import random

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 200

#COLORS
BACKGROUND_COLOR = "#020617"
BUTTON_COLOR = "#22C55E"
ACTIVE_BUTTON_COLOR = "#22C55E"
TITLE_COLOR = "#0EA5E9"


root = tk.Tk()
root.title("Example")
root.geometry("800x600")
root.configure(bg = BACKGROUND_COLOR)


title = tk.Label(root, text = "Password Manager", font = ("Inter", 40, "bold"), bg = BACKGROUND_COLOR, fg = TITLE_COLOR)
title.pack()

def generate_password():
    title.configure(text = "Generate Password")
    generate_password_button.destroy()
    view_passwords_button.destroy()
    add_passwords_button.destroy()

    char_count_text = tk.Label(root, text = "Number of Characters:", font = ("Inter", 20, "bold"), bg = BACKGROUND_COLOR, fg = "white")
    char_count_text.place(x = 50, y = 100)

    char_count = tk.Entry(root)
    char_count.place(x = 360, y = 111, width = 30)

    lowercase_letters = tk.BooleanVar()
    lowercase_letters_box = tk.Checkbutton(root, text = "Lowercase Letters?", font = ("Inter", 15, "bold"), bg = BACKGROUND_COLOR, fg = "white", activebackground = BACKGROUND_COLOR, activeforeground = "white", selectcolor = BACKGROUND_COLOR, variable = lowercase_letters)
    lowercase_letters_box.place(x = 50, y = 150)

    uppercase_letters = tk.BooleanVar()
    uppercase_letters_box = tk.Checkbutton(root, text = "Uppercase Letters?", font = ("Inter", 15, "bold"), bg = BACKGROUND_COLOR, fg = "white", activebackground = BACKGROUND_COLOR, activeforeground = "white", selectcolor = BACKGROUND_COLOR, variable = uppercase_letters)
    uppercase_letters_box.place(x = 50, y = 200)

    numbers = tk.BooleanVar()
    numbers_box = tk.Checkbutton(root, text = "Numbers?", font = ("Inter", 15, "bold"), bg = BACKGROUND_COLOR, fg = "white", activebackground = BACKGROUND_COLOR, activeforeground = "white", selectcolor = BACKGROUND_COLOR, variable = numbers)
    numbers_box.place(x = 50, y = 250)

    special_characters = tk.BooleanVar()
    special_characters_box = tk.Checkbutton(root, text = "Special Characters?", font = ("Inter", 15, "bold"), bg = BACKGROUND_COLOR, fg = "white", activebackground = BACKGROUND_COLOR, activeforeground = "white", selectcolor = BACKGROUND_COLOR, variable = special_characters)
    special_characters_box.place(x = 50, y = 300)


def view_passwords():
    title.configure(text = "View Passwords")
    generate_password_button.destroy()
    view_passwords_button.destroy()
    add_passwords_button.destroy()

def add_password():
    title.configure(text = "Add Password")
    generate_password_button.destroy()
    view_passwords_button.destroy()
    add_passwords_button.destroy()

generate_password_button = tk.Button(root, text = "Generate\nPassword", command = generate_password, bg = BUTTON_COLOR, activebackground = ACTIVE_BUTTON_COLOR, font = ("Imter", 27, "bold"))
generate_password_button.place(x = 50, y = 150, width = BUTTON_WIDTH, height = BUTTON_HEIGHT)

view_passwords_button = tk.Button(root, text = "View\nPasswords", command = view_passwords, bg = BUTTON_COLOR, activebackground = ACTIVE_BUTTON_COLOR, font = ("Inter", 27, "bold"))
view_passwords_button.place(x = 300, y = 150, width = BUTTON_WIDTH, height = BUTTON_HEIGHT)

add_passwords_button = tk.Button(root, text = "Add\nPassword", command = add_password, bg = BUTTON_COLOR, activebackground = ACTIVE_BUTTON_COLOR, font = ("Inter", 27, "bold"))
add_passwords_button.place(x = 550, y = 150, width = BUTTON_WIDTH, height = BUTTON_HEIGHT)





root.mainloop()