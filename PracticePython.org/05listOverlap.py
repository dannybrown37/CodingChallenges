# -*- coding: cp1252 -*-
# Practice Python
# Beginner Python Exercises
# Exercise 5
# Written by Danny Brown on November 23, 2017
# http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
"""
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates). Make sure your
program works on two lists of different sizes.
Extras:
Randomly generate two lists to test this
Write this in one line of Python
(don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""
import random

def generateList():
    # The xrange parameter returns random numbers from 1 to 99 with no duplicates
    # The second parameter provides the the number of list elements, randomized here
    randomList = random.sample(xrange(100), random.randint(5, 50)) 
    return randomList

def compareLists(list1, list2):
    commonList = []
    for num1 in list1:
        for num2 in list2:
            if num2 == num1:
                commonList.append(num1)
    return commonList

# Main
list1 = generateList()
list2 = generateList()
print "First randomly generated list: "
print list1
print "Second randomly generated list: "
print list2
commonList = compareLists(list1, list2)
print "Common numbers between the two lists: "
print commonList
        
# List comprehension solution
oneLine = []
oneLine = [list1[i] for i in range(0, len(list1)) if (list1[i] not in \
           oneLine and list1[i] in list2)] # cheater, it's two lines :)
print "Here's the operation using just one line of code: "
print oneLine
