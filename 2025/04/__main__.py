from pathlib import Path

from utils import parse_input_to_lines


def solution(multi_pass: bool, input_file: Path = Path("input.txt"), blocking_qty: int = 4) -> int:
    input_data = [list(row) for row in parse_input_to_lines(input_file)]
    height = len(input_data)
    length = len(input_data[0])

    total_accessible = 0

    while True:
        curr_accessible = 0

        for y, row in enumerate(input_data):
            for x, item in enumerate(row):
                if item != "@":
                    continue

                count = 0

                if x != 0 and y != 0 and input_data[y-1][x-1] == "@":
                    count += 1

                if y != 0 and input_data[y-1][x] == "@":
                    count += 1

                if x != length - 1 and y != 0 and input_data[y-1][x+1] == "@":
                    count += 1

                if x != 0 and input_data[y][x-1] == "@":
                    count += 1

                if x != length - 1 and input_data[y][x+1] == "@":
                    count += 1

                if x != 0 and y != height - 1 and input_data[y+1][x-1] == "@":
                    count += 1

                if y != height - 1 and input_data[y+1][x] == "@":
                    count += 1

                if x != length - 1 and y != height - 1 and input_data[y+1][x+1] == "@":
                    count += 1

                if count < blocking_qty:
                    curr_accessible += 1

                    if multi_pass:
                        input_data[y][x] = "x"

        total_accessible += curr_accessible

        if not multi_pass or curr_accessible == 0:
            break

    return total_accessible

if __name__ == "__main__":
    print(f"Solution 1: {solution(False)}")
    print(f"Solution 2: {solution(True)}")