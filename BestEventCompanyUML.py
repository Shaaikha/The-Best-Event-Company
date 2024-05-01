class Employee:
    """Class for employees working for Best Events Company"""

    def __init__(self, fullName="", employeeId="", deptName="", positionTitle="", monthlySalary=0, currentAge=0,
                 birthDate="",
                 passportInfo="", emailAddress="", phoneNumber="", homeAddress="", employmentStartDate=""):
        # Initialize employee attributes
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
                f"Monthly Salary: ${self.__monthlySalary}\n"
                f"Age: {self.__currentAge}\n"
                f"Date of Birth: {self.__birthDate}\n"
                f"Passport Details: {self.__passportInfo}\n"
                f"Email Address: {self.__emailAddress}\n"
                f"Phone Number: {self.__phoneNumber}\n"
                f"Home Address: {self.__homeAddress}\n"
                f"Employment Start Date: {self.__employmentStartDate}\n")


class SalesManager(Employee):
    """Class for sales manager working for Best Events Company"""

    def __init__(self, fullName="", employeeId="", deptName="", positionTitle="", monthlySalary=0, currentAge=0,
                 birthDate="",
                 passportInfo="", emailAddress="", phoneNumber="", homeAddress="", employmentStartDate="",
                 salesTarget=0, salesAchieved=0, bonus=0, salesRegion=""):
        super().__init__(fullName, employeeId, deptName, positionTitle, monthlySalary, currentAge, birthDate,
                         passportInfo,
                         emailAddress, phoneNumber, homeAddress, employmentStartDate)
        self.__salesTarget = salesTarget
        self.__salesAchieved = salesAchieved
        self.__bonus = bonus
        self.__salesRegion = salesRegion

    def updateSalesTarget(self, newTarget):
        # Function to update sales target
        try:
            self.__salesTarget = newTarget
        except Exception as e:
            print(f"Error updating sales target: {e}")

    def generateSalesReport(self):
        # Function to generate sales report
        try:
            # Add logic to generate sales report
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

from enum import Enum
class ClientStatus(Enum):
    """Enum class for client status"""
    ACTIVE = 1
    INACTIVE = 2
    PROSPECTIVE = 3


class SalesPerson(Employee):
    """Class for salesperson working for Best Events Company"""

    def __init__(self, fullName="", employeeId="", deptName="", positionTitle="", monthlySalary=0, currentAge=0,
                 birthDate="",
                 passportInfo="", emailAddress="", phoneNumber="", homeAddress="", employmentStartDate="",
                 clients=None):
        # Initialize salesperson attributes
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
        # String representation of the salesperson object
        employee_str = super().__str__()  # Get the string from the superclass
        client_list = ', '.join([client['name'] for client in self.__clients]) if self.__clients else "No clients"
        sales_person_str = f"Clients: {client_list}"
        return f"{employee_str}\n{sales_person_str}"


class MarketingManager(Employee):
    """Class for marketing manager working for Best Events Company"""

    def __init__(self, fullName="", employeeId="", deptName="", positionTitle="", monthlySalary=0, currentAge=0,
                 birthDate="",
                 passportInfo="", emailAddress="", phoneNumber="", homeAddress="", employmentStartDate="",
                 marketingStrategy=""):
        # Initialize marketing manager attributes
        super().__init__(fullName, employeeId, deptName, positionTitle, monthlySalary, currentAge, birthDate,
                         passportInfo,
                         emailAddress, phoneNumber, homeAddress, employmentStartDate)
        self.__marketingStrategy = marketingStrategy  # The marketing strategy employed by the marketing manager

    def updateMarketingStrategy(self, newStrategy):
        # Function to update marketing strategy
        try:
            self.__marketingStrategy = newStrategy
        except Exception as e:
            print(f"Error updating marketing strategy: {e}")

    def launchMarketingCampaign(self):
        # Function to launch a marketing campaign
        try:
            # Add logic to launch a marketing campaign
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

    def __init__(self, fullName="", employeeId="", deptName="", positionTitle="", monthlySalary=0, currentAge=0,
                 birthDate="",
                 passportInfo="", emailAddress="", phoneNumber="", homeAddress="", employmentStartDate="",
                 campaigns=None):
        # Initialize marketer attributes
        super().__init__(fullName, employeeId, deptName, positionTitle, monthlySalary, currentAge, birthDate,
                         passportInfo,
                         emailAddress, phoneNumber, homeAddress, employmentStartDate)
        self.__campaigns = campaigns if campaigns else []

    def createCampaign(self, campaign):
        # Function to create a marketing campaign
        try:
            self.__campaigns.append(campaign)
        except Exception as e:
            print(f"Error creating campaign: {e}")

    def updateCampaign(self, campaignID, updates):
        # Function to update an existing marketing campaign
        try:
            for campaign in self.__campaigns:
                if campaign['id'] == campaignID:
                    campaign.update(updates)
                    break
        except Exception as e:
            print(f"Error updating campaign: {e}")

    def getCampaigns(self):
        return self.__campaigns

    def setCampaigns(self, campaigns):
        self.__campaigns = campaigns

    def __str__(self):
        # String representation of the marketer object
        employee_str = super().__str__()  # Get the string from the superclass
        campaign_list = ', '.join(
            [campaign['name'] for campaign in self.__campaigns]) if self.__campaigns else "No campaigns"
        return f"{employee_str}\nCampaigns: {campaign_list}"


