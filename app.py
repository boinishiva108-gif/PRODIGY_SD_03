import tkinter as tk
import json
import os

DATA_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# Save contacts to file
def save_contacts():
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

# Refresh contact list display
def refresh_list():
    contact_list.delete(0, tk.END)
    for c in contacts:
        contact_list.insert(tk.END, f"{c['name']} - {c['phone']} - {c['email']}")

# Add new contact
def add_contact():
    name, phone, email = name_entry.get(), phone_entry.get(), email_entry.get()
    if name and phone and email:
        contacts.append({"name": name, "phone": phone, "email": email})
        save_contacts()
        refresh_list()
        clear_entries()
        status_label.config(text=" Contact added successfully")
    else:
        status_label.config(text=" Please fill all fields")

# Edit selected contact
def edit_contact():
    selected = contact_list.curselection()
    if selected:
        index = selected[0]
        contacts[index] = {
            "name": name_entry.get(),
            "phone": phone_entry.get(),
            "email": email_entry.get()
        }
        save_contacts()
        refresh_list()
        clear_entries()
        status_label.config(text=" Contact updated successfully")
    else:
        status_label.config(text=" Select a contact to edit")

# Delete selected contact
def delete_contact():
    selected = contact_list.curselection()
    if selected:
        index = selected[0]
        contacts.pop(index)
        save_contacts()
        refresh_list()
        clear_entries()
        status_label.config(text=" Contact deleted")
    else:
        status_label.config(text=" Select a contact to delete")

# Fill entry fields when selecting a contact
def select_contact(event):
    selected = contact_list.curselection()
    if selected:
        index = selected[0]
        c = contacts[index]
        name_entry.delete(0, tk.END)
        name_entry.insert(0, c["name"])
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, c["phone"])
        email_entry.delete(0, tk.END)
        email_entry.insert(0, c["email"])

# Clear all input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("📇 Contact Management System")
root.geometry("500x500")
root.resizable(True, True)

contacts = load_contacts()

# Input fields
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root, width=40)
phone_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root, width=40)
email_entry.pack()

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Add", width=10, command=add_contact).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Edit", width=10, command=edit_contact).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", width=10, command=delete_contact).grid(row=0, column=2, padx=5)

# Contact list
contact_list = tk.Listbox(root, width=60, height=10)
contact_list.pack(pady=10)
contact_list.bind("<<ListboxSelect>>", select_contact)

# Status label
status_label = tk.Label(root, text="", fg="blue")
status_label.pack()

# Load contacts into list
refresh_list()

# Run the app
root.mainloop()

