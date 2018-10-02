# Advent of Code
# Day 8 Parts 1 and 2, Written on December 8, 2017, by Danny Brown

# http://adventofcode.com/2017/day/8 This program does what the site describes.

# input file name = "day08input.txt"
# working input file name = "day08inputsample.txt"

# Contents of "day08inputsample.txt":
# b inc 5 if a > 1
# a inc 1 if b < 5
# c dec -10 if a >= 1
# c inc -20 if c == 10

import operator

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def line_parser(line):
    spaces = 0
    conditionregname = ""
    condition = ""
    toalter = ""
    direction = ""
    amount = ""
    keyname = ""
    # This loop parses the line for all the Christmas goodies
    for char in line: 
        if char == " ":
            spaces += 1
        if spaces == 0:
            toalter += char
        elif spaces == 1:
            direction += char
        elif spaces == 2:
            amount += char
        elif spaces == 4:
            conditionregname += char
        elif spaces >= 5:
            condition += char
    # Remove all the horrid whitespace and convert to int where appropriate
    conditionregname = conditionregname.strip()
    condition = condition.strip()
    toalter = toalter.strip()
    direction = direction.strip()
    amount = int(amount.strip())
    # Add needed registers
    if conditionregname not in registry.keys(): 
        registry[conditionregname] = 0
    if toalter not in registry.keys():
        registry[toalter] = 0
    # Put it all together and test the line
    keyname = "registry[\'" + conditionregname +"\']"
    condition = keyname + condition
    if eval(condition) == True:
        if direction == "inc":
            registry[toalter] += amount
        elif direction == "dec":
            registry[toalter] -= amount
    elif eval(condition) == False:
        pass
    
# Thanks for this one, StackOverflow
# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-\
# in-dictionary
def check_for_highest_value_in_registry():
    return max(registry.iterkeys(), key=(lambda key: registry[key]))

# Main
registry = {}
highestever = -1
register = open("day08input.txt")
size = file_len("day08input.txt")

for _ in range(size):
    line = register.readline()
    line_parser(line)
    high = check_for_highest_value_in_registry()
    if registry[high] > highestever:
        highestever = registry[high]

highest = check_for_highest_value_in_registry()
print registry[highest]
print highestever
