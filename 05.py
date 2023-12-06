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


def locations(intervals):
    for maps_block in input_maps.split("\n\n"):
        mappings = maps_block.split("\n")[1:]
        images = list()
        while intervals:
            x, y = intervals.pop()
            for mapping in mappings:
                a, b, delta = map(int, mapping.split())
                r_endpoint = b + delta - 1
                if b <= x <= y <= r_endpoint:
                    images.append((x - b + a, y - b + a))
                    break
                if b <= x <= r_endpoint < y:
                    intervals.extend([(x, r_endpoint), (r_endpoint + 1, y)])
                    break
            else:
                images.append((x, y))
        intervals = images
    return intervals


with open("05.txt") as f:
    input_seeds, input_maps = f.read().split("\n\n", 1)
    seed_data = [int(x) for x in re.findall(r"\d+", input_seeds)]


def one():
    return min(min(locations([(x, x) for x in seed_data])))


def two():
    seed_intervals = [(x, x + d - 1) for x, d in zip(seed_data[::2], seed_data[1::2])]

    return min(min(locations(seed_intervals)))


print(one())
print(two())
