class Employee:
    """Class for employees working for Best Events Company"""

    def __init__(self, name="", employeeID="", department="", jobTitle="", basicSalary=0, age=0, dateOfBirth="",
                 passportDetails="", email="", phone="", address="", joiningDate="", supervisor=None):
        self.__name = name
        self.__employeeID = employeeID
        self.__department = department
        self.__jobTitle = jobTitle
        self.__basicSalary = basicSalary
        self.__age = age
        self.__dateOfBirth = dateOfBirth
        self.__passportDetails = passportDetails
        self.__email = email
        self.__phone = phone
        self.__address = address
        self.__joiningDate = joiningDate
        self.__supervisor = supervisor


    # Getter and setter methods for all attributes

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_employeeID(self):
        return self.__employeeID

    def set_employeeID(self, employeeID):
        self.__employeeID = employeeID

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

    def get_jobTitle(self):
        return self.__jobTitle

    def set_jobTitle(self, jobTitle):
        self.__jobTitle = jobTitle

    def get_basicSalary(self):
        return self.__basicSalary

    def set_basicSalary(self, basicSalary):
        self.__basicSalary = basicSalary

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_dateOfBirth(self):
        return self.__dateOfBirth

    def set_dateOfBirth(self, dateOfBirth):
        self.__dateOfBirth = dateOfBirth

    def get_passportDetails(self):
        return self.__passportDetails

    def set_passportDetails(self, passportDetails):
        self.__passportDetails = passportDetails

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_joiningDate(self):
        return self.__joiningDate

    def set_joiningDate(self, joiningDate):
        self.__joiningDate = joiningDate

    def get_supervisor(self):
        return self.__supervisor

    def set_supervisor(self, supervisor):
        self.__supervisor = supervisor

    def calculateTotalSalary(self):
        # Function to calculate total salary including any bonuses or allowances
        try:
            # Add logic to calculate total salary
            pass
        except Exception as e:
            print(f"Error calculating total salary: {e}")

    def updateContactDetails(self, email, phone, address):
        # Function to update contact details and address
        try:
            # Add logic to update contact details and address
            pass
        except Exception as e:
            print(f"Error updating contact details: {e}")




class SalesManager(Employee):
    """Class for sales manager working for Best Events Company"""
    def __init__(self, name="", employeeID="", department="", jobTitle="", basicSalary=0, age=0, dateOfBirth="",
                 passportDetails="", email="", phone="", address="", joiningDate="", supervisor=None,
                 salesTarget=0, salesAchieved=0):
        super().__init__(name, employeeID, department, jobTitle, basicSalary, age, dateOfBirth, passportDetails,
                         email, phone, address, joiningDate, supervisor)
        self.salesTarget = salesTarget
        self.salesAchieved = salesAchieved

    def updateSalesTarget(self, newTarget):
        # Function to update sales target
        try:
            # Add logic to update sales target
            pass
        except Exception as e:
            print(f"Error updating sales target: {e}")

    def generateSalesReport(self):
        # Function to generate sales report
        try:
            # Add logic to generate sales report
            pass
        except Exception as e:
            print(f"Error generating sales report: {e}")
    # Getter and setter methods for SalesManager attributes

    def get_salesTarget(self):
        return self.__salesTarget

    def set_salesTarget(self, salesTarget):
        self.__salesTarget = salesTarget

    def get_salesAchieved(self):
        return self.__salesAchieved

    def set_salesAchieved(self, salesAchieved):
        self.__salesAchieved = salesAchieved




class SalesPerson(Employee):
    """Class for salesperson working for Best Events Company"""

    def __init__(self, name="", employeeID="", department="", jobTitle="", basicSalary=0, age=0, dateOfBirth="",
                 passportDetails="", email="", phone="", address="", joiningDate="", supervisor=None,
                 clients=None):
        super().__init__(name, employeeID, department, jobTitle, basicSalary, age, dateOfBirth, passportDetails,
                         email, phone, address, joiningDate, supervisor)
        self.__clients = clients if clients else []

    # Getter and setter methods for clients attribute
    def get_clients(self):
        return self.__clients

    def set_clients(self, clients):
        self.__clients = clients


    def addClient(self, client):
        # Function to add a client to the salesperson's client list
        try:
            # Add logic to add a client
            pass
        except Exception as e:
            print(f"Error adding client: {e}")

    def removeClient(self, clientID):
        # Function to remove a client from the salesperson's client list
        try:
            # Add logic to remove a client
            pass
        except Exception as e:
            print(f"Error removing client: {e}")


