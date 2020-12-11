def read_data_from_txt(filename) -> list:
    try:
        with open(filename) as f:
            return [line.strip().split() for line in f.readlines()]
    except OSError as identifier:
        return []

def run(instructions: list):
    i = 0
    acc = 0
    visited = set()
    while True:
        # part 1
        if i in visited:
            return (acc, False)
        # part 2
        elif i == len(instructions):
            return (acc, True)
        visited.add(i)
        instruction = instructions[i][0]
        value = int(instructions[i][1])
        if instruction == 'acc':
            acc += value
        if instruction == 'jmp':
            i += value
        else:
            i += 1
