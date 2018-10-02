# -*- coding: cp1252 -*-
# Practice Python
# Beginner Python Exercises
# Exercise 22
# Written by Danny Brown on December 3, 2017
# http://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html
"""
Given a .txt file that has a list of a bunch of names, count how many of each
name there are in the file, and print out the results to the screen. I have a
.txt file for you, if you want to use it!
Extra:
Instead of using the .txt file from above (or instead of, if you want the
challenge), take this .txt file, and count how many of each “category” of
each image there are. This text file is actually a list of files corresponding
to the SUN database scene recognition database, and lists the file directory
hierarchy for the images. Once you take a look at the first line or two of the
file, it will be clear which part represents the scene category. To do this,
you’re going to have to remember a bit about string parsing in Python 3. I
talked a little bit about it in this post.
"""

# .txt file with SUN database is named "22sundata.txt"

# Shamelessly stole this function from https://stackoverflow.com/\
# questions/845058/how-to-get-line-count-cheaply-in-python
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

# Main is all original code, though

fileLength = file_len("22sundata.txt")
sun = open("22sundata.txt", "r")
categoryCounts = {}

for line in range(0, fileLength):
    category = ""
    line = sun.readline()
    for letter in range(3,len(line)):
        if line[letter] == "/":
            break
        else:
            category += line[letter]
    if category in categoryCounts.keys():
        categoryCounts[category] += 1
    else:
        categoryCounts[category] = 1

for key,value in sorted(categoryCounts.items()):
    print key + ": " + str(value)
