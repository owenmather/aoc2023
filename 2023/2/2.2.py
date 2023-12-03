import os
from dotenv import load_dotenv

import utils

load_dotenv()

limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def solve():
    """
    Solve the problem here
    :return:
    """
    data = utils.read_input()
    data = data.split("\n")
    res = 0
    for line in data:
        game_info = line.replace(",", "").replace(";", "").split(" ")
        draws = game_info[2:]
        mins = {}
        while draws:
            num = int(draws.pop(0))
            color = draws.pop(0)
            mins[color] = max(mins.get(color, 0), num)
        # Get powers
        power = mins.get("red", 1) * mins.get("green", 1) * mins.get("blue", 1)
        res += power
    return res


if __name__ == "__main__":
    # Check if input.txt files exists in same directory as this file
    if not os.path.exists("input.txt"):
        utils.download_input(year="2023", day="2")
    else:
        answer = solve()
        print(answer)
        utils.send_answer(year="2023", day="2", level=2, answer=answer)
