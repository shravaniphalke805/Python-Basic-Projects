# Create a class named Car
class Car:
    # Constructor to initialize brand and model
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Method to display car information
    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

# Creating objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Calling method
car1.display_info()
car2.display_info()


# Create a class named Book
class Book:

    # Constructor to initialize title, author, and price
    def __init__(self, title, author, price):
        self.title = title      # Store book title
        self.author = author    # Store author name
        self.price = price      # Store book price

    # Method to display book details
    def show_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price: ₹", self.price)
        print()  # Print a blank line


# Create first Book object
book1 = Book("Python Programming", "John Smith", 499)

# Create second Book object
book2 = Book("Data Structures", "Alice Brown", 599)

# Display details of the first book
book1.show_details()

# Display details of the second book
book2.show_details()

# Create a class named BankAccount
class BankAccount:

    # Constructor to initialize account holder name and balance
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Store account holder name
        self.balance = balance                # Store initial balance

    # Method to deposit money
    def deposit(self, amount):
        self.balance += amount
        print("Deposited ₹", amount)

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn ₹", amount)
        else:
            print("Insufficient Balance!")

    # Method to display current balance
    def show_balance(self):
        print("Current Balance: ₹", self.balance)


# Create a BankAccount object
account1 = BankAccount("Rahul", 5000)

# Display initial balance
account1.show_balance()

# Deposit money
account1.deposit(2000)

# Display updated balance
account1.show_balance()

# Withdraw money
account1.withdraw(3000)

# Display updated balance
account1.show_balance()

# Try to withdraw more than available balance
account1.withdraw(10000)


