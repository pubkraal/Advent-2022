#!/usr/bin/env python3


def main():
    data = ""
    with open("../input/06.txt") as rd:
        data = rd.read().strip()

    print("p1:", find_packet_marker(data))
    print("p2:", find_message_marker(data))


def find_marker(data: str, size: int) -> int:
    for x in range(len(data) - size):
        if len(set(data[x : x + size])) == size:
            return x + size
    return 0


def find_packet_marker(data: str) -> int:
    return find_marker(data, 4)


def find_message_marker(data: str) -> int:
    return find_marker(data, 14)


if __name__ == "__main__":
    assert find_packet_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert find_packet_marker("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert find_packet_marker("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert find_packet_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert find_packet_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11

    assert find_message_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert find_message_marker("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert find_message_marker("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert find_message_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert find_message_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26
    main()
