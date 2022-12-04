#!/usr/bin/env python3


def main():
    data = []
    with open("../input/04.txt") as rd:
        for line in rd.readlines():
            line = line.strip().split(",")
            nums = tuple([int(i) for i in x.split("-")] for x in line)
            data.append(nums)

    print("p1", part1(data))
    print("p2", part2(data))


def part1(sets):
    return sum(
        1 if subset(s[0], s[1]) or subset(s[1], s[0]) else 0 for s in sets
    )


def part2(sets):
    return sum(1 if overlap(s[0], s[1]) else 0 for s in sets)


def subset(a, b):
    return a[0] >= b[0] and a[1] <= b[1]


def overlap(a, b):
    return (
        b[0] <= a[0] <= b[1]  # a starts somewhere in b
        or b[0] <= a[1] <= b[1]  # a ends somewhere in b
        or (a[0] <= b[0] and a[1] >= b[1])  # a fully overlaps b
        or (b[0] <= a[0] and b[1] >= a[1])  # b fully overlaps a
    )


if __name__ == "__main__":
    testinput = [
        ((2, 4), (6, 8)),
        ((2, 3), (4, 5)),
        ((5, 7), (7, 9)),
        ((2, 8), (3, 7)),
        ((6, 6), (4, 6)),
        ((2, 6), (4, 8)),
    ]
    assert part1(testinput) == 2
    assert part2(testinput) == 4
    main()
