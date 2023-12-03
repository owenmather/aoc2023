import os

import requests


def read_input():
    """
    Read input.txt file
    :return:
    """
    with open("input.txt", 'r') as f:
        return f.read().strip()


def read_input_lines():
    """
    Read input.txt file
    :return:
    """
    with open("input.txt", 'r') as f:
        return f.readlines()


def download_input(year, day):
    # Downloads input.txt from Advent of Code
    # and saves it in same directory as this file
    # Get session cookie from environment variable
    session_cookie = os.environ.get("AOC_SESSION_COOKIE")
    if session_cookie is None:
        raise Exception("AOC_SESSION_COOKIE environment variable not set")

    # Get input.txt from Advent of Code
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    resp = requests.get(url, cookies={"session": session_cookie})
    if resp.status_code != 200:
        raise Exception(f"Failed to download input.txt for year {year} day {day}")

    # Save input.txt in same directory as this file
    with open("input.txt", 'w') as f:
        f.write(resp.text)


def send_answer(year, day, level, answer):
    # Get session cookie from environment variable
    session_cookie = os.environ.get("AOC_SESSION_COOKIE")
    if session_cookie is None:
        raise Exception("AOC_SESSION_COOKIE environment variable not set")

    # Get input.txt from Advent of Code
    url = f"https://adventofcode.com/{year}/day/{day}/answer"
    resp = requests.post(url, cookies={"session": session_cookie}, data={"level": level, "answer": answer})
    if resp.status_code != 200:
        raise resp.raise_for_status()
    if "That's not the right answer" in resp.text:
        idx = resp.text.index("That's not the right answer")
        idx_end = resp.text.index(".", idx)
        print(resp.text[idx:idx_end])
    elif "That's the right answer" in resp.text:
        idx = resp.text.index("That's the right answer")
        idx_end = resp.text.index(".", idx)
        print(resp.text[idx:idx_end])
    elif "You don't seem" in resp.text:
        idx = resp.text.index("You don't seem")
        idx_end = resp.text.index(".", idx)
        print(resp.text[idx:idx_end])
    else:
        print(resp.text)
