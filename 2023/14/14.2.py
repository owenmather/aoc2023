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
        continue
    return res


if __name__ == "__main__":
    if not os.path.exists("input.txt"):
        # Just download input on first run. Second run should solve
        # update here to download+solve in one run
        utils.download_input(year="2023", day="14")
    else:
        answer = solve()
        print(answer)
        utils.send_answer(year="2023", day="14", level=2, answer=answer)
