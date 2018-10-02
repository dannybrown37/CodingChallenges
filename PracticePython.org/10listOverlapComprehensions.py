# -*- coding: cp1252 -*-
# Practice Python
# Beginner Python Exercises
# Exercise 10
# Written by Danny Brown on November 24, 2017
# http://www.practicepython.org/exercise/2014/04/10/10-list
# -overlap-comprehensions.html
"""
This week’s exercise is going to be revisiting an old exercise (see Exercise 5),
except require the solution in a different way.
Take two lists, say for example these two:
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are
common between the lists (without duplicates). Make sure your program works on
two lists of different sizes. Write this in one line of Python using at least
one list comprehension. (Hint: Remember list comprehensions from Exercise 7).
The original formulation of this exercise said to write the solution using one
line of Python, but a few readers pointed out that this was impossible to do
without using sets that I had not yet discussed on the blog, so you can either
choose to use the original directive and read about the set command in Python
3.3, or try to implement this on your own and use at least one list
comprehension in the solution.
Extra: Randomly generate two lists to test this
"""
import random

def generateList():
    # The xrange parameter returns random numbers from 0 to 99 with no duplicates
    # The second parameter provides the the number of list elements, randomized here
    randomList = random.sample(xrange(100), random.randint(5, 50)) 
    return randomList

# Main
list1 = generateList()
list2 = generateList()
print "First randomly generated list: "
print list1
print "Second randomly generated list: "
print list2
       
# List comprehension solution
oneLine = []
oneLine = [list1[i] for i in range(0, len(list1)) if (list1[i] not in \
           oneLine and list1[i] in list2)] # cheater, it's two lines :)
print "Common numbers between the two lists: "
print oneLine
