# -*- coding: cp1252 -*-
# Practice Python
# Beginner Python Exercises
# Exercise 13
# Written by Danny Brown on November 25, 2017
# http://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
"""
Write a program that asks the user how many Fibonnaci numbers to generate
and then generates them. Take this opportunity to think about how you can
use functions. Make sure to ask the user to enter the number of numbers in
the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers
where the next number in the sequence is the sum of the previous two numbers
in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""
fibonacci = []
current = 1
last = 1
places = int(input("How many Fibonacci numbers shall I print? "))
for x in range(places):
    fibonacci.append(current)
    last = current - last
    current += last
print "Here's a list of the Fibonacci numbers you selected."
print fibonacci
