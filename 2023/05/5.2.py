import os
from collections import defaultdict
from dotenv import load_dotenv
import math
import utils

load_dotenv()
mapinfo = {}


def solve():
    """
    Solve the problem here
    :return:
    """
    data = utils.read_input().split("\n")
    seeds = [int(seed) for seed in data.pop(0).split(":")[1].strip().split(" ")]
    order = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
    order_idx = -1

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

    # Need to check overlapping interval ranges
    bounds = defaultdict(list)
    while seeds:
        start, rng = seeds.pop(0), seeds.pop(0)
        end = start + rng - 1
        # Add tuples with start + ending ranges
        bounds["seed"].append((start, end))

    for idx, op in enumerate(order[:-1]):
        for (start, end) in bounds[op]:
            cur_elem = start
            # While the cur_elem is still in bounds we process
            while cur_elem <= end:
                # First we find the bounding range for this input elem
                cur_elem_destination, max_input_elem_in_range, d, s = get_location(cur_elem, op)
                if cur_elem_destination == -1:
                    # Unmapped element
                    if end <= max_input_elem_in_range:
                        possible_values = (cur_elem, end)
                        cur_elem = end + 1
                    else:
                        possible_values = (cur_elem, max_input_elem_in_range)
                        cur_elem = max_input_elem_in_range + 1
                    bounds[order[idx + 1]].append(possible_values)
                elif max_input_elem_in_range > end:
                    # We will always used the destination range found for this input range
                    # QUIT STATE
                    cur_elem = end + 1  # forces quit
                    possible_values = (cur_elem_destination, d + (end - s))
                    # Add input bounds for the next operation in sequence
                    bounds[order[idx + 1]].append(possible_values)
                else:
                    # We need process all possible bounds for the selected operation and continue
                    possible_values = (cur_elem_destination, d + (max_input_elem_in_range - s))
                    cur_elem = max_input_elem_in_range + 1
                    bounds[order[idx + 1]].append(possible_values)
    return min([start_location for (start_location, end_location) in bounds["location"]])


def get_location(cur_elem, o):
    for (d, s, r) in mapinfo[o]:
        if s <= cur_elem < s + r:
            cur_elem_destination = d + (cur_elem - s)
            max_input_elem_in_range = s + r - 1
            return cur_elem_destination, max_input_elem_in_range, d, s
    # Unmapped ranges - eww missed in first
    min_distance_to_next_valid = math.inf
    max_invalid = math.inf
    for (d, s, r) in mapinfo[o]:
        if s - cur_elem > 0:
            if s - cur_elem < min_distance_to_next_valid:
                min_distance_to_next_valid = s - cur_elem
                max_invalid = s - 1
    return -1, max_invalid, 0, 0


if __name__ == "__main__":
    if not os.path.exists("input.txt"):
        # Just download input on first run. Second run should solve
        # update here to download+solve in one run
        utils.download_input(year="2023", day="5")
    else:
        answer = solve()
        print(answer)
        utils.send_answer(year="2023", day="5", level=2, answer=answer)
