import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import pickle
import os

class ClientGUI:
    def __init__(self, root):
        self.root = root
        root.title("Client Management System")
        root.geometry("600x300")

        # Load clients if the file exists
        self.filename = 'clients.pkl'
        self.clients = self.load_clients()

        # Client form fields
        self.entries = {}
        labels = ['Client ID', 'Name', 'Address', 'Contact Details', 'Budget']
        for idx, label in enumerate(labels):
            ttk.Label(root, text=label).grid(row=idx, column=0, padx=10, pady=5, sticky='w')
            entry = ttk.Entry(root)
            entry.grid(row=idx, column=1, padx=10, pady=5, sticky='w')
            self.entries[label] = entry

        # Buttons for operations
        ttk.Button(root, text="Add", command=self.add_client).grid(row=len(labels), column=0, pady=10)
        ttk.Button(root, text="Modify", command=self.modify_client).grid(row=len(labels), column=1, pady=10)
        ttk.Button(root, text="Delete", command=self.delete_client).grid(row=len(labels)+1, column=0, pady=10)
        ttk.Button(root, text="Display", command=self.display_client).grid(row=len(labels)+1, column=1, pady=10)

    def load_clients(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as f:
                return pickle.load(f)
        return {}

    def save_clients(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.clients, f)

    def add_client(self):
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

    def modify_client(self):
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

    def delete_client(self):
        client_id = self.entries['Client ID'].get()
        if client_id in self.clients:
            del self.clients[client_id]
            self.save_clients()
            messagebox.showinfo("Success", "Client deleted successfully")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Client not found")

    def display_client(self):
        client_id = self.entries['Client ID'].get()
        if client_id in self.clients:
            client = self.clients[client_id]
            details = '\n'.join(f"{key}: {value}" for key, value in client.items())
            messagebox.showinfo("Client Details", details)
        else:
            messagebox.showerror("Error", "Client not found")

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

# Main window
if __name__ == '__main__':
    root = tk.Tk()
    app = ClientGUI(root)
    root.mainloop()

