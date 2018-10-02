# Practice Python
# Beginner Python Exercises
# Exercise 1
# Written by Danny Brown on November 23, 2017
# http://www.practicepython.org/exercise/2014/01/29/01-character-input.html
"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they
will turn 100 years old.
Add on to the previous program by asking the user for another number and
printing out that many copies of the previous message.
(Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button)
"""

import datetime

now = datetime.datetime.now()

userName = str(raw_input("What is your name? "))
userAge = int(raw_input("What is your age after your birthday this year? "))
year100 = 100 - userAge + now.year

print "Hello, " + userName + "! You will turn 100 in " + str(year100) + "."

timesToPrint = int(raw_input("Select a number of times to print the message. "))

for x in range(timesToPrint):
    print "Hello, " + userName + "! You will turn 100 in " + str(year100) + "."
