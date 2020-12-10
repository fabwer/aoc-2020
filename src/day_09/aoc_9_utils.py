def read_int_from_txt(filename) -> list:
    try:
        with open(filename) as f:
            return [int(line.strip()) for line in f.readlines()]
    except OSError as identifier:
        return []
