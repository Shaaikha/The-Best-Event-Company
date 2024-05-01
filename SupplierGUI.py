import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import pickle
import os

class SupplierGUI:
    def __init__(self, root):
        self.root = root
        root.title("Supplier Management System")
        root.geometry("600x300")

        # Load suppliers if the file exists
        self.filename = 'suppliers.pkl'
        self.suppliers = self.load_suppliers()

        # Supplier form fields
        self.entries = {}
        labels = ['Supplier ID', 'Name', 'Address', 'Contact Details']
        for idx, label in enumerate(labels):
            ttk.Label(root, text=label).grid(row=idx, column=0, padx=10, pady=5, sticky='w')
            entry = ttk.Entry(root)
            entry.grid(row=idx, column=1, padx=10, pady=5, sticky='w')
            self.entries[label] = entry

        # Buttons for operations
        ttk.Button(root, text="Add", command=self.add_supplier).grid(row=len(labels), column=0, pady=10)
        ttk.Button(root, text="Modify", command=self.modify_supplier).grid(row=len(labels), column=1, pady=10)
        ttk.Button(root, text="Delete", command=self.delete_supplier).grid(row=len(labels)+1, column=0, pady=10)
        ttk.Button(root, text="Display", command=self.display_supplier).grid(row=len(labels)+1, column=1, pady=10)

    def load_suppliers(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as f:
                return pickle.load(f)
        return {}

    def save_suppliers(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.suppliers, f)

    def add_supplier(self):
        data = {label: self.entries[label].get() for label in self.entries}
        if not all(data.values()):
            messagebox.showerror("Error", "All fields are required")
            return
        if data['Supplier ID'] in self.suppliers:
            messagebox.showerror("Error", "Supplier ID already exists")
            return
        self.suppliers[data['Supplier ID']] = data
        self.save_suppliers()
        messagebox.showinfo("Success", "Supplier added successfully")
        self.clear_entries()

    def modify_supplier(self):
        supplier_id = self.entries['Supplier ID'].get()
        if not supplier_id or supplier_id not in self.suppliers:
            messagebox.showerror("Error", "Invalid Supplier ID")
            return
        data = {label: self.entries[label].get() for label in self.entries}
        if not all(data.values()):
            messagebox.showerror("Error", "All fields must be filled to modify")
            return
        self.suppliers[supplier_id].update(data)
        self.save_suppliers()
        messagebox.showinfo("Success", "Supplier modified successfully")
        self.clear_entries()

    def delete_supplier(self):
        supplier_id = self.entries['Supplier ID'].get()
        if supplier_id in self.suppliers:
            del self.suppliers[supplier_id]
            self.save_suppliers()
            messagebox.showinfo("Success", "Supplier deleted successfully")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Supplier not found")

    def display_supplier(self):
        supplier_id = self.entries['Supplier ID'].get()
        if supplier_id in self.suppliers:
            supplier = self.suppliers[supplier_id]
            details = '\n'.join(f"{key}: {value}" for key, value in supplier.items())
            messagebox.showinfo("Supplier Details", details)
        else:
            messagebox.showerror("Error", "Supplier not found")

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

# Main window
if __name__ == '__main__':
    root = tk.Tk()
    app = SupplierGUI(root)
    root.mainloop()

