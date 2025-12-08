from pathlib import Path

from utils import parse_input_to_lines


def solution_1(input_file: Path = Path("input.txt")) -> int:
    rows = [list(line) for line in parse_input_to_lines(input_file)]
    row_counter = [1 if val == "S" else 0 for val in rows[0]]
    total_splits = 0

    for i, row in enumerate(rows):
        for j, char in enumerate(row):
            if char == "^" and i > 0 and row_counter[j]:
                row_counter[j - 1] = 1
                row_counter[j + 1] = 1
                row_counter[j] = 0
                total_splits += 1

    return total_splits


def solution_2(input_file: Path = Path("input.txt")) -> int:
    rows = [list(line) for line in parse_input_to_lines(input_file)]
    row_counter = [1 if val == "S" else 0 for val in rows[0]]

    for i, row in enumerate(rows):
        for j, char in enumerate(row):
            if char == "^" and i < len(rows) - 1:
                row_counter[j - 1] += row_counter[j]
                row_counter[j + 1] += row_counter[j]
                row_counter[j] = 0

    return sum(row_counter)


if __name__ == "__main__":
    print(f"Solution 1: {solution_1()}")
    print(f"Solution 2: {solution_2()}")
