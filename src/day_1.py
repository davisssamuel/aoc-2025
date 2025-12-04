import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Not enough arguments")
        exit()

    pos = 50
    zero_count = 0

    with open(sys.argv[1]) as f:
        for line in f:
            clicks = int(line[1:])
            delta = -clicks if line[0] == "L" else clicks

            # Part 1
            # pos = (pos + delta) % 100
            # if pos == 0:
            #     zero_count += 1

            # Part 2
            start = pos
            pos = (pos + delta) % 100

            if pos == 0:
                zero_count += 1
            elif delta > 0 and pos < start:
                zero_count += 1
            elif start != 0 and delta < 0 and pos > start:
                zero_count += 1

            zero_count += clicks // 100

    print(zero_count)
