import copy


def read_matrix_from_txt(filename):
    try:
        with open(filename) as f:
            return [list(line.strip('\n')) for line in f]
    except OSError as identifier:
        return []


def get_adjacent_cells(matrix, x_coord, y_coord, adjacency, direction):
    for dx, dy in adjacency:
        if 0 <= (x_coord + dx) < len(matrix) and 0 <= y_coord + dy < len(matrix[0]):
            dx_res = dx
            dy_res = dy
            if direction:
                while True:
                    if not (0 <= (x_coord + dx_res) < len(matrix) and 0 <= (y_coord + dy_res) < len(matrix[0])):
                        dx_res -= dx
                        dy_res -= dy
                        break
                    if matrix[x_coord + dx_res][y_coord + dy_res] != '.':
                        break
                    dx_res += dx
                    dy_res += dy
            yield matrix[x_coord + dx_res][y_coord + dy_res]


def calc_seats(layout, adjacency, limit, direction):
    cont = True
    run_count = 0
    while cont:
        prev_layout = copy.deepcopy(layout)
        for i in range(0, len(layout)):
            for j in range(0, len(layout[0])):
                current = prev_layout[i][j]
                if current != '.':
                    counter_empty = 0
                    counter_full = 0
                    for adj_cell in get_adjacent_cells(prev_layout, i, j, adjacency, direction):
                        if current == 'L':
                            if adj_cell == '#':
                                counter_empty += 1
                        if current == '#':
                            if adj_cell == '#':
                                counter_full += 1
                    if counter_empty == 0:
                        layout[i][j] = '#'
                    if counter_full >= limit:
                        layout[i][j] = 'L'
        cont = prev_layout != layout
        run_count += 1

    print('Number of optimization rounds: ', run_count)
    return layout
