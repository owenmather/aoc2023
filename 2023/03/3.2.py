import os
from dotenv import load_dotenv

import requests
import utils

load_dotenv()


def solve():
    """
    Solve the problem here
    :return:
    """
    # TODO: Investigate bug with added_coords and gears
    # If 2 valid gears have an overlapping coordinate, the second gear will not get picked up?
    # If a potential gear has an overlapping coordinate with a valid gear part,
    # the valid gear part will not get picked up?
    added_coords = set()
    data = utils.read_input()
    data = data.replace(".", "x")
    data = data.split("\n")
    res = 0
    for line_number, line in enumerate(data):
        for idx, char in enumerate(line):
            if not str(char).isalnum():
                if char != "*":
                    continue
                # We have found a gear symbol
                valid_coords = [(line_number - 1, idx), (line_number + 1, idx), (line_number, idx - 1),
                                (line_number, idx + 1), (line_number - 1, idx - 1), (line_number - 1, idx + 1),
                                (line_number + 1, idx - 1), (line_number + 1, idx + 1)]
                found_parts = []
                for (x, y) in valid_coords:
                    if x < 0 or y < 0:
                        continue
                    if x >= len(data) or y >= len(line):
                        continue
                    if data[x][y].isdigit():
                        if (x, y) in added_coords:
                            continue
                        y1 = y - 1
                        start_coord = (x, y)
                        added_coords.add(start_coord)
                        while 0 <= y1 < len(line) and data[x][y1].isdigit():
                            start_coord = (x, y1)
                            added_coords.add(start_coord)
                            y1 -= 1
                        end_coord = (x, y)
                        added_coords.add(end_coord)
                        y2 = y + 1
                        while 0 <= y2 < len(line) and data[x][y2].isdigit():
                            end_coord = (x, y2)
                            added_coords.add(end_coord)
                            y2 += 1

                        found_parts.append(int(data[x][start_coord[1]:end_coord[1] + 1]))
                        # res += int(data[x][start_coord[1]:end_coord[1] + 1])
                if len(found_parts) == 2:
                    res += found_parts[0] * found_parts[1]

    return res


if __name__ == "__main__":
    # Check if input.txt files exists in same directory as this file
    if not os.path.exists("input.txt"):
        utils.download_input(year="2023", day="3")
    else:
        answer = solve()
        print(answer)
        utils.send_answer(year="2023", day="3", level=2, answer=answer)
