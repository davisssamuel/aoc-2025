import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Not enough arguments")
        exit()

    pos = 50
    part_one_count = 0
    part_two_count = 0

    with open(sys.argv[1]) as f:
        for line in f:
            clicks = int(line[1:])
            delta = -clicks if line[0] == "L" else clicks

            start = pos
            pos = (pos + delta) % 100

            if pos == 0:
                part_one_count += 1
            elif (delta > 0 and pos < start) or (start != 0 and delta < 0 and pos > start):
                part_two_count += 1

            part_two_count += clicks // 100

    print(f"Part 1: {part_one_count}\nPart 2: {part_one_count + part_two_count}")
