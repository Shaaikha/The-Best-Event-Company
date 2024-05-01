import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import pickle
import os

class VenueGUI:
    def __init__(self, root):
        self.root = root
        root.title("Venue Management System")
        root.geometry("600x400")

        # Load venues if the file exists
        self.filename = 'venues.pkl'
        self.venues = self.load_venues()

        # Venue form fields
        self.entries = {}
        labels = ['Venue ID', 'Name', 'Address', 'Contact', 'Min Guests', 'Max Guests']
        for idx, label in enumerate(labels):
            ttk.Label(root, text=label).grid(row=idx, column=0, padx=10, pady=5, sticky='w')
            entry = ttk.Entry(root)
            entry.grid(row=idx, column=1, padx=10, pady=5, sticky='w')
            self.entries[label] = entry

        # Buttons for operations
        ttk.Button(root, text="Add", command=self.add_venue).grid(row=len(labels), column=0, pady=10)
        ttk.Button(root, text="Modify", command=self.modify_venue).grid(row=len(labels), column=1, pady=10)
        ttk.Button(root, text="Delete", command=self.delete_venue).grid(row=len(labels)+1, column=0, pady=10)
        ttk.Button(root, text="Display", command=self.display_venue).grid(row=len(labels)+1, column=1, pady=10)

    def load_venues(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as f:
                return pickle.load(f)
        return {}

    def save_venues(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.venues, f)

    def add_venue(self):
        data = {label: self.entries[label].get() for label in self.entries}
        if not all(data.values()):
            messagebox.showerror("Error", "All fields are required")
            return
        if data['Venue ID'] in self.venues:
            messagebox.showerror("Error", "Venue ID already exists")
            return
        self.venues[data['Venue ID']] = data
        self.save_venues()
        messagebox.showinfo("Success", "Venue added successfully")
        self.clear_entries()

    def modify_venue(self):
        venue_id = self.entries['Venue ID'].get()
        if not venue_id or venue_id not in self.venues:
            messagebox.showerror("Error", "Invalid Venue ID")
            return
        data = {label: self.entries[label].get() for label in self.entries}
        if not all(data.values()):
            messagebox.showerror("Error", "All fields must be filled to modify")
            return
        self.venues[venue_id].update(data)
        self.save_venues()
        messagebox.showinfo("Success", "Venue modified successfully")
        self.clear_entries()

    def delete_venue(self):
        venue_id = self.entries['Venue ID'].get()
        if venue_id in self.venues:
            del self.venues[venue_id]
            self.save_venues()
            messagebox.showinfo("Success", "Venue deleted successfully")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Venue not found")

    def display_venue(self):
        venue_id = self.entries['Venue ID'].get()
        if venue_id in self.venues:
            venue = self.venues[venue_id]
            details = '\n'.join(f"{key}: {value}" for key, value in venue.items())
            messagebox.showinfo("Venue Details", details)
        else:
            messagebox.showerror("Error", "Venue not found")

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

# Main window
if __name__ == '__main__':
    root = tk.Tk()
    app = VenueGUI(root)
    root.mainloop()