class Accountant(Employee):
    """Class for accountant working for Best Events Company"""

    def __init__(self, fullName="", employeeId="", deptName="", positionTitle="", monthlySalary=0, currentAge=0,
                 birthDate="",
                 passportInfo="", emailAddress="", phoneNumber="", homeAddress="", employmentStartDate="",
                 financialReports=None):
        # Initialize accountant attributes
        super().__init__(fullName, employeeId, deptName, positionTitle, monthlySalary, currentAge, birthDate,
                         passportInfo,
                         emailAddress, phoneNumber, homeAddress, employmentStartDate)
        self.__financialReports = financialReports if financialReports else []

    def generate_financial_report(self, startDate, endDate):
        # Function to generate a financial report for a specific period
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

    def __init__(self, fullName="", employeeId="", deptName="", positionTitle="", monthlySalary=0, currentAge=0,
                 birthDate="",
                 passportInfo="", emailAddress="", phoneNumber="", homeAddress="", employmentStartDate="",
                 designs=None):
        # Initialize designer attributes
        super().__init__(fullName, employeeId, deptName, positionTitle, monthlySalary, currentAge, birthDate,
                         passportInfo,
                         emailAddress, phoneNumber, homeAddress, employmentStartDate)
        self.__designs = designs if designs else []

    def createDesign(self, design):
        # Function to create a new design
        try:
            self.__designs.append(design)
        except Exception as e:
            print(f"Error creating design: {e}")

    def updateDesign(self, designID, updates):
        # Function to update an existing design
        try:
            for design in self.__designs:
                if design['id'] == designID:
                    design.update(updates)
                    break
        except Exception as e:
            print(f"Error updating design: {e}")

    def getDesigns(self):
        return self.__designs

    def setDesigns(self, designs):
        self.__designs = designs

    def __str__(self):
        # String representation of the designer object
        employee_str = super().__str__()  # Get the string from the superclass
        design_count = len(self.__designs)
        return f"{employee_str}\nDesigns Created: {design_count} designs"


class Handyman(Employee):
    """Class for Handyman working for Best Events Company"""

    def __init__(self, fullName="", employeeId="", deptName="", positionTitle="", monthlySalary=0, currentAge=0,
                 birthDate="",
                 passportInfo="", emailAddress="", phoneNumber="", homeAddress="", employmentStartDate="", tasks=None):
        # Initialize handyman attributes
        super().__init__(fullName, employeeId, deptName, positionTitle, monthlySalary, currentAge, birthDate,
                         passportInfo,
                         emailAddress, phoneNumber, homeAddress, employmentStartDate)
        self.__tasks = tasks if tasks else []

    def assign_task(self, task):
        # Function to assign a task to the handyman
        try:
            self.__tasks.append(task)
        except Exception as e:
            print(f"Error assigning task: {e}")

    def completeTask(self, taskID):
        # Function to mark a task as completed
        try:
            self.__tasks = [task for task in self.__tasks if task['id'] != taskID]
        except Exception as e:
            print(f"Error completing task: {e}")

    def getTasks(self):
        return self.__tasks

    def setTasks(self, tasks):
        self.__tasks = tasks

    def __str__(self):
        # String representation of the handyman object
        employee_str = super().__str__()  # Get the string from the superclass
        task_count = len(self.__tasks)
        return f"{employee_str}\nTasks Assigned: {task_count} tasks"


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

    def __init__(self, clientId="", clientName="", clientAddress="", contactDetails="", budget=0,
                 eventHistory="", loyaltyPoints=0, preferredContactMethod=ContactMethod.EMAIL, specialRequests="",
                 contractSigned=False):
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
        # Function to calculate total spending on events organized
        return sum(event['cost'] for event in eval(self._eventHistory))

    def updateEventHistory(self, event):
        # Function to update event history by adding a new event
        self._eventHistory.append(event)

    def sendReminder(self):
        # Function to send a reminder to the client about upcoming events
        return f"Reminder sent to {self._clientName} about upcoming events."

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

    def __str__(self):
        return (f"Client ID: {self._clientId}\n"
                f"Client Name: {self._clientName}\n"
                f"Client Address: {self._clientAddress}\n"
                f"Contact Details: {self._contactDetails}\n"
                f"Budget: ${self._budget}\n"
                f"Events: {len(eval(self._eventHistory))} events\n"
                f"Loyalty Points: {self._loyaltyPoints}\n"
                f"Preferred Contact Method: {self._preferredContactMethod.value}\n"
                f"Special Requests: {len(eval(self._specialRequests))}\n"
                f"Contract Signed: {'Yes' if self._contractSigned else 'No'}")