class MarketingManager(Employee):
    """Class for marketing manager working for Best Events Company"""

    def __init__(self, name="", employeeID="", department="", jobTitle="", basicSalary=0, age=0, dateOfBirth="",
                 passportDetails="", email="", phone="", address="", joiningDate="", supervisor=None,
                 marketingStrategy=""):
        super().__init__(name, employeeID, department, jobTitle, basicSalary, age, dateOfBirth, passportDetails,
                         email, phone, address, joiningDate, supervisor)
        self.__marketingStrategy = marketingStrategy

    def updateMarketingStrategy(self, newStrategy):
        # Function to update marketing strategy
        try:
            # Add logic to update marketing strategy
            pass
        except Exception as e:
            print(f"Error updating marketing strategy: {e}")

    def launchMarketingCampaign(self):
        # Function to launch a marketing campaign
        try:
            # Add logic to launch a marketing campaign
            pass
        except Exception as e:
            print(f"Error launching marketing campaign: {e}")

    # Getter and setter methods for marketingStrategy attribute
    def get_marketingStrategy(self):
        return self.__marketingStrategy

    def set_marketingStrategy(self, marketingStrategy):
        self.__marketingStrategy = marketingStrategy


class Marketer(Employee):
    """Class for marketer working for Best Events Company"""
    def __init__(self, name="", employeeID="", department="", jobTitle="", basicSalary=0, age=0, dateOfBirth="",
                 passportDetails="", email="", phone="", address="", joiningDate="", supervisor=None,
                 campaigns=None):
        super().__init__(name, employeeID, department, jobTitle, basicSalary, age, dateOfBirth, passportDetails,
                         email, phone, address, joiningDate, supervisor)
        self.__campaigns = campaigns if campaigns else []

    def createCampaign(self, campaign):
        # Function to create a marketing campaign
        try:
            # Add logic to create a campaign
            pass
        except Exception as e:
            print(f"Error creating campaign: {e}")

    def updateCampaign(self, campaignID, updates):
        # Function to update an existing marketing campaign
        try:
            # Add logic to update a campaign
            pass
        except Exception as e:
            print(f"Error updating campaign: {e}")

    # Getter and setter methods for campaigns attribute
    def get_campaigns(self):
        return self.__campaigns

    def set_campaigns(self, campaigns):
        self.__campaigns = campaigns



class Accountant(Employee):
    """Class for accountant working for Best Events Company"""
    def __init__(self, name="", employeeID="", department="", jobTitle="", basicSalary=0, age=0, dateOfBirth="",
                 passportDetails="", email="", phone="", address="", joiningDate="", supervisor=None,
                 financialReports=None):
        super().__init__(name, employeeID, department, jobTitle, basicSalary, age, dateOfBirth, passportDetails,
                         email, phone, address, joiningDate, supervisor)
        self.__financialReports = financialReports if financialReports else []

    def generateFinancialReport(self, startDate, endDate):
        # Function to generate a financial report for a specific period
        try:
            # Add logic to generate a financial report
            pass
        except Exception as e:
            print(f"Error generating financial report: {e}")

    def updateFinancialRecords(self, transaction):
        # Function to update financial records with a new transaction
        try:
            # Add logic to update financial records
            pass
        except Exception as e:
            print(f"Error updating financial records: {e}")


    # Getter and setter methods for financialReports attribute
    def get_financialReports(self):
        return self.__financialReports

    def set_financialReports(self, financialReports):
        self.__financialReports = financialReports



