def read_lines_from_txt(filename):
    try:
        with open(filename) as f:
            return [line.strip() for line in f]
    except OSError as identifier:
        return []
