import re
from collections import defaultdict, deque
from itertools import count


test = [
    "Time:      7  15   30",
    "Distance:  9  40  200",
]

with open("06.txt") as f:
    data = [line.rstrip("\n") for line in f.readlines()]


def one(input=data):
    times = re.sub(r"^\D+", "", input[0]).split()
    dists = re.sub(r"^\D+", "", input[1]).split()

    for i in range(len(times)):
        times[i] = int(times[i])
        dists[i] = int(dists[i])
    ways_per_race = 1
    for i in range(len(times)):
        times_beat = 0
        for j in range(times[i]):
            if j * (times[i] - j) > dists[i]:
                times_beat += 1
        ways_per_race *= times_beat
    return f"total: {ways_per_race}"


def two(input=data):
    time = int(re.sub(r"\D+ ", "", input[0]))
    dist = int(re.sub(r"\D+ ", "", input[1]))

    times_beat = 0
    for j in range(time):
        if j * (time - j) > dist:
            times_beat += 1

    return times_beat


print(one())

print(two())
