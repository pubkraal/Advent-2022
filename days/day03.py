#!/usr/bin/env python3


def main():
    data = []
    with open("../input/03.txt") as rd:
        data = [line.strip() for line in rd.readlines()]

    print("p1", part1(data))
    print("p2", part2(data))


def part2(instructions):
    p2 = 0
    for i in range(len(instructions) // 3):
        s = i * 3
        item = (
            set(instructions[s])
            & set(instructions[s + 1])
            & set(instructions[s + 2])
        )
        for x in item:
            p2 += score_item(x)
    return p2


def part1(instructions):
    common = []
    for line in instructions:
        h1 = line[: len(line) // 2]
        h2 = line[len(line) // 2 :]

        for x in set(h1) & set(h2):
            common.append(x)

    return sum([score_item(x) for x in common])


def score_item(item: str) -> int:
    c = ord(item)
    if 65 <= c <= 90:
        return c - ord("A") + 27
    elif 97 <= c <= 122:
        return c - ord("a") + 1
    return 0


if __name__ == "__main__":
    testinput = (
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    )
    assert score_item("A") == 27
    assert score_item("Z") == 52
    assert score_item("a") == 1
    assert score_item("z") == 26
    assert part1(testinput) == 157
    assert part2(testinput) == 70

    main()
