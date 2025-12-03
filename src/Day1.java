void main(String[] args) throws Exception {
    if (args.length < 1) {
        IO.println("Not enough arguments");
        return;
    }
    String input = Files.readString(Paths.get(args[0]));

    int pos = 50;
    int zeroCount = 0;

    for (String line : input.split("\n")) {
        int clicks = Integer.parseInt(line.substring(1));
        int delta = (line.charAt(0) == 'L') ? -clicks : clicks;

        int start = pos;

        // Part 1
        pos = (pos + delta) % 100;
        if (pos == 0) zeroCount++;

        // Part 2
        double cycles = clicks / 100.0;
        if (cycles < 1 &&
            ((delta > 0 && pos < start) || (delta < 0 && pos > start))) {
            zeroCount++;
        }
        zeroCount += Math.floor(cycles);
    }

    IO.println("Expected: 7199");
    IO.println("Actual: " + zeroCount);
}
