#TODO Accounts, hash account passwords, view passwords, improve passwords.json

import tkinter as tk
import random
import string
import json
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 200

#COLORS
BACKGROUND_COLOR = "#020617"
BUTTON_COLOR = "#22C55E"
ACTIVE_BUTTON_COLOR = "#22C55E"
TITLE_COLOR = "#0EA5E9"

PASSWORDS_FILE = "passwords.json"
ACCOUNTS_FILE = "accounts.json"



root = tk.Tk()
root.title("Password Manager")
root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
root.configure(bg = BACKGROUND_COLOR)

def load_passwords():
    if os.path.exists(PASSWORDS_FILE):
        try:
            with open(PASSWORDS_FILE, "r") as file:
                return json.load(file)
        except:
            return {}
    return {}

def load_accounts():
    if os.path.exists(ACCOUNTS_FILE):
        try:
            with open(ACCOUNTS_FILE, "r") as file:
                return json.load(file)
        except:
            return {}
    return {}

passwords = load_passwords()
accounts = load_accounts()
logged_in = False

def save_passwords(data):
    with open(PASSWORDS_FILE, "w") as file:
        json.dump(data, file, indent = 4)

def save_accounts(data):
    with open(ACCOUNTS_FILE, "w") as file:
        json.dump(data, file, indent = 4)

def add_password(site, username, password):
    site = site.get().strip() 
    username = username.get().strip() 
    password = password.get().strip()

    if site == "" or username == "" or password == "":
        error_text = tk.Label(root, text = "Fill in all fields", font = ("Inter", 15, "bold"), bg = BACKGROUND_COLOR, fg = "white")
        error_text.place(x = 0, y = 450, width = SCREEN_WIDTH)
        return
    
    passwords[site] = {"username": username, "password": password}
    save_passwords(passwords)

    password_saved_text = tk.Label(root, text = "Password Saved", font = ("Inter", 15, "bold"), bg = BACKGROUND_COLOR, fg = "white")
    password_saved_text.place(x = 0, y = 450, width = SCREEN_WIDTH)




