import os
from dotenv import load_dotenv
import utils

load_dotenv()


def generate_seq(nums, base, stack):
    seq = [nums[idx + 1] - val for idx, val in enumerate(nums[:-1])]
    stack.append(nums[0])
    if seq[0] == seq[-1]:
        # Now when everything is the same value we add extrapolate backwards
        left_value = seq[0]
        while stack:
            # Stack contains all the previous left side values
            left_value = stack.pop() - left_value
        return left_value
    return generate_seq(seq, base=base + nums[-1], stack=stack)


def solve():
    """
    Solve the problem here
    :return:
    """
    data = utils.read_input()
    data = data.split("\n")
    res = 0
    for line in data:
        ans = generate_seq(list(map(int, line.split(" "))), 0, [])
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
       # utils.send_answer(year="2023", day="9", level=2, answer=answer)
