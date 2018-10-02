# Advent of Code 2015, Written by Danny Brown in December 2017 (whomp whomp)

import re

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def line_parser_part_one():
    vowels = 0
    repeatChars = False
    line = inputfile.readline()    
    for c in line: # c if for char
        if c is 'a' or c is 'e' or c is 'i' or c is 'o' or c is 'u':
            vowels += 1
            if vowels > 3:
                break
    if vowels < 3:
        return False
    for index in range(len(line)-1):
        if line[index + 1] == line[index]:
            repeatChars = True
    if repeatChars == False:
        return False
    if "ab" in line or "cd" in line or "pq" in line or "xy" in line:
        return False
    return True

def part_one():      
    niceStrings = 0
    for _ in range(file_len(filename)):
        result = line_parser_part_one()
        if result == True:
            niceStrings += 1
    print "Nice strings, part one: " + str(niceStrings)

def line_parser_part_two():
    repeatCharsSplit = False
    first = False
    line = inputfile.readline()
    for index in range(len(line)-3):
        sub = line[index:index+2]
        if sub in line[index+2:]:
            first = True
    for index in range(len(line)-2):
        if line[index + 2] == line[index]:
            repeatCharsSplit = True
    if repeatCharsSplit == True and first == True:
        return True
    else:
        return False

def part_two():
    niceStrings = 0
    for _ in range(file_len(filename)):
        result = line_parser_part_two()
        if result == True:
            niceStrings += 1
    print "Nice strings, part two: " + str(niceStrings)

# Global; Part one
filename = "day05.txt"
inputfile = open(filename, "r")
part_one()
inputfile.close()

# Part two
inputfile = open(filename, "r")
part_two()
inputfile.close()
