import tkinter as tk

import random
import string

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 200

#COLORS
BACKGROUND_COLOR = "#020617"
BUTTON_COLOR = "#22C55E"
ACTIVE_BUTTON_COLOR = "#22C55E"
TITLE_COLOR = "#0EA5E9"


root = tk.Tk()
root.title("Example")
root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
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

    char_count = tk.StringVar()
    char_count_entry_box = tk.Entry(root, textvariable = char_count)
    char_count_entry_box.place(x = 360, y = 111, width = 30)

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

    make_password_button = tk.Button(root, text = "Make Password", command =  lambda: make_password(lowercase_letters, uppercase_letters, numbers, special_characters, char_count), bg = BUTTON_COLOR, activebackground = ACTIVE_BUTTON_COLOR, font = ("Inter", 27, "bold"))
    make_password_button.place(x = SCREEN_WIDTH // 2 - 150 , y = 375, width = 300)

def make_password(lowercase_letters, uppercase_letters, numbers, special_characters, char_count):
    
    possible_characters = ""
    try: error_text.destroy()
    except: pass

    if lowercase_letters.get():
        possible_characters += "abcdefghijklmnopqrstuvwxyz"
    
    if uppercase_letters.get():
        possible_characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if numbers.get():
        possible_characters += "1234567890"

    if special_characters.get():
        possible_characters += string.punctuation
    
    error = find_error(possible_characters, char_count)

    if error == 1:
        try: error_text.destroy()
        except: pass
        error_text = tk.Label(root, text = "Enter acceptable length (8 - 30)", font = ("Inter", 15, "bold"), bg = BACKGROUND_COLOR, fg = "white")
        error_text.place(x = 0, y = 500, width = SCREEN_WIDTH)
    
    if error == 2:
        try: error_text.destroy()
        except: pass
        error_text = tk.Label(root, text = "Select at least one of the boxes and input acceptable length (8 - 30)", font = ("Inter", 15, "bold"), bg = BACKGROUND_COLOR, fg = "white")
        error_text.place(x = 0, y = 500, width = SCREEN_WIDTH)

    if error == 3:
        try: error_text.destroy()
        except: pass
        error_text = tk.Label(root, text = "Enter length between 8 and 30", font = ("Inter", 15, "bold"), bg = BACKGROUND_COLOR, fg = "white")
        error_text.place(x = 0, y = 500, width = SCREEN_WIDTH)
    
    if error == 4:
        password = ""
        char_count = int(char_count.get())
        for i in range(char_count):
            password = password + possible_characters[random.randint(0, len(possible_characters) - 1)]
        
        print(password)
            


    


def find_error(possible_characters, char_count):
#Error Codes: 1 - Char-count not int, 2 - invalid char_count and no character type selctions, 3 - No character type selections, 4 - No Error

    try:
        char_count = int(char_count.get())
    except ValueError:
        if possible_characters == "":
            return 2
        else:
            return 1
    if possible_characters == "" and char_count < 7 or char_count > 30:
        return 2
    if char_count < 7 or char_count > 30:
        return 3
    
    return 4
    
    
    
        


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