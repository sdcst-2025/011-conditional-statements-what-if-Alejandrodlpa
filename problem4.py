#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# has a percent difference less than 2%
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle" below min
# - "that is an obtuse triangle" over max
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle
"""
import math 
a=float(input("first number: "))
b=float(input("second number: "))
c=float(input("last number: "))
if a>b>c:
    hyp=a
    mid=b
    small=c
if a>c>b:
    hyp=a
    mid=c
    small=b
if b>a>c:
    hyp=b
    mid=a
    small=c
if b>c>a:
    hyp=b
    mid=c
    small=a
if c>a>b:
    hyp=c 
    mid=a
    small=b
if c>b>a:
    hyp=c
    mid=b
    small=a
truehyp=((mid**2+small**2)**(1/2))
lowThyp=truehyp*.98
highThyp=truehyp*1.02

if hyp==truehyp:
    print("that is a right triangle")

if hyp<=lowThyp:
    print("That is a acute triangle")

if hyp>=highThyp:
    print("That is a obtuse triangle")
    