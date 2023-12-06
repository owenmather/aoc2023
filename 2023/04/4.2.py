import os
from dotenv import load_dotenv
from collections import defaultdict
import utils

load_dotenv()


def solve():
    """
    Solve the problem here
    :return:
    """
    data = utils.read_input()
    data = data.split("\n")
    res = 0
    card_counts = defaultdict(int)
    for idx, line in enumerate(data):

        pairs = line.split(":")[1].strip()
        game_score = 0
        next = ""
        key = "my_numbers"
        game = {
            "my_numbers": [],
            "winning_numbers": []
        }
        for c in pairs:
            if c.isdigit():
                next += c
            elif c == "|":
                key = "winning_numbers"
            elif next:
                game[key].append(int(next))
                next = ""
        if next:
            game[key].append(int(next))
        win_count = len(set(game["my_numbers"]).intersection(set(game["winning_numbers"])))
        # Add all the copies
        for i in range(win_count):
            card_counts[idx + i + 1] += 1 + card_counts[idx]
        # Add the original card count number of the current card to the card_counts dict
        card_counts[idx] += 1
        # Add the card count number of the current card to the card_counts dict
        res += card_counts[idx]
    return res


if __name__ == "__main__":
    if not os.path.exists("input.txt"):
        # Just download input on first run. Second run should solve
        # update here to download+solve in one run
        utils.download_input(year="2023", day="4")
    else:
        answer = solve()
        print(answer)
        utils.send_answer(year="2023", day="4", level=2, answer=answer)
