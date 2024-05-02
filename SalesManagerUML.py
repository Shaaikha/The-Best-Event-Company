class SalesManager(Employee):
    """Class for sales manager working for Best Events Company"""
    #Adding the instructor in order to initialize attributes and their data types for better efficiency
    def __init__(self, fullName="", employeeId="", deptName="", positionTitle="", monthlySalary=0, currentAge=0, birthDate="",
                 passportInfo="", emailAddress="", phoneNumber="", homeAddress="", employmentStartDate="",
                 salesTarget=0, salesAchieved=0, bonus=0, salesRegion=""):
        super().__init__(fullName, employeeId, deptName, positionTitle, monthlySalary, currentAge, birthDate, passportInfo,
                         emailAddress, phoneNumber, homeAddress, employmentStartDate)
        #The attributes are private using the prefix of "__"
        self.__salesTarget = salesTarget
        self.__salesAchieved = salesAchieved
        self.__bonus = bonus
        self.__salesRegion = salesRegion

    def updateSalesTarget(self, newTarget):
        #This function is used to update sales target, where it handles errors using try and except
        try:
            self.__salesTarget = newTarget
        except Exception as e:
            print(f"Error updating sales target: {e}")

    def generateSalesReport(self):
        #This function is used to generate sales report
        try:
            #Then we create an algorithm in order to generate sales report
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
