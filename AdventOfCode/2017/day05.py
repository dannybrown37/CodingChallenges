# Advent of Code
# Day 5 Parts 1 and 2, Written on December 7, 2017 (whomp whomp), by Danny Brown

# The instructions are kind of complex on this one. They involve traversing a
# maze based on particular criteria.
# See more here: http://adventofcode.com/2017/day/5

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def make_list_from_file():
    newList = []
    maze = open("day05input.txt")
    size = file_len("day05input.txt")
    for _ in range(size):
        line = maze.readline()
        newList.append(int(line))
    return newList

def traverse_the_maze(maze):
    index = 0 
    steps = 0
    while index < len(maze):
        steps += 1
        maze[index] += 1
        index += maze[index]-1
    return steps

def traverse_the_maze_part_two(maze):
    index = 0 
    steps = 0
    while index < len(maze):
        steps += 1
        if maze[index] >= 3:
            maze[index] -= 1
            index += maze[index]+1
        else:
            maze[index] += 1
            index += maze[index]-1
    return steps

# Main
maze = make_list_from_file()
steps = traverse_the_maze(maze)
print "Part one answer: " + str(steps)

maze = make_list_from_file()
steps = traverse_the_maze_part_two(maze)
print "Part two answer: " + str(steps)
