# -*- coding: cp1252 -*-
# Practice Python
# Beginner Python Exercises
# Exercise 20
# Written by Danny Brown on December 2, 2017
# http://www.practicepython.org/exercise/2014/11/11/20-element-search.html
"""
Write a function that takes an ordered list of numbers (a list where the
elements are in order from smallest to largest) and another number. The
function decides whether or not the given number is inside the list and
returns (then prints) an appropriate boolean.
Extras: Use binary search.
"""
import random

def generateList():
    randomList = random.sample(xrange(100), random.randint(5, 50)) 
    return randomList

def generateNum():
    randomNum = random.randint(1, 100)
    return randomNum

def numInListQuestionMark(listQ, numQ):
    if numQ in listQ:
        return True
    else:
        return False

def pynarySearch(listQ, numQ):    
    answerFound = False
    listQ.sort() # Order the list first or it's all for naught!
    while answerFound == False:
        newList = []
        if len(listQ) == 1 and listQ[0] != numQ or not listQ:
            answerFound = True
            return False
        elif listQ[len(listQ)/2] == numQ:
            answerFound = True
            return True    
        elif listQ[len(listQ)/2] > numQ:
            for x in range(len(listQ)/2):
                newList.append(listQ[x])
            listQ = list(newList)
        elif listQ[len(listQ)/2] < numQ:
            for x in range(len(listQ)/2 + 1, len(listQ)):
                newList.append(listQ[x])
            listQ = list(newList)
    
# Main

testList = generateList()
testNum = generateNum()
"""
print "Is " + str(testNum) + " found in " + str(testList) + "? Let's find out."
checker = numInListQuestionMark(testList, testNum)
print checker
"""
print testList
print testNum
checker = pynarySearch(testList, testNum)
print checker
