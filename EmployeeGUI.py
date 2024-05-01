import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import pickle
import os

class EmployeeGUI:
    def __init__(self, root):
        self.root = root
        root.title("Employee Management System")
        root.geometry("400x300")

        # Load employees if the file exists
        self.filename = 'employees.pkl'
        self.employees = self.load_employees()

        # Employee form fields
        self.entries = {}
        labels = ['ID', 'Name', 'Department', 'Job Title', 'Salary']
        for idx, label in enumerate(labels):
            ttk.Label(root, text=label).grid(row=idx, column=0, padx=10, pady=5, sticky='w')
            entry = ttk.Entry(root)
            entry.grid(row=idx, column=1, padx=10, pady=5, sticky='w')
            self.entries[label] = entry

        # Buttons for operations
        ttk.Button(root, text="Add", command=self.add_employee).grid(row=len(labels), column=0, pady=10)
        ttk.Button(root, text="Modify", command=self.modify_employee).grid(row=len(labels), column=1, pady=10)
        ttk.Button(root, text="Delete", command=self.delete_employee).grid(row=len(labels)+1, column=0, pady=10)
        ttk.Button(root, text="Display", command=self.display_employee).grid(row=len(labels)+1, column=1, pady=10)

    def load_employees(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as f:
                return pickle.load(f)
        return {}

    def save_employees(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.employees, f)

    def add_employee(self):
        data = {label: self.entries[label].get() for label in self.entries}
        if not all(data.values()):
            messagebox.showerror("Error", "All fields are required")
            return
        if data['ID'] in self.employees:
            messagebox.showerror("Error", "Employee ID already exists")
            return
        self.employees[data['ID']] = data
        self.save_employees()
        messagebox.showinfo("Success", "Employee added successfully")
        self.clear_entries()

    def modify_employee(self):
        id = self.entries['ID'].get()
        if not id or id not in self.employees:
            messagebox.showerror("Error", "Invalid Employee ID")
            return
        data = {label: self.entries[label].get() for label in self.entries}
        if not all(data.values()):
            messagebox.showerror("Error", "All fields must be filled to modify")
            return
        self.employees[id].update(data)
        self.save_employees()
        messagebox.showinfo("Success", "Employee modified successfully")
        self.clear_entries()

    def delete_employee(self):
        id = self.entries['ID'].get()
        if id in self.employees:
            del self.employees[id]
            self.save_employees()
            messagebox.showinfo("Success", "Employee deleted successfully")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Employee not found")

    def display_employee(self):
        id = self.entries['ID'].get()
        if id in self.employees:
            employee = self.employees[id]
            details = '\n'.join(f"{key}: {value}" for key, value in employee.items())
            messagebox.showinfo("Employee Details", details)
        else:
            messagebox.showerror("Error", "Employee not found")

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

# Main window
if __name__ == '__main__':
    root = tk.Tk()
    app = EmployeeGUI(root)
    root.mainloop()


