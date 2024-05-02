class Employee:
    """Class for employees working for Best Events Company"""

    # Adding the instructor in order to initialize attributes and their data types for better efficiency
    def __init__(self, fullName="", employeeId="", deptName="", positionTitle="", monthlySalary=0, currentAge=0,
                 birthDate="",
                 passportInfo="", emailAddress="", phoneNumber="", homeAddress="", employmentStartDate=""):
        # Initialize employee attributes such as their name, id, departement...
        # The attributes are private using the prefix of "__"
        self.__fullName = fullName
        self.__employeeId = employeeId
        self.__deptName = deptName
        self.__positionTitle = positionTitle
        self.__monthlySalary = monthlySalary
        self.__currentAge = currentAge
        self.__birthDate = birthDate
        self.__passportInfo = passportInfo
        self.__emailAddress = emailAddress
        self.__phoneNumber = phoneNumber
        self.__homeAddress = homeAddress
        self.__employmentStartDate = employmentStartDate

    # Getter and setter methods for all attributes
    def getFullName(self):
        return self.__fullName

    def setFullName(self, fullName):
        self.__fullName = fullName

    def getEmployeeId(self):
        return self.__employeeId

    def setEmployeeId(self, employeeId):
        self.__employeeId = employeeId

    def getDepartmentName(self):
        return self.__deptName

    def setDepartmentName(self, deptName):
        self.__deptName = deptName

    def getPositionTitle(self):
        return self.__positionTitle

    def setPositionTitle(self, positionTitle):
        self.__positionTitle = positionTitle

    def getMonthlySalary(self):
        return self.__monthlySalary

    def setMonthlySalary(self, monthlySalary):
        self.__monthlySalary = monthlySalary

    def getAge(self):
        return self.__currentAge

    def setAge(self, currentAge):
        self.__currentAge = currentAge

    def getBirthDate(self):
        return self.__birthDate

    def setBirthDate(self, birthDate):
        self.__birthDate = birthDate

    def getPassportInfo(self):
        return self.__passportInfo

    def setPassportInfo(self, passportInfo):
        self.__passportInfo = passportInfo

    def getEmailAddress(self):
        return self.__emailAddress

    def setEmailAddress(self, emailAddress):
        self.__emailAddress = emailAddress

    def getPhoneNumber(self):
        return self.__phoneNumber

    def setPhoneNumber(self, phoneNumber):
        self.__phoneNumber = phoneNumber

    def getHomeAddress(self):
        return self.__homeAddress

    def setHomeAddress(self, homeAddress):
        self.__homeAddress = homeAddress

    def getEmploymentStartDate(self):
        return self.__employmentStartDate

    def setEmploymentStartDate(self, employmentStartDate):
        self.__employmentStartDate = employmentStartDate

    def calculateTotalSalary(self):
        # Function to calculate total salary including any bonuses or allowances
        try:
            # Add logic to calculate total salary
            pass
        except Exception as e:
            print(f"Error calculating total salary: {e}")

    def updateContactDetails(self, emailAddress, phoneNumber, homeAddress):
        # Function to update contact details and address
        try:
            # Logic to update contact details and address
            pass
        except Exception as e:
            print(f"Error updating contact details: {e}")

    def __str__(self):
        # String representation of the employee object
        return (f"Employee Name: {self.__fullName}\n"
                f"Employee ID: {self.__employeeId}\n"
                f"Department: {self.__deptName}\n"
                f"Job Title: {self.__positionTitle}\n"
                f"Monthly Salary: AED{self.__monthlySalary}\n"
                f"Age: {self.__currentAge}\n"
                f"Date of Birth: {self.__birthDate}\n"
                f"Passport Details: {self.__passportInfo}\n"
                f"Email Address: {self.__emailAddress}\n"
                f"Phone Number: {self.__phoneNumber}\n"
                f"Home Address: {self.__homeAddress}\n"
                f"Employment Start Date: {self.__employmentStartDate}\n")


