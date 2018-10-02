# Advent of Code
# Day 4 Parts 1 and 2, Written on December 7, 2017 (whomp whomp), by Danny Brown

# This program tests strings with multiple words to check if any duplicate words
# appear in the string. It returns the number of strings without duplicates.

# File input name: "day04input.txt"

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def check_password_for_repeat_words():
    line = password.readline()
    line = line.split()
    return len(line) != len(set(line))

def check_password_for_repeat_words(sortedLine):
    return len(sortedLine) != len(set(sortedLine))

def check_whole_file():
    valids = 0
    rows = file_len("day04input.txt")
    for _ in range(rows):
        result = check_password_for_repeat_words()
        if result == True:
            pass
        elif result == False:
            valids += 1
    return valids

# Part 2 functions
def check_password_for_anagrams():
    valids = 0
    line = password.readline()
    line = line.split()
    sortedLine = []
    for word in line:
        word = ''.join(sorted(word))
        sortedLine.append(word)
    result = check_password_for_repeat_words(sortedLine)
    return result

def check_all_passwords_for_anagrams():
    valids = 0
    rows = file_len("day04input.txt")
    for _ in range(rows):
        result = check_password_for_anagrams()
        if result == True:
            pass
        elif result == False:
            valids += 1
    return valids
        
# Main
password = open("day04input.txt", "r")

result = check_all_passwords_for_anagrams()
print result


    

