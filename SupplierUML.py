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