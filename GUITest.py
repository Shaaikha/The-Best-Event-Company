import unittest
import tkinter as tk
from GUINavigation import BestEventCompanyGUI

class TestBestEventCompanyGUI(unittest.TestCase):
    def setUp(self):
        #Creating a set up the application for each test case
        self.root = tk.Tk()
        self.app = BestEventCompanyGUI(self.root)
        self.app.entities = {'Employees': {}, 'Events': {}, 'Clients': {}, 'Guests': {}, 'Suppliers': {}, 'Venues': {}}

    def test_add_employee(self):
        #This test adding an employee with names
        self.app.entries[('Employees', 'ID')].insert(0, '1')
        self.app.entries[('Employees', 'Name')].insert(0, 'Mohamed Ali')
        self.app.entries[('Employees', 'Department')].insert(0, 'IT')
        self.app.entries[('Employees', 'Job Title')].insert(0, 'Developer')
        self.app.entries[('Employees', 'Salary')].insert(0, '5000')
        self.app.add_entity('Employees')

        #First we check if the employee was added correctly
        self.assertIn('1', self.app.entities['Employees'])
        self.assertEqual(self.app.entities['Employees']['1']['Name'], 'Mohamed Ali')

    def test_display_employee(self):
        #Using this function we will prepare the environment by adding an employee
        self.app.entities['Employees']['1'] = {
            'ID': '1',
            'Name': 'Ahmed Hassan',
            'Department': 'Marketing',
            'Job Title': 'Manager',
            'Salary': '7000'
        }
        self.app.entries[('Employees', 'ID')].insert(0, '1')
        #Add the simulate display action
        self.app.display_entity('Employees')

        self.assertEqual(self.app.entities['Employees']['1']['Name'], 'Ahmed Hassan')

    def tearDown(self):
        #then we clean up after each test case
        self.app.root.destroy()

if __name__ == '__main__':
    unittest.main()




