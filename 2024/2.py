from pathlib import Path


def load_input(path: Path) -> list[str]:
    with open(path) as file:
        return [line.rstrip() for line in file]


def report_is_safe(levels: list[int]) -> bool:
    decreasing = None

    for i in range(1, len(levels)):
        prev = levels[i-1]
        curr = levels[i]

        difference = abs(prev - curr)
        if not 1 <= difference <= 3:
            return False

        curr_trend_decr = prev > curr
        if decreasing is None:
            decreasing = curr_trend_decr
        elif decreasing != curr_trend_decr:
            return False

    return True


def part_one() -> int:
    safe_count = 0

    for line in load_input(Path("2.txt")):
        report = [int(val) for val in line.split()]
        safe_count += 1 if report_is_safe(report) else 0

    return safe_count


def part_two() -> int:
    safe_count = 0

    for line in load_input(Path("2.txt")):
        report = [int(val) for val in line.split()]
        for i in range(len(report)):
            new_report = [val for val in report]
            new_report.pop(i)

            if report_is_safe(new_report):
                safe_count += 1
                break

    return safe_count


if __name__ == "__main__":
    print(f"Part 1: {part_one()}")
    print(f"Part 2: {part_two()}")
