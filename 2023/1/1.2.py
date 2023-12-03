import os
from dotenv import load_dotenv

import requests
import utils

load_dotenv()

valid = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

valid_to_digit = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
valid_ranges = {
    "o": [3],
    "t": [3, 5],
    "f": [4],
    "s": [3, 5],
    "e": [5],
    "n": [4]
}

valid_ranges_backwards = {
    'n': [5],
    'o': [3],
    't': [5],
    'e': [3, 4, 5],
    'x': [3],
    'r': [4]
}
valid_ranges_keys = valid_ranges.keys()


def solve():
    """
    Solve the problem here
    :return:
    """
    data = utils.read_input()
    data = data.split("\n")
    result = 0
    for line in data:
        to_add = ""
        for idx, c in enumerate(line):
            if c.isdigit():
                to_add += c
                break
            if c in valid_ranges_keys:
                found = False
                for valid_len in valid_ranges[c]:
                    if line[idx:idx + valid_len] in valid:
                        to_add += f"{valid_to_digit[line[idx:idx + valid_len]]}"
                        found = True
                        break
                if found:
                    break
        for idx, c in enumerate(line[::-1]):
            if c.isdigit():
                to_add += c
                break
            if c in valid_ranges_backwards.keys():
                found = False
                for valid_len in valid_ranges_backwards[c]:
                    if line[::-1][idx:idx + valid_len][::-1] in valid:
                        to_add += f"{valid_to_digit[line[::-1][idx:idx + valid_len][::-1]]}"
                        found = True
                        break
                if found:
                    break
        result += int(to_add)
    return result


if __name__ == "__main__":
    # Check if input.txt files exists in same directory as this file
    if not os.path.exists("input.txt"):
        utils.download_input(year="2023", day="1")
    else:
        answer = solve()
        print(answer)
        utils.send_answer(year="2023", day="1", level=2, answer=answer)
