# -*- coding: cp1252 -*-
# Practice Python
# Beginner Python Exercises
# Exercise 18
# Written by Danny Brown on November 27, 2017
# http://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html
"""
Create a program that will play the “cows and bulls” game with the user.
The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place, they
have a “cow”. For every digit the user guessed correctly in the wrong place is
a “bull.” Every time the user makes a guess, tell them how many “cows” and
“bulls” they have. Once the user guesses the correct number, the game is over.
Keep track of the number of guesses the user makes throughout teh game and tell
the user at the end.
"""

import random, re

# Function Definitions
def validateDifficulty():
    while True:
        try:
            nd = str(raw_input("Select a difficulty between 2 and 9: "))
        except ValueError:
            print "That's not a valid value. ", 
            continue
        if nd != "2" and nd != "3" and nd != "4" and nd != "5" and nd != "6" \
           and nd != "7" and nd != "8" and nd != "9":
            print "That's not a valid value. ", 
            continue
        else:
            return int(nd)  

def generateBoard(gameDiff):
    newBoard = []
    for x in range(4):
        newBoard.append(random.randint(1, gameDiff))
    return newBoard

def guessFunc(diff):
    guess = str(input(": ")) # accepts guess in format like '1234'
    while not re.match("[1-" + str(diff) + "][1-" + str(diff) + "][1-" + \
                       str(diff) + "][1-" + str(diff) + "]", guess) \
                       or len(guess) != 4: # validates guess
        guess = str(input("No. Guess exactly four numerals between 1 and " \
                          + str(diff) +":\n > "))
    transformedGuess = list(guess) # Example: ['1', '2', '3', '4']
    transformedGuess = list(map(int, transformedGuess)) # Example: [1, 2, 3, 4]
    return transformedGuess 

def compareLists(list1, list2):
    matchCount = 0
    almostCount = 0
    remaining_list1 = []
    remaining_list2 = []
    for index in range(4):
        if list2[index] == list1[index]:
            matchCount += 1
        else:
            remaining_list1.append(list1[index])
            remaining_list2.append(list2[index])
    for num in remaining_list1:
        if num in remaining_list2:
            almostCount += 1
            remaining_list2.remove(num)
    print " *" * matchCount
    print " $" * almostCount
    if matchCount == 4:
        print "\n\nYou win!"
        print "The board was: ", 
        print board 
        return True
    else:
        print
        return False        

# Main
diff = validateDifficulty()
board = generateBoard(diff)

print "\n*****************************INSTRUCTIONS*****************************"
print "You are guessing four numbers in order ranging from 1 to " + str(diff) + "."
print "The * symbols indicate how many of your numbers are placed correctly."
print "The $ symbols indicate correct numbers placed in an incorrect position."
print "You will have 10 guesses before you lose. Guess right to win!"
print "Format your guesses like this: 1231. Duplicates are possible."
print "**********************************************************************\n"

guessCount = 0
winner = False

while winner == False:
    guessCount += 1
    if guessCount > 10:
        print "You lose!"
        print "The board was: ", 
        print board
        break
    print "Guess #" + str(guessCount), 
    guessList = guessFunc(diff)
    winner = compareLists(board, guessList)
