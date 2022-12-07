#!/usr/bin/env python3

from collections import namedtuple

NODE = namedtuple("Node", ["name", "size", "type", "children"])


def main():
    lines = []
    with open("../input/07.txt") as rd:
        lines = [l.strip() for l in rd.readlines()]

    # print(len(lines))
    print("p1:", part1(lines))
    print("p2:", part2(lines))


def part1(instructions):
    # Passing lines [1:] because the first is always cd /
    root, remaining_instructions = build_tree("/", instructions[1:])
    assert len(remaining_instructions) == 0
    return sum([calc_size(n) for n in find_max_sized_nodes(root, 100000)])


def part2(instructions):
    root, remaining_instructions = build_tree("/", instructions[1:])
    assert len(remaining_instructions) == 0

    totsize = 70000000
    req = 30000000
    used = calc_size(root)
    free = totsize - used
    need = req - free
    return min(
        [calc_size(n) for n in find_all_nodes(root) if calc_size(n) > need]
    )


def find_all_nodes(root):
    nodes = [root]
    for child in root.children:
        if child.type == "dir":
            nodes += find_all_nodes(child)
    return nodes


def find_max_sized_nodes(node, maxsize):
    nodes = []
    if calc_size(node) < maxsize:
        nodes.append(node)
    for child in node.children:
        if child.type == "dir":
            nodes += find_max_sized_nodes(child, maxsize)
    return nodes


def build_tree(name, instructions):
    current = NODE(name, 0, "dir", [])

    # instructions I care about:
    # \$ cd \.\.$   -> return
    # \$ cd .*$     -> dive deeper
    # \$ ls         -> list nodes

    while len(instructions):
        instruction = instructions.pop(0)
        if instruction == "$ cd ..":
            return current, instructions
        elif instruction == "$ ls":
            # do some reading of nodes here
            # only append files
            while len(instructions) > 0 and not instructions[0].startswith(
                "$"
            ):
                nxt = instructions.pop(0)
                if not nxt.startswith("dir"):
                    size, name = nxt.split(" ", 1)
                    current.children.append(
                        NODE(name, int(size), "file", None)
                    )
        elif instruction[:4] == "$ cd":
            newnode, rem = build_tree(instruction[5:], instructions)
            current.children.append(newnode)
            instructions = rem

    return current, []


def calc_size(node):
    size = 0
    for child in node.children:
        if child.type == "file":
            size += child.size
        else:
            size += calc_size(child)
    return size


if __name__ == "__main__":
    testinput = [
        "$ cd /",
        "$ ls",
        "dir a",
        "14848514 b.txt",
        "8504156 c.dat",
        "dir d",
        "$ cd a",
        "$ ls",
        "dir e",
        "29116 f",
        "2557 g",
        "62596 h.lst",
        "$ cd e",
        "$ ls",
        "584 i",
        "$ cd ..",
        "$ cd ..",
        "$ cd d",
        "$ ls",
        "4060174 j",
        "8033020 d.log",
        "5626152 d.ext",
        "7214296 k",
    ]

    assert part1(testinput) == 95437
    assert part2(testinput) == 24933642

    main()
