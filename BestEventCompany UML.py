from enum import Enum

class EventType(Enum):
    WEDDING = "Wedding"
    BIRTHDAY = "Birthday"
    THEMED_PARTY = "Themed Party"
    GRADUATION = "Graduation"
class BestEventCompany:
    """Class to manage the operations of Best Event Company, including events, venues, clients, suppliers, and employees."""
    #Adding the instructor in order to initialize attributes and their data types for better efficiency
    #The attributes are protected using the prefix of "_"
    def __init__(self, managedEvents=None, managedVenues=None, registeredClients=None, associatedSuppliers=None, companyEmployees=None, eventtype=EventType.WEDDING):
        self._managedEvents = managedEvents if managedEvents else []
        self._managedVenues = managedVenues if managedVenues else []
        self._registeredClients = registeredClients if registeredClients else []
        self._associatedSuppliers = associatedSuppliers if associatedSuppliers else []
        self._companyEmployees = companyEmployees if companyEmployees else []
        self._eventtype = eventtype


    # Getters and Setters
    def get_managed_events(self):
        #Get the list of managed events
        return self._managedEvents

    def set_managed_events(self, events):
        #Set the list of managed events
        self._managedEvents = events

    def get_managed_venues(self):
        #Get the list of managed venues
        return self._managedVenues

    def set_managed_venues(self, venues):
        #Set the list of managed venues
        self._managedVenues = venues

    def get_registered_clients(self):
         #Get the list of registered clients
        return self._registeredClients

    def set_registered_clients(self, clients):
        #Set the list of registered clients.
        self._registeredClients = clients

    def get_associated_suppliers(self):
        #Get the list of associated suppliers
        return self._associatedSuppliers

    def set_associated_suppliers(self, suppliers):
        #Set the list of associated suppliers
        self._associatedSuppliers = suppliers

    def get_company_employees(self):
        #Get the list of company employees
        return self._companyEmployees

    def set_company_employees(self, employees):
        #Set the list of company employees
        self._companyEmployees = employees

    def get_event_type(self):
        #Get the default event type
        return self._eventtype

    def set_event_type(self, event_type):
        #Set the default event type
        self._eventtype = event_type

    # Management Functions
    def add_event(self, event):
        #Add a new event to the managed events list
        self._managedEvents.append(event)

    def remove_event(self, eventID):
        #Remove an event by ID from the managed events list
        self._managedEvents = [event for event in self._managedEvents if event.get_event_id() != eventID]

    def add_venue(self, venue):
        #Add a new venue to the managed venues list
        self._managedVenues.append(venue)

    def remove_venue(self, venueID):
        #Remove a venue by ID from the managed venues list
        self._managedVenues = [venue for venue in self._managedVenues if venue.get_venue_id() != venueID]

    def add_client(self, client):
        #Add a new client to the registered clients list
        self._registeredClients.append(client)

    def remove_client(self, clientID):
        #Remove a client by ID from the registered clients list
        self._registeredClients = [client for client in self._registeredClients if client.get_client_id() != clientID]

    def add_supplier(self, supplier):
        #Add a new supplier to the associated suppliers list
        self._associatedSuppliers.append(supplier)

    def remove_supplier(self, supplierID):
        #Remove a supplier by ID from the associated suppliers list
        self._associatedSuppliers = [supplier for supplier in self._associatedSuppliers if supplier.get_supplier_id() != supplierID]

    def add_employee(self, employee):
        #Add a new employee to the company employees list
        self._companyEmployees.append(employee)

    def remove_employee(self, employeeID):
        #Remove an employee by ID from the company employees list
        self._companyEmployees = [employee for employee in self._companyEmployees if employee.get_employee_id() != employeeID]

    def __str__(self):
        #Provide a formatted string for the company's current status
        return (f"Best Event Company currently manages {len(self._managedEvents)} events, "
                f"{len(self._managedVenues)} venues, {len(self._registeredClients)} clients, "
                f"{len(self._associatedSuppliers)} suppliers, and employs {len(self._companyEmployees)} staff members.")