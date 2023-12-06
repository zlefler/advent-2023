import re
from itertools import count
from collections import defaultdict, deque

test = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]

with open("02.txt") as f:
    data = f.readlines()


def one(input=data):
    maxes = {"red": 12, "green": 13, "blue": 14}
    game_num = 1
    total = 0
    for game in input:
        invalid = False
        words = re.sub("[^a-zA-Z0-9 ]", "", game).split()[2:]
        i = 0
        while i < len(words):
            if int(words[i]) > maxes[words[i + 1]]:
                invalid = True
                break
            i += 2
        if not invalid:
            total += game_num
        game_num += 1
    return total


def two(input=data):
    res = 0
    for game in input:
        mins = defaultdict(int)
        words = re.sub("[^a-zA-Z0-9 ]", "", game).split()[2:]
        i = 0
        while i < len(words):
            mins[words[i + 1]] = max(int(words[i]), mins[words[i + 1]])
            i += 2
        total = 1
        for num in mins.values():
            total *= num
        res += total
    return res


print(one())
print(two())
