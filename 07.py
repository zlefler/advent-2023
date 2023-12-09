import re
from collections import defaultdict, Counter

test = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
]

with open("07.txt") as f:
    data = [line.rstrip("\n") for line in f.readlines()]


def card_val(card, joker=False):
    card_map = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }
    if card == "J" and joker:
        return 1
    return card_map[card]


# hand rank map:
# 0 = high card, 1 = pair, 2 = two pair, 3 = three of a kind, 4 = full house
# 5 = four of a kind, 6 = five of a kind


def get_hands(input, joker=False):
    for line in input:
        hand, rank = line.split()
        hand_rank_map[hand] = rank
        card_count = Counter(hand)
        best = max(card_count.values())
        if joker:
            best += card_count["J"]
        if best == 1:
            hands[0].append(hand)
        elif best == 2:
            if list(card_count.values()).count(2) == 2:
                hands[2].append(hand)
            else:
                hands[1].append(hand)
        elif best == 3:
            if list(card_count.values()).count(2) == 1:
                hands[4].append(hand)
            else:
                hands[3].append(hand)
        elif best == 4:
            hands[5].append(hand)
        else:
            hands[6].append(hand)
    return hands


def one(input=data):
    hands = get_hands(input)

    def card_key(s):
        return tuple(card_val(c) for c in s)

    sorted_hands = {}
    for group in hands.items():
        sorted_hands[group[0]] = sorted(group[1], key=card_key, reverse=True)
    rank = len(input)
    winnings = 0
    for i in range(6, -1, -1):
        for hand in sorted_hands[i]:
            winnings += int(hand_rank_map[hand]) * rank
            rank -= 1
    return winnings


def two(input=data):
    hands = get_hands(input, True)

    def card_key(s):
        return tuple(card_val(c, True) for c in s)

    sorted_hands = {}
    for group in hands.items():
        sorted_hands[group[0]] = sorted(group[1], key=card_key, reverse=True)

    rank = len(input)
    winnings = 0
    for i in range(6, -1, -1):
        if i in sorted_hands:
            for hand in sorted_hands[i]:
                winnings += int(hand_rank_map[hand]) * rank
                rank -= 1
    return winnings


hands = defaultdict(list)
hand_rank_map = {}
print(one())
hands = defaultdict(list)
hand_rank_map = {}
print(two())
