from math import floor, log10

from utils import load_lines


def main(input_path):
    lines = load_lines(input_path)
    part1_count = 0
    ranges = lines[0].split(",")

    for r in ranges:
        bounds = r.split("-")
        start = int(bounds[0])
        end = int(bounds[1])
        part1_count += part1(start, end)

    print(f"Part 1: {part1_count}")

def part1(start: int, end: int) -> int:
    invalid_count = 0

    for n in range(start, end + 1):
        mask = 0
        num_digits = floor(log10(n) + 1)

        for i in range(0, num_digits):
            digit = (n // 10**i) % 10
            mask = ~(mask ^ digit) & 0xF
            # print(f"number: {n:<10} index: {i} digit: {digit} mask: {num_mask:04b}")

        if mask == 0:
            invalid_count += n

    return invalid_count
