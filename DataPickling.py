# data pickle.py
import pickle
import os

def load_data(filename):
    """Load data from a pickle file."""
    try:
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                return pickle.load(file)
        else:
            return {}  #This code will return an empty dictionary if the file doesn't exist
    except Exception as e:
        raise IOError(f"Failed to load data from {filename}: {str(e)}")

def save_data(data, filename):
    """Save data to a pickle file."""
    try:
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
    except Exception as e:
        raise IOError(f"Failed to save data to {filename}: {str(e)}")
