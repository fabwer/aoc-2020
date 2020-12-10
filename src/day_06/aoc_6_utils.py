def read_data_from_txt(filename) -> list:
    try:
        with open(filename) as f:
            return f.read().split('\n\n')
    except OSError as identifier:
        return []