class SalesManager(Employee):
    """Class for sales manager working for Best Events Company"""

    # Adding the instructor in order to initialize attributes and their data types for better efficiency
    def __init__(self, fullName="", employeeId="", deptName="", positionTitle="", monthlySalary=0, currentAge=0,
                 birthDate="",
                 passportInfo="", emailAddress="", phoneNumber="", homeAddress="", employmentStartDate="",
                 salesTarget=0, salesAchieved=0, bonus=0, salesRegion=""):
        super().__init__(fullName, employeeId, deptName, positionTitle, monthlySalary, currentAge, birthDate,
                         passportInfo,
                         emailAddress, phoneNumber, homeAddress, employmentStartDate)
        # The attributes are private using the prefix of "__"
        self.__salesTarget = salesTarget
        self.__salesAchieved = salesAchieved
        self.__bonus = bonus
        self.__salesRegion = salesRegion

    def updateSalesTarget(self, newTarget):
        # This function is used to update sales target, where it handles errors using try and except
        try:
            self.__salesTarget = newTarget
        except Exception as e:
            print(f"Error updating sales target: {e}")

    def generateSalesReport(self):
        # This function is used to generate sales report
        try:
            # Then we create an algorithm in order to generate sales report
            return f"Sales Report - Target: {self.__salesTarget}, Achieved: {self.__salesAchieved}"
        except Exception as e:
            print(f"Error generating sales report: {e}")

    def getSalesTarget(self):
        return self.__salesTarget

    def setSalesTarget(self, salesTarget):
        self.__salesTarget = salesTarget

    def getSalesAchieved(self):
        return self.__salesAchieved

    def setSalesAchieved(self, salesAchieved):
        self.__salesAchieved = salesAchieved

    def getBonus(self):
        return self.__bonus

    def setBonus(self, bonus):
        self.__bonus = bonus

    def getSalesRegion(self):
        return self.__salesRegion

    def setSalesRegion(self, salesRegion):
        self.__salesRegion = salesRegion

    def __str__(self):
        # Inherits the string representation from Employee and appends SalesManager specific details
        employee_str = super().__str__()  # Get the string from the superclass
        sales_manager_str = (f"Sales Target: {self.__salesTarget}\n"
                             f"Sales Achieved: {self.__salesAchieved}\n"
                             f"Bonus: {self.__bonus}\n"
                             f"Sales Region: {self.__salesRegion}")
        return employee_str + "\n" + sales_manager_str


# Using enum class to list the options of client status as the client can be active, inactive, or prospective
from enum import Enum


class ClientStatus(Enum):
    """Enum class for client status"""
    ACTIVE = 1
    INACTIVE = 2
    PROSPECTIVE = 3


class SalesPerson(Employee):
    """Class for salesperson working for Best Events Company"""

    # Adding the instructor in order to initialize attributes and their data types for better efficiency
    def __init__(self, fullName="", employeeId="", deptName="", positionTitle="", monthlySalary=0, currentAge=0,
                 birthDate="",
                 passportInfo="", emailAddress="", phoneNumber="", homeAddress="", employmentStartDate="",
                 clients=None):
        # Initialize salesperson attributes
        # The attributes are private using the prefix of "__"
        super().__init__(fullName, employeeId, deptName, positionTitle, monthlySalary, currentAge, birthDate,
                         passportInfo,
                         emailAddress, phoneNumber, homeAddress, employmentStartDate)
        self.__clients = clients

    # Getters and setters for clients
    def getClients(self):
        # Get the list of clients
        return self.clients

    def setClients(self, clients):
        # Set the list of clients
        self.clients = clients

    def addClient(self, client):
        # Add a client to the salesperson's client list
        try:
            self.clients.append(client)
        except Exception as e:
            print(f"Error adding client: {e}")

    def removeClient(self, clientID):
        # Remove a client from the salesperson's client list
        try:
            self.clients = [client for client in self.clients if client['id'] != clientID]
        except Exception as e:
            print(f"Error removing client: {e}")

    def __str__(self):
        # Through using the string function it will display string representation of the salesperson object
        employee_str = super().__str__()  # Get the string from the superclass
        client_list = ', '.join([client['name'] for client in self.__clients]) if self.__clients else "No clients"
        sales_person_str = f"Clients: {client_list}"
        return f"{employee_str}\n{sales_person_str}"


