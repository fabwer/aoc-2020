from collections import defaultdict

# from itertools import count


def read_numbers_from_txt(filename):
    try:
        with open(filename) as f:
            return list(map(int, f.read().split(',')))
    except OSError as identifier:
        return []


def play_memory_game(starting_nums, end):
    seq = defaultdict(list)
    # count(1) might be better for large ranges (ram usage) because range() inits an array, count() only single variables
    for i in range(1, end + 1):
        if i <= len(starting_nums):
            current = starting_nums[i-1]
        elif len(seq[last_num]) == 1:
            current = 0
        else:
            current = seq[last_num][-1] - seq[last_num][-2]
        # if i == end:
        #     return current
        seq[current].append(i)
        last_num = current
    return current
