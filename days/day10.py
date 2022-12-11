#!/usr/bin/env python3.11


def main():
    with open("../input/10.txt") as rd:
        instructions = (x.strip() for x in rd.readlines())

    strength, history = execute(instructions, [20, 60, 100, 140, 180, 220])

    print("p1:", strength)
    print("p2:")
    render(history)


def render(data):
    line = []
    for idx, val in enumerate(data):
        # if idx < 80:
        #     print(idx, val - 1, val, val + 1)
        if val - 1 <= idx % 40 <= val + 1:
            line.append("#")
        else:
            line.append(".")

    line = "".join(line)
    print(line[:40])
    print(line[40:80])
    print(line[80:120])
    print(line[120:160])
    print(line[160:200])
    print(line[200:240])


def execute(instructions, datapoints=None):
    collect = []
    if datapoints is not None:
        collect = sorted(datapoints)
    signal = 1
    counter = 0
    strength = 0

    datahist = []

    for instruction in instructions:
        val = 0
        datahist.append(signal)
        if instruction.startswith("addx"):
            val = int(instruction.split(" ")[1])
            datahist.append(signal)
            counter += 2
        elif instruction == "noop":
            counter += 1

        if collect and counter >= collect[0]:
            cnt = collect.pop(0)
            strength += signal * cnt

        signal += val
    return strength, datahist


if __name__ == "__main__":
    testinput = [
        "addx 15",
        "addx -11",
        "addx 6",
        "addx -3",
        "addx 5",
        "addx -1",
        "addx -8",
        "addx 13",
        "addx 4",
        "noop",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx -35",
        "addx 1",
        "addx 24",
        "addx -19",
        "addx 1",
        "addx 16",
        "addx -11",
        "noop",
        "noop",
        "addx 21",
        "addx -15",
        "noop",
        "noop",
        "addx -3",
        "addx 9",
        "addx 1",
        "addx -3",
        "addx 8",
        "addx 1",
        "addx 5",
        "noop",
        "noop",
        "noop",
        "noop",
        "noop",
        "addx -36",
        "noop",
        "addx 1",
        "addx 7",
        "noop",
        "noop",
        "noop",
        "addx 2",
        "addx 6",
        "noop",
        "noop",
        "noop",
        "noop",
        "noop",
        "addx 1",
        "noop",
        "noop",
        "addx 7",
        "addx 1",
        "noop",
        "addx -13",
        "addx 13",
        "addx 7",
        "noop",
        "addx 1",
        "addx -33",
        "noop",
        "noop",
        "noop",
        "addx 2",
        "noop",
        "noop",
        "noop",
        "addx 8",
        "noop",
        "addx -1",
        "addx 2",
        "addx 1",
        "noop",
        "addx 17",
        "addx -9",
        "addx 1",
        "addx 1",
        "addx -3",
        "addx 11",
        "noop",
        "noop",
        "addx 1",
        "noop",
        "addx 1",
        "noop",
        "noop",
        "addx -13",
        "addx -19",
        "addx 1",
        "addx 3",
        "addx 26",
        "addx -30",
        "addx 12",
        "addx -1",
        "addx 3",
        "addx 1",
        "noop",
        "noop",
        "noop",
        "addx -9",
        "addx 18",
        "addx 1",
        "addx 2",
        "noop",
        "noop",
        "addx 9",
        "noop",
        "noop",
        "noop",
        "addx -1",
        "addx 2",
        "addx -37",
        "addx 1",
        "addx 3",
        "noop",
        "addx 15",
        "addx -21",
        "addx 22",
        "addx -6",
        "addx 1",
        "noop",
        "addx 2",
        "addx 1",
        "noop",
        "addx -10",
        "noop",
        "noop",
        "addx 20",
        "addx 1",
        "addx 2",
        "addx 2",
        "addx -6",
        "addx -11",
        "noop",
        "noop",
        "noop",
    ]
    assert execute(testinput, [20, 60, 100, 140, 180, 220])[0] == 13140
    main()