class MarketingManager(Employee):
    """Class for marketing manager working for Best Events Company"""

    # Adding the instructor in order to initialize attributes and their data types for better efficiency
    def __init__(self, fullName="", employeeId="", deptName="", positionTitle="", monthlySalary=0, currentAge=0,
                 birthDate="",
                 passportInfo="", emailAddress="", phoneNumber="", homeAddress="", employmentStartDate="",
                 marketingStrategy=""):
        # Initialize marketing manager attributes
        super().__init__(fullName, employeeId, deptName, positionTitle, monthlySalary, currentAge, birthDate,
                         passportInfo,
                         emailAddress, phoneNumber, homeAddress, employmentStartDate)
        # The attributes are private using the prefix of "__"
        self.__marketingStrategy = marketingStrategy  # The marketing strategy employed by the marketing manager

    def updateMarketingStrategy(self, newStrategy):
        # The function is generated to update marketing strategy
        try:
            self.__marketingStrategy = newStrategy
        except Exception as e:
            print(f"Error updating marketing strategy: {e}")

    def launchMarketingCampaign(self):
        # Lunch marketing function is created to launch a marketing campaign
        try:
            # Then we add the logic for launch a marketing campaign
            return f"Launching marketing campaign with strategy: {self.__marketingStrategy}"
        except Exception as e:
            print(f"Error launching marketing campaign: {e}")

    def getMarketingStrategy(self):
        # Get the marketing strategy.
        return self.__marketingStrategy

    def setMarketingStrategy(self, marketingStrategy):
        # Set the marketing strategy.
        self.__marketingStrategy = marketingStrategy

    def __str__(self):
        # String representation of the MarketingManager object.
        employee_str = super().__str__()
        return f"{employee_str}\nMarketing Strategy: {self.__marketingStrategy}"


class Marketer(Employee):
    """Class for marketer working for Best Events Company"""

    # Adding the instructor in order to initialize attributes and their data types for better efficiency
    def __init__(self, fullName="", employeeId="", deptName="", positionTitle="", monthlySalary=0, currentAge=0,
                 birthDate="",
                 passportInfo="", emailAddress="", phoneNumber="", homeAddress="", employmentStartDate="",
                 campaigns=None):
        # Initialize marketer attributes
        # The attributes are private using the prefix of "__"
        super().__init__(fullName, employeeId, deptName, positionTitle, monthlySalary, currentAge, birthDate,
                         passportInfo,
                         emailAddress, phoneNumber, homeAddress, employmentStartDate)
        self.__campaigns = campaigns if campaigns else []

    def createCampaign(self, campaign):
        # Creating a function to develop a marketing campaign
        try:
            self.__campaigns.append(campaign)
        except Exception as e:
            print(f"Error creating campaign: {e}")

    def updateCampaign(self, campaignID, updates):
        # Ceating a function in order to update an existing marketing campaign
        try:
            for campaign in self.__campaigns:
                if campaign['id'] == campaignID:
                    campaign.update(updates)
                    break
        except Exception as e:
            print(f"Error updating campaign: {e}")

    # Creating setter and getter for campaigns attribute
    def getCampaigns(self):
        return self.__campaigns

    def setCampaigns(self, campaigns):
        self.__campaigns = campaigns

    def __str__(self):
        # Then we use string function for string representation of the marketer object
        employee_str = super().__str__()  # Get the string from the superclass
        campaign_list = ', '.join(
            [campaign['name'] for campaign in self.__campaigns]) if self.__campaigns else "No campaigns"
        return f"{employee_str}\nCampaigns: {campaign_list}"


