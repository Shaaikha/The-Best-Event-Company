class Employee:
    """Class for employees working for Best Events Company"""
    #Adding the instructor in order to initialize attributes and their data types for better efficiency
    def __init__(self, fullName="", employeeId="", deptName="", positionTitle="", monthlySalary=0, currentAge=0, birthDate="",
                 passportInfo="", emailAddress="", phoneNumber="", homeAddress="", employmentStartDate=""):
        # Initialize employee attributes such as their name, id, departement...
        #The attributes are private using the prefix of "__"
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