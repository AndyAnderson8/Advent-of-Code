from pathlib import Path

from utils import parse_input_to_lines


def solution_1(input_file: Path = Path("input.txt")) -> int:
    lines = parse_input_to_lines(input_file, ",")
    invalid_sum = 0

    for line in lines:
        low, high = map(int, line.split("-"))

        for prod_id in range(low, high + 1):
            id_str = str(prod_id)

            if len(id_str) % 2:
                continue

            idx = len(id_str) // 2
            left_val = int(id_str[:idx])
            right_val = int(id_str[idx:])

            if left_val == right_val:
                invalid_sum += prod_id

    return invalid_sum


def solution_2(input_file: Path = Path("input.txt")) -> int:
    lines = parse_input_to_lines(input_file, ",")
    invalid_sum = 0

    for line in lines:
        low, high = map(int, line.split("-"))

        for prod_id in range(low, high + 1):
            id_str = str(prod_id)

            for slice_len in range(1, (len(id_str) // 2) + 1):
                if len(id_str) % slice_len:
                    continue

                slices = [id_str[i:i+slice_len] for i in range(0, len(id_str), slice_len)]
                if all(slice_i == slices[0] for slice_i in slices):
                    invalid_sum += prod_id
                    break  # don't recheck same id (e.g., check '2' and '22' in id '2222')

    return invalid_sum


if __name__ == "__main__":
    print(f"Solution 1: {solution_1()}")
    print(f"Solution 2: {solution_2()}")
