class Guest:
    """Class for guests that are invited to services Best Events Company provides"""

    # Adding the instructor in order to initialize attributes and their data types for better efficiency
    def __init__(self, guestId="", guestName="", guestAddress="", contactDetails="",
                 rsvpStatus="", mealPreference="", accommodationDetails="", giftRegistry="",
                 specialNeeds=""):
        # The attributes are protected using the prefix of "_"
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
        # The confirm rsvp is a function to confirm RSVP status for the event
        self._rsvpStatus = "Confirmed"
        return f"RSVP status confirmed for {self._guestName}."

    def updateMealPreference(self, preference):
        # The update meal preference is a function to update meal preference
        self._mealPreference = preference
        return f"Meal preference updated to {preference} for {self._guestName}."

    def requestTransportation(self):
        # The request transportation is used as a function to request transportation arrangements
        return f"Transportation request initiated for {self._guestName}."

    # Developing the setters and getters for guest class
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

    # Adding a string to simplify the final result of guest object readibility
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

