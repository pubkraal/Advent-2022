#!/usr/bin/env python3
import re
import collections

INSTRUCTIONRE = re.compile(r"move (\d+) from (\d+) to (\d+)")


def main():
    lines = []

    with open("../input/05.txt") as rd:
        lines = list(rd)
    msg, msg2 = move(lines)
    print("p1:", msg)
    print("p2:", msg2)


def move(lines):
    # Build initial stack
    for idx, line in enumerate(lines):
        line = line.strip()
        if line == "":
            break

    stacks = build_stacks(lines[:idx])
    stacks2 = build_stacks(lines[:idx])

    # go through instructions
    for line in lines[idx + 1 :]:
        num, frm, to = INSTRUCTIONRE.findall(line)[0]
        tmp = []
        for x in range(int(num)):
            stacks[int(to)].append(stacks[int(frm)].pop())
            tmp.append(stacks2[int(frm)].pop())
        for x in range(int(num)):
            stacks2[int(to)].append(tmp.pop())

    msg = "".join([stacks[k].pop() for k in sorted(stacks.keys())])
    msg2 = "".join([stacks2[k].pop() for k in sorted(stacks.keys())])
    return msg, msg2


def build_stacks(lines):
    stacks = {}
    for col in lines[-1].split():
        stacks[int(col)] = []
    keys = sorted(stacks.keys())
    for row in lines[::-1][1:]:
        for k in keys:
            val = row[((k - 1) * 4) + 1]
            if val != " ":
                stacks[k].append(val)
    return stacks


if __name__ == "__main__":
    testinput = [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
        "",
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]
    assert move(testinput) == ("CMZ", "MCD")
    main()
