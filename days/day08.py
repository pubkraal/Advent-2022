#!/usr/bin/env python3


def main():
    with open("../input/08.txt") as rd:
        grid = [[int(y) for y in x.strip()] for x in rd.readlines()]

    print("p1:", count_visible_trees(grid))
    print("p2:", find_highest_scenic_score(grid))


def find_highest_scenic_score(grid):
    max_score = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            max_score = max([get_scenic_score(grid, y, x), max_score])
    return max_score


def get_scenic_score(grid, y, x):
    height = grid[y][x]
    west = 0
    east = 0
    north = 0
    south = 0

    # look west
    for vx in range(x, 0, -1):
        west += 1
        if grid[y][vx - 1] >= height:
            break

    # look east
    for vx in range(x + 1, len(grid[0])):
        east += 1
        if grid[y][vx] >= height:
            break

    # look north
    for vy in range(y, 0, -1):
        north += 1
        if grid[vy - 1][x] >= height:
            break

    # look south
    for vy in range(y + 1, len(grid)):
        south += 1
        if grid[vy][x] >= height:
            break

    return west * east * north * south


def count_visible_trees(grid):
    visible = (len(grid) * 2) + ((len(grid[0]) - 2) * 2)
    height = len(grid) - 2
    width = len(grid[0]) - 2

    for y in range(1, height + 1):
        for x in range(1, width + 1):
            vis = is_visible(grid, y, x)
            visible += 1 if vis else 0

    return visible


def is_visible(grid, y, x):
    height = grid[y][x]
    # The dumb way is to just look at it from every angle
    # So guess what I did

    # From the west
    for vx in range(x):
        if grid[y][vx] >= height:
            break
    else:
        return True

    # From the east
    for vx in range(x + 1, len(grid[0])):
        if grid[y][vx] >= height:
            break
    else:
        return True

    # From the north
    for vy in range(y):
        if grid[vy][x] >= height:
            break
    else:
        return True

    # From the south
    for vy in range(y + 1, len(grid)):
        if grid[vy][x] >= height:
            break
    else:
        return True
    return False


if __name__ == "__main__":
    testinput = [
        [3, 0, 3, 7, 3],
        [2, 5, 5, 1, 2],
        [6, 5, 3, 3, 2],
        [3, 3, 5, 4, 9],
        [3, 5, 3, 9, 0],
    ]
    assert count_visible_trees(testinput) == 21
    assert find_highest_scenic_score(testinput) == 8
    main()
