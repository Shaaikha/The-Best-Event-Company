import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import pickle
import os

class VenueGUI:
    def __init__(self, root):
        self.root = root
        root.title("Venue Management System")
        root.geometry("600x400")

        # Initialize the application and load existing venue data from a pickle file, if available.
        self.filename = 'venues.pkl'
        self.venues = self.load_venues()

        # Define the input fields for venue details.
        self.entries = {}
        labels = ['Venue ID', 'Name', 'Address', 'Contact', 'Min Guests', 'Max Guests']
        for idx, label in enumerate(labels):
            ttk.Label(root, text=label).grid(row=idx, column=0, padx=10, pady=5, sticky='w')
            entry = ttk.Entry(root)
            entry.grid(row=idx, column=1, padx=10, pady=5, sticky='w')
            self.entries[label] = entry

        # Create buttons for CRUD operations (Add, Modify, Delete, Display).
        ttk.Button(root, text="Add", command=self.add_venue).grid(row=len(labels), column=0, pady=10)
        ttk.Button(root, text="Modify", command=self.modify_venue).grid(row=len(labels), column=1, pady=10)
        ttk.Button(root, text="Delete", command=self.delete_venue).grid(row=len(labels)+1, column=0, pady=10)
        ttk.Button(root, text="Display", command=self.display_venue).grid(row=len(labels)+1, column=1, pady=10)

    def load_venues(self):
        # Attempt to load venue data from a file, handling possible file corruption or IO errors.
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'rb') as f:
                    return pickle.load(f)
        except Exception as e:
            messagebox.showerror("Load Error", f"An error occurred while loading venues: {e}")
        return {}

    def save_venues(self):
        # Save the current state of venue data to a file, catching any file writing errors.
        try:
            with open(self.filename, 'wb') as f:
                pickle.dump(self.venues, f)
        except Exception as e:
            messagebox.showerror("Save Error", f"An error occurred while saving venues: {e}")

    def add_venue(self):
        # Validate the entries and add a new venue to the system if all fields are filled and the ID is unique.
        try:
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
        except Exception as e:
            messagebox.showerror("Add Error", f"Failed to add venue: {e}")

    def modify_venue(self):
        # Modify an existing venue's details after validating the venue ID and ensuring all fields are filled.
        try:
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
        except Exception as e:
            messagebox.showerror("Modification Error", f"Failed to modify venue: {e}")

    def delete_venue(self):
        # Delete a venue from the system after confirming the venue ID exists.
        try:
            venue_id = self.entries['Venue ID'].get()
            if venue_id in self.venues:
                del self.venues[venue_id]
                self.save_venues()
                messagebox.showinfo("Success", "Venue deleted successfully")
                self.clear_entries()
            else:
                messagebox.showerror("Error", "Venue not found")
        except Exception as e:
            messagebox.showerror("Deletion Error", f"Failed to delete venue: {e}")

    def display_venue(self):
        # Display detailed information for a specified venue.
        try:
            venue_id = self.entries['Venue ID'].get()
            if venue_id in self.venues:
                venue = self.venues[venue_id]
                details = '\n'.join(f"{key}: {value}" for key, value in venue.items())
                messagebox.showinfo("Venue Details", details)
            else:
                messagebox.showerror("Error", "Venue not found")
        except Exception as e:
            messagebox.showerror("Display Error", f"Failed to display venue details: {e}")

    def clear_entries(self):
        # Clear all entry widgets to be ready for new data entry.
        for entry in self.entries.values():
            entry.delete(0, tk.END)

# Main window
if __name__ == '__main__':
    root = tk.Tk()
    app = VenueGUI(root)
    root.mainloop()

