#!/usr/bin/env python3


def elf_generator(rd):
    elf = []
    for line in rd.readlines():
        x = line.strip()
        if x == "":
            yield elf
            elf = []
            continue
        elf.append(int(x))
    yield elf


def main():
    elves = []
    elvessums = []
    elf = []
    with open("../input/01.txt") as rd:
        for elf in elf_generator(rd):
            elves.append(elf)
            elvessums.append(sum(elf))
    elvessums = sorted(elvessums, reverse=True)
    print("p1:", elvessums[0])
    print("p2:", sum(elvessums[0:3]))


if __name__ == "__main__":
    main()
