from pathlib import Path

from utils import parse_input_to_lines


def solution(battery_qty: int, input_file: Path = Path("input.txt")) -> int:
    batt_banks = parse_input_to_lines(input_file)
    jolts_sum = 0

    for batt_bank in batt_banks:
        max_bank_jolts = 0

        for curr_magnitude in range(battery_qty, 0, -1):
            # Chop off N end elements so they're still available for successive iterations
            # Also, apparently [:-0] resolves to [:0], so the new list would always be empty, hence the "or None"... Very dumb!
            elig_batts = batt_bank[:-(curr_magnitude - 1) or None]
            max_batt = max(map(int, elig_batts))

            # Move the list up to last idx found
            batt_bank = batt_bank[batt_bank.index(str(max_batt)) + 1:]

            max_bank_jolts *= 10  # Shift total val over, open a new ones-place for new value
            max_bank_jolts += max_batt

        jolts_sum += max_bank_jolts

    return jolts_sum


if __name__ == "__main__":
    print(f"Solution 1: {solution(2)}")
    print(f"Solution 1: {solution(12)}")
