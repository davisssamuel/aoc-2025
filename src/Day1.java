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

        // Part 1
        // pos = Math.floorMod(pos + delta, 100);
        // if (pos == 0) zeroCount++;

        // Part 2
        int start = pos;
        pos = Math.floorMod(pos + delta, 100);

        if (pos == 0) {
            zeroCount++;
        } else if (delta > 0 && pos < start) {
            zeroCount++;
        } else if (start != 0 && delta < 0 && pos > start) {
            zeroCount++;
        }
        zeroCount += Math.floorDiv(clicks, 100);
    }

    IO.println(zeroCount);
}