class Accountant(Employee):
    """Class for accountant working for Best Events Company"""

    # Adding the instructor in order to initialize attributes and their data types for better efficiency
    def __init__(self, fullName="", employeeId="", deptName="", positionTitle="", monthlySalary=0, currentAge=0,
                 birthDate="",
                 passportInfo="", emailAddress="", phoneNumber="", homeAddress="", employmentStartDate="",
                 financialReports=None):
        # Initialize accountant attributes
        # The attributes are private using the prefix of "__"
        super().__init__(fullName, employeeId, deptName, positionTitle, monthlySalary, currentAge, birthDate,
                         passportInfo,
                         emailAddress, phoneNumber, homeAddress, employmentStartDate)
        self.__financialReports = financialReports if financialReports else []

    def generate_financial_report(self, startDate, endDate):
        # Creating a function to generate a financial report for a specific period
        try:
            # Simulate report generation
            report = f"Financial report from {startDate} to {endDate}"
            self.__financialReports.append(report)
            return report
        except Exception as e:
            print(f"Error generating financial report: {e}")

    def update_financial_records(self, transaction):
        # Function to update financial records with a new transaction
        try:
            self.__financialReports.append(transaction)
        except Exception as e:
            print(f"Error updating financial records: {e}")

    # Setters and getters for financial reports for reading and editing
    def getFinancialReports(self):
        return self.__financialReports

    def setFinancialReports(self, financialReports):
        self.__financialReports = financialReports

    def __str__(self):
        # String representation of the accountant object
        employee_str = super().__str__()  # Get the string from the superclass
        return f"{employee_str}\nFinancial Reports: {len(self.__financialReports)} reports available"


class Designer(Employee):
    """Class for designer working for Best Events Company"""

    # Adding the instructor in order to initialize attributes and their data types for better efficiency
    def __init__(self, fullName="", employeeId="", deptName="", positionTitle="", monthlySalary=0, currentAge=0,
                 birthDate="",
                 passportInfo="", emailAddress="", phoneNumber="", homeAddress="", employmentStartDate="",
                 designs=None):
        # Initialize designer attributes
        # The attributes are private using the prefix of "__"
        super().__init__(fullName, employeeId, deptName, positionTitle, monthlySalary, currentAge, birthDate,
                         passportInfo,
                         emailAddress, phoneNumber, homeAddress, employmentStartDate)
        self.__designs = designs if designs else []

    def createDesign(self, design):
        # This function is applied to create a new design
        try:
            self.__designs.append(design)
        except Exception as e:
            print(f"Error creating design: {e}")

    def updateDesign(self, designID, updates):
        # This function is used to update an existing design
        try:
            for design in self.__designs:
                if design['id'] == designID:
                    design.update(updates)
                    break
        except Exception as e:
            print(f"Error updating design: {e}")

    # Creating setters and getters to handle the designs attribute effectively
    def getDesigns(self):
        return self.__designs

    def setDesigns(self, designs):
        self.__designs = designs

    def __str__(self):
        # Adding string function for string representation of the designer object
        employee_str = super().__str__()  # Get the string from the superclass
        design_count = len(self.__designs)
        return f"{employee_str}\nDesigns Created: {design_count} designs"


class Handyman(Employee):
    """Class for Handyman working for Best Events Company"""

    # Adding the instructor in order to initialize attributes and their data types for better efficiency
    def __init__(self, fullName="", employeeId="", deptName="", positionTitle="", monthlySalary=0, currentAge=0,
                 birthDate="",
                 passportInfo="", emailAddress="", phoneNumber="", homeAddress="", employmentStartDate="", tasks=None):
        # Initialize handyman attributes
        # The attributes are private using the prefix of "__"
        super().__init__(fullName, employeeId, deptName, positionTitle, monthlySalary, currentAge, birthDate,
                         passportInfo,
                         emailAddress, phoneNumber, homeAddress, employmentStartDate)
        self.__tasks = tasks if tasks else []

    def assign_task(self, task):
        # This function is developed to assign a task to the handyman
        try:
            self.__tasks.append(task)
        except Exception as e:
            print(f"Error assigning task: {e}")

    def completeTask(self, taskID):
        # This function is developed to mark a task as completed
        try:
            self.__tasks = [task for task in self.__tasks if task['id'] != taskID]
        except Exception as e:
            print(f"Error completing task: {e}")

    # Adding setters and getters for tasks attributes that are completed by the handman in the company
    def getTasks(self):
        return self.__tasks

    def setTasks(self, tasks):
        self.__tasks = tasks

    def __str__(self):
        # Adding string representation of the handyman object in order to simplify and clarify the end result
        employee_str = super().__str__()  # Get the string from the superclass
        task_count = len(self.__tasks)
        return f"{employee_str}\nTasks Assigned: {task_count} tasks"


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


