# -*- coding: cp1252 -*-
# Practice Python
# Beginner Python Exercises
# Exercise 8
# Written by Danny Brown on November 24, 2017
# http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
"""
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner, and
ask if the players want to start a new game)
Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock
"""

# I'm doing this a little differently. Instead I am going to simulate various
# strategies to test what is most likely to win. -- DB

import random

def trueRandom():
    throw = random.randint(1, 3)
    if throw == 1:
        return "rock"
    elif throw == 2:
        return "paper"
    elif throw == 3:
        return "scissors"

def testWinner(throw1, throw2):
    if throw1 == throw2:
        return "draw"
    elif throw1 == "rock" and throw2 == "paper" \
    or throw1 == "paper" and throw2 == "scissors" \
    or throw1 == "scissors" and throw2 == "rock":
        return "throw2"
    elif throw1 == "rock" and throw2 == "scissors" \
    or throw1 == "paper" and throw2 == "rock" \
    or throw1 == "scissors" and throw2 == "paper":
        return "throw1"

def alwaysRock(testSize):
    randomWins = 0
    rockWins = 0
    draws = 0
    
    for x in range(0,testSize):
        winner = testWinner(trueRandom(), "rock")
        if winner == "throw1":
            randomWins += 1
        elif winner == "throw2":
            rockWins += 1
        elif winner == "draw":
            draws += 1
    print "Results over " + str(testSize) + " simulations:"
    print str(randomWins) + ": Wins for Random Throws"  
    print str(rockWins) + ": Always Throws Rock" 
    print str(draws) + ": Draws"


def alwaysPaper(testSize):
    randomWins = 0
    paperWins = 0
    draws = 0
    
    for x in range(0,testSize):
        winner = testWinner(trueRandom(), "paper")
        if winner == "throw1":
            randomWins += 1
        elif winner == "throw2":
            paperWins += 1
        elif winner == "draw":
            draws += 1
    print "Results over " + str(testSize) + " simulations:"
    print str(randomWins) + ": Wins for Random Throws"  
    print str(paperWins) + ": Always Throws Paper" 
    print str(draws) + ": Draws"

def alwaysScissors(testSize):
    randomWins = 0
    scissorsWins = 0
    draws = 0
    
    for x in range(0,testSize):
        winner = testWinner(trueRandom(), "scissors")
        if winner == "throw1":
            randomWins += 1
        elif winner == "throw2":
            scissorsWins += 1
        elif winner == "draw":
            draws += 1
    print "Results over " + str(testSize) + " simulations:"
    print str(randomWins) + ": Wins for Random Throws"  
    print str(scissorsWins) + ": Always Throws Scissors" 
    print str(draws) + ": Draws"

def testPatternVersusRandom(testSize):

    def pattern123(lastThrow):
        if lastThrow == "rock":
            nextThrow = "paper"
        elif lastThrow == "paper":
            nextThrow = "scissors"
        elif lastThrow == "scissors":
            nextThrow = "rock"
        return nextThrow
    
    randomWins = 0
    patternWins = 0
    draws = 0
    currentThrow = "rock"

    for x in range(0,testSize):
        currentThrow = pattern123(currentThrow)
        winner = testWinner(trueRandom(), currentThrow)
        if winner == "throw1":
            randomWins += 1
        elif winner == "throw2":
            patternWins += 1
        elif winner == "draw":
            draws += 1
    print "Results over " + str(testSize) + " simulations:"
    print str(randomWins) + ": Wins for Random Throws"  
    print str(patternWins) + ": Wins Following a Strict 1-2-3 Pattern" 
    print str(draws) + ": Draws"

def lastToWinVersusRandom(testSize):
    randomWins = 0
    patternWins = 0
    draws = 0
    lastWinningThrow = "rock"

    for x in range(0,testSize):
        random = trueRandom()
        winner = testWinner(random, lastWinningThrow)
        if winner == "throw1":
            randomWins += 1
            lastWinningThrow = random
        elif winner == "throw2":
            patternWins += 1
        elif winner == "draw":
            draws += 1

    print "Results over " + str(testSize) + " simulations:"
    print str(randomWins) + ": Wins for Random Throws"  
    print str(patternWins) + ": Always Throws Last Winning Throw"
    print str(draws) + ": Draws"  

def beatsLastWinVersusRandom(testSize):
    randomWins = 0
    patternWins = 0
    draws = 0
    beatsLast = "rock"

    for x in range(0,testSize):
        random = trueRandom()
        winner = testWinner(random, beatsLast)
        if winner == "throw1" and random == "rock":
            randomWins += 1
            beatsLast = "paper"
        elif winner == "throw1" and random == "paper":
            randomWins += 1
            beatsLast = "scissors"
        elif winner == "throw1" and random == "scissors":
            randomWins += 1
            beatsLast = "rock"
        elif winner == "throw2" and random == "rock":
            patternWins += 1
            beatsLast = "scissors"
        elif winner == "throw2" and random == "scissors":
            patternWins += 1
            beatsLast = "paper"
        elif winner == "throw2" and random == "paper":
            patternWins += 1
            beatsLast = "rock"
        elif winner == "draw":
            draws += 1

    print "Results over " + str(testSize) + " simulations:"
    print str(randomWins) + ": Wins for Random Throws"  
    print str(patternWins) + ": Always Throws What Beats Last Winning Throw"
    print str(draws) + ": Draws"  

# Main

testSize = 1000000
   
testPatternVersusRandom(testSize)
print
lastToWinVersusRandom(testSize)
print
beatsLastWinVersusRandom(testSize)
print
alwaysRock(testSize)
print
alwaysPaper(testSize)
print
alwaysScissors(testSize)
print
print "Hey, cool! We can simulate a ton of rock-paper-scissors games quickly!"
