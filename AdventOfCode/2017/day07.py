# Advent of Code
# Day 7 Part 1, Written on December 9, 2017 (whomp whomp), by Danny Brown

# http://adventofcode.com/2017/day/7 This program does what the site describes.

# puzzle input file "day07input.txt"
# working input file "day07inputsample.txt"

import numpy

def part_one():
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

# Advent of Code
# Day 7 Part 2, Written on December 12, 2017 (whomp whomp), by Danny Brown

# http://adventofcode.com/2017/day/7 This program does what the site describes.

# puzzle input file "day07input.txt"
# working input file "day07inputsample.txt"


def part_two(): # THIS DOESN'T WORK YET!
    def file_len(fname):
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        return i + 1

    def line_parser(line):
        leftProg = ""
        weight = ""
        # Get left program and weight to return
        for char in line:
            if char == " ":
                break
            leftProg += char
        for char in line:
            if char.isdigit():
                weight += char
            elif char is ")":
                break
        # Dictionary time
        progWeights[leftProg] = int(weight)

    def weight_adder(line):
        leftProg = ""
        rightProg = ""
        rightPrograms = []
        spaces = 0
        total = 0
        if "->" in line:
            for char in line:
                if char == " ":
                    spaces += 1
                if spaces == 0 and char.isalpha():
                    leftProg += char
                if char == "(":
                    leftProgramsWithStacks[leftProg] = []
                if spaces >= 3 and char.isalpha():
                    rightProg += char
                if char == "," or char == "\n" and rightProg != "":
                    rightPrograms.append(rightProg)
                    rightProg = ""
            total += progWeights[leftProg]
            for prog in rightPrograms:
                total += progWeights[prog]
                leftProgramsWithStacks[leftProg].append(prog)
        addedWeights[leftProg] = total


    # Main
    bottomProgram = "tknk" # We got this answer in part 1
    addedWeights = {}
    progWeights = {}
    leftProgramsWithStacks = {}
    fileName = "day07inputsample.txt"
    size = file_len(fileName)
    disc = open(fileName, "r")

    for _ in range(size):
        line = disc.readline()
        line_parser(line)
    print progWeights

    disc.close()
    disc = open(fileName, "r")

    for _ in range(size):
        line = disc.readline()
        weight_adder(line)
    addedWeights.pop('', None)
    print addedWeights
    print leftProgramsWithStacks

    disc.close()
    disc = open(fileName, "r")

    for holderProg, heldProgs in leftProgramsWithStacks.iteritems():
        for prog in heldProgs:
            print prog + str(progWeights[prog])


part_one()
part_two()
