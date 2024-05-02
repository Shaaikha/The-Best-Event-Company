
#Using enum class to list the options of client status as the client can be active, inactive, or prospective
from enum import Enum
class ClientStatus(Enum):
    """Enum class for client status"""
    ACTIVE = 1
    INACTIVE = 2
    PROSPECTIVE = 3

class SalesPerson(Employee):
    """Class for salesperson working for Best Events Company"""
    #Adding the instructor in order to initialize attributes and their data types for better efficiency
    def __init__(self, fullName="", employeeId="", deptName="", positionTitle="", monthlySalary=0, currentAge=0, birthDate="",
                 passportInfo="", emailAddress="", phoneNumber="", homeAddress="", employmentStartDate="",
                 clients=None):
        # Initialize salesperson attributes
        #The attributes are private using the prefix of "__"
        super().__init__(fullName, employeeId, deptName, positionTitle, monthlySalary, currentAge, birthDate, passportInfo,
                         emailAddress, phoneNumber, homeAddress, employmentStartDate)
        self.__clients = clients

    # Getters and setters for clients
    def getClients(self):
        #Get the list of clients
        return self.clients

    def setClients(self, clients):
        #Set the list of clients
        self.clients = clients

    def addClient(self, client):
        #Add a client to the salesperson's client list
        try:
            self.clients.append(client)
        except Exception as e:
            print(f"Error adding client: {e}")

    def removeClient(self, clientID):
        #Remove a client from the salesperson's client list
        try:
            self.clients = [client for client in self.clients if client['id'] != clientID]
        except Exception as e:
            print(f"Error removing client: {e}")

    def __str__(self):
        #Through using the string function it will display string representation of the salesperson object
        employee_str = super().__str__()  # Get the string from the superclass
        client_list = ', '.join([client['name'] for client in self.__clients]) if self.__clients else "No clients"
        sales_person_str = f"Clients: {client_list}"
        return f"{employee_str}\n{sales_person_str}"