def read_vector_from_txt(filename):
    try:
        with open(filename) as f:
            return [int(scalar.strip("\n")) for scalar in f]
    except OSError as identifier:
        return []
