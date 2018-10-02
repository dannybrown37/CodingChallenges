# -*- coding: cp1252 -*-
# Practice Python
# Beginner Python Exercises
# Exercise 14
# Written by Danny Brown on November 25, 2017
# http://www.practicepython.org/exercise/2014/05/15/14-list-remove-
# duplicates.html
"""
Write a program (function!) that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates.
Extras:
Write two different functions to do this - one using a loop and constructing
a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a
different function.
"""
import random

def generateList():
    newList = []
    for x in range(random.randint(50,100)):
        newList.append(random.randint(1, 100))
    return newList

def removeDupes(lst):
    noDupes = []
    for num in lst:
        if num in lst and num not in noDupes:
            noDupes.append(num)
    return noDupes

# Main
withDupes = generateList()
print "Here's a randomly generated list:"
print withDupes
dupesGone = removeDupes(withDupes)
print "And here's the same list with all duplicates removed:"
print dupesGone

passWords = ["dinosaur", "puppy", "kisses", "angel", "demon", "scimitar",
             "sword", "magic", "airplane", "boat", "car", "face", "camel",
             "elephant", "donkey", "horse", "tapir", "noble", "steed",
             "baby", "cute", "demon", "laughter", "monkey", "elf", "skill",
             "angle", "square", "rectangle", "triangle", "circle", "fork",
             "pentagon", "lion", "hyena", "tiger", "bear", "redhead",
             "blonde", "brunette", "kangaroo", "piglet", "fox", "bunny",
             "rabbit", "grotto", "old", "young", "love", "bagel", "plate",
             "chicken", "viola", "spicy", "butter", "oil", "leaf", "plant",
             "noodle", "soup", "rainbow", "gay", "bland", "flavorful", 
             "sweet", "trumpet", "guitar", "bugle", "cello", "violin", 
             "trombone", "cry", "lennon", "mccartney", "harrison", "star",
             "piano", "ukulele", "boxer", "fighter", "trade", "carry", 
             "reminder", "blimp", "blame", "military", "tank", "bomb", 
             "every", "fake", "nonfiction", "book", "spa", "web", "shed",
             "glove", "laid", "down", "cut", "cried", "anger", "shame", 
             "leaving", "remains", "southern", "red", "fiction", "news",
             "changes", "still", "same", "bus", "truck", "bangle", "tangle",
             "south", "leaves", "crumble", "wind", "air", "fire", "water",
             "park", "central", "northern", "western", "eastern", "pulp"
             "chef", "poor", "rich", "token", "black", "white", "brown", 
             "yellow", "random", "computer", "memory", "manifesto", "box",
             "blue", "purple", "pink", "brown", "glove", "bat", "ball",
             "net", "hoop", "hole", "goal", "microphone", "soda", "pop",
             "soft", "hard", "hops", "mild", "barley", "gangster", "rap",
             "sharp", "sour", "bitter", "crazy", "spoon", "banner", "ska",
             "shingle", "beam", "wall", "panda", "grizzly", "polar", "hog"]

passWordsRevised = removeDupes(passWords)
print passWords
print passWordsRevised
