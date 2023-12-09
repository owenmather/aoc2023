import math
import os
from dotenv import load_dotenv

import utils

load_dotenv()


def lcm(numbers):
    ans = 1
    for _, x in numbers:
        ans = (ans * x) // math.gcd(ans, x)
    return ans


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
    routes = {"L": {}, "R": {}}
    positions = []
    for line in data:
        # Build the paths
        source, paths = line.split(" = ")
        paths = paths[1:-1].split(", ")
        routes["L"][source] = paths[0]
        routes["R"][source] = paths[1]
        if source[-1] == "A":
            positions.append(source)

    idx = 0
    loops = {}
    distances = set()
    while True:
        nxt = []
        for i, p in enumerate(positions):
            position = routes[instruction[idx % len(instruction)]][p]
            if position[-1] == "Z":
                if i in loops:
                    # print(i, idx - loops[i])
                    if (i, idx - loops[i]) not in distances:
                        print((i, idx - loops[i]))
                    distances.add((i, idx - loops[i]))
                    if len(distances) == len(positions):
                        # All loop and loop step distances found
                        return lcm(distances)
                # print(i, idx, position)
                loops[i] = idx
            nxt.append(position)
        positions = nxt
        idx = (idx + 1)
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
        utils.send_answer(year="2023", day="8", level=2, answer=answer)
