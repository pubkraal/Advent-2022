#!/usr/bin/env python3

SCORING = {
    ("A", "X"): 4,  # rock rock tie 3+1
    ("A", "Y"): 8,  # rock paper win 6+2
    ("A", "Z"): 3,  # rock scissors lose 0+3
    ("B", "X"): 1,  # paper rock lose 0+1
    ("B", "Y"): 5,  # paper paper tie 3+2
    ("B", "Z"): 9,  # paper scissors win 6+3
    ("C", "X"): 7,  # scissors rock win 6+1
    ("C", "Y"): 2,  # scissors paper lose 0+2
    ("C", "Z"): 6,  # scissors scissors tie 3+3
}

SCORING2 = {
    ("A", "X"): 3,  # rock, must lose = scissors 3+0
    ("A", "Y"): 4,  # rock, must draw = rock 1+3
    ("A", "Z"): 8,  # rock, must win = paper 2+6
    ("B", "X"): 1,  # paper, must lose = rock 1+0
    ("B", "Y"): 5,  # paper, must draw = paper 2+3
    ("B", "Z"): 9,  # paper, must win = scissors 6+3
    ("C", "X"): 2,  # scissors, must lose = paper 2+0
    ("C", "Y"): 6,  # scissors, must draw = scissors 3+3
    ("C", "Z"): 7,  # scissors, must win = rock 1+6
}


def main():
    instructions = []
    with open("../input/02.txt") as rd:
        for line in rd.readlines():
            instructions.append(line.split())

    p1, p2 = score(instructions)

    print("p1,", p1)
    print("p2,", p2)


def score(instructions):
    score = 0
    score2 = 0
    for a, b in instructions:
        score += SCORING[(a, b)]
        score2 += SCORING2[(a, b)]
    return score, score2


if __name__ == "__main__":
    assert (15, 12) == score(
        [
            ("A", "Y"),
            ("B", "X"),
            ("C", "Z"),
        ]
    )
    main()
