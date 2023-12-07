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
    "J": 1,  # now the weakest card
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
        if "J" in self.value:
            hand = sorted(Counter(list(self.value.replace("J", ""))).values(), reverse=True)
            # How to handle 1 to 5 J's?
            hand_length = len(hand)
            if hand_length <= 1:
                # hands with 1 or 0 cards left over become 5 of a kind
                hand = [5, 0]
            elif hand_length == 2:
                # hands with 2 different cards left over either become FH or 4 of a kind
                # [3,1], [2,2],[2,1],[1,1]
                if hand[1] == 2:
                    hand = [3, 2]
                else:
                    hand = [4, 1]
            elif hand_length == 3:
                # hands with 3 different cards left over either become 3 of a kind
                # [1,1,1] [2,1,1] -> 3 of a kind,
                hand = [3, 1]
            elif hand_length == 4:
                # Only one jack and no pairs
                # [1,1,1,1] -> pair
                hand = [2, 1]
            return type_map[(hand[0], hand[1])]
        else:
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
        return self.value == other.value


def solve():
    """
    Solve the problem here
    :return:
    """
    data = utils.read_input()
    data = data.split("\n")
    l = []
    for line in data:
        # JJJJ8 619
        value, bid = line.split(" ")
        c = Card(value, int(bid))
        bisect.insort(l, c)
    [print(cc.value, cc.type, cc.bid) for cc in l]
    return sum([(idx + 1) * cc.bid for idx, cc in enumerate(l)])


if __name__ == "__main__":
    if not os.path.exists("input.txt"):
        # Just download input on first run. Second run should solve
        # update here to download+solve in one run
        utils.download_input(year="2023", day="7")
    else:
        answer = solve()
        print(answer)
        utils.send_answer(year="2023", day="7", level=2, answer=answer)
