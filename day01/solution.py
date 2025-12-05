from utils import read_lines


def main(input_path):
    lines = read_lines(input_path)
    pos = 50
    part1_count = 0
    part2_count = 0

    for line in lines:
        clicks = int(line[1:])
        delta = -clicks if line[0] == "L" else clicks

        start = pos
        pos = (pos + delta) % 100

        if pos == 0:
            part1_count += 1
        elif (delta > 0 and pos < start) or (start != 0 and delta < 0 and pos > start):
            part2_count += 1

        part2_count += clicks // 100

    print(f"Part 1: {part1_count}\nPart 2: {part1_count + part2_count}")