class Designer(Employee):
    """Class for designer working for Best Events Company"""
    def __init__(self, name="", employeeID="", department="", jobTitle="", basicSalary=0, age=0, dateOfBirth="",
                 passportDetails="", email="", phone="", address="", joiningDate="", supervisor=None,
                 designs=None):
        super().__init__(name, employeeID, department, jobTitle, basicSalary, age, dateOfBirth, passportDetails,
                         email, phone, address, joiningDate, supervisor)
        self.__designs = designs if designs else []

    def createDesign(self, design):
        # Function to create a new design
        try:
            # Add logic to create a design
            pass
        except Exception as e:
            print(f"Error creating design: {e}")

    def updateDesign(self, designID, updates):
        # Function to update an existing design
        try:
            # Add logic to update a design
            pass
        except Exception as e:
            print(f"Error updating design: {e}")

    # Getter and setter methods for designs attribute
    def get_designs(self):
        return self.__designs

    def set_designs(self, designs):
        self.__designs = designs


class Handyman(Employee):
    """Class for Handyman working for Best Events Company"""
    def __init__(self, name="", employeeID="", department="", jobTitle="", basicSalary=0, age=0, dateOfBirth="",
                 passportDetails="", email="", phone="", address="", joiningDate="", supervisor=None,
                 tasks=None):
        super().__init__(name, employeeID, department, jobTitle, basicSalary, age, dateOfBirth, passportDetails,
                         email, phone, address, joiningDate, supervisor)
        self.__tasks = tasks if tasks else []

    def assignTask(self, task):
        # Function to assign a task to the handyman
        try:
            # Add logic to assign a task
            pass
        except Exception as e:
            print(f"Error assigning task: {e}")

    def completeTask(self, taskID):
        # Function to mark a task as completed
        try:
            # Add logic to mark a task as completed
            pass
        except Exception as e:
            print(f"Error completing task: {e}")

    # Getter and setter methods for tasks attribute
    def get_tasks(self):
        return self.__tasks

    def set_tasks(self, tasks):
        self.__tasks = tasks



class Client:
    """ Class for clients that are collaborating with best events company"""
    def __init__(self, clientID="", name="", address="", contactDetails="", budget=0,
                 eventHistory=None, loyaltyPoints=0, preferredContactMethod="", specialRequests=None,
                 contractSigned=False):
        self._clientID = clientID
        self._name = name
        self._address = address
        self._contactDetails = contactDetails
        self._budget = budget
        self._eventHistory = eventHistory if eventHistory else []
        self._loyaltyPoints = loyaltyPoints
        self._preferredContactMethod = preferredContactMethod
        self._specialRequests = specialRequests if specialRequests else []
        self._contractSigned = contractSigned

    def calculateTotalSpending(self):
        # Function to calculate total spending on events organized
        try:
            # Add logic to calculate total spending
            pass
        except Exception as e:
            print(f"Error calculating total spending: {e}")

    def updateEventHistory(self, event):
        # Function to update event history by adding a new event
        try:
            # Add logic to update event history
            pass
        except Exception as e:
            print(f"Error updating event history: {e}")

    def sendReminder(self):
        # Function to send a reminder to the client about upcoming events
        try:
            # Add logic to send a reminder
            pass
        except Exception as e:
            print(f"Error sending reminder: {e}")

    # Getter and setter methods for clientID attribute
    def get_clientID(self):
        return self._clientID

    def set_clientID(self, clientID):
        self._clientID = clientID

    # Getter and setter methods for name attribute
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Getter and setter methods for address attribute
    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    # Getter and setter methods for contactDetails attribute
    def get_contactDetails(self):
        return self._contactDetails

    def set_contactDetails(self, contactDetails):
        self._contactDetails = contactDetails

    # Getter and setter methods for budget attribute
    def get_budget(self):
        return self._budget

    def set_budget(self, budget):
        self._budget = budget

    # Getter and setter methods for eventHistory attribute
    def get_eventHistory(self):
        return self._eventHistory

    def set_eventHistory(self, eventHistory):
        self._eventHistory = eventHistory

    # Getter and setter methods for loyaltyPoints attribute
    def get_loyaltyPoints(self):
        return self._loyaltyPoints

    def set_loyaltyPoints(self, loyaltyPoints):
        self._loyaltyPoints = loyaltyPoints

    # Getter and setter methods for preferredContactMethod attribute
    def get_preferredContactMethod(self):
        return self._preferredContactMethod

    def set_preferredContactMethod(self, preferredContactMethod):
        self._preferredContactMethod = preferredContactMethod

    # Getter and setter methods for specialRequests attribute
    def get_specialRequests(self):
        return self._specialRequests

    def set_specialRequests(self, specialRequests):
        self._specialRequests = specialRequests

    # Getter and setter methods for contractSigned attribute
    def get_contractSigned(self):
        return self._contractSigned

    def set_contractSigned(self, contractSigned):
        self._contractSigned = contractSigned

