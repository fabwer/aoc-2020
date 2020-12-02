import re


def read_string_from_txt(filename):
    try:
        with open(filename) as f:
            return [line.strip("\n") for line in f]
    except OSError as identifier:
        return []


def contains_min_max(line):
    min = int(line[0])
    max = int(line[1])
    char = str(line[2])
    string = str(line[3])
    return min <= string.count(char) <= max


def contains_exact_position_once(line):
    pos1 = int(line[0]) - 1
    pos2 = int(line[1]) - 1
    char = str(line[2])
    string = str(line[3])
    return len([m.start() for m in re.finditer(char, string) if m.start() == pos1 or m.start() == pos2]) == 1
