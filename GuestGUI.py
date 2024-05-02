import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import pickle
import os

class GuestGUI:
    """Class for Guest GUI"""
    def __init__(self, root):
        self.root = root
        root.title("Guest Management System")
        root.geometry("600x300")

        # Initialize the GUI for managing guest data, loading existing data if available.
        self.filename = 'guests.pkl'
        self.guests = self.load_guests()

        # Define the form fields for guest data entry.
        self.entries = {}
        labels = ['Guest ID', 'Name', 'Address', 'Contact Details']
        for idx, label in enumerate(labels):
            ttk.Label(root, text=label).grid(row=idx, column=0, padx=10, pady=5, sticky='w')
            entry = ttk.Entry(root)
            entry.grid(row=idx, column=1, padx=10, pady=5, sticky='w')
            self.entries[label] = entry

        # Setup buttons for CRUD operations (Create, Read, Update, Delete).
        ttk.Button(root, text="Add", command=self.add_guest).grid(row=len(labels), column=0, pady=10)
        ttk.Button(root, text="Modify", command=self.modify_guest).grid(row=len(labels), column=1, pady=10)
        ttk.Button(root, text="Delete", command=self.delete_guest).grid(row=len(labels)+1, column=0, pady=10)
        ttk.Button(root, text="Display", command=self.display_guest).grid(row=len(labels)+1, column=1, pady=10)

    def load_guests(self):
        # Load guest data from a pickle file, handle exceptions related to file access and data integrity.
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'rb') as f:
                    return pickle.load(f)
        except Exception as e:
            messagebox.showerror("Load Error", f"An error occurred while loading guests: {e}")
        return {}

    def save_guests(self):
        # Save the current guest data to a file, handling potential data writing errors.
        try:
            with open(self.filename, 'wb') as f:
                pickle.dump(self.guests, f)
        except Exception as e:
            messagebox.showerror("Save Error", f"An error occurred while saving guests: {e}")

    def add_guest(self):
        # Validate the entries and add a new guest if all fields are filled and the guest ID is unique.
        try:
            data = {label: self.entries[label].get() for label in self.entries}
            if not all(data.values()):
                messagebox.showerror("Validation Error", "All fields are required")
                return
            if data['Guest ID'] in self.guests:
                messagebox.showerror("Duplicate Error", "Guest ID already exists")
                return
            self.guests[data['Guest ID']] = data
            self.save_guests()
            messagebox.showinfo("Success", "Guest added successfully")
            self.clear_entries()
        except Exception as e:
            messagebox.showerror("Add Error", f"An error occurred while adding a guest: {e}")

    def modify_guest(self):
        # Modify an existing guest's details after validating the guest ID and data completeness.
        try:
            guest_id = self.entries['Guest ID'].get()
            if not guest_id or guest_id not in self.guests:
                messagebox.showerror("Invalid ID", "Invalid Guest ID")
                return
            data = {label: self.entries[label].get() for label in self.entries}
            if not all(data.values()):
                messagebox.showerror("Incomplete Data", "All fields must be filled to modify")
                return
            self.guests[guest_id].update(data)
            self.save_guests()
            messagebox.showinfo("Success", "Guest modified successfully")
            self.clear_entries()
        except Exception as e:
            messagebox.showerror("Modification Error", f"An error occurred while modifying guest details: {e}")

    def delete_guest(self):
        # Delete a guest after confirming the guest ID exists.
        try:
            guest_id = self.entries['Guest ID'].get()
            if guest_id in self.guests:
                del self.guests[guest_id]
                self.save_guests()
                messagebox.showinfo("Success", "Guest deleted successfully")
                self.clear_entries()
            else:
                messagebox.showerror("Not Found", "Guest not found")
        except Exception as e:
            messagebox.showerror("Deletion Error", f"An error occurred while deleting the guest: {e}")

    def display_guest(self):
        # Display details of a specific guest.
        try:
            guest_id = self.entries['Guest ID'].get()
            if guest_id in self.guests:
                guest = self.guests[guest_id]
                details = '\n'.join(f"{key}: {value}" for key, value in guest.items())
                messagebox.showinfo("Guest Details", details)
            else:
                messagebox.showerror("Not Found", "Guest not found")
        except Exception as e:
            messagebox.showerror("Display Error", f"An error occurred while displaying guest details: {e}")

    def clear_entries(self):
        # Clear all entry widgets to be ready for new data entry.
        for entry in self.entries.values():
            entry.delete(0, tk.END)

# Main window setup and event loop
if __name__ == '__main__':
    root = tk.Tk()
    app = GuestGUI(root)
    root.mainloop()

