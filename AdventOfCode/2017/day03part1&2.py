# Advent of Code
# Day 3 Parts 1 and 2, Written on December 7, 2017 (whomp whomp), by Danny Brown

# This program finds the "Manhattan distance" in a grid design (see below) from
# a given number back to 1.

# I didn't have the slightest idea how to even approach this one, so I reviewed
# some solutions at the Reddit discussion thread:
# https://www.reddit.com/r/adventofcode/comments/7h7ufl/2017_day_3_solutions/
# And tested them for my own use. 

"""
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
"""
import math
from itertools import count

test = 289326 # 419 steps

# Part 1

def side_length(number):
    side = math.ceil(math.sqrt(number))
    side = side if side % 2 != 0 else side + 1
    return side

side = side_length(test)
steps_to_reach_center_from_axis = (side-1)/2
axes = [side**2 - ((side-1) * i) - math.floor(side/2) for i in range(0, 4)]
steps_to_reach_axis_from_input = min([abs(axis - test) for axis in axes])

print(steps_to_reach_axis_from_input + steps_to_reach_center_from_axis)

# Part 2

def sum_spiral():
    a, i, j = {(0,0) : 1}, 0, 0
    for s in count(1, 2):
        for (ds, di, dj) in [(0,1,0),(0,0,-1),(1,-1,0),(1,0,1)]:
            for _ in range(s+ds):
                i += di; j += dj
                a[i,j] = sum(a.get((k,l), 0) for k in range(i-1,i+2)
                                             for l in range(j-1,j+2))
                yield a[i,j]

def part2(n):
    for x in sum_spiral():
        if x>n: return x

print part2(test)
