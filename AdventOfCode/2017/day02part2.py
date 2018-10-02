# Advent of Code
# Day 2 Part 2, Written on December 7, 2017 (whomp whomp), by Danny Brown

# This program takes a spreadsheet and finds the only two numbers in each
# line that evenly divide into each other. It takes the results of this division
# for each row and adds them, returning the result. 

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
    
    

