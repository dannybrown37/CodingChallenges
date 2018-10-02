# -*- coding: cp1252 -*-
# Practice Python
# Beginner Python Exercises
# Exercise 11
# Written by Danny Brown on November 24, 2017
# http://www.practicepython.org/exercise/2014/04/16/11-check-primality
# -functions.html
"""
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.)
You can (and should!) use your answer to Exercise 4 to help you. Take this
opportunity to practice using functions, described below.
"""

def newDivisorList(userNumber, userRange):
    divisorList = []
    for num in userRange:
        if userNumber % num == 0:
            divisorList.append(num)
    return divisorList

def keepGoingOrNot():
    keepGoing = str(raw_input("Keep going? (enter Q to quit): "))
    if keepGoing == "q" or keepGoing == "Q" or keepGoing == "0":
        return False
    else:
        return True

# Main    
keepGoing = True
while keepGoing == True:
    userNumber = int(input("Enter a number; I will tell you if it is prime: "))
    userRange = range(2, userNumber)
    divisors = newDivisorList(userNumber, userRange)
    if not divisors:
        print "The number is PRIME!"
    else:
        print "The number is NOT PRIME!"
    keepGoing = keepGoingOrNot()