def generate_password():
    for widget in root.winfo_children():
        widget.destroy()
    
    title = tk.Label(root, text = "Generate Password", font = ("Inter", 40, "bold"), bg = BACKGROUND_COLOR, fg = TITLE_COLOR)
    title.pack()

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

    home_button = tk.Button(root, text = "Home", command = home_screen, bg = BUTTON_COLOR, activebackground = ACTIVE_BUTTON_COLOR, font = ("Inter", 27, "bold"))
    home_button.place(x = 0, y = 0)

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
        error_text = tk.Label(root, text = "Enter acceptable length (8 - 30)", font = ("Inter", 15, "bold"), bg = BACKGROUND_COLOR, fg = "white")
        error_text.place(x = 0, y = 450, width = SCREEN_WIDTH)
    
    if error == 2:
        error_text = tk.Label(root, text = "Select at least one of the boxes and input acceptable length (8 - 30)", font = ("Inter", 15, "bold"), bg = BACKGROUND_COLOR, fg = "white")
        error_text.place(x = 0, y = 450, width = SCREEN_WIDTH)

    if error == 3:
        error_text = tk.Label(root, text = "Enter length between 8 and 30", font = ("Inter", 15, "bold"), bg = BACKGROUND_COLOR, fg = "white")
        error_text.place(x = 0, y = 450, width = SCREEN_WIDTH)
    
    if error == 4:
        error_text = tk.Label(root, text = "Select atleast one of the boxes", font = ("Inter", 15, "bold"), bg = BACKGROUND_COLOR, fg = "white")
        error_text.place(x = 0, y = 450, width = SCREEN_WIDTH)
    
    if error == 5:
        password = ""
        lowercase_pool = "abcdefghijklmnopqrstuv"
        uppercase_pool = "ABCDEFGHIJKLMNOPQRSTUV"
        numbers_pool = "1234567890"
        special_pool = string.punctuation
        
        char_count = int(char_count.get())
        if lowercase_letters.get():
            password = password + lowercase_pool[random.randint(0, len(lowercase_pool) - 1)]
            char_count -= 1
        if uppercase_letters.get():
            password = password + uppercase_pool[random.randint(0, len(uppercase_pool) - 1)]
            char_count -= 1
        if numbers.get():
            password = password + numbers_pool[random.randint(0, len(numbers_pool) - 1)]
            char_count -= 1
        if special_characters.get():
            password = password + special_pool[random.randint(0, len(special_pool) - 1)]
            char_count -= 1
        
        for i in range(char_count):
            password = password + possible_characters[random.randint(0, len(possible_characters) -1 )]
        
        password = list(password)
        random.shuffle(password)
        password = "".join(password)
        
        password_text = tk.Label(root, text = password, font = ("Inter", 15, "bold"), bg = BACKGROUND_COLOR, fg = "white")
        password_text.place(x = 0, y = 450, width = SCREEN_WIDTH)

        copy_button = tk.Button(root, text = "Copy Password", command =  lambda: copy_to_clipboard(password), bg = BUTTON_COLOR, activebackground = ACTIVE_BUTTON_COLOR, font = ("Inter", 14, "bold"))
        copy_button.place(x = SCREEN_WIDTH // 2 - 150, y = 500, width = 300, height = 25)

        add_button = tk.Button(root, text = "Add to Manager", command = add_password_screen, bg = BUTTON_COLOR, activebackground = ACTIVE_BUTTON_COLOR, font = ("Inter", 14, "bold"))
        add_button.place(x = SCREEN_WIDTH // 2 - 150, y = 530, width = 300, height = 25)

def find_error(possible_characters, char_count):
#Error Codes: 1 - Char-count not int, 2 - invalid char_count and no character type selctions, 3 - Invalid length, 4 - No character selection, 5 - No Error

    try:
        char_count = int(char_count.get())
    except ValueError:
        if possible_characters == "":
            return 2
        else:
            return 1
    if possible_characters == "" and (char_count < 7 or char_count > 30):
        return 2
    if char_count < 7 or char_count > 30:
        return 3
    if possible_characters == "":
        return 4
    
    return 5

def copy_to_clipboard(password):
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()
    

def view_passwords():
    for widget in root.winfo_children():
        widget.destroy()

    if logged_in == False:
        login_screen()
    
    else:
    
        title = tk.Label(root, text = "View Passwords", font = ("Inter", 40, "bold"), bg = BACKGROUND_COLOR, fg = TITLE_COLOR)
        title.pack()

        home_button = tk.Button(root, text = "Home", command = home_screen, bg = BUTTON_COLOR, activebackground = ACTIVE_BUTTON_COLOR, font = ("Inter", 27, "bold"))
        home_button.place(x = 0, y = 0)

def add_password_screen():
    for widget in root.winfo_children():
        widget.destroy()
    
    title = tk.Label(root, text = "Add Password", font = ("Inter", 40, "bold"), bg = BACKGROUND_COLOR, fg = TITLE_COLOR)
    title.pack()

    home_button = tk.Button(root, text = "Home", command = home_screen, bg = BUTTON_COLOR, activebackground = ACTIVE_BUTTON_COLOR, font = ("Inter", 27, "bold"))
    home_button.place(x = 0, y = 0)

    site_entry_text = tk.Label(root, text = "Website: ", font = ("Inter", 20, "bold"), bg = BACKGROUND_COLOR, fg = "white")
    site_entry_text.place(x = 50, y = 100)

    username_entry_text = tk.Label(root, text = "Username: ", font = ("Inter", 20, "bold"), bg = BACKGROUND_COLOR, fg = "white")
    username_entry_text.place(x = 50, y = 135)

    password_entry_text = tk.Label(root, text = "Password: ", font = ("Inter", 20, "bold"), bg = BACKGROUND_COLOR, fg = "white")
    password_entry_text.place(x = 50, y = 170)

    site = tk.StringVar()
    site_entry = tk.Entry(root, textvariable = site)
    site_entry.place(x = 170, y = 110, width = 300)

    username = tk.StringVar()
    username_entry = tk.Entry(root, textvariable = username)
    username_entry.place(x = 200, y = 145, width = 300)

    password = tk.StringVar()
    password_entry = tk.Entry(root, textvariable = password, show = "*")
    password_entry.place(x = 200, y = 180, width = 300)

    save_button = tk.Button(root, text = "Save Password", command = lambda: add_password(site, username, password), bg = BUTTON_COLOR, activebackground = ACTIVE_BUTTON_COLOR, font = ("Inter", 20, "bold"))
    save_button.place(x = SCREEN_WIDTH // 2 - 150 , y = 250, width = 300)



def home_screen():
    for widget in root.winfo_children():
        widget.destroy()
    
    title = tk.Label(root, text = "Password Manager", font = ("Inter", 40, "bold"), bg = BACKGROUND_COLOR, fg = TITLE_COLOR)
    title.pack()

    generate_password_button = tk.Button(root, text = "Generate\nPassword", command = generate_password, bg = BUTTON_COLOR, activebackground = ACTIVE_BUTTON_COLOR, font = ("Imter", 27, "bold"))
    generate_password_button.place(x = 50, y = 150, width = BUTTON_WIDTH, height = BUTTON_HEIGHT)

    view_passwords_button = tk.Button(root, text = "View\nPasswords", command = view_passwords, bg = BUTTON_COLOR, activebackground = ACTIVE_BUTTON_COLOR, font = ("Inter", 27, "bold"))
    view_passwords_button.place(x = 300, y = 150, width = BUTTON_WIDTH, height = BUTTON_HEIGHT)

    add_passwords_button = tk.Button(root, text = "Add\nPassword", command = add_password_screen, bg = BUTTON_COLOR, activebackground = ACTIVE_BUTTON_COLOR, font = ("Inter", 27, "bold"))
    add_passwords_button.place(x = 550, y = 150, width = BUTTON_WIDTH, height = BUTTON_HEIGHT)

def login_screen():

    title = tk.Label(root, text = "Login or Add Account", font = ("Inter", 38, "bold"), bg = BACKGROUND_COLOR, fg = TITLE_COLOR)
    title.pack()

    login_button = tk.Button(root, text = "Login", command = login, bg = BUTTON_COLOR, activebackground = ACTIVE_BUTTON_COLOR, font = ("Inter", 27, "bold"))
    login_button.place(x = 150, y = 200, width = BUTTON_WIDTH, height = BUTTON_HEIGHT)

    add_account_button = tk.Button(root, text = "Add\nAccount", command = add_account, bg = BUTTON_COLOR, activebackground = ACTIVE_BUTTON_COLOR, font = ("Inter", 27, "bold"))
    add_account_button.place(x = 400, y = 200, width = BUTTON_WIDTH, height = BUTTON_HEIGHT)

    home_button = tk.Button(root, text = "Home", command = home_screen, bg = BUTTON_COLOR, activebackground = ACTIVE_BUTTON_COLOR, font = ("Inter", 27, "bold"))
    home_button.place(x = 0, y = 0)


def login():
    pass

def add_account():
    for widget in root.winfo_children():
        widget.destroy()

    title = tk.Label(root, text = "Add Account", font = ("Inter", 38, "bold"), bg = BACKGROUND_COLOR, fg = TITLE_COLOR)
    title.pack()

    username_entry_text = tk.Label(root, text = "Username: ", font = ("Inter", 20, "bold"), bg = BACKGROUND_COLOR, fg = "white")
    username_entry_text.place(x = 50, y = 135)

    password_entry_text = tk.Label(root, text = "Password: ", font = ("Inter", 20, "bold"), bg = BACKGROUND_COLOR, fg = "white")
    password_entry_text.place(x = 50, y = 170)

    username = tk.StringVar()
    username_entry = tk.Entry(root, textvariable = username)
    username_entry.place(x = 200, y = 145, width = 300)

    password = tk.StringVar()
    password_entry = tk.Entry(root, textvariable = password, show = "*")
    password_entry.place(x = 200, y = 180, width = 300)

    login_button = tk.Button(root, text = "Login", command = check_login, bg = BUTTON_COLOR, activebackground = ACTIVE_BUTTON_COLOR, font = ("Inter", 27, "bold"))
    login_button.place(x = 150, y = 200)

    def check_login():
        pass

home_screen()
root.mainloop()