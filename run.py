import importlib
import sys
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 run.py <day> <file>")
        sys.exit(1)

    day_num = int(sys.argv[1])
    input_file = sys.argv[2] if len(sys.argv) >= 3 else "input.txt"

    module_name = f"day{day_num:02d}.solution"
    module = importlib.import_module(module_name)

    # Construct path like day03/example.txt
    input_path = Path(f"day{day_num:02d}") / input_file

    if not input_path.exists():
        print(f"Input file not found: {input_path}")
        sys.exit(1)

    module.main(input_path)

if __name__ == "__main__":
    main()
