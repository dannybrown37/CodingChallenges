# Advent of Code
# Day 10 Part 2, Written on December 12, 2017 (whomp whomp), by Danny Brown

# http://adventofcode.com/2017/day/10 This program does what the site describes.

# sample input: [3, 4, 1, 5]
# test rope = [x for x in range(5)]
# actual input: [129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108]

def part_two():
    # rope = [x for x in range(256)]
    rope = [x for x in range(5)]
    rsize = len(rope)
    # wtf = "129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108"
    wtf = "3,4,1,5"
    twists = []
    for char in wtf:
        twists.append(ord(char))
    appendList = [17, 31, 73, 47, 23]
    for num in appendList:
        twists.append(num)
    print twists
    pos = 0 # current position
    skipSize = 0

    for twist in twists:
        left = []
        right = []
        if pos+twist <= rsize:
            left = rope[pos:pos+twist]
            right = rope[pos+twist:]
        elif pos+twist > rsize:
            left = rope[pos:]
            end = twist-len(left)
            left += rope[0:end]
            right = rope[end:pos]
        left = left[::-1] # reverse the left string
        if pos == 0:
            rope = []
            rope = left + right
        else:
            index = pos
            for num in left:
                if index == rsize:
                    index = 0
                rope[index] = num
                index += 1
            for num in right:
                if index == rsize:
                    index = 0
                rope[index] = num
                index += 1
        pos += twist
        pos += skipSize
        pos = pos % rsize
        skipSize += 1

    print rope[0] * rope[1]
    return rope

# Main
rope = part_two()
print rope
