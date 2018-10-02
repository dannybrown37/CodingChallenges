# Practice Python
# Beginner Python Exercises
# Exercise 3
# Written by Danny Brown on November 23, 2017
# http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
"""
Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
Extras:
Instead of printing the elements one by one, make a new list that has all the elements
less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the original
list a that are smaller than that number given by the user.
"""

import random

def generateList(givenLimit):
    randomList = []
    numberOfElements = int(input("How many random numbers would you like to generate? "))
    for num in range(numberOfElements):
        randomList.append(random.randint(1, givenLimit))
    return randomList

def printBelow(list, limit):
    for x in list:
        if x < limit:
            print x

def genNewList(list, limit):
    newList = []
    for x in list:
        if x < limit:
            newList.append(x)
    print newList

# Main
print "This program will randomly generate a list of between 1 and 100 numbers."
userLimit = int(input("Please choose an upper limit for the generated numbers. "))

workingList = generateList(userLimit)

print "The randomly generated list is:"
print workingList

print "Now we will print all numbers from the list less than a number you select. "
newLimit = int(input("Print all numbers below...? "))

print "First, we'll print the numbers individually: "
printBelow(workingList, newLimit)
print "Next, we'll generate a new list of the relevant numbers and print that: "
genNewList(workingList, newLimit)
print "And now we'll do it all in a single line of code: "
print([element for element in workingList if element < newLimit])
