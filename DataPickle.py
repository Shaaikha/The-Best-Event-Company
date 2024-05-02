import pickle
import os
from tkinter import messagebox

class DataHandler:
    """Class to handle pickle operations for storing and retrieving data."""

    def __init__(self, filename):
        """Initialize with the file name where the data is stored."""
        self.filename = filename

    def load_data(self):
        """Load data from a pickle file."""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'rb') as file:
                    return pickle.load(file)
            else:
                return self.initialize_empty_data()
        except Exception as e:
            messagebox.showerror("Loading Error", f"Failed to load data: {e}")
            return self.initialize_empty_data()

    def save_data(self, data):
        """Save data to a pickle file."""
        try:
            with open(self.filename, 'wb') as file:
                pickle.dump(data, file)
        except Exception as e:
            messagebox.showerror("Saving Error", f"Failed to save data: {e}")

    def initialize_empty_data(self):
        """Return an empty data structure for all entity types."""
        return {'Employees': {}, 'Events': {}, 'Clients': {}, 'Guests': {}, 'Suppliers': {}, 'Venues': {}}
