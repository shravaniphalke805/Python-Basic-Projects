# Tuples + Dictionaries + OOP
# Create Employee class
class Employee:
    # Constructor to initialize employee details
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        # Store department and salary as a tuple
        self.details = (department, salary)
    # Method to display employee information
    def show_details(self):
        print("\nEmployee Details")
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.details[0])
        print("Salary:", self.details[1])
# Create dictionary with employee ID as key
# and Employee object as value
employees = {}

# Add 3 employee objects
emp1 = Employee(101, "Rahul", "IT", 50000)
emp2 = Employee(102, "Priya", "HR", 45000)
emp3 = Employee(103, "Amit", "Finance", 60000)

# Store objects in dictionary
employees[101] = emp1
employees[102] = emp2
employees[103] = emp3

# Display all employee details using loop
for emp_id, employee in employees.items():
    employee.show_details()
