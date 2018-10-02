# PracticePython.org, Exercise #25, written by Danny Brown on 12/15/2017
# http://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html

def guessing_game(theList):
    left = 0
    right = len(theList) - 1    
    answerFound = False
    guesses = 0
    print "Use these numbers to answer my questions: "
    print "1. Too high "
    print "2. Too low "
    print "3. You got it! "
    while not answerFound:
        guesses += 1
        if left > right:
            answerFound = True
            print "Something has gone horribly wrong." 
        middle = int((left + right) / 2)
        print "Is your number " + str(theList[middle]) + "?"
        answer = int(raw_input("Drumroll(1, 2, or 3): "))
        if answer == 1:
            left = middle - 1
        elif answer == 2:
            right = middle + 1
        elif answer == 3:
            answerFound = True
            print "You're god damn right I did!"
            print "And it only took me " + str(guesses) + " guesses. "
            
def main():
    print "Think of a number between 1 and 100. I will guess it. "
    theList = range(1, 101)
    guessing_game(theList)

main()





