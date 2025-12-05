def read_lines(input_path: str) -> list[str]:
    with open(input_path) as f:
        return f.readlines()
