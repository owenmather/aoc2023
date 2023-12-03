# Advent of Code Python

This repo contains my solutions to the [Advent of Code](https://adventofcode.com/) challenges.

Supports generation solution directories for a given year and day, downloading the input for a given day and posting a solution to the site.


## Usage

Create a .env file with the following variables:

```
AOC_SESSION_COOKIE=<your session cookie from adventofcode.com>
AOC_YEAR=<the year you want to run>
```

Then run the following commands to install dependencies and build the solution directory structure:

```
pip install -r requirements.txt
python main.py
```
