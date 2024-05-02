class Handyman(Employee):
    """Class for Handyman working for Best Events Company"""
    #Adding the instructor in order to initialize attributes and their data types for better efficiency
    def __init__(self, fullName="", employeeId="", deptName="", positionTitle="", monthlySalary=0, currentAge=0, birthDate="",
                 passportInfo="", emailAddress="", phoneNumber="", homeAddress="", employmentStartDate="", tasks=None):
        # Initialize handyman attributes
        #The attributes are private using the prefix of "__"
        super().__init__(fullName, employeeId, deptName, positionTitle, monthlySalary, currentAge, birthDate, passportInfo,
                         emailAddress, phoneNumber, homeAddress, employmentStartDate)
        self.__tasks = tasks if tasks else []

    def assign_task(self, task):
        #This function is developed to assign a task to the handyman
        try:
            self.__tasks.append(task)
        except Exception as e:
            print(f"Error assigning task: {e}")

    def completeTask(self, taskID):
        #This function is developed to mark a task as completed
        try:
            self.__tasks = [task for task in self.__tasks if task['id'] != taskID]
        except Exception as e:
            print(f"Error completing task: {e}")
    #Adding setters and getters for tasks attributes that are completed by the handman in the company
    def getTasks(self):
        return self.__tasks

    def setTasks(self, tasks):
        self.__tasks = tasks

    def __str__(self):
        #Adding string representation of the handyman object in order to simplify and clarify the end result
        employee_str = super().__str__()  # Get the string from the superclass
        task_count = len(self.__tasks)
        return f"{employee_str}\nTasks Assigned: {task_count} tasks"