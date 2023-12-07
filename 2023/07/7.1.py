import bisect
import os
from collections import Counter, defaultdict
from dotenv import load_dotenv
import utils

load_dotenv()

type_map = defaultdict(int)
type_map[(5, 0)] = 6
type_map[(4, 1)] = 5
type_map[(3, 2)] = 4
type_map[(3, 1)] = 3
type_map[(2, 2)] = 2
type_map[(2, 1)] = 1

value_map = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}


class Card:
    def __init__(self, value, bid):
        self.value = value
        self.type = self.get_type()
        self.bid = bid

    def get_type(self):
        hand = sorted(Counter(list(self.value)).values(), reverse=True)
        if len(hand) == 1:
            hand.append(0)
        return type_map[(hand[0], hand[1])]

    # Compare two cards
    def __gt__(self, other):
        if self.type == other.type:
            for idx, val in enumerate(self.value):
                if val != other.value[idx]:
                    return value_map[val] > value_map[other.value[idx]]
        return self.type > other.type

    def __lt__(self, other):
        return not self.__gt__(other)

    def __eq__(self, other):
        return self.type == other.type and self.value == other.value


def solve():
    """
    Solve the problem here
    :return:
    """
    data = utils.read_input()
    data = data.split("\n")
    l = []
    res = 0
    for line in data:
        # JJJJ8 619
        value, bid = line.split(" ")
        c = Card(value, int(bid))
        bisect.insort(l, c)
    return sum([(idx + 1) * cc.bid for idx, cc in enumerate(l)])


if __name__ == "__main__":
    if not os.path.exists("input.txt"):
        # Just download input on first run. Second run should solve
        # update here to download+solve in one run
        utils.download_input(year="2023", day="7")
    else:
        answer = solve()
        print(answer)
        utils.send_answer(year="2023", day="7", level=1, answer=answer)
