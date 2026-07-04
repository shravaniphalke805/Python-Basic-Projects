#1) if Statement
#Take age input from the user and convert it to integer 
age=int(input('Enter Your Age:'))
#Check if age is 18 or more 
if(age>=18):        
   #if condition is true, user is eligible to vote 
    print('You are eligible to vote.')


#2) if-else Statement
#Take age input from the user and convert it to integer
num=int(input('Enter Number:'))
#Check if num is even or odd 
if (num%2==0):
    #if condition is true,the number is even
    print('The number is even')
#else condition ,the number is odd
else:
    print('The number is odd')

#3) if-elif-else Statement
marks=int(input('Enter Your Marks:'))
if(marks>=90):
    print('Grade A  Excellent')
elif(marks>=75):
    print('Grade B  Good')
elif(marks>=60):
    print('Grade C  Average')
elif(marks>=40):
    print('Grade D  Pass')
else:
    print('Fail')


#4) For Loop with range
#a)All numbers from 1 to 30.
a=1
for a in range(31): # Loop from 0 to 30 
    print(a)        # Print the current value of a in each iteration
print('----------------End----------------------')

#b)All odd numbers from 1 to 50
i=1
for i in range(51): # loop runs from 0 to 50
    if (i%2!=0):    # check if number is odd (not divisible by 2)
     print(i)       # print the odd number
print('----------------End----------------------')

#c)Sum of numbers from 1 to 15
sum=0
for num in range(16): # loop from 0 to 15
    sum+=num          # add each number to sum
print('sum',sum) # print the final result after loop ends
print('----------------End----------------------')



# 5) While Loop
i = 1  
# loop until i becomes greater than 20
while i <= 20:
    print(i, "cube is", i**3)  # print number and its cube
    i += 1  # increase i by 1 each time

# loop stops automatically when i becomes 21


#6) While Loop - User Controlled
total = 0  
# ask user for first number
num = float(input("Enter a positive number (0 or negative to stop): "))

# keep looping until user enters 0 or negative number
while num > 0:
    total += num  # add number to total

    # ask again
    num = float(input("Enter a positive number (0 or negative to stop): "))

# print final result
print("Total sum is:", total)


# 7) Nested if Statement
# take inputs from user
temperature = int(input("Enter temperature: "))
is_raining = input("Is it raining? (yes/no): ")

# nested if conditions
if temperature > 30:
    if is_raining == "no":
        print("Hot day, wear light clothes.")
    else:
        print("Hot and rainy, carry umbrella.")

elif temperature < 15:
    if is_raining == "yes":
        print("Cold and rainy, wear jacket and take umbrella.")
    else:
        print("Cold day, wear warm clothes.")

else:
    print("Pleasant weather, dress comfortably.")



# 8) For Loop + if-elif-else
# loop from 1 to 40
for i in range(1, 41):
    
    # check if number is divisible by both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    
    # check if number is divisible by 3
    elif i % 3 == 0:
        print("Fizz")
    
    # check if number is divisible by 5
    elif i % 5 == 0:
        print("Buzz")
    
    # if none of the above conditions are true
    else:
        print(i)


# 9) Menu Driven Calculator Program
while True:

    # display menu
    print("\nSimple Calculator")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Multiply two numbers")
    print("4. Divide two numbers")
    print("5. Exit")

    # take user choice
    choice = int(input("Enter your choice: "))

    # exit the program
    if choice == 5:
        print("Exiting calculator. Goodbye!")
        break

    # check for invalid choice
    if choice not in [1, 2, 3, 4]:
        print("Invalid choice! Please select 1 to 5.")
        continue

    # take two numbers from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # add two numbers
    if choice == 1:
        print("Result:", num1 + num2)

    # subtract two numbers
    elif choice == 2:
        print("Result:", num1 - num2)

    # multiply two numbers
    elif choice == 3:
        print("Result:", num1 * num2)

    # divide two numbers
    elif choice == 4:

        # check division by zero
        if num2 == 0:
            print("Error: Cannot divide by zero")
        else:
            print("Result:", num1 / num2)



# 10) Debugging
# take number input and convert it to integer
num = int(input("Enter a number: "))

# check if number is greater than 100
if num > 100:
    print("Large number")

# check if number is greater than 50
elif num > 50:
    print("Medium number")

# if none of the above, number is small
else:
    print("Small number")

# start counter from 1
count = 1

# loop until count is less than 10
while count < 10:
    print(count)   # print current number
    count += 1     # increase count by 1 each time 




















 























































            



