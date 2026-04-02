import tkinter as tk 
from tkinter import messagebox 
import json 
import os

FILE_NAME = "passwords.json"

def load_passwords(): 
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file: 
                return json.load(file)
        except:
            return {}
    return {}

def save_passwords(data): 
    with open(FILE_NAME, "w") as file: 
        json.dump(data, file, indent=4)

def add_password(): 
    site = site_entry.get().strip() 
    username = username_entry.get().strip() 
    password = password_entry.get().strip()

    if not site or not username or not password:
        messagebox.showerror("Error", "Fill in all fields")
        return

    passwords[site] = {"username": username, "password": password}
    save_passwords(passwords)
    update_listbox()

    site_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

def search_password():
    site = site_entry.get().strip()
    if site in passwords:
        info = passwords[site] 
        username_entry.delete(0, tk.END)
        username_entry.insert(0, info["username"]) 
        password_entry.delete(0, tk.END)
        password_entry.insert(0, info["password"])
    else: 
        messagebox.showinfo("Not found", "No password saved for that site")

def delete_password():
    site = site_entry.get().strip()
    if site in passwords:
        del passwords[site]
        save_passwords(passwords)
        update_listbox() 
        messagebox.showinfo("Deleted", "Password removed")
    else:
        messagebox.showerror("Error", "Site not found")

def copy_password():
    password = password_entry.get()
    root.clipboard_clear() 
    root.clipboard_append(password) 
    messagebox.showinfo("Copied", "Password copied to clipboard")

def update_listbox():
    saved_list.delete(0, tk.END)
    for site in passwords:
        saved_list.insert(tk.END, site)

#Window

root = tk.Tk() 
root.title("Password Manager") 
root.geometry("500x500") 
root.config(padx=20, pady=20)

passwords = load_passwords()

#Labels + entries

tk.Label(root, text="Website").pack() 
site_entry = tk.Entry(root, width=40) 
site_entry.pack()

tk.Label(root, text="Username").pack() 
username_entry = tk.Entry(root, width=40) 
username_entry.pack()

tk.Label(root, text="Password").pack() 
password_entry = tk.Entry(root, width=40, show="*") 
password_entry.pack()

#Buttons

tk.Button(root, text="Save", command=add_password).pack(pady=5) 
tk.Button(root, text="Search", command=search_password).pack(pady=5) 
tk.Button(root, text="Delete", command=delete_password).pack(pady=5) 
tk.Button(root, text="Copy Password", command=copy_password).pack(pady=5)

#Saved sites list

tk.Label(root, text="Saved Websites").pack(pady=10) 
saved_list = tk.Listbox(root, width=40, height=10) 
saved_list.pack()

update_listbox()

root.mainloop()