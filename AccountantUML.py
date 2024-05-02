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