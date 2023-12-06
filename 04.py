import re
from collections import defaultdict, deque
from itertools import count


test = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]

with open("04.txt") as f:
    data = [line.rstrip("\n") for line in f.readlines()]


def one(input=data):
    total = 0
    for line in input:
        game_total = 0
        past_winning = False
        winning_nums = set()
        nums = line.split(" ")[2:]
        for num in nums:
            if num == "":
                continue
            if num == "|":
                past_winning = True
            elif past_winning:
                if num in winning_nums:
                    if game_total == 0:
                        game_total = 1
                    else:
                        game_total *= 2
            else:
                winning_nums.add(num)
        total += game_total
    return total


def two(input=data):
    copies = {}

    for i, line in enumerate(input):
        if i not in copies:
            copies[i] = 1
        game_total = 0
        past_winning = False
        winning_nums = set()
        nums = line.split(" ")[2:]
        for num in nums:
            if num == "":
                continue
            if num == "|":
                past_winning = True
            elif past_winning:
                if num in winning_nums:
                    game_total += 1
            else:
                winning_nums.add(num)
        for num in range(1, game_total + 1):
            if i + num not in copies:
                copies[i + num] = 1 + copies[i]
            else:
                copies[i + num] += copies[i]
    return f"total: {sum(copies.values())}"


print(one())

print(two())
