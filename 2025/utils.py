from pathlib import Path

def parse_input_to_lines(file_path: Path, char: str = "\n") -> list[str]:
    text = Path(file_path).read_text()
    return [cleaned.strip() for cleaned in text.split(char)]

