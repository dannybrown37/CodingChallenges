# -*- coding: cp1252 -*-
# Practice Python
# Beginner Python Exercises
# Exercise 23
# Written by Danny Brown on December 6, 2017
# http://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html
"""
Given two .txt files that have lists of numbers in them, find the numbers
that are overlapping. One .txt file has a list of all prime numbers under
1000, and the other .txt file has a list of happy numbers up to 1000.
(If you forgot, prime numbers are numbers that can’t be divided by any
other number. And yes, happy numbers are a real thing in mathematics - you
can look it up on Wikipedia. The explanation is easier with an example,
which I will describe below.)
"""
# .txt file with prime numbers  is named "23primenumbers.txt"
# .txt file with happy numers is named "23happynumbers.txt"

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def return_array(numbersFile, size):
    workingArray = []
    workingFile = open(numbersFile, "r")
    for line in range(0, size):
        line = workingFile.readline()
        workingArray.append(int(line))
    return workingArray
        
# Main
primes = []
happys = []
inBoth = []

primeFile = "23primenumbers.txt"
happyFile = "23happynumbers.txt"

primeLength = file_len("23primenumbers.txt")
happyLength = file_len("23happynumbers.txt")

primes = return_array(primeFile, primeLength)
happys = return_array(happyFile, happyLength)

inBoth = [primes[i] for i in range(0, len(primes)) if (primes[i] not in \
          inBoth and primes[i] in happys)]
print inBoth
