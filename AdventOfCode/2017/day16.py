# Written by Danny Brown on September 30, 2018
# https://adventofcode.com/2017/day/16

def main():
    dance = []
    for c in char_range('a', 'p'):
        dance.append(c)

    with open("day16input.txt") as f:
        inputs = f.read().split(",")

    for input in inputs:
        if input[0] == "s": # spin
            num = int(filter(str.isdigit, input))
            for _ in range(num):
                popper = dance.pop()
                dance.insert(0, popper)
        elif input[0] == "x": # exchange
            nums = input[1:].split("/")
            num_0, num_1 = int(nums[0]), int(nums[1])
            dance[num_0], dance[num_1] = dance[num_1], dance[num_0]
        elif input[0] == "p": # partner
            progs = input[1:].split("/")
            num_0 = dance.index(progs[0])
            num_1 = dance.index(progs[1])
            dance[num_0], dance[num_1] = dance[num_1], dance[num_0]

    string_dance = ''.join(dance)
    print string_dance

def char_range(c1, c2):
    # Generates the characters from `c1` to `c2`, inclusive.
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)


if __name__ == '__main__':
    main()
