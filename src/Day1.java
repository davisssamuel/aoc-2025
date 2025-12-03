int DIAL_START = 50;

void main(String[] args) throws Exception {
    if (args.length < 1) {
        IO.println("Not enough arguments");
        return;
    }
    String input = Files.readString(Paths.get(args[0]));

    int pos = DIAL_START;
    int zeroCount = 0;

    for (String line : input.split("\n")) {
        int clicks = Integer.parseInt(line.substring(1));
        int delta = (line.charAt(0) == 'L') ? -clicks : clicks;

        // Part 1
        // if (pos == 0) zeroCount++;
        // pos = (pos + delta) % 100;

        // Part 2
        int old = pos;
        pos = (((pos + delta) % 100) + 100) % 100;
        int crossed = Math.floorDiv((old + delta - pos), 100);
        zeroCount += Math.abs(crossed);
    }

    IO.println(zeroCount);
}
