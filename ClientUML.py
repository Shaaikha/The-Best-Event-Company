# Adding enum classes for contact method and special requests as they have limited list of options
from enum import Enum


class ContactMethod(Enum):
    EMAIL = "Email"
    PHONE = "Phone"
    SMS = "SMS"


class SpecialRequest(Enum):
    CATERING = "Catering"
    DECORATION = "Decoration"
    ENTERTAINMENT = "Entertainment"
    TRANSPORTATION = "Transportation"


class Client:
    """Class for clients that are collaborating with Best Events Company"""

    # Adding the instructor in order to initialize attributes and their data types for better efficiency
    def __init__(self, clientId="", clientName="", clientAddress="", contactDetails="", budget=0,
                 eventHistory="", loyaltyPoints=0, preferredContactMethod=ContactMethod.EMAIL, specialRequests="",
                 contractSigned=False):
        # The attributes are protected using the prefix of "_"
        self._clientId = clientId
        self._clientName = clientName
        self._clientAddress = clientAddress
        self._contactDetails = contactDetails
        self._budget = budget
        self._eventHistory = eventHistory
        self._loyaltyPoints = loyaltyPoints
        self._preferredContactMethod = preferredContactMethod
        self._specialRequests = specialRequests
        self._contractSigned = contractSigned

    def calculateTotalSpending(self):
        # calculate total spending function is used to calculate total spending on events organized
        return sum(event['cost'] for event in eval(self._eventHistory))

    def updateEventHistory(self, event):
        # Update the event history is a function to update event history by adding a new event
        self._eventHistory.append(event)

    def sendReminder(self):
        # the send reminder function is used to send a reminder to the client about upcoming events
        return f"Reminder sent to {self._clientName} about upcoming events."

    # Adding setters and getters for all attributes developed in the client class
    def getClientId(self):
        return self._clientId

    def setClientId(self, clientId):
        self._clientId = clientId

    def getClientName(self):
        return self._clientName

    def setClientName(self, clientName):
        self._clientName = clientName

    def getClientAddress(self):
        return self._clientAddress

    def setClientAddress(self, clientAddress):
        self._clientAddress = clientAddress

    def getContactDetails(self):
        return self._contactDetails

    def setContactDetails(self, contactDetails):
        self._contactDetails = contactDetails

    def getBudget(self):
        return self._budget

    def setBudget(self, budget):
        self._budget = budget

    def getEventHistory(self):
        return self._eventHistory

    def setEventHistory(self, eventHistory):
        self._eventHistory = eventHistory

    def getLoyaltyPoints(self):
        return self._loyaltyPoints

    def setLoyaltyPoints(self, loyaltyPoints):
        self._loyaltyPoints = loyaltyPoints

    def getPreferredContactMethod(self):
        return self._preferredContactMethod

    def setPreferredContactMethod(self, preferredContactMethod):
        self._preferredContactMethod = preferredContactMethod

    def getSpecialRequests(self):
        return self._specialRequests

    def setSpecialRequests(self, specialRequests):
        self._specialRequests = specialRequests

    def getContractSigned(self):
        return self._contractSigned

    def setContractSigned(self, contractSigned):
        self._contractSigned = contractSigned

    # Adding the string function to clarify the result of the object
    def __str__(self):
        return (f"Client ID: {self._clientId}\n"
                f"Client Name: {self._clientName}\n"
                f"Client Address: {self._clientAddress}\n"
                f"Contact Details: {self._contactDetails}\n"
                f"Budget: DHS{self._budget}\n"
                f"Events: {len(eval(self._eventHistory))} events\n"
                f"Loyalty Points: {self._loyaltyPoints}\n"
                f"Preferred Contact Method: {self._preferredContactMethod.value}\n"
                f"Special Requests: {len(eval(self._specialRequests))}\n"
                f"Contract Signed: {'Yes' if self._contractSigned else 'No'}")

