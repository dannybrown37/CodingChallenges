# -*- coding: cp1252 -*-
# Practice Python
# Beginner Python Exercises
# Exercise 4
# Written by Danny Brown on November 23, 2017
# http://www.practicepython.org/exercise/2014/02/26/04-divisors.html
"""
Create a program that asks the user for a number and then prints out a list of
all the divisors of that number. (If you don’t know what a divisor is, it is a
number that divides evenly into another number. For example, 13 is a divisor of
26 because 26 / 13 has no remainder.)
"""

def newDivisorList(userNumber, userRange):
    divisorList = []
    for num in userRange:
        if userNumber % num == 0:
            divisorList.append(num)
    print divisorList

# Main    
keepGoing = True
while keepGoing == True:
    userNumber = int(input("Select a number and I will tell you all divisors for it: "))
    userRange = range(2, userNumber)
    newDivisorList(userNumber, userRange)
    keepGoing = str(raw_input("Keep going? (y/n): "))
    if keepGoing == "n" or keepGoing == "N" or keepGoing == "0" or keepGoing == "no":
        keepGoing = False
    else:
        keepGoing = True
