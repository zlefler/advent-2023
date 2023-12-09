import re
import math
from collections import defaultdict, deque
from itertools import count


tests = [
    [
        "RL",
        "",
        "AAA = (BBB, CCC)",
        "BBB = (DDD, EEE)",
        "CCC = (ZZZ, GGG)",
        "DDD = (DDD, DDD)",
        "EEE = (EEE, EEE)",
        "GGG = (GGG, GGG)",
        "ZZZ = (ZZZ, ZZZ)",
    ],
    [
        "LLR",
        "",
        "AAA = (BBB, BBB)",
        "BBB = (AAA, ZZZ)",
        "ZZZ = (ZZZ, ZZZ)",
    ],
]

with open("08.txt") as f:
    data = [line.rstrip("\n") for line in f.readlines()]

ll = [x for x in open("08.txt").read().strip().split("\n\n")]


def one(input=data):
    steps = input[0]
    i = 0

    def get_dir():
        if steps[i % len(steps)] == "L":
            return 0
        return 1

    maps = {}

    starts = []
    for line in input[2:]:
        reg = re.findall(r"[A-Z]", line)
        key = "".join(reg[:3])
        a = "".join(reg[3:6])
        b = "".join(reg[6:])
        maps[key] = (a, b)
        if key.endswith("A"):
            starts.append(key)

    start = "AAA"
    goal = "ZZZ"
    while start != goal and i < 100000:
        next = maps[start]
        dir = get_dir()
        start = next[dir]
        i += 1
    print(f"part one: {i}")

    def win(nodes):
        for node in nodes:
            if not node.endswith("Z"):
                return False
        return True

    i = 0
    print(starts)
    while True:
        if win(starts):
            return f"part two: {i}"
        for start in starts:
            next = maps[start]
            dir = get_dir()
            start = next[dir]
        i += 1


# def two(input=data):


# for test in tests:
# print(one(test))

print(one())

test2 = [
    "LR",
    "",
    "11A = (11B, XXX)",
    "11B = (XXX, 11Z)",
    "11Z = (11B, XXX)",
    "22A = (22B, XXX)",
    "22B = (22C, 22C)",
    "22C = (22Z, 22Z)",
    "22Z = (22B, 22B)",
    "XXX = (XXX, XXX)",
]

# print(two(test2))
