import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import pickle
import os

class GuestGUI:
    def __init__(self, root):
        self.root = root
        root.title("Guest Management System")
        root.geometry("600x300")

        # Load guests if the file exists
        self.filename = 'guests.pkl'
        self.guests = self.load_guests()

        # Guest form fields
        self.entries = {}
        labels = ['Guest ID', 'Name', 'Address', 'Contact Details']
        for idx, label in enumerate(labels):
            ttk.Label(root, text=label).grid(row=idx, column=0, padx=10, pady=5, sticky='w')
            entry = ttk.Entry(root)
            entry.grid(row=idx, column=1, padx=10, pady=5, sticky='w')
            self.entries[label] = entry

        # Buttons for operations
        ttk.Button(root, text="Add", command=self.add_guest).grid(row=len(labels), column=0, pady=10)
        ttk.Button(root, text="Modify", command=self.modify_guest).grid(row=len(labels), column=1, pady=10)
        ttk.Button(root, text="Delete", command=self.delete_guest).grid(row=len(labels)+1, column=0, pady=10)
        ttk.Button(root, text="Display", command=self.display_guest).grid(row=len(labels)+1, column=1, pady=10)

    def load_guests(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as f:
                return pickle.load(f)
        return {}

    def save_guests(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.guests, f)

    def add_guest(self):
        data = {label: self.entries[label].get() for label in self.entries}
        if not all(data.values()):
            messagebox.showerror("Error", "All fields are required")
            return
        if data['Guest ID'] in self.guests:
            messagebox.showerror("Error", "Guest ID already exists")
            return
        self.guests[data['Guest ID']] = data
        self.save_guests()
        messagebox.showinfo("Success", "Guest added successfully")
        self.clear_entries()

    def modify_guest(self):
        guest_id = self.entries['Guest ID'].get()
        if not guest_id or guest_id not in self.guests:
            messagebox.showerror("Error", "Invalid Guest ID")
            return
        data = {label: self.entries[label].get() for label in self.entries}
        if not all(data.values()):
            messagebox.showerror("Error", "All fields must be filled to modify")
            return
        self.guests[guest_id].update(data)
        self.save_guests()
        messagebox.showinfo("Success", "Guest modified successfully")
        self.clear_entries()

    def delete_guest(self):
        guest_id = self.entries['Guest ID'].get()
        if guest_id in self.guests:
            del self.guests[guest_id]
            self.save_guests()
            messagebox.showinfo("Success", "Guest deleted successfully")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Guest not found")

    def display_guest(self):
        guest_id = self.entries['Guest ID'].get()
        if guest_id in self.guests:
            guest = self.guests[guest_id]
            details = '\n'.join(f"{key}: {value}" for key, value in guest.items())
            messagebox.showinfo("Guest Details", details)
        else:
            messagebox.showerror("Error", "Guest not found")

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

# Main window
if __name__ == '__main__':
    root = tk.Tk()
    app = GuestGUI(root)
    root.mainloop()
