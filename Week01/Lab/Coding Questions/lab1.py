# Q1 - Comments
# Sample Coding Questions 01 Week 01
# Andrea Salswach Lopez

# Q2 - Defining Variables
# Define an array variable with the following elements 1, 4, 7, 9
my_List = [1, 4, 7, 9]

# Q3 - Order of Operations
# Define 4 variables a, b, c, d and give them the values 1, 2, 3, 4
a = 1
b = 2
c = 3
d = 4
# the fully bracketed version of
# e = a * c - b / d is 
# e = (a * c) - (b / d)
# give the Fully-Bracketed Version of: e = a - b ** c // d + a % c

e = ( a - (b ** c ) // d ) + ( a % c )

# Q4 - Formatting
# Create a variable called “temperature” with the value 32.6. Then, print the following
# sentence by using the variable and the format function, with 1 line of code.“The temperature
# today is: 32.600 degrees Celsius”. Do not hard code the extra two zeros
temperature = 32.6
print( "The temperature today is: {:.3f} degrees Celsius.".format( temperature ))

# Q5 - Common Functions
# Ask the user to input their age, and then save that input into the variable
# “userAge”. For the user input, add 22.Then print the following sentence followed by the value of
# userAge. “Now showing the shop items filtered by age: 22”. Do not hard code the number 22.

userAge = int(input("Please enter your age: "))
print("Now showing the shop items filtered by age: {}.".format(userAge))