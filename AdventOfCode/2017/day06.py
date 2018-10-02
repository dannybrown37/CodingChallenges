# Advent of Code
# Day 6 Parts 1 and 2, Written on December 7, 2017 (whomp whomp), by Danny Brown

# This program reallocates data from memory blocks and counts how many
# iterations until we end up with equal values to a previous iteration.
# For details, see: http://adventofcode.com/2017/day/6

def reallocation_cycle(data):
    listy = data[:]
    highest = -1
    for index, num in enumerate(listy):
        if num > highest:
            highest = num
            highIndex = index
    distribute = highest
    listy[highIndex] = 0
    while distribute > 0:
        for _ in range(highest):
            highIndex += 1
            distribute -= 1
            if highIndex == len(listy):
                highIndex = 0
            listy[highIndex] += 1
    return listy

def iterate_reallocations(data):
    allIterations = []
    allIterations.append(data)
    count = 1
    current = reallocation_cycle(data)
    while current not in allIterations:
        allIterations.append(current)
        current = reallocation_cycle(current)
        count += 1
    return count

def space_between_loops(data):
    allIterations = []
    allIterations.append(data)
    count = 1
    current = reallocation_cycle(data)
    while current not in allIterations:
        allIterations.append(current)
        current = reallocation_cycle(current)
        count += 1
    return len(allIterations) - allIterations.index(current)
        
# Main
data = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]
# data = [0, 2, 7, 0]
iterations = iterate_reallocations(data)
print iterations
loopSize = space_between_loops(data)
print loopSize
