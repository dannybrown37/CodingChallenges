# -*- coding: cp1252 -*-
# Practice Python
# Beginner Python Exercises
# Exercise 9
# Written by Danny Brown on November 24, 2017
# http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed
too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)
Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends,
print this out.
"""

import random

wrongGuesses = 0
rightGuesses = 0
keepGoing = True

randomNum = random.randint(1, 9)

while keepGoing == True:
    userGuess = str(raw_input("Guess a number between 1 and 9 (or type exit.)"))
    if userGuess == "exit" or userGuess == "EXIT" or userGuess == "Exit":
        print "Goodbye!"
        keepGoing = False
    elif int(userGuess) == randomNum:
        print "You guessed right! The number has been reset!"
        rightGuesses += 1
        randomNum = random.randint(1,9)
    elif int(userGuess) > randomNum:
        print "Too high!"
        wrongGuesses += 1
    elif int(userGuess) < randomNum:
        print "Too low!"
        wrongGuesses += 1
    
    print str(rightGuesses) + ": Correct Guesses"
    print str(wrongGuesses) + ": Incorrect Guesses"
    print str(rightGuesses + wrongGuesses) + ": Total Guesses"
