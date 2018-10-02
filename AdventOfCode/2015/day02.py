# Advent of Code 2015, Written by Danny Brown in December 2017 (whomp whomp)

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def paper_calculator():
    inputfile = open("day02.txt")
    totalPaperNeeded = 0
    for _ in range(file_len("day02.txt")):
        line = inputfile.readline().split('x')
        paperNeeded = (2 * int(line[0]) * int(line[1])) + \
                      (2 * int(line[1]) * int(line[2])) + \
                      (2 * int(line[2]) * int(line[0]))
        paperNeeded += min(int(line[0]) * int(line[1]), \
                           int(line[1]) * int(line[2]), \
                           int(line[2]) * int(line[0]))
        totalPaperNeeded += paperNeeded
    inputfile.close()
    return totalPaperNeeded

def ribbon_calculator():
    inputfile = open("day02.txt")
    totalRibbonNeeded = 0
    for _ in range(file_len("day02.txt")):
        line = inputfile.readline().split('x')
        ribbonNeeded = min((2 * int(line[0])) + (2 * int(line[1])), \
                           (2 * int(line[1])) + (2 * int(line[2])), \
                           (2 * int(line[2])) + (2 * int(line[0])))
        ribbonNeeded += int(line[0]) * int(line[1]) * int(line[2])
        totalRibbonNeeded += ribbonNeeded
    return totalRibbonNeeded

def main():
    partOne = paper_calculator()
    print partOne

    partTwo = ribbon_calculator()
    print partTwo

main()
