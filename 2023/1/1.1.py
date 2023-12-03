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
    data = utils.read_input()
    data = data.split("\n")
    result = 0
    for line in data:
        to_add = ""
        for c in line:
            if c.isdigit():
                to_add += c
                break
        for c in line[::-1]:
            if c.isdigit():
                to_add += c
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
        utils.send_answer(year="2023", day="1", level=1, answer=answer)
