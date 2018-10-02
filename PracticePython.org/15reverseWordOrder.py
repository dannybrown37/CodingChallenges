# -*- coding: cp1252 -*-
# Practice Python
# Beginner Python Exercises
# Exercise 15
# Written by Danny Brown on November 25, 2017
# http://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
"""
Write a program (using functions!) that asks the user for a long string
containing multiple words. Print back to the user the same string, except
with the words in backwards order. For example, say I type the string:
  My name is Michele
Then I would see the string:
  Michele is name My
shown back to me.
"""

def reverseWordsInString(str):
    workingList = str.split(" ")
    newString = ""
    for word in reversed(workingList):
        newString += word + " "
    return newString

# Main
again = True
prompt = "Please enter a string with multiple words (or Q to quit):\n> "
while again == True:
    userString = str(raw_input(prompt))
    if userString == "q" or userString == "Q" or userString == "0":
        again = False
        break
    revString = reverseWordsInString(userString)
    print revString

