
class Event:
    """Class for events hosted by Best Events Company"""
    #Adding the instructor in order to initialize attributes and their data types for better efficiency
    def __init__(self, eventId="", eventType="", eventTheme="", eventDate="", eventTime="", eventDuration="", venueAddress="", clientId="",
                 guestList=None, invoice="", eventStatus="", attendeeCount=0, feedback="", expenses=0, profit=0):
        #The attributes are private using the prefix of "__"
        self.__eventId = eventId
        self.__eventType = eventType
        self.__eventTheme = eventTheme
        self.__eventDate = eventDate
        self.__eventTime = eventTime
        self.__eventDuration = eventDuration
        self.__venueAddress = venueAddress
        self.__clientId = clientId
        self.__guestList = guestList if guestList else []
        self.__invoice = invoice
        self.__eventStatus = eventStatus
        self.__attendeeCount = attendeeCount
        self.__feedback = feedback
        self.__expenses = expenses
        self.__profit = profit



    # Getters and Setters for each attribute
    def getEventId(self):
        return self.__eventId

    def setEventId(self, eventId):
        self.__eventId = eventId

    def getEventType(self):
        return self.__eventType

    def setEventType(self, eventType):
        self.__eventType = eventType

    def getEventTheme(self):
        return self.__eventTheme

    def setEventTheme(self, eventTheme):
        self.__eventTheme = eventTheme

    def getEventDate(self):
        return self.__eventDate

    def setEventDate(self, eventDate):
        self.__eventDate = eventDate

    def getEventTime(self):
        return self.__eventTime

    def setEventTime(self, eventTime):
        self.__eventTime = eventTime

    def getEventDuration(self):
        return self.__eventDuration

    def setEventDuration(self, eventDuration):
        self.__eventDuration = eventDuration

    def getVenueAddress(self):
        return self.__venueAddress

    def setVenueAddress(self, venueAddress):
        self.__venueAddress = venueAddress

    def getClientId(self):
        return self.__clientId

    def setClientId(self, clientId):
        self.__clientId = clientId

    def getGuestList(self):
        return self.__guestList

    def setGuestList(self, guestList):
        self.__guestList = guestList

    def getInvoice(self):
        return self.__invoice

    def setInvoice(self, invoice):
        self.__invoice = invoice

    def getEventStatus(self):
        return self.__eventStatus

    def setEventStatus(self, eventStatus):
        self.__eventStatus = eventStatus

    def getAttendeeCount(self):
        return self.__attendeeCount

    def setAttendeeCount(self, attendeeCount):
        self.__attendeeCount = attendeeCount

    def getFeedback(self):
        return self.__feedback

    def setFeedback(self, feedback):
        self.__feedback = feedback

    def getExpenses(self):
        return self.__expenses

    def setExpenses(self, expenses):
        self.__expenses = expenses

    def getProfit(self):
        return self.__profit

    def setProfit(self, profit):
        self.__profit = profit

    #This function is created in order to update the status of the event
    def updateStatus(self, newStatus):
        self.__eventStatus = newStatus
        return f"Event status updated to {newStatus}."
    #Creating a function to keep record of the feedback
    def recordFeedback(self, feedback):
        self.__feedback += feedback
        return "Feedback recorded successfully."
   #This function in order to calculate the total profit of the event
    def calculateProfit(self):
        self.__profit = self.__attendeeCount * 50 - self.__expenses  # Assuming a fixed price per attendee
        return self.__profit
    #Adding a function in order to add guests for the event
    def addGuest(self, guest):
        self.__guestList.append(guest)
        self.__attendeeCount = len(self.__guestList)
    #Adding a string function for easier readibility for the guests
    def __str__(self):
        return (f"Event ID: {self.__eventId}\n"
                f"Event Type: {self.__eventType}\n"
                f"Event Theme: {self.__eventTheme}\n"
                f"Event Date: {self.__eventDate}\n"
                f"Event Time: {self.__eventTime}\n"
                f"Event Duration: {self.__eventDuration}\n"
                f"Venue Address: {self.__venueAddress}\n"
                f"Client ID: {self.__clientId}\n"
                f"Guest List: {len(self.__guestList)} guests\n"
                f"Invoice: {self.__invoice}\n"
                f"Event Status: {self.__eventStatus}\n"
                f"Attendee Count: {self.__attendeeCount}\n"
                f"Feedback: {self.__feedback}\n"
                f"Expenses: AED{self.__expenses}\n"
                f"Profit: AED{self.__profit}")
