def read_binary_numbers_from_txt(filename) -> list:
    try:
        with open(filename) as f:
            data_list = []
            for data in f.read().split("\n"):
                row = int(data[0:7].replace("F", "0").replace("B", "1"), 2)
                column = int(data[7:].replace("L", "0").replace("R", "1"), 2)
                data_list.append([row, column])
            return data_list
    except OSError as identifier:
        return []