# Create a class named Student
class Student:

    # Constructor to initialize name and marks
    def __init__(self, name, marks):
        self.name = name      # Store student name
        self.marks = marks    # Store student marks

    # Method to calculate grade
    def calculate_grade(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"

    # Method to display student details
    def display_details(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Grade:", self.calculate_grade())
        print()

# Create 3 Student objects
student1 = Student("Rahul", 75)
student2 = Student("Priya", 35)
student3 = Student("Amit", 50)

# Display details and grades
student1.display_details()
student2.display_details()
student3.display_details()


# Create a class named Employee
class Employee:

    # Constructor to initialize name and salary
    def __init__(self, name, salary):
        self.name = name        # Store employee name
        self.salary = salary    # Store employee salary

    # Method to display employee details
    def display_details(self):
        print("Employee Name:", self.name)
        print("Salary: ₹", self.salary)

    # Method to increase salary
    def give_raise(self, amount):
        self.salary += amount
        print("Salary increased by ₹", amount)
        print("New Salary: ₹", self.salary)

    # Method to calculate yearly bonus
    def yearly_bonus(self):
        return self.salary * 0.10

# Create an Employee object
emp1 = Employee("Rahul", 50000)

# Display employee details
emp1.display_details()

# Give a salary raise
emp1.give_raise(5000)

# Calculate and display yearly bonus
bonus = emp1.yearly_bonus()
print("Yearly Bonus: ₹", bonus)


# Create a class named MobilePhone
class MobilePhone:

    # Constructor to initialize brand, model, and battery percentage
    def __init__(self, brand, model, battery_percentage):
        self.brand = brand                          # Store mobile brand
        self.model = model                          # Store mobile model
        self.battery_percentage = battery_percentage # Store battery level

    # Method to increase battery percentage
    def charge(self, percent):
        self.battery_percentage += percent

        # Ensure battery does not exceed 100%
        if self.battery_percentage > 100:
            self.battery_percentage = 100
        print("Phone charged by", percent, "%")

    # Method to reduce battery based on usage time
    def use_phone(self, minutes):
        battery_used = minutes // 10  # 1% battery decreases for every 10 minutes

        if battery_used <= self.battery_percentage:
            self.battery_percentage -= battery_used
        else:
            self.battery_percentage = 0
        print("Phone used for", minutes, "minutes")

    # Method to display current phone status
    def show_status(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Battery:", self.battery_percentage, "%")
        print()

# Create a MobilePhone object
phone1 = MobilePhone("Samsung", "Galaxy S24", 80)

# Display initial status
phone1.show_status()

# Use the phone
phone1.use_phone(30)

# Display status after usage
phone1.show_status()

# Charge the phone
phone1.charge(15)

# Display final status
phone1.show_status()


# Create a class named Rectangle
class Rectangle:

    # Constructor to initialize length and width
    def __init__(self, length, width):
        self.length = length    # Store length of rectangle
        self.width = width      # Store width of rectangle

    # Method to calculate area
    def area(self):
        return self.length * self.width

    # Method to calculate perimeter
    def perimeter(self):
        return 2 * (self.length + self.width)

    # Method to display rectangle details
    def display(self):
        print("Length:", self.length)
        print("Width:", self.width)
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())


# Take input from user
length = float(input("Enter length: "))
width = float(input("Enter width: "))

# Create Rectangle object
rectangle1 = Rectangle(length, width)

# Display results
rectangle1.display()

# Create a class named Player
class Player:

    # Constructor to initialize player details
    def __init__(self, name, score, level):
        self.name = name      # Store player name
        self.score = score    # Store player score
        self.level = level    # Store player level
    # Method to increase score
    def increase_score(self, points):
        self.score += points
        print(points, "points added")
    # Method to increase level by 1
    def level_up(self):
        self.level += 1
        print("Level increased")
    # Method to display player progress
    def show_progress(self):
        print("Player Name:", self.name)
        print("Score:", self.score)
        print("Level:", self.level)
        print()
# Create a Player object
player1 = Player("Rahul", 0, 1)

# Show initial progress
player1.show_progress()

# Update score and level multiple times
player1.increase_score(100)
player1.level_up()
player1.increase_score(200)
player1.level_up()
player1.increase_score(150)
# Show final progress
player1.show_progress()

# Create a class named Person
class Person:

    # Constructor method to initialize name and age
    # Added 'self' parameter to access object attributes
    def __init__(self, name, age):
        self.name = name   # Store name as an object attribute using self
        self.age = age     # Store age as an object attribute using self

    # Method to introduce the person
    # Added 'self' parameter to access object data
    def introduce(self):
        
        # Used + or f-string for combining strings and variables
        print(f"My name is {self.name} and I am {self.age} years old.")


# Create a Person object
p1 = Person("Rahul", 25)

# Call introduce method
p1.introduce()


# Create a class named Book
class Book:

    # Constructor to initialize book details
    def __init__(self, title, author):
        self.title = title              # Store book title
        self.author = author            # Store book author
        self.status = "Available"       # Default status of book

    # Method to issue a book
    def issue_book(self):
        if self.status == "Available":
            self.status = "Issued"
            print("Book issued successfully!")
        else:
            print("Book is already issued.")

    # Method to return a book
    def return_book(self):
        if self.status == "Issued":
            self.status = "Available"
            print("Book returned successfully!")
        else:
            print("Book is already available.")

    # Method to display book information
    def show_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Status:", self.status)
        print()


# Create an empty list to store books
library = []

# Add some initial book objects
library.append(Book("Python Programming", "John Smith"))
library.append(Book("Data Structures", "Alice Brown"))

# Menu-driven program
while True:
    print("----- Library Management System -----")
    print("1. Add a new book")
    print("2. Issue a book")
    print("3. Return a book")
    print("4. Show all books")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    # Add a new book
    if choice == 1:
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        new_book = Book(title, author)
        library.append(new_book)
        print("Book added successfully!")

    # Issue a book
    elif choice == 2:
        title = input("Enter book title to issue: ")
        found = False
        for book in library:
            if book.title == title:
                book.issue_book()
                found = True
                break
        if not found:
            print("Book not found.")

    # Return a book
    elif choice == 3:
        title = input("Enter book title to return: ")
        found = False
        for book in library:
            if book.title == title:
                book.return_book()
                found = True
                break
        if not found:
            print("Book not found.")

    # Show all books
    elif choice == 4:
        if len(library) == 0:
            print("No books available.")
        else:
            for book in library:
                book.show_info()

    # Exit program
    elif choice == 5:
        print("Thank you for using Library Management System.")
        break

    else:
        print("Invalid choice! Please try again.")

