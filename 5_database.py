# Dictionaries + Functions + Control Structures
def student_database():
    # Dictionary to store student records
    students = {}
    while True:
        # Display menu
        print("\n----- Student Database Menu -----")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice (1-4): "))
            # Option 1: Add Student
            if choice == 1:
                roll_no = input("Enter Roll Number: ")
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                city = input("Enter City: ")

                # Add student using update()
                students.update({
                    roll_no: {
                        "Name": name,
                        "Age": age,
                        "City": city
                    }
                })
                print("Student added successfully.")
            # Option 2: Search Student
            elif choice == 2:
                roll_no = input("Enter Roll Number to Search: ")
                # Search using get()
                student = students.get(roll_no)
                if student:
                    print("\nStudent Found")
                    print("Roll Number:", roll_no)
                    print("Name:", student["Name"])
                    print("Age:", student["Age"])
                    print("City:", student["City"])
                else:
                    print("Student not found.")

            # Option 3: Display All Students
            elif choice == 3:
                if len(students) == 0:
                    print("No student records available.")
                else:
                    print("\nAll Student Records")
                    for roll_no, details in students.items():
                        print("--------------------------")
                        print("Roll Number:", roll_no)
                        print("Name:", details["Name"])
                        print("Age:", details["Age"])
                        print("City:", details["City"])

            # Option 4: Exit
            elif choice == 4:
                print("Exiting program...")
                break

            else:
                print("Invalid choice! Please enter a number between 1 and 4.")

        # Handle invalid numeric input
        except ValueError:
            print("Invalid input! Please enter the correct value.")

# Call the function
student_database()
