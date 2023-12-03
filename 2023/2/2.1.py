import os
from dotenv import load_dotenv

import requests
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
        game_number = int(game_info[1][:-1])
        draws = game_info[2:]
        while draws:
            num = int(draws.pop(0))
            color = draws.pop(0)
            if num > limits[color]:
                break
            if not draws:
                res += game_number
    return res


if __name__ == "__main__":
    # Check if input.txt files exists in same directory as this file
    if not os.path.exists("input.txt"):
        utils.download_input(year="2023", day="2")
    else:
        answer = solve()
        print(answer)
        utils.send_answer(year="2023", day="2", level=1, answer=answer)
