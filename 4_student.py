# OOP + Lists + Exception Handling
class Student:
    # Constructor to initialize student details
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []

    # Method to add a mark
    def add_mark(self, mark):
        if 0 <= mark <= 100:
            self.marks_list.append(mark)
        else:
            raise ValueError("Marks should be between 0 and 100.")
    # Method to calculate average marks
    def get_average(self):
        if len(self.marks_list) == 0:
            return 0
        return sum(self.marks_list) / len(self.marks_list)
    # Method to display student information
    def display_info(self):
        print("\nStudent Information")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks_list)
        print("Average:", self.get_average())

# Take student details from the user
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
# Create a Student object
student = Student(name, roll_no)
# Take marks as input
for i in range(5):
    while True:
        try:
            mark = float(input(f"Enter mark {i + 1}: "))
            student.add_mark(mark)
            break
        except ValueError as e:
            print("Error:", e)
# Display student details
student.display_info()
