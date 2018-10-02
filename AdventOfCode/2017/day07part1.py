# Advent of Code
# Day 7 Part 1, Written on December 9, 2017 (whomp whomp), by Danny Brown

# http://adventofcode.com/2017/day/7 This program does what the site describes.

# puzzle input file "day07input.txt"
# working input file "day07inputsample.txt"

import numpy

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def line_parser(line):
    leftProg = ""
    rightProg = ""
    # Get left program to return
    for char in line:
        if char == " ":
            break
        leftProg += char
    # Get right programs and append to global array
    spaces = 0
    for char in line:
        if char == " ":
            spaces += 1
        if spaces >= 3 and char.isalpha():
            rightProg += char
        if char == "," or char == "\n" and rightProg != "":
            rightPrograms.append(rightProg)
            rightProg = ""
    return leftProg

def compare_left_and_right(left, right):
    notInRight = numpy.setdiff1d(left, right)
    print notInRight
    
# Main
leftPrograms = []
rightPrograms = []
size = file_len("day07input.txt")
disc = open("day07input.txt")

for _ in range(size):
    line = disc.readline()
    lefty = line_parser(line)
    leftPrograms.append(lefty)

compare_left_and_right(leftPrograms, rightPrograms)
