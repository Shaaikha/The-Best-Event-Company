import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import pickle
import os

class EventGUI:
    def __init__(self, root):
        self.root = root
        root.title("Event Management System")
        root.geometry("600x400")

        # Load existing events from a file if it exists
        self.filename = 'events.pkl'
        self.events = self.load_events()

        # Setup form fields for event details
        self.entries = {}
        labels = ['Event ID', 'Type', 'Theme', 'Date', 'Time', 'Venue']
        for idx, label in enumerate(labels):
            ttk.Label(root, text=label).grid(row=idx, column=0, padx=10, pady=5, sticky='w')
            entry = ttk.Entry(root)
            entry.grid(row=idx, column=1, padx=10, pady=5, sticky='w')
            self.entries[label] = entry

        # Setup buttons for adding, modifying, deleting, and displaying events
        ttk.Button(root, text="Add", command=self.add_event).grid(row=len(labels), column=0, pady=10)
        ttk.Button(root, text="Modify", command=self.modify_event).grid(row=len(labels), column=1, pady=10)
        ttk.Button(root, text="Delete", command=self.delete_event).grid(row=len(labels)+1, column=0, pady=10)
        ttk.Button(root, text="Display", command=self.display_event).grid(row=len(labels)+1, column=1, pady=10)

    def load_events(self):
        # Load events from a pickle file, handling possible file corruption or IO errors
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'rb') as f:
                    return pickle.load(f)
        except Exception as e:
            messagebox.showerror("Loading Error", f"Failed to load events: {e}")
        return {}

    def save_events(self):
        # Save the current events to a pickle file, handling potential IO errors
        try:
            with open(self.filename, 'wb') as f:
                pickle.dump(self.events, f)
        except Exception as e:
            messagebox.showerror("Saving Error", f"Failed to save events: {e}")

    def add_event(self):
        # Add a new event after validating all fields are filled
        try:
            data = {label: self.entries[label].get() for label in self.entries}
            if not all(data.values()):
                messagebox.showerror("Error", "All fields are required")
                return
            if data['Event ID'] in self.events:
                messagebox.showerror("Error", "Event ID already exists")
                return
            self.events[data['Event ID']] = data
            self.save_events()
            messagebox.showinfo("Success", "Event added successfully")
            self.clear_entries()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add event: {e}")

    def modify_event(self):
        # Modify an existing event after validating the event ID and all fields
        try:
            event_id = self.entries['Event ID'].get()
            if not event_id or event_id not in self.events:
                messagebox.showerror("Error", "Invalid Event ID")
                return
            data = {label: self.entries[label].get() for label in self.entries}
            if not all(data.values()):
                messagebox.showerror("Error", "All fields must be filled to modify")
                return
            self.events[event_id].update(data)
            self.save_events()
            messagebox.showinfo("Success", "Event modified successfully")
            self.clear_entries()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to modify event: {e}")

    def delete_event(self):
        # Delete an event after confirming the event ID exists
        try:
            event_id = self.entries['Event ID'].get()
            if event_id in self.events:
                del self.events[event_id]
                self.save_events()
                messagebox.showinfo("Success", "Event deleted successfully")
                self.clear_entries()
            else:
                messagebox.showerror("Error", "Event not found")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete event: {e}")

    def display_event(self):
        # Display details of a specific event
        try:
            event_id = self.entries['Event ID'].get()
            if event_id in self.events:
                event = self.events[event_id]
                details = '\n'.join(f"{key}: {value}" for key, value in event.items())
                messagebox.showinfo("Event Details", details)
            else:
                messagebox.showerror("Error", "Event not found")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to display event details: {e}")

    def clear_entries(self):
        # Clear all entry widgets in the form
        for entry in self.entries.values():
            entry.delete(0, tk.END)

# Main application entry point
if __name__ == '__main__':
    root = tk.Tk()
    app = EventGUI(root)
    root.mainloop()
