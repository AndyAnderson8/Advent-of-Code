from pathlib import Path


def parse_input_to_lines(file_path: Path) -> list[str]:
    with open(file_path, "r") as file:
        return [line.rstrip() for line in file]
