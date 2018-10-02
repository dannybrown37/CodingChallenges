# -*- coding: cp1252 -*-
# Practice Python
# Beginner Python Exercises
# Exercise 7
# Written by Danny Brown on November 23, 2017
# http://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
"""
Let’s say I give you a list saved in a variable:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has
only the even elements of this list in it.
"""

import random

def generateList():
    # The xrange parameter returns random numbers from 1 to 99 with no duplicates
    # The second parameter provides the the number of list elements, randomized here
    randomList = random.sample(xrange(100), random.randint(5, 50)) 
    return randomList

# Main
randomList = generateList()
print randomList

# This prints the elements whose values are even
evenElements = [i for i in randomList if i % 2 == 0]
print evenElements

# This prints every other element in the list, starting with the second
evenElements = [i for i in randomList[1::2]]
print evenElements
