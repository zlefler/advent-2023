test = [
    "3szfjrv",
    "2p1nggbmpklvfivethree8",
    "sixeightfive3sdtwo",
    "lkmvnjmhzhseven2jxsix8",
]

with open("01.txt") as f:
    data = f.readlines()


def one(input=data):
    res = 0
    for line in input:
        first = ""
        last = ""
        for char in line:
            if char.isnumeric():
                if not first:
                    first = char
                last = char
        res += int(first + last)
    return res


def two(input=data):
    nums = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    res = 0

    for line in input:
        first = ""
        first_idx = float("inf")
        last = ""
        last_idx = -1
        for num in nums.keys():
            if num in line:
                left = line.find(num)
                right = line.rfind(num)
                if left < first_idx:
                    first_idx = left
                    first = nums[num]
                if right + len(num) > last_idx:
                    last_idx = right + len(num) - 1
                    last = nums[num]
        for i, char in enumerate(line):
            if char.isnumeric():
                if i < first_idx:
                    first_idx = i
                    first = char
                if i > last_idx:
                    last_idx = i
                    last = char
        res += int(first + last)
    return res


print(one())
print(two())
