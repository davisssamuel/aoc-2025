void main(String[] args) throws Exception {
    if (args.length < 1) {
        IO.println("Not enough arguments");
        return;
    }
    String input = Files.readString(Paths.get(args[0]));

    long invalidCount = 0;

    for (String ids : input.split(",")) {
        String[] range = ids.trim().split("-");
        long start = Long.parseLong(range[0]);
        long end = Long.parseLong(range[1]);

        for (long i = start; i <= end; i++) {
            String str = ((Long) i).toString();
            int len = str.length();

            if (len % 2 == 0 && str.substring(0, len / 2).equals(str.substring(len / 2))) {
                invalidCount += i;
            }
        }
    }

    IO.println(invalidCount);
}