class Guest:
    """Class for guests that are invited to services Best Events Company provides"""

    # Adding the instructor in order to initialize attributes and their data types for better efficiency
    def __init__(self, guestId="", guestName="", guestAddress="", contactDetails="",
                 rsvpStatus="", mealPreference="", accommodationDetails="", giftRegistry="",
                 specialNeeds=""):
        # The attributes are protected using the prefix of "_"
        self._guestId = guestId
        self._guestName = guestName
        self._guestAddress = guestAddress
        self._contactDetails = contactDetails
        self._rsvpStatus = rsvpStatus
        self._mealPreference = mealPreference
        self._accommodationDetails = accommodationDetails
        self._giftRegistry = giftRegistry
        self._specialNeeds = specialNeeds

    def confirmRsvp(self):
        # The confirm rsvp is a function to confirm RSVP status for the event
        self._rsvpStatus = "Confirmed"
        return f"RSVP status confirmed for {self._guestName}."

    def updateMealPreference(self, preference):
        # The update meal preference is a function to update meal preference
        self._mealPreference = preference
        return f"Meal preference updated to {preference} for {self._guestName}."

    def requestTransportation(self):
        # The request transportation is used as a function to request transportation arrangements
        return f"Transportation request initiated for {self._guestName}."

    # Developing the setters and getters for guest class
    def getGuestId(self):
        return self._guestId

    def setGuestId(self, guestId):
        self._guestId = guestId

    def getGuestName(self):
        return self._guestName

    def setGuestName(self, guestName):
        self._guestName = guestName

    def getGuestAddress(self):
        return self._guestAddress

    def setGuestAddress(self, guestAddress):
        self._guestAddress = guestAddress

    def getContactDetails(self):
        return self._contactDetails

    def setContactDetails(self, contactDetails):
        self._contactDetails = contactDetails

    def getRsvpStatus(self):
        return self._rsvpStatus

    def setRsvpStatus(self, rsvpStatus):
        self._rsvpStatus = rsvpStatus

    def getMealPreference(self):
        return self._mealPreference

    def setMealPreference(self, mealPreference):
        self._mealPreference = mealPreference

    def getAccommodationDetails(self):
        return self._accommodationDetails

    def setAccommodationDetails(self, accommodationDetails):
        self._accommodationDetails = accommodationDetails

    def getGiftRegistry(self):
        return self._giftRegistry

    def setGiftRegistry(self, giftRegistry):
        self._giftRegistry = giftRegistry

    def getSpecialNeeds(self):
        return self._specialNeeds

    def setSpecialNeeds(self, specialNeeds):
        self._specialNeeds = specialNeeds

    # Adding a string to simplify the final result of guest object readibility
    def __str__(self):
        return (f"Guest ID: {self._guestId}\n"
                f"Guest Name: {self._guestName}\n"
                f"Guest Address: {self._guestAddress}\n"
                f"Contact Details: {self._contactDetails}\n"
                f"RSVP Status: {self._rsvpStatus}\n"
                f"Meal Preference: {self._mealPreference}\n"
                f"Accommodation Details: {self._accommodationDetails}\n"
                f"Gift Registry: {self._giftRegistry}\n"
                f"Special Needs: {self._specialNeeds}")


