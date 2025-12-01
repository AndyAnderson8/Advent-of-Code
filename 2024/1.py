from pathlib import Path


def load_input(path: Path) -> list[str]:
    with open(path) as file:
        return [line.rstrip() for line in file]


def get_lists() -> tuple[list[int], list[int]]:
    left_list = []
    right_list = []

    for line in load_input(Path("1.txt")):
        left_val, right_val = line.split()
        left_list.append(int(left_val))
        right_list.append(int(right_val))

    return left_list, right_list


def part_one() -> int:
    left_list, right_list = get_lists()

    left_list.sort()
    right_list.sort()

    total = 0
    for i in range(len(left_list)):
        total += abs(left_list[i] - right_list[i])

    return total


def part_two() -> int:
    left_list, right_list = get_lists()

    similarity_map = {}
    for l_val in left_list:
        if l_val not in similarity_map:
            count = 0
            for r_val in right_list:
                if l_val == r_val:
                    count += 1

            similarity_map[l_val] = l_val * count

        else:
            similarity_map[l_val] += similarity_map[l_val]

    return sum(similarity_map.values())


if __name__ == "__main__":
    print(f"Part 1: {part_one()}")
    print(f"Part 2: {part_two()}")