class Guest:
    """ Class for guests that are invited to services best events company provide"""
    def __init__(self, guestID="", name="", address="", contactDetails="",
                 rsvpStatus="", mealPreference="", accommodationDetails="", giftRegistry="",
                 specialNeeds=""):
        self._guestID = guestID
        self._name = name
        self._address = address
        self._contactDetails = contactDetails
        self._rsvpStatus = rsvpStatus
        self._mealPreference = mealPreference
        self._accommodationDetails = accommodationDetails
        self._giftRegistry = giftRegistry
        self._specialNeeds = specialNeeds

    def confirmRSVP(self):
        # Function to confirm RSVP status for the event
        try:
            # Add logic to confirm RSVP
            pass
        except Exception as e:
            print(f"Error confirming RSVP: {e}")

    def updateMealPreference(self, preference):
        # Function to update meal preference
        try:
            # Add logic to update meal preference
            pass
        except Exception as e:
            print(f"Error updating meal preference: {e}")

    def requestTransportation(self):
        # Function to request transportation arrangements
        try:
            # Add logic to request transportation
            pass
        except Exception as e:
            print(f"Error requesting transportation: {e}")


    # Getter and setter methods for guestID attribute
    def get_guestID(self):
        return self._guestID

    def set_guestID(self, guestID):
        self._guestID = guestID

    # Getter and setter methods for name attribute
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Getter and setter methods for address attribute
    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    # Getter and setter methods for contactDetails attribute
    def get_contactDetails(self):
        return self._contactDetails

    def set_contactDetails(self, contactDetails):
        self._contactDetails = contactDetails

    # Getter and setter methods for rsvpStatus attribute
    def get_rsvpStatus(self):
        return self._rsvpStatus

    def set_rsvpStatus(self, rsvpStatus):
        self._rsvpStatus = rsvpStatus

    # Getter and setter methods for mealPreference attribute
    def get_mealPreference(self):
        return self._mealPreference

    def set_mealPreference(self, mealPreference):
        self._mealPreference = mealPreference

    # Getter and setter methods for accommodationDetails attribute
    def get_accommodationDetails(self):
        return self._accommodationDetails

    def set_accommodationDetails(self, accommodationDetails):
        self._accommodationDetails = accommodationDetails

    # Getter and setter methods for giftRegistry attribute
    def get_giftRegistry(self):
        return self._giftRegistry

    def set_giftRegistry(self, giftRegistry):
        self._giftRegistry = giftRegistry

    # Getter and setter methods for specialNeeds attribute
    def get_specialNeeds(self):
        return self._specialNeeds

    def set_specialNeeds(self, specialNeeds):
        self._specialNeeds = specialNeeds


