import re
from collections import defaultdict, deque
from itertools import count


test = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]

with open("03.txt") as f:
    data = [line.rstrip("\n") for line in f.readlines()]


def one(input=data):
    rows = len(input)
    cols = len(input[0])

    symbols = set()
    for i in range(rows):
        for j in range(len(input[i])):
            if not input[i][j].isnumeric() and input[i][j] != ".":
                symbols.add((i, j))

    def is_valid(x, y, length):
        y = y - length + 1
        dirs = (-1, 0, 1)
        for z in range(length):
            for i in dirs:
                for j in dirs:
                    if (x + i, y + j + z) in symbols:
                        return True
        return False

    total = 0

    for i in range(rows):
        curr_num = ""
        for j in range(cols):
            if input[i][j].isnumeric():
                curr_num += input[i][j]
                if j == cols - 1 or not input[i][j + 1].isnumeric():
                    if is_valid(i, j, len(curr_num)):
                        total += int(curr_num)
                    curr_num = ""
    return f"total: {total}"


def two(input=data):
    rows = len(input)
    cols = len(input[0])

    def get_ratio(x, y):
        dirs = (-1, 0, 1)
        nums = []
        seen = set()
        for i in dirs:
            for j in dirs:
                a = x + i
                b = y + j
                if input[a][b].isnumeric() and (a, b) not in seen:
                    seen.add((a, b))
                    num = input[a][b]
                    l = b - 1
                    while l >= 0 and input[a][l].isnumeric():
                        # print("left", num)
                        seen.add((a, l))
                        num = input[a][l] + num
                        l -= 1
                    r = b + 1
                    while r < cols and input[a][r].isnumeric():
                        # print("right", num)
                        seen.add((a, r))
                        num += input[a][r]
                        r += 1
                    nums.append(num)
        if len(nums) == 2:
            return int(nums[0]) * int(nums[1])
        return 0

    total = 0

    for i in range(rows):
        for j in range(cols):
            if input[i][j] == "*":
                total += get_ratio(i, j)
    return f"total: {total}"


# print(one(test))
print(one(data))

# print(two(test))
print(two())