class Event:
    """Class for events hosted by Best Events Company"""

    # Adding the instructor in order to initialize attributes and their data types for better efficiency
    def __init__(self, eventId="", eventType="", eventTheme="", eventDate="", eventTime="", eventDuration="",
                 venueAddress="", clientId="",
                 guestList=None, invoice="", eventStatus="", attendeeCount=0, feedback="", expenses=0, profit=0):
        # The attributes are private using the prefix of "__"
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

    # This function is created in order to update the status of the event
    def updateStatus(self, newStatus):
        self.__eventStatus = newStatus
        return f"Event status updated to {newStatus}."

    # Creating a function to keep record of the feedback
    def recordFeedback(self, feedback):
        self.__feedback += feedback
        return "Feedback recorded successfully."

    # This function in order to calculate the total profit of the event
    def calculateProfit(self):
        self.__profit = self.__attendeeCount * 50 - self.__expenses  # Assuming a fixed price per attendee
        return self.__profit

    # Adding a function in order to add guests for the event
    def addGuest(self, guest):
        self.__guestList.append(guest)
        self.__attendeeCount = len(self.__guestList)

    # Adding a string function for easier readibility for the guests
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


# adding enum class for specialization including catering, cleaning, furniture supply, and decorations supply
from enum import Enum


class Specialization(Enum):
    CATERING = "Catering"
    CLEANING = "Cleaning"
    FURNITURE_SUPPLY = "Furniture Supply"
    DECORATIONS_SUPPLY = "Decorations Supply"


class Supplier:
    """Class for suppliers that provide services/products for Best Events Company"""

    # Adding the instructor in order to initialize attributes and their data types for better efficiency
    def __init__(self, supplierId="", supplierName="", supplierAddress="", supplierContactDetails="",
                 serviceArea="", availability="", contractSigned=False, preferredPaymentMethod="",
                 specialization=Specialization.CATERING):  # Default specialization set to Catering
        # The attributes are private using the prefix of "__"
        self.__supplierId = supplierId
        self.__supplierName = supplierName
        self.__supplierAddress = supplierAddress
        self.__supplierContactDetails = supplierContactDetails
        self.__serviceArea = serviceArea
        self.__availability = availability
        self.__contractSigned = contractSigned
        self.__preferredPaymentMethod = preferredPaymentMethod
        self.__specialization = specialization

    # Adding the update avaibility function to help the suppliers to manage avaiblity
    def updateAvailability(self, schedule):
        self.__availability = schedule
        return f"Availability updated to: {schedule}"

    # Adding a function to keep track of the contract signed
    def signContract(self):
        if not self.__contractSigned:
            self.__contractSigned = True
            return "Contract signed successfully."
        return "Contract already signed."

    # adding a function to process the payment
    def processPayment(self, amount):
        return f"Processed payment of ${amount}."

    # adding a string function for easier readibility of the attributes of the supplier class
    def __str__(self):
        return (f"Supplier ID: {self.__supplierId}\n"
                f"Supplier Name: {self.__supplierName}\n"
                f"Supplier Address: {self.__supplierAddress}\n"
                f"Supplier Contact Details: {self.__supplierContactDetails}\n"
                f"Service Area: {self.__serviceArea}\n"
                f"Availability: {self.__availability}\n"
                f"Contract Signed: {'Yes' if self.__contractSigned else 'No'}\n"
                f"Preferred Payment Method: {self.__preferredPaymentMethod}\n"
                f"Specialization: {self.__specialization.value}")

    # Creating setters and getters for the attributes in the supplier class
    def getSupplierId(self):
        return self.__supplierId

    def setSupplierId(self, supplierId):
        self.__supplierId = supplierId

    def getSupplierName(self):
        return self.__supplierName

    def setSupplierName(self, supplierName):
        self.__supplierName = supplierName

    def getSupplierAddress(self):
        return self.__supplierAddress

    def setSupplierAddress(self, supplierAddress):
        self.__supplierAddress = supplierAddress

    def getSupplierContactDetails(self):
        return self.__supplierContactDetails

    def setSupplierContactDetails(self, supplierContactDetails):
        self.__supplierContactDetails = supplierContactDetails

    def getServiceArea(self):
        return self.__serviceArea

    def setServiceArea(self, serviceArea):
        self.__serviceArea = serviceArea

    def getAvailability(self):
        return self.__availability

    def setAvailability(self, availability):
        self.__availability = availability

    def getContractSigned(self):
        return self.__contractSigned

    def setContractSigned(self, contractSigned):
        self.__contractSigned = contractSigned

    def getPreferredPaymentMethod(self):
        return self.__preferredPaymentMethod

    def setPreferredPaymentMethod(self, preferredPaymentMethod):
        self.__preferredPaymentMethod = preferredPaymentMethod

    def getSpecialization(self):
        return self.__specialization

    def setSpecialization(self, specialization):
        self.__specialization = specialization


