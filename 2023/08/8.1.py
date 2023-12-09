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
    instruction = data.pop(0)
    data.pop(0)  # drop empty line
    routes = {}
    for line in data:
        # Build the paths
        source, paths = line.split(" = ")
        paths = paths[1:-1].split(", ")
        routes[source] = paths

    position = "AAA"
    lr = {"L": 0, "R": 1}
    idx = 0
    while position != "ZZZ":
        position = routes[position][lr[instruction[idx]]]
        idx = (idx + 1) % len(instruction)
        res += 1
    return res


if __name__ == "__main__":
    if not os.path.exists("input.txt"):
        # Just download input on first run. Second run should solve
        # update here to download+solve in one run
        utils.download_input(year="2023", day="8")
    else:
        answer = solve()
        print(answer)
        utils.send_answer(year="2023", day="8", level=1, answer=answer)
