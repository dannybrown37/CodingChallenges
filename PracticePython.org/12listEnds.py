# -*- coding: cp1252 -*-
# Practice Python
# Beginner Python Exercises
# Exercise 12
# Written by Danny Brown on November 24, 2017
# http://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
"""
Write a program that takes a list of numbers (for example,
a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
"""

import random

def generateList():
    randomList = random.sample(xrange(100), random.randint(5, 50))
    return randomList

def alphaAndOmega(list):
    firstLast = []
    active = list[0]
    firstLast.append(active)
    active = list[len(list) -1]
    firstLast.append(active)
    return firstLast

# Main
newList = generateList()
print newList
firstAndLast = alphaAndOmega(newList)
print firstAndLast