class Venue:
    """Class for venues that Best Events Company provides"""

    def __init__(self, venueIdentifier="", venueName="", venueAddress="", venueContactInfo="", minimumGuestCapacity=0,
                 maximumGuestCapacity=0,
                 venueAmenities=None, currentBookingStatus="", bookingDateDetails="", cancellationTerms="",
                 additionalServiceFees=None):
        # The attributes are private using the prefix of "__"
        self.__venueIdentifier = venueIdentifier
        self.__venueName = venueName
        self.__venueAddress = venueAddress
        self.__venueContactInfo = venueContactInfo
        self.__minimumGuestCapacity = minimumGuestCapacity
        self.__maximumGuestCapacity = maximumGuestCapacity
        self.__venueAmenities = venueAmenities if venueAmenities else []
        self.__currentBookingStatus = currentBookingStatus
        self.__bookingDateDetails = bookingDateDetails
        self.__cancellationTerms = cancellationTerms
        self.__additionalServiceFees = additionalServiceFees if additionalServiceFees else []

    # Creating a function for updating the venue amentities
    def update_venue_amenities(self, newAmenities):
        try:
            self.__venueAmenities = newAmenities
        except Exception as e:
            print(f"Error updating amenities: {e}")

    # Adding a function to check the availability of the venue
    def check_venue_availability(self, date):
        try:
            # Adding logic to check availability based on existing bookings
            pass
        except Exception as e:
            print(f"Error checking availability: {e}")

    # Adding function in order to calculate the total cost of the venue
    def calculate_venue_cost(self, duration):
        try:
            total_cost = 0
            # Implement logic to calculate cost based on duration and additional fees
            return total_cost
        except Exception as e:
            print(f"Error calculating total cost: {e}")

    # Getter and setter methods updated with new attribute names
    def get_venue_identifier(self):
        return self.__venueIdentifier

    def set_venue_identifier(self, venueIdentifier):
        self.__venueIdentifier = venueIdentifier

    def get_venue_name(self):
        return self.__venueName

    def set_venue_name(self, venueName):
        self.__venueName = venueName

    def get_venue_address(self):
        return self.__venueAddress

    def set_venue_address(self, venueAddress):
        self.__venueAddress = venueAddress

    def get_venue_contact_info(self):
        return self.__venueContactInfo

    def set_venue_contact_info(self, venueContactInfo):
        self.__venueContactInfo = venueContactInfo

    def get_minimum_guest_capacity(self):
        return self.__minimumGuestCapacity

    def set_minimum_guest_capacity(self, minimumGuestCapacity):
        self.__minimumGuestCapacity = minimumGuestCapacity

    def get_maximum_guest_capacity(self):
        return self.__maximumGuestCapacity

    def set_maximum_guest_capacity(self, maximumGuestCapacity):
        self.__maximumGuestCapacity = maximumGuestCapacity

    def get_venue_amenities(self):
        return self.__venueAmenities

    def set_venue_amenities(self, venueAmenities):
        self.__venueAmenities = venueAmenities

    def get_current_booking_status(self):
        return self.__currentBookingStatus

    def set_current_booking_status(self, currentBookingStatus):
        self.__currentBookingStatus = currentBookingStatus

    def get_booking_date_details(self):
        return self.__bookingDateDetails

    def set_booking_date_details(self, bookingDateDetails):
        self.__bookingDateDetails = bookingDateDetails

    def get_cancellation_terms(self):
        return self.__cancellationTerms

    def set_cancellation_terms(self, cancellationTerms):
        self.__cancellationTerms = cancellationTerms

    def get_additional_service_fees(self):
        return self.__additionalServiceFees

    def set_additional_service_fees(self, additionalServiceFees):
        self.__additionalServiceFees = additionalServiceFees


