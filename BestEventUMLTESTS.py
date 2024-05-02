from BestEventCompanyUML import BestEventCompany, Employee, Event, SalesPerson, SalesManager, MarketingManager, Marketer
from BestEventCompanyUML import Handyman, Designer, Event, Guest, Client, Supplier, Venue

# Test Case 1: Initialize a basic employee
employee1 = Employee(fullName="Shaikha Mohammed", employeeId="EMP001", deptName="Marketing", positionTitle="Manager",
                     monthlySalary=5000, currentAge=35, birthDate="1986-07-15", passportInfo="A12345678", emailAddress="shaikha.m@example.com",
                     phoneNumber="+971501234567", homeAddress="123 Street, Dubai", employmentStartDate="2015-01-10")
print("Test case 1:",employee1)

# Test Case 2: Modify attributes using setters
employee1.setFullName("Shaikha Mubarak")
employee1.setEmailAddress("shaikha.mubarak@example.com")
employee1.setPhoneNumber("+971508765432")
print("Test case 2:",employee1)

# Test Case 3: Initialize a Sales Manager and test updating sales target
sales_manager1 = SalesManager(fullName="Ahmed Al Falasi", employeeId="SM001", deptName="Sales", positionTitle="Sales Manager",
                              monthlySalary=7000, currentAge=40, birthDate="1982-03-15", passportInfo="A123456789",
                              emailAddress="ahmed.alfalasi@example.com", phoneNumber="+971500123456", homeAddress="450 Market St, Dubai",
                              employmentStartDate="2010-04-01", salesTarget=1000000, salesAchieved=750000, bonus=5000, salesRegion="UAE")
sales_manager1.setSalesTarget(1100000)
print("Test case 3:", sales_manager1.generateSalesReport())

# Test Case 4: Add a client to a SalesPerson and update their information
sales_person1 = SalesPerson(fullName="Fatima Al Hashimi", employeeId="SP001", deptName="Sales", positionTitle="Sales Representative",
                            monthlySalary=4500, currentAge=30, birthDate="1991-07-21", passportInfo="B987654321",
                            emailAddress="initial@example.com", phoneNumber="1234567890", homeAddress="789 Crescent Rd, Abu Dhabi",
                            employmentStartDate="2019-08-15", clients=[])
sales_person1.addClient({'id': 'C001', 'name': "Khalid Bin Walid"})
sales_person1.updateContactDetails("fatima.alhashimi@example.com", "+971509876543", "234 Avenue, Abu Dhabi")
print("Test case 4:", sales_person1)

# Test Case 5: Initialize and update Marketing Manager
marketing_manager1 = MarketingManager(fullName="Saeed Al Mansoori", employeeId="MM001", deptName="Marketing", positionTitle="Marketing Manager",
                                      monthlySalary=8000, currentAge=38, birthDate="1984-02-28", passportInfo="C123456789",
                                      emailAddress="saeed.almansoori@example.com", phoneNumber="+971500999888", homeAddress="123 Marina St, Dubai",
                                      employmentStartDate="2012-05-10", marketingStrategy="Social Media Dominance")
marketing_manager1.updateMarketingStrategy("Influencer Outreach")
print("Test case 5:", marketing_manager1.launchMarketingCampaign())

# Test Case 6: Create a Designer and add a new design
designer1 = Designer(fullName="Mariam Al Rais", employeeId="D001", deptName="Design", positionTitle="Lead Designer",
                     monthlySalary=6500, currentAge=29, birthDate="1992-11-12", passportInfo="D123456789",
                     emailAddress="mariam.alrais@example.com", phoneNumber="+971500111222", homeAddress="321 Palm Jumeirah, Dubai",
                     employmentStartDate="2018-09-15", designs=[])
designer1.createDesign({'id': 'D101', 'name': "Wedding Theme A"})
print("Test case 6:", designer1)

# Test Case 7: Assign a task to a Handyman
handyman1 = Handyman(fullName="Ali Al Amri", employeeId="H001", deptName="Maintenance", positionTitle="Senior Handyman",
                     monthlySalary=4000, currentAge=45, birthDate="1976-04-17", passportInfo="E123456789",
                     emailAddress="ali.amri@example.com", phoneNumber="+971502233445", homeAddress="222 Industrial Area, Sharjah",
                     employmentStartDate="2015-01-20", tasks=[])
