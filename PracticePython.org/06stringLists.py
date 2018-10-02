# -*- coding: cp1252 -*-
# Practice Python
# Beginner Python Exercises
# Exercise 6
# Written by Danny Brown on November 23, 2017
# http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
"""
Ask the user for a string and print out whether this string is a palindrome
or not. (A palindrome is a string that reads the same forwards and backwards.)
"""
def isPalindrome(test):
    test = test.lower()
    noSpaces = ""
    for letter in test:
        if letter != ' ' and letter.isalpha() == True or \
           letter.isdigit() == True:
            noSpaces += letter
    size = len(noSpaces)
    substring1 = noSpaces[0:size/2]
    if size % 2 == 1:
        substring2 = noSpaces[size-1:size/2:-1]
    elif size % 2 == 0:
        substring2 = noSpaces[size-1:size/2-1:-1]
    if substring1 == substring2:
        return True
    else:
        return False

def goAgain():
    againQ = str(raw_input("Go again? (enter Q to quit):"))
    if againQ == "q" or againQ == "Q" or againQ == "0" or againQ == "quit":
        return False
    else:
        return True
    
# Main
print "This program takes a statement and says whether it is a palindrome."
print "It ignores spaces, so the statement \"a but tuba\" would return true."
print "It also ignores capitilization and punctuation. Have fun! "
whatIsIt = False
again = True
while again == True:
    palTest = str(raw_input("Please enter a statement: "))
    whatIsIt = isPalindrome(palTest)
    print "It's a palindrome!" if whatIsIt == True else "It's not a palindrome!"
    again = goAgain()
