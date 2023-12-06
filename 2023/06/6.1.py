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
    res = 1
    times = map(int, data.pop(0).split("Time:")[1].strip().split("     "))
    distance = map(int, data.pop(0).split("Distance:")[1].strip().split("   "))
    times_to_distance = list(zip(times, distance))
    for (time, distance) in times_to_distance:
        # For i in range(1,time):
        # Distance is the sum of all ((time-i)*i) for i in range(1,time)
        winning_games = len(list(filter(lambda x: x > distance, [((time - i) * i) for i in range(1, time)])))
        res *= winning_games
    return res


if __name__ == "__main__":
    if not os.path.exists("input.txt"):
        # Just download input on first run. Second run should solve
        # update here to download+solve in one run
        utils.download_input(year="2023", day="6")
    else:
        answer = solve()
        print(answer)
        utils.send_answer(year="2023", day="6", level=1, answer=answer)
