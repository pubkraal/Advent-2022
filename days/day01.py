#!/usr/bin/env python3


def main():
    elves = []
    elvessums = []
    elf = []
    with open("../input/01.txt") as rd:
        for line in rd.readlines():
            x = line.strip()
            if x == "":
                elves.append(elf)
                elvessums.append(sum(elf))
                elf = []
                continue

            elf.append(int(x))
        elvessums.append(sum(elf))
        elves.append(elf)
    elvessums = sorted(elvessums, reverse=True)
    print("p1:", elvessums[0])
    print("p2:", sum(elvessums[0:3]))


if __name__ == "__main__":
    main()
