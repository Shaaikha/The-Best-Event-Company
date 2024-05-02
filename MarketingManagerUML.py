class MarketingManager(Employee):
    """Class for marketing manager working for Best Events Company"""
    #Adding the instructor in order to initialize attributes and their data types for better efficiency
    def __init__(self, fullName="", employeeId="", deptName="", positionTitle="", monthlySalary=0, currentAge=0, birthDate="",
                 passportInfo="", emailAddress="", phoneNumber="", homeAddress="", employmentStartDate="",
                 marketingStrategy=""):
        # Initialize marketing manager attributes
        super().__init__(fullName, employeeId, deptName, positionTitle, monthlySalary, currentAge, birthDate, passportInfo,
                         emailAddress, phoneNumber, homeAddress, employmentStartDate)
        #The attributes are private using the prefix of "__"
        self.__marketingStrategy = marketingStrategy  # The marketing strategy employed by the marketing manager

    def updateMarketingStrategy(self, newStrategy):
        #The function is generated to update marketing strategy
        try:
            self.__marketingStrategy = newStrategy
        except Exception as e:
            print(f"Error updating marketing strategy: {e}")

    def launchMarketingCampaign(self):
        #Lunch marketing function is created to launch a marketing campaign
        try:
            #Then we add the logic for launch a marketing campaign
            return f"Launching marketing campaign with strategy: {self.__marketingStrategy}"
        except Exception as e:
            print(f"Error launching marketing campaign: {e}")

    def getMarketingStrategy(self):
        #Get the marketing strategy.
        return self.__marketingStrategy

    def setMarketingStrategy(self, marketingStrategy):
        #Set the marketing strategy.
        self.__marketingStrategy = marketingStrategy

    def __str__(self):
        #String representation of the MarketingManager object.
        employee_str = super().__str__()