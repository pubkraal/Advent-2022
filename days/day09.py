#!/usr/bin/env python3.11


def main():
    with open("../input/09.txt") as rd:
        data = [x.strip().split() for x in rd.readlines()]

    print("p1:", part1(data))
    print("p2:", part2(data))


def part2(moves):
    head = (0, 0)
    tails = [
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
    ]
    touched = set()

    for move in moves:
        vector = (0, 0)
        match move[0]:
            case "R":
                vector = (1, 0)
            case "L":
                vector = (-1, 0)
            case "U":
                vector = (0, 1)
            case "D":
                vector = (0, -1)
        num = int(move[1])

        for x in range(num):
            head = (head[0] + vector[0], head[1] + vector[1])
            new_tail = move_tail(head, tails[0], vector)
            tail_vector = detect_vector(tails[0], new_tail)
            tails[0] = new_tail
            for y in range(1, 9):
                new_tail = move_tail(tails[y - 1], tails[y], tail_vector)
                tail_vector = detect_vector(tails[y], new_tail)
                tails[y] = new_tail
            touched.add(tails[-1])
            print("step:", move, head, tails)

    print("end:", len(touched))
    return len(touched)


def detect_vector(old, new):
    return (new[0] - old[0], new[1] - old[1])


def part1(moves):
    head = (0, 0)
    tail = (0, 0)
    touched = set()
    for move in moves:
        vector = (0, 0)
        match move[0]:
            case "R":
                vector = (1, 0)
            case "L":
                vector = (-1, 0)
            case "U":
                vector = (0, 1)
            case "D":
                vector = (0, -1)
        num = int(move[1])
        for x in range(num):
            head = (head[0] + vector[0], head[1] + vector[1])
            tail = move_tail(head, tail, vector)
            touched.add(tail)
    return len(touched)


def move_tail(head, tail, vector):
    # Tail needs to touch head at all times, so both can be max 1 off, and
    # otherwise we have to move it to behind

    # still touching
    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
        return tail

    # No longer touching, so find vector head moved and follow
    n = (head[0] - vector[0], head[1] - vector[1])
    return n


if __name__ == "__main__":
    testinput = [
        ("R", "4"),
        ("U", "4"),
        ("L", "3"),
        ("D", "1"),
        ("R", "4"),
        ("D", "1"),
        ("L", "5"),
        ("R", "2"),
    ]
    testinput2 = [
        ("R", "5"),
        ("U", "8"),
        ("L", "8"),
        ("D", "3"),
        ("R", "17"),
        ("D", "10"),
        ("L", "25"),
        ("U", "20"),
    ]
    assert part1(testinput) == 13
    assert part2(testinput) == 1
    assert part2(testinput2) == 36
    main()
