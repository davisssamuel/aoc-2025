void main(String[] args) throws Exception {
    if (args.length < 1) {
        IO.println("Not enough arguments");
        return;
    }
    String input = Files.readString(Paths.get(args[0]));

    int pos = 50;
    int partOneCount = 0;
    int partTwoCount = 0;

    for (String line : input.split("\n")) {
        int clicks = Integer.parseInt(line.substring(1));
        int delta = (line.charAt(0) == 'L') ? -clicks : clicks;

        int start = pos;
        pos = Math.floorMod(pos + delta, 100);

        if (pos == 0) {
            partOneCount++;
        } else if ((delta > 0 && pos < start) ||  (start != 0 && delta < 0 && pos > start)) {
            partTwoCount++;
        }

        partTwoCount += Math.floorDiv(clicks, 100);
    }

    IO.println("Part 1: " + partOneCount + "\nPart 2: " + (partOneCount + partTwoCount));
}
