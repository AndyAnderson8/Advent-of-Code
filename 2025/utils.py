from pathlib import Path


def parse_input_to_lines(file_path: Path, char: str = "\n", keep_whitespace: bool = False) -> list[str]:
    text = Path(file_path).read_text()
    elems = text.split(char)

    if elems[-1] == "":
        elems = elems[:-1]

    if not keep_whitespace:
        elems = [elem.strip() for elem in elems]

    return elems
