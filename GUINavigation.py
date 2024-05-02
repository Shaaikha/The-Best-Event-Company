import tkinter as tk
from tkinter import messagebox, ttk
import pickle
import os

class BestEventCompanyGUI:
    """Class for best event company GUI to handle the company's operations"""
    def __init__(self, root):
        self.root = root
        root.title("Event Management System")
        root.geometry("500x500")

        #First, we will load existing data from file or initialize new data structure
        self.filename = 'ALLDATA.pkl'
        self.entities = self.load_data()
        self.current_entity_type = 'Employees'

        #Then we add entity form setup: dictionaries to store entry widgets and labels
        self.entries = {}
        self.labels = {}
        self.setup_labels()  # Initialize labels based on entity types

        #The addition of tabs creation for each entity type
        self.tabControl = ttk.Notebook(root)
        self.tabControl.pack(expand=1, fill="both")

        for entity_type in self.labels.keys():
            tab = ttk.Frame(self.tabControl)
            self.tabControl.add(tab, text=entity_type)

            #Add each tab with labels and entry fields
            for idx, label in enumerate(self.labels[entity_type]):
                ttk.Label(tab, text=label).grid(row=idx, column=0, padx=10, pady=5, sticky='w')
                entry = ttk.Entry(tab)
                entry.grid(row=idx, column=1, padx=10, pady=5, sticky='w')
                self.entries[(entity_type, label)] = entry

            #Then, we add the buttons for Add, Modify, Delete, Display operations
            ttk.Button(tab, text="Add", command=lambda et=entity_type: self.add_entity(et)).grid(row=len(self.labels[entity_type]), column=0, pady=10)
            ttk.Button(tab, text="Modify", command=lambda et=entity_type: self.modify_entity(et)).grid(row=len(self.labels[entity_type]), column=1, pady=10)
            ttk.Button(tab, text="Delete", command=lambda et=entity_type: self.delete_entity(et)).grid(row=len(self.labels[entity_type])+1, column=0, pady=10)
            ttk.Button(tab, text="Display", command=lambda et=entity_type: self.display_entity(et)).grid(row=len(self.labels[entity_type])+1, column=1, pady=10)

        #Adding a button to clear all entry fields
        ttk.Button(root, text="Clear Entries", command=self.clear_entries).pack(pady=10)

    def load_data(self):
        """Load entity data from a file if it exists; otherwise, initialize an empty data structure."""
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as f:
                return pickle.load(f)
        return {'Employees': {}, 'Events': {}, 'Clients': {}, 'Guests': {}, 'Suppliers': {}, 'Venues': {}}

    def save_data(self):
        """Save the current entities to a file."""
        with open(self.filename, 'wb') as f:
            pickle.dump(self.entities, f)

    def add_entity(self, entity_type):
        """Add a new entity after validating all fields are filled."""
        data = {label: self.entries[(entity_type, label)].get() for label in self.labels[entity_type]}
        if not all(data.values()):
            messagebox.showerror("Error", "All fields are required")
            return
        if data['ID'] in self.entities[entity_type]:
            messagebox.showerror("Error", f"{entity_type[:-1]} ID already exists")
            return
        self.entities[entity_type][data['ID']] = data
        self.save_data()
        messagebox.showinfo("Success", f"{entity_type[:-1]} added successfully")
        self.clear_entries()

    def modify_entity(self, entity_type):
        """Modify an existing entity after validating the ID and all fields are filled."""
        entity_id = self.entries[(entity_type, 'ID')].get()
        if not entity_id or entity_id not in self.entities[entity_type]:
            messagebox.showerror("Error", "Invalid ID")
            return
        data = {label: self.entries[(entity_type, label)].get() for label in self.labels[entity_type]}
        if not all(data.values()):
            messagebox.showerror("Error", "All fields must be filled to modify")
            return
        self.entities[entity_type][entity_id].update(data)
        self.save_data()
        messagebox.showinfo("Success", f"{entity_type[:-1]} modified successfully")
        self.clear_entries()

    def delete_entity(self, entity_type):
        """Delete an entity after validating the ID exists."""
        entity_id = self.entries[(entity_type, 'ID')].get()
        if entity_id in self.entities[entity_type]:
            del self.entities[entity_type][entity_id]
            self.save_data()
            messagebox.showinfo("Success", f"{entity_type[:-1]} deleted successfully")
            self.clear_entries()
        else:
            messagebox.showerror("Error", f"{entity_type[:-1]} not found (ERROR: please add ID)")

    def display_entity(self, entity_type):
        """Display details of an entity if the ID exists."""
        entity_id = self.entries[(entity_type, 'ID')].get()
        if entity_id in self.entities[entity_type]:
            entity = self.entities[entity_type][entity_id]
            details = '\n'.join(f"{key}: {value}" for key, value in entity.items())
            messagebox.showinfo(f"{entity_type[:-1]} Details", details)
        else:
            messagebox.showerror("Error", f"{entity_type[:-1]} not found (ERROR: please add ID)")

    def clear_entries(self):
        """Clear all entry fields."""
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def setup_labels(self):
        """Define labels for each entity type to be used in forms."""
        self.labels = {
            'Employees': ['ID', 'Name', 'Department', 'Job Title', 'Salary'],
            'Events': ['ID', 'Type', 'Theme', 'Date', 'Venue'],
            'Clients': ['ID', 'Name', 'Address', 'Contact Details', 'Budget'],
            'Guests': ['ID', 'Name', 'Address', 'Contact Details'],
            'Suppliers': ['ID', 'Name', 'Address', 'Contact Details'],
            'Venues': ['ID', 'Name', 'Address', 'Details']
        }

# Main window
if __name__ == '__main__':
    root = tk.Tk()
    app = BestEventCompanyGUI(root)
    root.mainloop()







