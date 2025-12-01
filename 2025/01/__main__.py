from pathlib import Path

from utils import parse_input_to_lines


def solution(
    include_zero_passes: bool,
    input_file: Path = Path("input.txt"),
    curr_pos: int = 50,
    max_clicks: int = 100,
) -> int:
    turns = parse_input_to_lines(input_file)
    zero_counter = 0

    for turn in turns:
        direction = turn[0]
        value = int(turn[1:])

        # reduce value early - reducing later with directional loops makes logic harder
        while abs(value) > max_clicks:
            value -= max_clicks
            zero_counter += 1 if include_zero_passes else 0
        value = -value if direction == "L" else value

        prev_pos = curr_pos
        curr_pos += value

        if curr_pos >= max_clicks:  # i.e., turned right past 0
            curr_pos -= max_clicks

            # edge case: checking didn't end on 100
            if include_zero_passes and curr_pos != 0:
                zero_counter += 1

        if curr_pos < 0:  # i.e., turned left past 0
            curr_pos += max_clicks

            # edge case: checking it didn't start on 0
            if include_zero_passes and prev_pos != 0:
                zero_counter += 1

        if curr_pos == 0:
            zero_counter += 1

    return zero_counter


if __name__ == "__main__":
    print(f"Solution 1: {solution(False)}")
    print(f"Solution 2: {solution(True)}")
