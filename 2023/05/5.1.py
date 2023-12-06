import os
from dotenv import load_dotenv

import utils

load_dotenv()


def solve():
    """
    Solve the problem here
    :return:
    """
    data = utils.read_input().split("\n")
    seeds = [int(seed) for seed in data.pop(0).split(":")[1].strip().split(" ")]
    order = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity"]
    order_idx = -1
    mapinfo = {}
    for line in data:
        # Build Map Data
        if not line:
            order_idx += 1
            continue
        if "map" in line:
            source, dest = line.split(" map")[0].split("-to-")
            mapinfo[source] = []
        else:
            d, s, r = line.split(" ")
            mapinfo[order[order_idx]].append((int(d), int(s), int(r)))

    locations = []
    for seed in seeds:
        cur_elem = seed
        for o in order:
            for (d, s, r) in mapinfo[o]:
                if s <= cur_elem <= s + r:
                    cur_elem = d + (cur_elem - s)
                    break
        locations.append(cur_elem)

    return min(locations)


if __name__ == "__main__":
    if not os.path.exists("input.txt"):
        # Just download input on first run. Second run should solve
        # update here to download+solve in one run
        utils.download_input(year="2023", day="5")
    else:
        answer = solve()
        print(answer)
        utils.send_answer(year="2023", day="5", level=1, answer=answer)
