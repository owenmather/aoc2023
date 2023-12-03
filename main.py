import os
import dotenv

from jinja2 import Environment, FileSystemLoader

dotenv.load_dotenv()
environment = Environment(loader=FileSystemLoader("template/"))
template = environment.get_template("solution_template.py")


def mkdir_if_not_exists(path):
    if not os.path.exists(path):
        os.mkdir(path)


def generate_aoc_structure(year, force=False):
    mkdir_if_not_exists(year)
    for day in range(1, 26):
        day_dir = f'{day:02}'  # Pad single digits with 0 for directory name sorting
        mkdir_if_not_exists(os.path.join(year, day_dir))
        for level in [1, 2]:
            python_file = os.path.join(year, day_dir, f"{day}.{level}.py")
            if force or not os.path.exists(python_file):
                with open(python_file, 'w') as f:
                    f.write(template.render(year=year, day=day, level=level))


if __name__ == "__main__":
    generate_aoc_structure(year=os.environ.get("AOC_YEAR", "2023"))
