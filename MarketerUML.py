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