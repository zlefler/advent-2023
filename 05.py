import re
from collections import defaultdict, deque
from itertools import count


test = [
    "seeds: 79 14 55 13",
    "",
    "seed-to-soil map:",
    "50 98 2",
    "52 50 48",
    "",
    "soil-to-fertilizer map:",
    "0 15 37",
    "37 52 2",
    "39 0 15",
    "",
    "fertilizer-to-water map:",
    "49 53 8",
    "0 11 42",
    "42 0 7",
    "57 7 4",
    "",
    "water-to-light map:",
    "88 18 7",
    "18 25 70",
    "",
    "light-to-temperature map:",
    "45 77 23",
    "81 45 19",
    "68 64 13",
    "",
    "temperature-to-humidity map:",
    "0 69 1",
    "1 0 69",
    "",
    "humidity-to-location map:",
    "60 56 37",
    "56 93 4",
]


def parse_data_one(data):
    seeds = re.sub(r"^\D+", "", data[0]).split()
    for i in range(len(seeds)):
        seeds[i] = int(seeds[i])
    i = 0
    maps = defaultdict(list)
    for line in data[3:]:
        if line == "":
            continue
        if line[0].isalpha():
            i += 1
        else:
            nums = line.split(" ")
            for j in range(len(nums)):
                nums[j] = int(nums[j])
            maps[i].append(nums)
    return (seeds, maps)


with open("05.txt") as f:
    data = [line.rstrip("\n") for line in f.readlines()]


def traverse_maps(seeds, maps):
    for i in range(len(maps.items())):
        for j in range(len(seeds)):
            for row in maps[i]:
                if seeds[j] >= row[1] and seeds[j] < row[1] + row[2]:
                    diff = row[0] - row[1]
                    seeds[j] += diff
                    break
    return f"total: {min(seeds)}"


def one(input=data):
    seeds, maps = parse_data_one(input)
    return traverse_maps(seeds, maps)


def parse_data_two(data):
    seed_ranges = re.sub(r"^\D+", "", data[0]).split()
    seeds = []
    for i in range(0, len(seed_ranges), 2):
        seed = int(seed_ranges[i])
        k = int(seed_ranges[i + 1])
        for j in range(k):
            seeds.append(seed + j)
    i = 0
    maps = defaultdict(list)
    for line in data[3:]:
        if line == "":
            continue
        if line[0].isalpha():
            i += 1
        else:
            nums = line.split(" ")
            for j in range(len(nums)):
                nums[j] = int(nums[j])
            maps[i].append(nums)
    return (seeds, maps)


def two(input=data):
    seeds, maps = parse_data_two(input)
    return traverse_maps(seeds, maps)


print(one())

# doesn't work
# print(two())
