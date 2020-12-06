def read_data_from_txt(filename) -> list:
    try:
        with open(filename) as f:
            # todo
            return []
    except OSError as identifier:
        return []
