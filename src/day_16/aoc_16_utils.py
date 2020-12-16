def read_data_from_txt(filename):
    try:
        with open(filename) as f:
            return [line.strip() for line in f.readlines()]
    except OSError as identifier:
        return []
