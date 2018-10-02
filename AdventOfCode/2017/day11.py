# Advent of Code
# Day 11 Part 1, Written/stolen on December 11 and 12, 2017, by Danny Brown

# http://adventofcode.com/2017/day/11 This program does what the site describes.

# input file name = "day11input.txt"

# Interesting resource: https://www.redblobgames.com/grids/hexagons/
# Studied a lot of solutions on Reddit too
# https://www.reddit.com/r/adventofcode/comments/7izym2/2017_day_11_solutions/

def main():
    f = open("day11input.txt", "r")
    directions = f.read().split(",")

    x = 0
    y = 0
    z = 0

    dists = []

    for move in directions:
      if move == "n":
        y += 1
        z -= 1
      elif move == "s":
        y -= 1
        z += 1        
      elif move == "ne":
        x += 1
        z -= 1
      elif move == "sw":
        x -= 1
        z += 1
      elif move == "nw":
        x -= 1
        y += 1
      elif move == "se":
        x += 1
        y -= 1
      dists.append((abs(x) + abs(y) + abs(z)) / 2)

    print (abs(x) + abs(y) + abs(z)) / 2
    print max(dists)

main()
 
"""
I guess this isn't needed? Cool way to create a dictionary with the names
and values, though, so I'm saving it here.

def direction_counter(directions):
    directory = {}
    direction = ""
    for letter in directions:
        if letter.isalpha():
            direction += letter
        if letter is ",":
            if direction not in directory.keys():
                directory[direction] = 1
                direction = ""
            else:
                directory[direction] += 1
                direction = ""
    return directory
"""
