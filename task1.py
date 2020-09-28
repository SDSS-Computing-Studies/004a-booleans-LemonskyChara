#! python3

# Have the user input a number. 
# Determine if the number is larger than 100 
# If it is, the output should read "The number is larger than 100" 
# (2 points)
# Inputs:
# number

# Outputs:
# "The number is larger than 100"
# "The number is smaller than 100"
# "The number is 100"

Number = input("The number is: ")
b = 100
number = int(Number)
if number > b:
    print("The number is larger than 100")
if number < b:
    print("The number is smaller than 100")
if number == b:
    print("The number is 100")       
