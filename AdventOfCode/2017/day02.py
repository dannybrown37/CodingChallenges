# Advent of Code
# Day 2 Part 1, Written on December 7, 2017 (whomp whomp), by Danny Brown

# This program takes a spreadsheet and finds the difference between the largest
# and smallest numbers in each row. Spreadsheet name: "day02input.txt"

def part_one():
    def file_len(fname):
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        return i + 1

    def calculate_row():
        lowest = 1000000000000000000000
        highest = -10000000000000000000
        line = spreadsheet.readline()
        lineList = line.split()
        lineList = map(int, lineList)
        for i in range(len(lineList)):
            if lineList[i] > highest:
                highest = lineList[i]
            if lineList[i] < lowest:
                lowest = lineList[i]
        return highest - lowest

    # Main
    totalTotal = 0
    spreadsheet = open("day02input.txt")
    rows = file_len("day02input.txt")
    for row in range(0, rows):
        rowTotal = calculate_row()
        totalTotal += rowTotal
    print totalTotal

# Advent of Code
# Day 2 Part 2, Written on December 7, 2017 (whomp whomp), by Danny Brown

# This program takes a spreadsheet and finds the only two numbers in each
# line that evenly divide into each other. It takes the results of this division
# for each row and adds them, returning the result.

def part_two():
    def file_len(fname):
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        return i + 1

    def calculate_row():
        line = spreadsheet.readline()
        lineList = line.split()
        lineList = map(int, lineList)
        for i in range(len(lineList)):
            for j in range(len(lineList)):
                if lineList[i] % lineList[j] == 0 and lineList[i] != lineList[j]:
                    return lineList[i] / lineList[j]

    # Main
    totalTotal = 0
    spreadsheet = open("day02input.txt")
    rows = file_len("day02input.txt")
    for row in range(0, rows):
        rowTotal = calculate_row()
        totalTotal += rowTotal
    print totalTotal


part_one()
part_two()
