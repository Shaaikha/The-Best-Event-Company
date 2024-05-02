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