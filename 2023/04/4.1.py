import os
from dotenv import load_dotenv
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
    for line in data:
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
        # Two to power of win_count
        if win_count:
            game_score += 2 ** (win_count - 1)
        res += game_score
    return res


if __name__ == "__main__":
    if not os.path.exists("input.txt"):
        # Just download input on first run. Second run should solve
        # update here to download+solve in one run
        utils.download_input(year="2023", day="4")
    else:
        answer = solve()
        print(answer)
        utils.send_answer(year="2023", day="4", level=1, answer=answer)