class Guest:
    """Class for guests that are invited to services Best Events Company provides"""

    def __init__(self, guestId="", guestName="", guestAddress="", contactDetails="",
                 rsvpStatus="", mealPreference="", accommodationDetails="", giftRegistry="",
                 specialNeeds=""):
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
        # Function to confirm RSVP status for the event
        self._rsvpStatus = "Confirmed"
        return f"RSVP status confirmed for {self._guestName}."

    def updateMealPreference(self, preference):
        # Function to update meal preference
        self._mealPreference = preference
        return f"Meal preference updated to {preference} for {self._guestName}."

    def requestTransportation(self):
        # Function to request transportation arrangements
        return f"Transportation request initiated for {self._guestName}."

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

    def __init__(self, eventId="", eventType="", eventTheme="", eventDate="", eventTime="", eventDuration="",
                 venueAddress="", clientId="",
                 guestList=None, invoice="", eventStatus="", attendeeCount=0, feedback="", expenses=0, profit=0):
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

    def updateStatus(self, newStatus):
        self.__eventStatus = newStatus
        return f"Event status updated to {newStatus}."

    def recordFeedback(self, feedback):
        self.__feedback += feedback
        return "Feedback recorded successfully."

    def calculateProfit(self):
        self.__profit = self.__attendeeCount * 50 - self.__expenses  # Assuming a fixed price per attendee
        return self.__profit

    def addGuest(self, guest):
        self.__guestList.append(guest)
        self.__attendeeCount = len(self.__guestList)

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
                f"Expenses: ${self.__expenses}\n"
                f"Profit: ${self.__profit}")


from enum import Enum


class Specialization(Enum):
    CATERING = "Catering"
    CLEANING = "Cleaning"
    FURNITURE_SUPPLY = "Furniture Supply"
    DECORATIONS_SUPPLY = "Decorations Supply"


class Supplier:
    """Class for suppliers that provide services/products for Best Events Company"""

    def __init__(self, supplierId="", supplierName="", supplierAddress="", supplierContactDetails="",
                 serviceArea="", availability="", contractSigned=False, preferredPaymentMethod="",
                 specialization=Specialization.CATERING):  # Default specialization set to Catering
        self.__supplierId = supplierId
        self.__supplierName = supplierName
        self.__supplierAddress = supplierAddress
        self.__supplierContactDetails = supplierContactDetails
        self.__serviceArea = serviceArea
        self.__availability = availability
        self.__contractSigned = contractSigned
        self.__preferredPaymentMethod = preferredPaymentMethod
        self.__specialization = specialization

    def updateAvailability(self, schedule):
        self.__availability = schedule
        return f"Availability updated to: {schedule}"

    def signContract(self):
        if not self.__contractSigned:
            self.__contractSigned = True
            return "Contract signed successfully."
        return "Contract already signed."

    def processPayment(self, amount):
        return f"Processed payment of ${amount}."

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

    def update_venue_amenities(self, newAmenities):
        try:
            self.__venueAmenities = newAmenities
        except Exception as e:
            print(f"Error updating amenities: {e}")

    def check_venue_availability(self, date):
        try:
            # Implement logic to check availability based on existing bookings
            pass
        except Exception as e:
            print(f"Error checking availability: {e}")

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

    def __init__(self, managedEvents=None, managedVenues=None, registeredClients=None, associatedSuppliers=None,
                 companyEmployees=None, eventtype=EventType.WEDDING):
        self._managedEvents = managedEvents if managedEvents else []
        self._managedVenues = managedVenues if managedVenues else []
        self._registeredClients = registeredClients if registeredClients else []
        self._associatedSuppliers = associatedSuppliers if associatedSuppliers else []
        self._companyEmployees = companyEmployees if companyEmployees else []
        self._eventtype = eventtype

    def add_event(self, event):
        self._managedEvents.append(event)

    def remove_event(self, eventID):
        self._managedEvents = [event for event in self._managedEvents if event.get_eventID() != eventID]

    def add_venue(self, venue):
        self._managedVenues.append(venue)

    def remove_venue(self, venueID):
        self._managedVenues = [venue for venue in self._managedVenues if venue.get_venue_identifier() != venueID]

    def add_client(self, client):
        self._registeredClients.append(client)

    def remove_client(self, clientID):
        self._registeredClients = [client for client in self._registeredClients if client.get_client_id() != clientID]

    def add_supplier(self, supplier):
        self._associatedSuppliers.append(supplier)

    def remove_supplier(self, supplierID):
        self._associatedSuppliers = [supplier for supplier in self._associatedSuppliers if
                                     supplier.get_supplier_id() != supplierID]

    def add_employee(self, employee):
        self._companyEmployees.append(employee)

    def remove_employee(self, employeeID):
        self._companyEmployees = [employee for employee in self._companyEmployees if
                                  employee.get_employee_id() != employeeID]

    def __str__(self):
        return (f"Best Event Company currently manages {len(self._managedEvents)} events, "
                f"{len(self._managedVenues)} venues, {len(self._registeredClients)} clients, "
                f"{len(self._associatedSuppliers)} suppliers, and employs {len(self._companyEmployees)} staff members.")