#! python3
"""
 Have the user input a number 
 Determine if the number is positive, negative or 0 
 2 points

 Inputs:
 number

 Outputs:
 - "positive"
 - "negative"
 - "zero"

 Example:

Enter a number: 3
positive

Enter a number: -1.2
negative
"""
import math
num=float(input("Enter number: "))
if num>0:
    print("The number is positive")
if num<0:
    print("The number is negative")
if num==0:
    print("the number is 0")
