#1st
# Variables 
#Create variables to store the information about yourself
fullname="Shravani Dipak Phalke"             
age=18                                        
height=5.5                                    
is_student=True                               
not_student=False                             
print(fullname)
print(age)
print(height)
print(is_student)
# fullname variable  is used to store name student
# age variable  is used to store age of student 
# height variable is used to store height of student
# is_student is a variable that stores whether someone is a student or not
print(type(fullname))
print(type(age))
print(type(height))
print(type(is_student))


#2nd
#Datatypes
string='Datatypes'
num=10
decimal=10.5
is_integer=True
print(string)
print(num)
print(decimal)
print(is_integer)
print(type(string))
print(type(num))
print(type(decimal))
print(type(is_integer))
 
# converting the integer to float and float to integer
num =float(num)
decimal=int(decimal)
print(num)
print(decimal)


#3rd
#Operators - Arithmetic
num1=15
num2=4
Addition=num1+num2
print(Addition)
Subtraction=num1-num2
print(Subtraction)
Multiplication=num1*num2
print(Multiplication)
Division=num1/num2
print(Division)
Floor_Division=num1//num2 
print(Floor_Division)
Modulo=num1%num2
print(Modulo)
Exponentiation=num1**num2
print(Exponentiation)

# Difference between / and // operators with an example
#Example
Division=num1/num2
print(Division)
Floor_Division=num1//num2 
print(Floor_Division)

#Explanation
#/ gives 3.75(a float)
#// gives 3 (an integer)


#4th 
#Operators - Comparison & Logical

# Comparison and Logical Operators
x = 25
y = 30
z = 25
print("Is x greater than y?")
print( x > y)
print("Is x equal to z?")
print(x == z)
print("Is x less than or equal to y AND y is not equal to z?")
print( x <= y and y != z)
print("Is x greater than y OR x equal to z?")
print( x > y or x == z)


#5th
# Program to calculate age based on user input

# Ask user for their name
name = input("Enter your name: ")

# Ask user for their birth year

birth_year = int(input("Enter your birth year: ")) #input() returns a string, so we convert to int to do arithmetic

# Assume current year is 2026
current_year = 2026

# Calculate age
age = current_year - birth_year

# Print the result with a descriptive message
print("Hello", name + "!", "You are", age, "years old.")


#6th
# BMI Calculator
# Formula: BMI = weight / (height ** 2)

# Ask user for weight in kilograms
weight = float(input("Enter your weight (kg): "))

# Ask user for height in meters
height = float(input("Enter your height (m): "))

# Calculate BMI
bmi = weight / (height ** 2)

# Print BMI rounded to 2 decimal places
print("Your BMI is:", round(bmi, 2))


#7th
# Program to calculate area and perimeter of a rectangle

# Taking input from the user for length and width
length = float(input("Enter length: "))
width = float(input("Enter width: "))

"""
We use float so that decimal values can also be entered,
like 5.5 or 10.2, which makes the program more flexible.
"""

# Formula for area of rectangle = length * width
area = length * width

# Formula for perimeter of rectangle = 2 * (length + width)
perimeter = 2 * (length + width)

# Displaying the results 
print("Area =", area)
print("Perimeter =", perimeter)


#8th
# Given data
fruits = ["mango", "apple", "banana", "cherry"]
score = 50

# Assignment operator (+=)
score += 25

# Membership operators
is_apple_present = "apple" in fruits
is_grape_absent = "grape" not in fruits

# Printing results
print("Updated score:", score)
print("Is 'apple' in fruits?:", is_apple_present)
print("Is 'grape' not in fruits?:", is_grape_absent)


#9th
# Student Profile Generator Program

# Taking input from the user
student_name = input("Enter student name: ")
student_age = int(input("Enter student age: "))
student_city = input("Enter student city: ")

# Marks in 3 subjects (converted to integers)
subject1_marks = float(input("Enter marks in Subject 1: "))
subject2_marks = float(input("Enter marks in Subject 2: "))
subject3_marks = float(input("Enter marks in Subject 3: "))

# Calculating total and percentage
total_marks = subject1_marks + subject2_marks + subject3_marks
percentage = (total_marks / 300) * 100   # assuming each subject is out of 100

# Printing formatted student profile
print("\n----- Student Profile -----")
print("Name      :", student_name)
print("Age       :", student_age)
print("City      :", student_city)
print("Marks     :", subject1_marks, subject2_marks, subject3_marks)
print("Total     :", total_marks)
print("Percentage:", percentage, "%")

#10th
Name = "Alice" #Variables need = for assignment
age =20        
city = "Amsterdam" #Strings must be in quotes
print("My name is" + Name)
print("I am", age ,"years old") #You can’t directly join strings and numbers without conversion or commas
print("I live in ", city)
# Check if age is greater than 18 and print message
print("Adult:", age > 18) #print() needs proper separators or formatting




























