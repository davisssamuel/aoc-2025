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
            for _ in range(clicks):
                if delta > 0:
                    pos = (pos + 1) % 100
                else:
                    pos = (pos - 1) % 100

                if pos == 0:
                    zero_count += 1

    print(zero_count)