from enum import Enum


class EventType(Enum):
    WEDDING = "Wedding"
    BIRTHDAY = "Birthday"
    THEMED_PARTY = "Themed Party"
    GRADUATION = "Graduation"


class BestEventCompany:
    """Class to manage the operations of Best Event Company, including events, venues, clients, suppliers, and employees."""

    # Adding the instructor in order to initialize attributes and their data types for better efficiency
    # The attributes are protected using the prefix of "_"
    def __init__(self, managedEvents=None, managedVenues=None, registeredClients=None, associatedSuppliers=None,
                 companyEmployees=None, eventtype=EventType.WEDDING):
        self._managedEvents = managedEvents if managedEvents else []
        self._managedVenues = managedVenues if managedVenues else []
        self._registeredClients = registeredClients if registeredClients else []
        self._associatedSuppliers = associatedSuppliers if associatedSuppliers else []
        self._companyEmployees = companyEmployees if companyEmployees else []
        self._eventtype = eventtype

    # Getters and Setters
    def get_managed_events(self):
        # Get the list of managed events
        return self._managedEvents

    def set_managed_events(self, events):
        # Set the list of managed events
        self._managedEvents = events

    def get_managed_venues(self):
        # Get the list of managed venues
        return self._managedVenues

    def set_managed_venues(self, venues):
        # Set the list of managed venues
        self._managedVenues = venues

    def get_registered_clients(self):
        # Get the list of registered clients
        return self._registeredClients

    def set_registered_clients(self, clients):
        # Set the list of registered clients.
        self._registeredClients = clients

    def get_associated_suppliers(self):
        # Get the list of associated suppliers
        return self._associatedSuppliers

    def set_associated_suppliers(self, suppliers):
        # Set the list of associated suppliers
        self._associatedSuppliers = suppliers

    def get_company_employees(self):
        # Get the list of company employees
        return self._companyEmployees

    def set_company_employees(self, employees):
        # Set the list of company employees
        self._companyEmployees = employees

    def get_event_type(self):
        # Get the default event type
        return self._eventtype

    def set_event_type(self, event_type):
        # Set the default event type
        self._eventtype = event_type

    # Management Functions
    def add_event(self, event):
        # Add a new event to the managed events list
        self._managedEvents.append(event)

    def remove_event(self, eventID):
        # Remove an event by ID from the managed events list
        self._managedEvents = [event for event in self._managedEvents if event.get_event_id() != eventID]

    def add_venue(self, venue):
        # Add a new venue to the managed venues list
        self._managedVenues.append(venue)

    def remove_venue(self, venueID):
        # Remove a venue by ID from the managed venues list
        self._managedVenues = [venue for venue in self._managedVenues if venue.get_venue_id() != venueID]

    def add_client(self, client):
        # Add a new client to the registered clients list
        self._registeredClients.append(client)

    def remove_client(self, clientID):
        # Remove a client by ID from the registered clients list
        self._registeredClients = [client for client in self._registeredClients if client.get_client_id() != clientID]

    def add_supplier(self, supplier):
        # Add a new supplier to the associated suppliers list
        self._associatedSuppliers.append(supplier)

    def remove_supplier(self, supplierID):
        # Remove a supplier by ID from the associated suppliers list
        self._associatedSuppliers = [supplier for supplier in self._associatedSuppliers if
                                     supplier.get_supplier_id() != supplierID]

    def add_employee(self, employee):
        # Add a new employee to the company employees list
        self._companyEmployees.append(employee)

    def remove_employee(self, employeeID):
        # Remove an employee by ID from the company employees list
        self._companyEmployees = [employee for employee in self._companyEmployees if
                                  employee.get_employee_id() != employeeID]

    def __str__(self):
        # Provide a formatted string for the company's current status
        return (f"Best Event Company currently manages {len(self._managedEvents)} events, "
                f"{len(self._managedVenues)} venues, {len(self._registeredClients)} clients, "
                f"{len(self._associatedSuppliers)} suppliers, and employs {len(self._companyEmployees)} staff members.")