class Event:
    """ Class for events hosted by best events company provide"""
    def __init__(self, eventID="", type="", theme="", date="", time="", duration="", venueAddress="", clientID="",
                 guestList=None, invoice="", status="", attendeeCount=0, feedback="", expenses=0, profit=0):
        self.__eventID = eventID
        self.__type = type
        self.__theme = theme
        self.__date = date
        self.__time = time
        self.__duration = duration
        self.__venueAddress = venueAddress
        self.__clientID = clientID
        self.__guestList = guestList if guestList else []
        self.__invoice = invoice
        self.__status = status
        self.__attendeeCount = attendeeCount
        self.__feedback = feedback
        self.__expenses = expenses
        self.__profit = profit

    def updateStatus(self, newStatus):
        # Function to update status of the event
        try:
            # Add logic to update event status
            pass
        except Exception as e:
            print(f"Error updating event status: {e}")

    def recordFeedback(self, feedback):
        # Function to record feedback received after the event
        try:
            # Add logic to record feedback
            pass
        except Exception as e:
            print(f"Error recording feedback: {e}")

    def calculateProfit(self):
        # Function to calculate profit generated from the event
        try:
            # Add logic to calculate profit
            pass
        except Exception as e:
            print(f"Error calculating profit: {e}")

    # Getter and setter methods for eventID attribute
    def get_eventID(self):
        return self.__eventID

    def set_eventID(self, eventID):
        self.__eventID = eventID

    # Getter and setter methods for type attribute
    def get_type(self):
        return self.__type

    def set_type(self, type):
        self.__type = type

    # Getter and setter methods for theme attribute
    def get_theme(self):
        return self.__theme

    def set_theme(self, theme):
        self.__theme = theme

    # Getter and setter methods for date attribute
    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date

    # Getter and setter methods for time attribute
    def get_time(self):
        return self.__time

    def set_time(self, time):
        self.__time = time

    # Getter and setter methods for duration attribute
    def get_duration(self):
        return self.__duration

    def set_duration(self, duration):
        self.__duration = duration

    # Getter and setter methods for venueAddress attribute
    def get_venueAddress(self):
        return self.__venueAddress

    def set_venueAddress(self, venueAddress):
        self.__venueAddress = venueAddress

    # Getter and setter methods for clientID attribute
    def get_clientID(self):
        return self.__clientID

    def set_clientID(self, clientID):
        self.__clientID = clientID

    # Getter and setter methods for guestList attribute
    def get_guestList(self):
        return self.__guestList

    def set_guestList(self, guestList):
        self.__guestList = guestList

    # Getter and setter methods for invoice attribute
    def get_invoice(self):
        return self.__invoice

    def set_invoice(self, invoice):
        self.__invoice = invoice

    # Getter and setter methods for status attribute
    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    # Getter and setter methods for attendeeCount attribute
    def get_attendeeCount(self):
        return self.__attendeeCount

    def set_attendeeCount(self, attendeeCount):
        self.__attendeeCount = attendeeCount

    # Getter and setter methods for feedback attribute
    def get_feedback(self):
        return self.__feedback

    def set_feedback(self, feedback):
        self.__feedback = feedback

    # Getter and setter methods for expenses attribute
    def get_expenses(self):
        return self.__expenses

    def set_expenses(self, expenses):
        self.__expenses = expenses

    # Getter and setter methods for profit attribute
    def get_profit(self):
        return self.__profit

    def set_profit(self, profit):
        self.__profit = profit

class Supplier:
    """ Class for suppliers that provide services/products for best events company provide"""
    def __init__(self, supplierID="", name="", address="", contactDetails="",
                 serviceArea="", availability="", contractSigned=False, preferredPaymentMethod="",
                 specialization=""):
        self.__supplierID = supplierID
        self.__name = name
        self.__address = address
        self.__contactDetails = contactDetails
        self.__serviceArea = serviceArea
        self.__availability = availability
        self.__contractSigned = contractSigned
        self.__preferredPaymentMethod = preferredPaymentMethod
        self.__specialization = specialization

    def updateAvailability(self, schedule):
        # Function to update availability schedule
        try:
            # Add logic to update availability
            pass
        except Exception as e:
            print(f"Error updating availability: {e}")

    def signContract(self):
        # Function to mark the contract as signed
        try:
            # Add logic to mark contract as signed
            pass
        except Exception as e:
            print(f"Error signing contract: {e}")

    def processPayment(self, amount):
        # Function to process payment for services rendered
        try:
            # Add logic to process payment
            pass
        except Exception as e:
            print(f"Error processing payment: {e}")


    # Getter and setter methods for supplierID attribute
    def get_supplierID(self):
        return self.__supplierID

    def set_supplierID(self, supplierID):
        self.__supplierID = supplierID

    # Getter and setter methods for name attribute
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Getter and setter methods for address attribute
    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    # Getter and setter methods for contactDetails attribute
    def get_contactDetails(self):
        return self.__contactDetails

    def set_contactDetails(self, contactDetails):
        self.__contactDetails = contactDetails

    # Getter and setter methods for serviceArea attribute
    def get_serviceArea(self):
        return self.__serviceArea

    def set_serviceArea(self, serviceArea):
        self.__serviceArea = serviceArea

    # Getter and setter methods for availability attribute
    def get_availability(self):
        return self.__availability

    def set_availability(self, availability):
        self.__availability = availability

    # Getter and setter methods for contractSigned attribute
    def get_contractSigned(self):
        return self.__contractSigned

    def set_contractSigned(self, contractSigned):
        self.__contractSigned = contractSigned

    # Getter and setter methods for preferredPaymentMethod attribute
    def get_preferredPaymentMethod(self):
        return self.__preferredPaymentMethod

    def set_preferredPaymentMethod(self, preferredPaymentMethod):
        self.__preferredPaymentMethod = preferredPaymentMethod

    # Getter and setter methods for specialization attribute
    def get_specialization(self):
        return self.__specialization

    def set_specialization(self, specialization):
        self.__specialization = specialization


