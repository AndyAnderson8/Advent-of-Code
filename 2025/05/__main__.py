from pathlib import Path

from utils import parse_input_to_lines


def get_distinct_ranges(pending_ranges: list[set[int]]) -> list[set[int]]:
    distinct_ranges = []

    for pending_range in pending_ranges:
        for distinct_range in distinct_ranges:
            pending_low, pending_high = pending_range
            low, high = distinct_range

            # Nothing new; same bounds or nested inside existing bounds
            if pending_low >= low and pending_high <= high:
                pending_range = None
                break

            # Check for lower low
            if pending_low < low <= pending_high:
                low = pending_low

            # Check for higher high
            if pending_low <= high < pending_high:
                high = pending_high

            # If changed, updates pending, not distinct, because it might now overlap with subsequent distincts
            if (low, high) != distinct_range:
                pending_range = (low, high)
                distinct_ranges.remove(distinct_range)

        # Falls fully outside any range, so it's distinct
        if pending_range:
            distinct_ranges.append(pending_range)

    return distinct_ranges


def get_inputs(input_file: Path = Path("input.txt")) -> tuple[list[set[int]], list[int]]:
    input_lines = parse_input_to_lines(input_file)
    ranges = []
    test_vals = []

    for line in input_lines:
        if "-" in line:
            low, high = map(int, line.split("-"))
            ranges.append((low, high))
        elif line != "":
            test_vals.append(int(line))

    distinct_ranges = get_distinct_ranges(ranges)

    return distinct_ranges, test_vals


def solution_1(ranges: list[set[int]], test_vals: list[int]) -> int:
    fresh_qty = 0

    for test_val in test_vals:
        for distinct_range in ranges:
            low, high = distinct_range
            if low <= test_val <= high:
                fresh_qty += 1

    return fresh_qty


def solution_2(ranges: list[set[int]]) -> int:
    fresh_qty = 0

    for distinct_range in ranges:
        low, high = distinct_range
        fresh_qty += (high - low) + 1  # inclusive, so +1

    return fresh_qty


if __name__ == "__main__":
    parsed_ranges, parsed_test_vals = get_inputs()
    print(f"Solution 1: {solution_1(parsed_ranges, parsed_test_vals)}")
    print(f"Solution 2: {solution_2(parsed_ranges)}")
