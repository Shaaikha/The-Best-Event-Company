import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import pickle
import os

class ClientGUI:
    """Class for Client GUI"""
    def __init__(self, root):
        self.root = root
        root.title("Client Management System")
        root.geometry("600x300")

        # Load existing client data from file, if available.
        self.filename = 'clients.pkl'
        self.clients = self.load_clients()

        # Setup form fields for client information entry.
        self.entries = {}
        labels = ['Client ID', 'Name', 'Address', 'Contact Details', 'Budget']
        for idx, label in enumerate(labels):
            ttk.Label(root, text=label).grid(row=idx, column=0, padx=10, pady=5, sticky='w')
            entry = ttk.Entry(root)
            entry.grid(row=idx, column=1, padx=10, pady=5, sticky='w')
            self.entries[label] = entry

        # Create buttons for client operations (Add, Modify, Delete, Display)
        ttk.Button(root, text="Add", command=self.add_client).grid(row=len(labels), column=0, pady=10)
        ttk.Button(root, text="Modify", command=self.modify_client).grid(row=len(labels), column=1, pady=10)
        ttk.Button(root, text="Delete", command=self.delete_client).grid(row=len(labels)+1, column=0, pady=10)
        ttk.Button(root, text="Display", command=self.display_client).grid(row=len(labels)+1, column=1, pady=10)

    def load_clients(self):
        # Attempt to load clients from a pickle file; handle potential errors gracefully.
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'rb') as f:
                    return pickle.load(f)
        except Exception as e:
            messagebox.showerror("Loading Error", f"Failed to load client data: {e}")
            return {}
        return {}

    def save_clients(self):
        # Save current client data to a pickle file; handle file write errors.
        try:
            with open(self.filename, 'wb') as f:
                pickle.dump(self.clients, f)
        except Exception as e:
            messagebox.showerror("Saving Error", f"Failed to save client data: {e}")

    def add_client(self):
        # Validate inputs and add a new client if all fields are filled and the ID is unique.
        try:
            data = {label: self.entries[label].get() for label in self.entries}
            if not all(data.values()):
                messagebox.showerror("Error", "All fields are required")
                return
            if data['Client ID'] in self.clients:
                messagebox.showerror("Error", "Client ID already exists")
                return
            self.clients[data['Client ID']] = data
            self.save_clients()
            messagebox.showinfo("Success", "Client added successfully")
            self.clear_entries()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add client: {e}")

    def modify_client(self):
        # Modify an existing client's details after validating the client ID and all fields.
        try:
            client_id = self.entries['Client ID'].get()
            if not client_id or client_id not in self.clients:
                messagebox.showerror("Error", "Invalid Client ID")
                return
            data = {label: self.entries[label].get() for label in self.entries}
            if not all(data.values()):
                messagebox.showerror("Error", "All fields must be filled to modify")
                return
            self.clients[client_id].update(data)
            self.save_clients()
            messagebox.showinfo("Success", "Client modified successfully")
            self.clear_entries()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to modify client: {e}")

    def delete_client(self):
        # Delete a client after confirming the client ID exists.
        try:
            client_id = self.entries['Client ID'].get()
            if client_id in self.clients:
                del self.clients[client_id]
                self.save_clients()
                messagebox.showinfo("Success", "Client deleted successfully")
                self.clear_entries()
            else:
                messagebox.showerror("Error", "Client not found")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete client: {e}")

    def display_client(self):
        # Display details of a specific client.
        try:
            client_id = self.entries['Client ID'].get()
            if client_id in self.clients:
                client = self.clients[client_id]
                details = '\n'.join(f"{key}: {value}" for key, value in client.items())
                messagebox.showinfo("Client Details", details)
            else:
                messagebox.showerror("Error", "Client not found")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to display client details: {e}")

    def clear_entries(self):
        # Clear all entry fields in the GUI to prepare for new data entry.
        for entry in self.entries.values():
            entry.delete(0, tk.END)

# Main window initialization and event loop.
if __name__ == '__main__':
    root = tk.Tk()
    app = ClientGUI(root)
    root.mainloop()

