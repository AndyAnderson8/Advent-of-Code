from pathlib import Path


def parse_input_to_lines(file_path: Path, char: str = "\n") -> list[str]:
    text = Path(file_path).read_text()
    elems = text.split(char)
    return [elem.strip() for elem in elems if elem.strip() != ""]
