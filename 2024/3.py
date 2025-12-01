from pathlib import Path
import re


def load_input(path: Path) -> str:
    with open(path) as file:
        return file.read()


def part_one() -> int:
    data = load_input(Path("3.txt"))
    regex_str = "mul(\d,\d\)"

    arr = re.findall(regex_str, data)
    print(arr)


def part_two() -> int:
    pass


if __name__ == "__main__":
    print(f"Part 1: {part_one()}")
    print(f"Part 2: {part_two()}")
