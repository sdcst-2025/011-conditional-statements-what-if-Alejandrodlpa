#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"
import math 

number=float(input("Give me a number"))


if "." in str(number):
    print("Your number is not an integer")
else:
    print("Your number is an integer")