handyman1.assign_task({'id': 'T001', 'description': "Fix lighting in event hall A"})
print("Test case 7:", handyman1)



# Test Case 8: Create a Supplier and process a payment
supplier1 = Supplier(supplierId="S001", supplierName="Khaled Al Maktoum", supplierAddress="123 Industrial Area, Sharjah",
                     supplierContactDetails="+971506789012", serviceArea="Dubai and Sharjah", availability="Weekdays",
                     contractSigned=True, preferredPaymentMethod="Bank Transfer")
print("Test case 8:",supplier1.processPayment(5000))

# Test Case 9: Creating and updating an event
event1 = Event(
    eventId="EV001",
    eventType="Wedding",
    eventTheme="Beach Wedding",
    eventDate="2023-12-15",
    eventTime="18:00",
    eventDuration="6 hours",
    venueAddress="123 Ocean Drive, Beach City",
    clientId="CL001",
    guestList=["Shaikha Mohammed", "Ahmed Al Falasi"],
    invoice="INV1001",
    eventStatus="Planned",
    attendeeCount=100,
    feedback="",
    expenses=20000,
    profit=5000
)

# Updating the status of the event
event1.updateStatus("Completed")
event1.recordFeedback("Excellent venue and arrangements.")

# Displaying the updated event details
print("Test case 9:",event1)


# Test Case 10: Managing events and venues in a company
best_event_company = BestEventCompany()

# Creating a new event and a new venue
event2 = Event(
    eventId="EV002",
    eventType="Birthday",
    eventTheme="Superhero Party",
    eventDate="2023-05-20",
    eventTime="15:00",
    eventDuration="4 hours",
    venueAddress="555 Fun Park Blvd, Adventure City",
    clientId="CL002",
    guestList=["Fatima Al Hashimi", "Saeed Al Mansoori"],
    invoice="INV1002",
    eventStatus="Scheduled",
    attendeeCount=50,
    feedback="",
    expenses=10000,
    profit=3000
)

venue1 = Venue(
    venueIdentifier="VN001",
    venueName="Grand Ballroom",
    venueAddress="789 Royal St, Downtown",
    venueContactInfo="+971500112233",
    minimumGuestCapacity=50,
    maximumGuestCapacity=200,
    currentBookingStatus="Available",
    bookingDateDetails="2023 Entire Year",
    cancellationTerms="No refund on cancellation within 30 days",
    additionalServiceFees=["Lighting: $500", "Security: $300"]
)

# Adding the new event and venue to the company's management
best_event_company.add_event(event2)
best_event_company.add_venue(venue1)

# Printing the current state of the company's management
print("Test case 10:", best_event_company)
# Initializing a few employees from the table
employees = {
    47899: Employee("Susan Meyers", 47899, "Sales", "Manager", 37500, 45, "1977-03-22",
                    "AB1234567", "susan.meyers@example.com", "+971500123456", "123 Palm St, Dubai", "2010-08-15"),
    81774: Employee("Joy Rogers", 81774, "Sales", "Manager", 24000, 38, "1984-06-17",
                    "CD8901234", "joy.rogers@example.com", "+971500654321", "456 Cedar St, Abu Dhabi", "2013-04-01"),
    11234: Employee("Shyam Sundar", 11234, "Sales", "Salesperson", 20000, 28, "1994-11-12",
                    "EF4567890", "shyam.sundar@example.com", "+971501234567", "789 Maple St, Sharjah", "2016-09-23")
}

# Test Case 1: Print initial details
print("Test Case 1: Initial Details")
print(employees[47899])

# Test Case 2: Update Contact Details for Susan Meyers
print("\nTest Case 2: Update Contact Details")
employees[47899].updateContactDetails("susan.new@example.com", "+971500999888", "321 New Palm St, Dubai")
print(employees[47899])

# Test Case 3: Calculate and display total salary after a hypothetical bonus is added
print("\nTest Case 3: Calculate Total Salary")
employees[47899].setMonthlySalary(employees[47899].getMonthlySalary() + 5000)  # adding a bonus of AED 5000
print(employees[47899])

# Running the tests
if __name__ == "__main__":
    print(employees[47899])
    employees[47899].setEmailAddress("new_email@susanmeyers.com")
    employees[47899].setPhoneNumber("+971500987654")
    print(employees[47899])