class Venue:
    """ Class for venues that best events company provide"""
    def __init__(self, venueID="", name="", address="", contact="", minGuests=0, maxGuests=0,
                 amenities=None, bookingStatus="", bookingDate="", cancellationPolicy="", additionalFees=None):
        self.__venueID = venueID
        self.__name = name
        self.__address = address
        self.__contact = contact
        self.__minGuests = minGuests
        self.__maxGuests = maxGuests
        self.__amenities = amenities if amenities else []
        self.__bookingStatus = bookingStatus
        self.__bookingDate = bookingDate
        self.__cancellationPolicy = cancellationPolicy
        self.__additionalFees = additionalFees if additionalFees else []

    def updateAmenities(self, newAmenities):
        # Function to update the list of amenities available at the venue
        try:
            self.__amenities = newAmenities
        except Exception as e:
            print(f"Error updating amenities: {e}")

    def checkAvailability(self, date):
        # Function to check the availability of the venue for a given date
        try:
            # Implement logic to check availability based on existing bookings
            pass
        except Exception as e:
            print(f"Error checking availability: {e}")

    def calculateTotalCost(self, duration):
        # Function to calculate the total cost of renting the venue for a specified duration,
        # including any additional fees
        try:
            total_cost = 0
            # Implement logic to calculate cost based on duration and additional fees
            return total_cost
        except Exception as e:
            print(f"Error calculating total cost: {e}")


    # Getter and setter methods for venueID attribute
    def get_venueID(self):
        return self.__venueID

    def set_venueID(self, venueID):
        self.__venueID = venueID

    # Getter and setter methods for name attribute
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Getter and setter methods for address attribute
    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    # Getter and setter methods for contact attribute
    def get_contact(self):
        return self.__contact

    def set_contact(self, contact):
        self.__contact = contact

    # Getter and setter methods for minGuests attribute
    def get_minGuests(self):
        return self.__minGuests

    def set_minGuests(self, minGuests):
        self.__minGuests = minGuests

    # Getter and setter methods for maxGuests attribute
    def get_maxGuests(self):
        return self.__maxGuests

    def set_maxGuests(self, maxGuests):
        self.__maxGuests = maxGuests

    # Getter and setter methods for amenities attribute
    def get_amenities(self):
        return self.__amenities

    def set_amenities(self, amenities):
        self.__amenities = amenities

    # Getter and setter methods for bookingStatus attribute
    def get_bookingStatus(self):
        return self.__bookingStatus

    def set_bookingStatus(self, bookingStatus):
        self.__bookingStatus = bookingStatus

    # Getter and setter methods for bookingDate attribute
    def get_bookingDate(self):
        return self.__bookingDate

    def set_bookingDate(self, bookingDate):
        self.__bookingDate = bookingDate

    # Getter and setter methods for cancellationPolicy attribute
    def get_cancellationPolicy(self):
        return self.__cancellationPolicy

    def set_cancellationPolicy(self, cancellationPolicy):
        self.__cancellationPolicy = cancellationPolicy

    # Getter and setter methods for additionalFees attribute
    def get_additionalFees(self):
        return self.__additionalFees

    def set_additionalFees(self, additionalFees):
        self.__additionalFees = additionalFees

