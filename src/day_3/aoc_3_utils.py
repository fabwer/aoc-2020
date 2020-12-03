def read_matrix_from_txt(filename):
    try:
        with open(filename) as f:
            return [list(line.strip("\n")) for line in f]
    except OSError as identifier:
        return []
