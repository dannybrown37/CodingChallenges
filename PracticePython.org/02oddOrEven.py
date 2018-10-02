# Practice Python
# Beginner Python Exercises
# Exercise 2
# Written by Danny Brown on November 23, 2017
# http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
"""
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. Hint: how does an even / odd
number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one
number to divide by (check). If check divides evenly into num, tell that
to the user. If not, print a different appropriate message.
"""
keepPlaying = True
while keepPlaying == True:
    userNumber = int(input("Enter a number: "))
    userDivisor = int(input("Enter a divisor: "))
    if userNumber % userDivisor == 0:
        print "Your first number divides by your second number evenly. "
    if userNumber % userDivisor >= 1:
        print "Dividing your first number by your second number leaves " \
              "you with a remainder of " + str(userNumber % userDivisor) \
              + "."
    keepPlaying = str(input("Keep playing? (y/n): "))
    if keepPlaying == "n" or keepPlaying == "N" or keepPlaying == "0":
        keepPlaying = False
        print "Goodbye!"
    else:
        keepPlaying = True
