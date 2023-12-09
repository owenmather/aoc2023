import os
from dotenv import load_dotenv
import utils

load_dotenv()


def generate_seq(ln, base=0):
    nums = list(map(int, ln))
    seq = []
    for idx, val in enumerate(nums[:-1]):
        seq.append(nums[idx + 1] - val)
    if len(set(seq)) == 1:
        return base + seq[-1] + nums[-1]
    return generate_seq(seq, base=base + nums[-1])


def solve():
    """
    Solve the problem here
    :return:
    """
    data = utils.read_input()
    data = data.split("\n")
    res = 0
    for line in data:
        ans = generate_seq(line.split(" "))
        print(line)
        print(ans)
        res += ans
    return res


if __name__ == "__main__":
    if not os.path.exists("input.txt"):
        # Just download input on first run. Second run should solve
        # update here to download+solve in one run
        utils.download_input(year="2023", day="9")
    else:
        answer = solve()
        print(answer)
        utils.send_answer(year="2023", day="9", level=1, answer=answer)
