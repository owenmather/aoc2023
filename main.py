import os
import dotenv

from jinja2 import Environment, FileSystemLoader

dotenv.load_dotenv()
environment = Environment(loader=FileSystemLoader("template/"))
template = environment.get_template("solution_template.py")


def mkdir_if_not_exists(path):
    if not os.path.exists(path):
        os.mkdir(path)


def generate_aoc_structure(year):
    mkdir_if_not_exists(year)
    for i in range(4, 26):
        mkdir_if_not_exists(os.path.join(year, str(i)))
        with open(os.path.join(year, str(i), f"{i}.1.py"), 'w') as f:
            f.write(template.render(year=year, day=i, level=1))
        with open(os.path.join(year, str(i), f"{i}.2.py"), 'w') as f:
            f.write(template.render(year=year, day=i, level=2))


if __name__ == "__main__":
    generate_aoc_structure(year=os.environ.get("AOC_YEAR", "2023"))
