# PracticePython.org, Exercise #24, written by Danny Brown on 12/15/2017
# http://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html

def generate_board(width, height):
    print " ---" * width
    for _ in range(height):        
        print "|   " * width + "|"
        print " ---" * width
    
def main():
    width = int(raw_input("How many tiles wide do you want your game board? "))
    height = int(raw_input("How many tiles tall do you want your game board? "))
    generate_board(width, height)

main()
