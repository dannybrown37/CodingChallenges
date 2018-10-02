# Advent of Code 2015, Written by Danny Brown in December 2017 (whomp whomp)

inputfile = open("day01.txt")
steps = inputfile.read()
floor = 0

for index, char in enumerate(steps):
    if char is "(":
        floor += 1
    elif char is ")":
        floor -= 1
        if floor is -1:
            print index + 1

print floor

