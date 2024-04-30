import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pickle

# Define Employee class
class Employee:
    def __init__(self, emp_id, name, department, job_title, basic_salary, age, dob, passport_details):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.dob = dob
        self.passport_details = passport_details

# Define Event class
class Event:
    def __init__(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list,
                 catering_company, cleaning_company, decorations_company, entertainment_company, furniture_supply_company, invoice):
        self.event_id = event_id
        self.event_type = event_type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue_address = venue_address
        self.client_id = client_id
        self.guest_list = guest_list
        self.catering_company = catering_company
        self.cleaning_company = cleaning_company
        self.decorations_company = decorations_company
        self.entertainment_company = entertainment_company
        self.furniture_supply_company = furniture_supply_company
        self.invoice = invoice

# Define Client class
class Client:
    def __init__(self, client_id, name, address, contact_details, budget):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget

# Define Guest class
class Guest:
    def __init__(self, guest_id, name, address, contact_details):
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

# Define Supplier class
class Supplier:
    def __init__(self, supplier_id, name, address, contact_details):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

# Define Venue class
class Venue:
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact = contact
        self.min_guests = min_guests
        self.max_guests = max_guests

# Define ManagementGUI class
class ManagementGUI:
    def __init__(self, root):
        self.root = root
        root.title("Event Management System")

        # Load data from binary files
        self.load_data()

        # Create a notebook
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True)

        # Create frames for each category
        self.frames = {}
        categories = ['Employees', 'Events', 'Clients', 'Guests', 'Suppliers', 'Venues']
        for category in categories:
            frame = ttk.Frame(self.notebook)
            self.frames[category] = frame
            self.notebook.add(frame, text=category)

        # Initialize the setup for employees
        self.setup_employees(self.frames['Employees'])

    def load_data(self):
        try:
            with open("employees.dat", "rb") as file:
                self.employees = pickle.load(file)
        except FileNotFoundError:
            self.employees = {}
        try:
            with open("events.dat", "rb") as file:
                self.events = pickle.load(file)
        except FileNotFoundError:
            self.events = {}
        try:
            with open("clients.dat", "rb") as file:
                self.clients = pickle.load(file)
        except FileNotFoundError:
            self.clients = {}
        try:
            with open("guests.dat", "rb") as file:
                self.guests = pickle.load(file)
        except FileNotFoundError:
            self.guests = {}
        try:
            with open("suppliers.dat", "rb") as file:
                self.suppliers = pickle.load(file)
        except FileNotFoundError:
            self.suppliers = {}
        try:
            with open("venues.dat", "rb") as file:
                self.venues = pickle.load(file)
        except FileNotFoundError:
            self.venues = {}

    def save_data(self):
        with open("employees.dat", "wb") as file:
            pickle.dump(self.employees, file)
        with open("events.dat", "wb") as file:
            pickle.dump(self.events, file)
        with open("clients.dat", "wb") as file:
            pickle.dump(self.clients, file)
        with open("guests.dat", "wb") as file:
            pickle.dump(self.guests, file)
        with open("suppliers.dat", "wb") as file:
            pickle.dump(self.suppliers, file)
        with open("venues.dat", "wb") as file:
            pickle.dump(self.venues, file)

    def setup_employees(self, frame):
        # GUI setup for managing employees
        pass  # Implement this method

    # Other setup methods for events
