import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class ManagementGUI:
    def __init__(self, root):
        self.root = root
        root.title("Event Management System")

        # Initialize dictionaries for different entities
        self.entities = {
            'Employees': {},
            'Events': {},
            'Clients': {},
            'Guests': {},
            'Suppliers': {}
        }

        # Create a notebook
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True)

        # Setup frames for each entity
        for category in self.entities:
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=category)
            self.setup_entity_frame(frame, category)

    def setup_entity_frame(self, frame, entity_type):
        labels = self.get_entity_labels(entity_type)
        self.entries = {}
        for idx, label in enumerate(labels):
            ttk.Label(frame, text=label).grid(row=idx, column=0, padx=10, pady=5, sticky='w')
            entry = ttk.Entry(frame)
            entry.grid(row=idx, column=1, padx=10, pady=5, sticky='w')
            self.entries[label] = entry

        # Action Buttons
        actions_frame = ttk.Frame(frame)
        actions_frame.grid(row=len(labels), column=0, columnspan=2, pady=10)
        ttk.Button(actions_frame, text="Add", command=lambda: self.add_entity(entity_type)).pack(side=tk.LEFT, padx=5)
        ttk.Button(actions_frame, text="Modify", command=lambda: self.modify_entity(entity_type)).pack(side=tk.LEFT, padx=5)
        ttk.Button(actions_frame, text="Delete", command=lambda: self.delete_entity(entity_type)).pack(side=tk.LEFT, padx=5)
        ttk.Button(actions_frame, text="Display", command=lambda: self.display_entity(entity_type)).pack(side=tk.LEFT, padx=5)

    def get_entity_labels(self, entity_type):
        # Return labels based on entity type
        if entity_type == 'Employees':
            return ['Name', 'ID', 'Department', 'Job Title', 'Salary']
        elif entity_type == 'Events':
            return ['Event ID', 'Type', 'Theme', 'Date', 'Venue']
        elif entity_type == 'Clients':
            return ['Client ID', 'Name', 'Address', 'Contact Details', 'Budget']
        elif entity_type == 'Guests':
            return ['Guest ID', 'Name', 'Address', 'Contact Details']
        elif entity_type == 'Suppliers':
            return ['Supplier ID', 'Name', 'Address', 'Contact Details']

    def add_entity(self, entity_type):
        data = {key: entry.get() for key, entry in self.entries.items()}
        if not all(data.values()):
            messagebox.showerror("Error", "All fields are required")
            return
        entity_id = data.get('ID') or data.get('Event ID') or data.get('Client ID') or data.get('Guest ID') or data.get('Supplier ID')
        if entity_id in self.entities[entity_type]:
            messagebox.showerror("Error", f"{entity_type[:-1]} ID already exists")
            return
        self.entities[entity_type][entity_id] = data
        messagebox.showinfo("Success", f"{entity_type[:-1]} added successfully")
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def modify_entity(self, entity_type):
        entity_id = simpledialog.askstring(f"Modify {entity_type[:-1]}", f"Enter {entity_type[:-1]} ID", parent=self.root)
        if entity_id and entity_id in self.entities[entity_type]:
            self.open_modify_window(entity_id, entity_type)
        else:
            messagebox.showerror("Error", f"{entity_type[:-1]} not found")

    def open_modify_window(self, entity_id, entity_type):
        entity = self.entities[entity_type][entity_id]
        mod_win = tk.Toplevel(self.root)
        mod_win.title(f"Modify {entity_type[:-1]}")
        labels = self.get_entity_labels(entity_type)
        entries = {}
        row = 0
        for label in labels:
            tk.Label(mod_win, text=label + ":").grid(row=row, column=0)
            entry = tk.Entry(mod_win)
            entry.insert(0, entity[label])
            entry.grid(row=row, column=1)
            entries[label] = entry
            row += 1
        tk.Button(mod_win, text="Save Changes", command=lambda: self.save_changes(entity_id, entries, mod_win, entity_type)).grid(row=row, column=0, columnspan=2)

    def save_changes(self, entity_id, entries, mod_win, entity_type):
        updated_data = {key: entry.get() for key, entry in entries.items()}
        self.entities[entity_type][entity_id] = updated_data
        mod_win.destroy()
        messagebox.showinfo("Success", f"{entity_type[:-1]} details updated successfully")

    def delete_entity(self, entity_type):
        entity_id = simpledialog.askstring(f"Delete {entity_type[:-1]}", f"Enter {entity_type[:-1]} ID", parent=self.root)
        if entity_id in self.entities[entity_type]:
            del self.entities[entity_type][entity_id]
            messagebox.showinfo("Success", f"{entity_type[:-1]} deleted successfully")
        else:
            messagebox.showerror("Error", f"{entity_type[:-1]} not found")

    def display_entity(self, entity_type):
        entity_id = simpledialog.askstring(f"Display {entity_type[:-1]}", f"Enter {entity_type[:-1]} ID", parent=self.root)
        if entity_id in self.entities[entity_type]:
            entity = self.entities[entity_type][entity_id]
            details = '\n'.join(f"{key}: {value}" for key, value in entity.items())
            messagebox.showinfo(f"{entity_type[:-1]} Details", details)
        else:
            messagebox.showerror("Error", f"{entity_type[:-1]} not found")

# Main window
root = tk.Tk()
app = ManagementGUI(root)
root.mainloop()

if __name__ == '__main__':
    main_menu()




