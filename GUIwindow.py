import tkinter as tk
from tkinter import simpledialog, messagebox
import pickle
import os

# Define paths for the binary files
EMPLOYEES_FILE = 'employees.bin'
EVENTS_FILE = 'events.bin'
CLIENTS_FILE = 'clients.bin'
GUESTS_FILE = 'guests.bin'
SUPPLIERS_FILE = 'suppliers.bin'
VENUES_FILE = 'venues.bin'

# Function to load data from a binary file
def load_data(file_path):
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'rb') as file:
        return pickle.load(file)

# Function to save data to a binary file
def save_data(data, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)

# Employee Management GUI
class EmployeeManagementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management")
        self.employees = load_data(EMPLOYEES_FILE)
        self.initialize_gui_components()

    def initialize_gui_components(self):
        # Labels
        tk.Label(self.root, text='Name:').grid(row=0, column=0)
        tk.Label(self.root, text='ID:').grid(row=1, column=0)
        tk.Label(self.root, text='Department:').grid(row=2, column=0)
        tk.Label(self.root, text='Job Title:').grid(row=3, column=0)
        tk.Label(self.root, text='Basic Salary:').grid(row=4, column=0)

        # Entry widgets
        self.name_entry = tk.Entry(self.root)
        self.id_entry = tk.Entry(self.root)
        self.department_entry = tk.Entry(self.root)
        self.title_entry = tk.Entry(self.root)
        self.salary_entry = tk.Entry(self.root)

        self.name_entry.grid(row=0, column=1)
        self.id_entry.grid(row=1, column=1)
        self.department_entry.grid(row=2, column=1)
        self.title_entry.grid(row=3, column=1)
        self.salary_entry.grid(row=4, column=1)

        # Buttons
        tk.Button(self.root, text='Add Employee', command=self.add_employee).grid(row=5, column=0, columnspan=2)
        tk.Button(self.root, text='Modify Employee', command=self.modify_employee).grid(row=6, column=0, columnspan=2)
        tk.Button(self.root, text='Delete Employee', command=self.delete_employee).grid(row=7, column=0, columnspan=2)
        tk.Button(self.root, text='Display Employee', command=self.display_employee_wrapper).grid(row=8, column=0, columnspan=2)

        # Initialize display area
        self.display_area = tk.Text(self.root, height=10, width=50)
        self.display_area.grid(row=9, column=0, columnspan=2)

    def add_employee(self):
        name = self.name_entry.get()
        employee_id = self.id_entry.get()
        department = self.department_entry.get()
        job_title = self.title_entry.get()
        basic_salary = self.salary_entry.get()

        if not (name and employee_id and department and job_title and basic_salary):
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            basic_salary = float(basic_salary)
        except ValueError:
            messagebox.showerror("Error", "Invalid salary input")
            return

        self.employees[employee_id] = {
            'name': name,
            'employee_id': employee_id,
            'department': department,
            'job_title': job_title,
            'basic_salary': basic_salary
        }

        save_data(self.employees, EMPLOYEES_FILE)
        messagebox.showinfo("Success", "Employee added successfully")

        # Clear the entry fields
        self.name_entry.delete(0, tk.END)
        self.id_entry.delete(0, tk.END)
        self.department_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.salary_entry.delete(0, tk.END)

    def modify_employee(self):
        employee_id = simpledialog.askstring("Modify Employee", "Enter Employee ID", parent=self.root)
        if employee_id in self.employees:
            new_salary = simpledialog.askstring("Modify Employee", "Enter New Salary", parent=self.root)
            try:
                new_salary = float(new_salary)
                self.employees[employee_id]['basic_salary'] = new_salary
                save_data(self.employees, EMPLOYEES_FILE)
                messagebox.showinfo("Success", "Employee salary updated successfully")
            except ValueError:
                messagebox.showerror("Error", "Invalid salary input")
        else:
            messagebox.showerror("Error", "Employee not found")

    def delete_employee(self):
        employee_id = simpledialog.askstring("Delete Employee", "Enter Employee ID", parent=self.root)
        if employee_id in self.employees:
            del self.employees[employee_id]
            save_data(self.employees, EMPLOYEES_FILE)
            messagebox.showinfo("Success", "Employee deleted successfully")
        else:
            messagebox.showerror("Error", "Employee not found")

    def display_employee_wrapper(self):
        employee_id = simpledialog.askstring("Input", "Enter Employee ID", parent=self.root)
        if employee_id:
            self.display_employee_details(employee_id)

    def display_employee_details(self, employee_id):
        employee = self.employees.get(employee_id)
        if employee:
            display_text = f"Name: {employee['name']}\n"
            display_text += f"ID: {employee['employee_id']}\n"
            display_text += f"Department: {employee['department']}\n"
            display_text += f"Job Title: {employee['job_title']}\n"
            display_text += f"Basic Salary: {employee['basic_salary']}\n"
            self.display_area.delete(1.0, tk.END)
            self.display_area.insert(tk.END, display_text)
        else:
            messagebox.showerror("Error", "Employee not found")

class EventManagementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Management")
        self.events = load_data(EVENTS_FILE)
        self.initialize_gui_components()

    def initialize_gui_components(self):
        # Setup labels and entry widgets for event details
        tk.Label(self.root, text='Event ID:').grid(row=0, column=0)
        tk.Label(self.root, text='Type:').grid(row=1, column=0)
        tk.Label(self.root, text='Date:').grid(row=2, column=0)
        tk.Label(self.root, text='Client ID:').grid(row=3, column=0)
        tk.Label(self.root, text='Details:').grid(row=4, column=0)

        self.event_id_entry = tk.Entry(self.root)
        self.type_entry = tk.Entry(self.root)
        self.date_entry = tk.Entry(self.root)
        self.client_id_entry = tk.Entry(self.root)
        self.details_entry = tk.Entry(self.root)

        self.event_id_entry.grid(row=0, column=1)
        self.type_entry.grid(row=1, column=1)
        self.date_entry.grid(row=2, column=1)
        self.client_id_entry.grid(row=3, column=1)
        self.details_entry.grid(row=4, column=1)

        # Setup buttons
        tk.Button(self.root, text='Add Event', command=self.add_event).grid(row=5, column=0, columnspan=2)
        tk.Button(self.root, text='Modify Event', command=self.modify_event).grid(row=6, column=0, columnspan=2)
        tk.Button(self.root, text='Delete Event', command=self.delete_event).grid(row=7, column=0, columnspan=2)
        tk.Button(self.root, text='Display Event', command=self.display_event_wrapper).grid(row=8, column=0, columnspan=2)

        # Initialize display area
        self.display_area = tk.Text(self.root, height=10, width=50)
        self.display_area.grid(row=9, column=0, columnspan=2)

    def add_event(self):
        event_id = self.event_id_entry.get()
        type = self.type_entry.get()
        date = self.date_entry.get()
        client_id = self.client_id_entry.get()
        details = self.details_entry.get()

        if not (event_id and type and date and client_id and details):
            messagebox.showerror("Error", "All fields are required")
            return

        self.events[event_id] = {
            'event_id': event_id,
            'type': type,
            'date': date,
            'client_id': client_id,
            'details': details
        }

        save_data(self.events, EVENTS_FILE)
        messagebox.showinfo("Success", "Event added successfully")

        # Clear the entry fields
        self.event_id_entry.delete(0, tk.END)
        self.type_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.client_id_entry.delete(0, tk.END)
        self.details_entry.delete(0, tk.END)

    def modify_event(self):
        event_id = simpledialog.askstring("Modify Event", "Enter Event ID", parent=self.root)
        if event_id in self.events:
            new_type = simpledialog.askstring("Modify Event", "Enter New Type", parent=self.root)
            self.events[event_id]['type'] = new_type
            save_data(self.events, EVENTS_FILE)
            messagebox.showinfo("Success", "Event type updated successfully")
        else:
            messagebox.showerror("Error", "Event not found")

    def delete_event(self):
        event_id = simpledialog.askstring("Delete Event", "Enter Event ID", parent=self.root)
        if event_id in self.events:
            del self.events[event_id]
            save_data(self.events, EVENTS_FILE)
            messagebox.showinfo("Success", "Event deleted successfully")
        else:
            messagebox.showerror("Error", "Event not found")

    def display_event_wrapper(self):
        event_id = simpledialog.askstring("Input", "Enter Event ID", parent=self.root)
        if event_id:
            self.display_event_details(event_id)

    def display_event_details(self, event_id):
        event = self.events.get(event_id)
        if event:
            display_text = f"Event ID: {event['event_id']}\n"
            display_text += f"Type: {event['type']}\n"
            display_text += f"Date: {event['date']}\n"
            display_text += f"Client ID: {event['client_id']}\n"
            display_text += f"Details: {event['details']}\n"
            self.display_area.delete(1.0, tk.END)
            self.display_area.insert(tk.END, display_text)
        else:
            messagebox.showerror("Error", "Event not found")


class ClientManagementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Client Management")
        self.clients = load_data(CLIENTS_FILE)
        self.initialize_gui_components()

    def initialize_gui_components(self):
        # Setup labels and entry widgets for client details
        tk.Label(self.root, text='Client ID:').grid(row=0, column=0)
        tk.Label(self.root, text='Name:').grid(row=1, column=0)
        tk.Label(self.root, text='Address:').grid(row=2, column=0)
        tk.Label(self.root, text='Contact Details:').grid(row=3, column=0)
        tk.Label(self.root, text='Budget:').grid(row=4, column=0)

        self.client_id_entry = tk.Entry(self.root)
        self.name_entry = tk.Entry(self.root)
        self.address_entry = tk.Entry(self.root)
        self.contact_details_entry = tk.Entry(self.root)
        self.budget_entry = tk.Entry(self.root)

        self.client_id_entry.grid(row=0, column=1)
        self.name_entry.grid(row=1, column=1)
        self.address_entry.grid(row=2, column=1)
        self.contact_details_entry.grid(row=3, column=1)
        self.budget_entry.grid(row=4, column=1)

        # Setup buttons
        tk.Button(self.root, text='Add Client', command=self.add_client).grid(row=5, column=0, columnspan=2)
        tk.Button(self.root, text='Modify Client', command=self.modify_client).grid(row=6, column=0, columnspan=2)
        tk.Button(self.root, text='Delete Client', command=self.delete_client).grid(row=7, column=0, columnspan=2)
        tk.Button(self.root, text='Display Client', command=self.display_client_wrapper).grid(row=8, column=0, columnspan=2)

        # Initialize display area
        self.display_area = tk.Text(self.root, height=10, width=50)
        self.display_area.grid(row=9, column=0, columnspan=2)

    def add_client(self):
        client_id = self.client_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_details_entry.get()
        budget = self.budget_entry.get()

        if not (client_id and name and address and contact_details and budget):
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            budget = float(budget)  # Ensure that the budget is a valid number
        except ValueError:
            messagebox.showerror("Error", "Invalid budget input")
            return

        self.clients[client_id] = {
            'client_id': client_id,
            'name': name,
            'address': address,
            'contact_details': contact_details,
            'budget': budget
        }

        save_data(self.clients, CLIENTS_FILE)
        messagebox.showinfo("Success", "Client added successfully")

        # Clear the entry fields
        self.client_id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.contact_details_entry.delete(0, tk.END)
        self.budget_entry.delete(0, tk.END)

    def modify_client(self):
        client_id = simpledialog.askstring("Modify Client", "Enter Client ID", parent=self.root)
        if client_id in self.clients:
            new_budget = simpledialog.askstring("Modify Client", "Enter New Budget", parent=self.root)
            try:
                new_budget = float(new_budget)
                self.clients[client_id]['budget'] = new_budget
                save_data(self.clients, CLIENTS_FILE)
                messagebox.showinfo("Success", "Client budget updated successfully")
            except ValueError:
                messagebox.showerror("Error", "Invalid budget input")
        else:
            messagebox.showerror("Error", "Client not found")

    def delete_client(self):
        client_id = simpledialog.askstring("Delete Client", "Enter Client ID", parent=self.root)
        if client_id in self.clients:
            del self.clients[client_id]
            save_data(self.clients, CLIENTS_FILE)
            messagebox.showinfo("Success", "Client deleted successfully")
        else:
            messagebox.showerror("Error", "Client not found")

    def display_client_wrapper(self):
        client_id = simpledialog.askstring("Input", "Enter Client ID", parent=self.root)
        if client_id:
            self.display_client_details(client_id)

    def display_client_details(self, client_id):
        client = self.clients.get(client_id)
        if client:
            display_text = f"Client ID: {client['client_id']}\n"
            display_text += f"Name: {client['name']}\n"
            display_text += f"Address: {client['address']}\n"
            display_text += f"Contact Details: {client['contact_details']}\n"
            display_text += f"Budget: {client['budget']}\n"
            self.display_area.delete(1.0, tk.END)
            self.display_area.insert(tk.END, display_text)
        else:
            messagebox.showerror("Error", "Client not found")

class GuestManagementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Guest Management")
        self.guests = load_data(GUESTS_FILE)
        self.initialize_gui_components()

    def initialize_gui_components(self):
        # Setup labels and entry widgets for guest details
        tk.Label(self.root, text='Guest ID:').grid(row=0, column=0)
        tk.Label(self.root, text='Name:').grid(row=1, column=0)
        tk.Label(self.root, text='Address:').grid(row=2, column=0)
        tk.Label(self.root, text='Contact Details:').grid(row=3, column=0)
        tk.Label(self.root, text='RSVP Status:').grid(row=4, column=0)

        self.guest_id_entry = tk.Entry(self.root)
        self.name_entry = tk.Entry(self.root)
        self.address_entry = tk.Entry(self.root)
        self.contact_details_entry = tk.Entry(self.root)
        self.rsvp_status_entry = tk.Entry(self.root)

        self.guest_id_entry.grid(row=0, column=1)
        self.name_entry.grid(row=1, column=1)
        self.address_entry.grid(row=2, column=1)
        self.contact_details_entry.grid(row=3, column=1)
        self.rsvp_status_entry.grid(row=4, column=1)

        # Setup buttons
        tk.Button(self.root, text='Add Guest', command=self.add_guest).grid(row=5, column=0, columnspan=2)
        tk.Button(self.root, text='Modify Guest', command=self.modify_guest).grid(row=6, column=0, columnspan=2)
        tk.Button(self.root, text='Delete Guest', command=self.delete_guest).grid(row=7, column=0, columnspan=2)
        tk.Button(self.root, text='Display Guest', command=self.display_guest_wrapper).grid(row=8, column=0, columnspan=2)

        # Initialize display area
        self.display_area = tk.Text(self.root, height=10, width=50)
        self.display_area.grid(row=9, column=0, columnspan=2)

    def add_guest(self):
        guest_id = self.guest_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_details_entry.get()
        rsvp_status = self.rsvp_status_entry.get()

        if not (guest_id and name and address and contact_details and rsvp_status):
            messagebox.showerror("Error", "All fields are required")
            return

        self.guests[guest_id] = {
            'guest_id': guest_id,
            'name': name,
            'address': address,
            'contact_details': contact_details,
            'rsvp_status': rsvp_status
        }

        save_data(self.guests, GUESTS_FILE)
        messagebox.showinfo("Success", "Guest added successfully")

        # Clear the entry fields
        self.guest_id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.contact_details_entry.delete(0, tk.END)
        self.rsvp_status_entry.delete(0, tk.END)

    def modify_guest(self):
        guest_id = simpledialog.askstring("Modify Guest", "Enter Guest ID", parent=self.root)
        if guest_id in self.guests:
            new_rsvp_status = simpledialog.askstring("Modify Guest", "Enter New RSVP Status", parent=self.root)
            self.guests[guest_id]['rsvp_status'] = new_rsvp_status
            save_data(self.guests, GUESTS_FILE)
            messagebox.showinfo("Success", "Guest RSVP status updated successfully")
        else:
            messagebox.showerror("Error", "Guest not found")

    def delete_guest(self):
        guest_id = simpledialog.askstring("Delete Guest", "Enter Guest ID", parent=self.root)
        if guest_id in self.guests:
            del self.guests[guest_id]
            save_data(self.guests, GUESTS_FILE)
            messagebox.showinfo("Success", "Guest deleted successfully")
        else:
            messagebox.showerror("Error", "Guest not found")

    def display_guest_wrapper(self):
        guest_id = simpledialog.askstring("Input", "Enter Guest ID", parent=self.root)
        if guest_id:
            self.display_guest_details(guest_id)

    def display_guest_details(self, guest_id):
        guest = self.guests.get(guest_id)
        if guest:
            display_text = f"Guest ID: {guest['guest_id']}\n"
            display_text += f"Name: {guest['name']}\n"
            display_text += f"Address: {guest['address']}\n"
            display_text += f"Contact Details: {guest['contact_details']}\n"
            display_text += f"RSVP Status: {guest['rsvp_status']}\n"
            self.display_area.delete(1.0, tk.END)
            self.display_area.insert(tk.END, display_text)
        else:
            messagebox.showerror("Error", "Guest not found")

class SupplierManagementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Supplier Management")
        self.suppliers = load_data(SUPPLIERS_FILE)
        self.initialize_gui_components()

    def initialize_gui_components(self):
        # Setup labels and entry widgets for supplier details
        tk.Label(self.root, text='Supplier ID:').grid(row=0, column=0)
        tk.Label(self.root, text='Name:').grid(row=1, column=0)
        tk.Label(self.root, text='Address:').grid(row=2, column=0)
        tk.Label(self.root, text='Contact Details:').grid(row=3, column=0)
        tk.Label(self.root, text='Service Type:').grid(row=4, column=0)

        self.supplier_id_entry = tk.Entry(self.root)
        self.name_entry = tk.Entry(self.root)
        self.address_entry = tk.Entry(self.root)
        self.contact_details_entry = tk.Entry(self.root)
        self.service_type_entry = tk.Entry(self.root)

        self.supplier_id_entry.grid(row=0, column=1)
        self.name_entry.grid(row=1, column=1)
        self.address_entry.grid(row=2, column=1)
        self.contact_details_entry.grid(row=3, column=1)
        self.service_type_entry.grid(row=4, column=1)

        # Setup buttons
        tk.Button(self.root, text='Add Supplier', command=self.add_supplier).grid(row=5, column=0, columnspan=2)
        tk.Button(self.root, text='Modify Supplier', command=self.modify_supplier).grid(row=6, column=0, columnspan=2)
        tk.Button(self.root, text='Delete Supplier', command=self.delete_supplier).grid(row=7, column=0, columnspan=2)
        tk.Button(self.root, text='Display Supplier', command=self.display_supplier_wrapper).grid(row=8, column=0, columnspan=2)

        # Initialize display area
        self.display_area = tk.Text(self.root, height=10, width=50)
        self.display_area.grid(row=9, column=0, columnspan=2)

    def add_supplier(self):
        supplier_id = self.supplier_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact_details = self.contact_details_entry.get()
        service_type = self.service_type_entry.get()

        if not (supplier_id and name and address and contact_details and service_type):
            messagebox.showerror("Error", "All fields are required")
            return

        self.suppliers[supplier_id] = {
            'supplier_id': supplier_id,
            'name': name,
            'address': address,
            'contact_details': contact_details,
            'service_type': service_type
        }

        save_data(self.suppliers, SUPPLIERS_FILE)
        messagebox.showinfo("Success", "Supplier added successfully")

        # Clear the entry fields
        self.supplier_id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.contact_details_entry.delete(0, tk.END)
        self.service_type_entry.delete(0, tk.END)

    def modify_supplier(self):
        supplier_id = simpledialog.askstring("Modify Supplier", "Enter Supplier ID", parent=self.root)
        if supplier_id in self.suppliers:
            new_service_type = simpledialog.askstring("Modify Supplier", "Enter New Service Type", parent=self.root)
            self.suppliers[supplier_id]['service_type'] = new_service_type
            save_data(self.suppliers, SUPPLIERS_FILE)
            messagebox.showinfo("Success", "Supplier service type updated successfully")
        else:
            messagebox.showerror("Error", "Supplier not found")

    def delete_supplier(self):
        supplier_id = simpledialog.askstring("Delete Supplier", "Enter Supplier ID", parent=self.root)
        if supplier_id in self.suppliers:
            del self.suppliers[supplier_id]
            save_data(self.suppliers, SUPPLIERS_FILE)
            messagebox.showinfo("Success", "Supplier deleted successfully")
        else:
            messagebox.showerror("Error", "Supplier not found")

    def display_supplier_wrapper(self):
        supplier_id = simpledialog.askstring("Input", "Enter Supplier ID", parent=self.root)
        if supplier_id:
            self.display_supplier_details(supplier_id)

    def display_supplier_details(self, supplier_id):
        supplier = self.suppliers.get(supplier_id)
        if supplier:
            display_text = f"Supplier ID: {supplier['supplier_id']}\n"
            display_text += f"Name: {supplier['name']}\n"
            display_text += f"Address: {supplier['address']}\n"
            display_text += f"Contact Details: {supplier['contact_details']}\n"
            display_text += f"Service Type: {supplier['service_type']}\n"
            self.display_area.delete(1.0, tk.END)
            self.display_area.insert(tk.END, display_text)
        else:
            messagebox.showerror("Error", "Supplier not found")


class VenueManagementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Venue Management")
        self.venues = load_data(VENUES_FILE)
        self.initialize_gui_components()

    def initialize_gui_components(self):
        # Setup labels and entry widgets for venue details
        tk.Label(self.root, text='Venue ID:').grid(row=0, column=0)
        tk.Label(self.root, text='Name:').grid(row=1, column=0)
        tk.Label(self.root, text='Address:').grid(row=2, column=0)
        tk.Label(self.root, text='Contact:').grid(row=3, column=0)
        tk.Label(self.root, text='Capacity:').grid(row=4, column=0)

        self.venue_id_entry = tk.Entry(self.root)
        self.name_entry = tk.Entry(self.root)
        self.address_entry = tk.Entry(self.root)
        self.contact_entry = tk.Entry(self.root)
        self.capacity_entry = tk.Entry(self.root)

        self.venue_id_entry.grid(row=0, column=1)
        self.name_entry.grid(row=1, column=1)
        self.address_entry.grid(row=2, column=1)
        self.contact_entry.grid(row=3, column=1)
        self.capacity_entry.grid(row=4, column=1)

        # Setup buttons
        tk.Button(self.root, text='Add Venue', command=self.add_venue).grid(row=5, column=0, columnspan=2)
        tk.Button(self.root, text='Modify Venue', command=self.modify_venue).grid(row=6, column=0, columnspan=2)
        tk.Button(self.root, text='Delete Venue', command=self.delete_venue).grid(row=7, column=0, columnspan=2)
        tk.Button(self.root, text='Display Venue', command=self.display_venue_wrapper).grid(row=8, column=0, columnspan=2)

        # Initialize display area
        self.display_area = tk.Text(self.root, height=10, width=50)
        self.display_area.grid(row=9, column=0, columnspan=2)

    def add_venue(self):
        venue_id = self.venue_id_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        contact = self.contact_entry.get()
        capacity = self.capacity_entry.get()

        if not (venue_id and name and address and contact and capacity):
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            capacity = int(capacity)  # Ensure that the capacity is a valid integer
        except ValueError:
            messagebox.showerror("Error", "Invalid capacity input")
            return

        self.venues[venue_id] = {
            'venue_id': venue_id,
            'name': name,
            'address': address,
            'contact': contact,
            'capacity': capacity
        }

        save_data(self.venues, VENUES_FILE)
        messagebox.showinfo("Success", "Venue added successfully")

        # Clear the entry fields
        self.venue_id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)
        self.capacity_entry.delete(0, tk.END)

    def modify_venue(self):
        venue_id = simpledialog.askstring("Modify Venue", "Enter Venue ID", parent=self.root)
        if venue_id in self.venues:
            new_contact = simpledialog.askstring("Modify Venue", "Enter New Contact", parent=self.root)
            self.venues[venue_id]['contact'] = new_contact
            save_data(self.venues, VENUES_FILE)
            messagebox.showinfo("Success", "Venue contact updated successfully")
        else:
            messagebox.showerror("Error", "Venue not found")

    def delete_venue(self):
        venue_id = simpledialog.askstring("Delete Venue", "Enter Venue ID", parent=self.root)
        if venue_id in self.venues:
            del self.venues[venue_id]
            save_data(self.venues, VENUES_FILE)
            messagebox.showinfo("Success", "Venue deleted successfully")
        else:
            messagebox.showerror("Error", "Venue not found")

    def display_venue_wrapper(self):
        venue_id = simpledialog.askstring("Input", "Enter Venue ID", parent=self.root)
        if venue_id:
            self.display_venue_details(venue_id)

    def display_venue_details(self, venue_id):
        venue = self.venues.get(venue_id)
        if venue:
            display_text = f"Venue ID: {venue['venue_id']}\n"
            display_text += f"Name: {venue['name']}\n"
            display_text += f"Address: {venue['address']}\n"
            display_text += f"Contact: {venue['contact']}\n"
            display_text += f"Capacity: {venue['capacity']}\n"
            self.display_area.delete(1.0, tk.END)
            self.display_area.insert(tk.END, display_text)
        else:
            messagebox.showerror("Error", "Venue not found")



def main_menu():
    root = tk.Tk()
    root.title("Company Management System")
    tk.Button(root, text='Manage Employees', command=lambda: EmployeeManagementGUI(root)).pack(fill='x')
    tk.Button(root, text='Manage Events', command=lambda: EventManagementGUI(root)).pack(fill='x')
    tk.Button(root, text='Manage Clients', command=lambda: ClientManagementGUI(root)).pack(fill='x')
    tk.Button(root, text='Manage Guests', command=lambda: GuestManagementGUI(root)).pack(fill='x')
    tk.Button(root, text='Manage Suppliers', command=lambda: SupplierManagementGUI(root)).pack(fill='x')
    tk.Button(root, text='Manage Venues', command=lambda: VenueManagementGUI(root)).pack(fill='x')
    root.mainloop()

if __name__ == '__main__':
    main_menu()

