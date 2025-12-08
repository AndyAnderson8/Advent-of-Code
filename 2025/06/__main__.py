from math import prod
from pathlib import Path

from utils import parse_input_to_lines


def solution_1(input_file: Path = Path("input.txt")) -> int:
    rows = [line.split() for line in parse_input_to_lines(input_file)]
    result_sum = 0

    for col_idx in range(len(rows[0])):
        vals = [int(rows[row_idx][col_idx]) for row_idx in range(len(rows) - 1)]
        operator = rows[-1][col_idx]

        match operator:
            case "+":
                result_sum += sum(vals)
            case "*":
                result_sum += prod(vals)

    return result_sum


def solution_2(input_file: Path = Path("input.txt")) -> int:
    rows = parse_input_to_lines(input_file, keep_whitespace=True)
    result_sum = 0

    val = 0
    vals = []
    for col_idx in range(len((rows[0])) - 1, -1, -1):
        for row_idx in range(len(rows)):
            char = rows[row_idx][col_idx]
            match char:
                case "+":
                    vals.append(val)
                    result_sum += sum(vals)
                    vals = []
                    val = 0
                case "*":
                    vals.append(val)
                    result_sum += prod(vals)
                    vals = []
                    val = 0
                case " ":
                    pass
                case _:  # integer
                    val *= 10
                    val += int(char)

        if val:  # Skip 0 since its just empty column
            vals.append(val)
            val = 0

    return result_sum


if __name__ == "__main__":
    print(f"Solution 1: {solution_1()}")
    print(f"Solution 2: {solution_2()}")
