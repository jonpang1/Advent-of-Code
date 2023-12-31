import time


def profiler(func):
    def wrapper_method(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, time.time()-start, result)
        return result
    return wrapper_method


def main():
    galaxy_map = open("mirage.py")
    find_total_galaxy_distances(galaxy_map)
    find_total_galaxy_distances_2(galaxy_map)


@profiler
def find_total_galaxy_distances_2(galaxy_map):
    galaxy_map.seek(0)
    galaxy_map = galaxy_map.read().strip().split("\n")

    empty_rows = []
    empty_cols = []
    galaxy_list = []

    for i in range(len(galaxy_map)):
        line = galaxy_map[i]
        if "#" not in line:
            empty_rows.append(i)

    transposed_galaxy_map = [list(i) for i in zip(*galaxy_map)]
    for i in range(len(transposed_galaxy_map)):
        line = transposed_galaxy_map[i]
        if "#" not in line:
            empty_cols.append(i)

    for i, line in enumerate(galaxy_map):
        for j, char in enumerate(galaxy_map[i]):
            if galaxy_map[i][j] == "#":
                galaxy_list.append((i, j))

    total_manhattan_distance = 0
    for no, galaxy in enumerate(galaxy_list):
        galaxy_no = no + 1
        while galaxy_no < len(galaxy_list):
            total_manhattan_distance = total_manhattan_distance + calculate_manhattan_distance_2(galaxy, galaxy_list[galaxy_no], empty_rows, empty_cols, 1000000)
            galaxy_no = galaxy_no + 1
    return total_manhattan_distance


def calculate_manhattan_distance_2(start_coord, end_coord, empty_rows, empty_cols, empty_add):
    add_manhattan_distance = 0
    for empty_row in empty_rows:
        if empty_row in range(min(start_coord[0], end_coord[0]), max(start_coord[0], end_coord[0]) + 1):
            add_manhattan_distance = add_manhattan_distance + (empty_add - 1)
    for empty_col in empty_cols:
        if empty_col in range(min(start_coord[1], end_coord[1]), max(start_coord[1], end_coord[1]) + 1):
            add_manhattan_distance = add_manhattan_distance + (empty_add - 1)
    return abs((start_coord[1] - end_coord[1])) + abs((start_coord[0] - end_coord[0])) + add_manhattan_distance


@profiler
def find_total_galaxy_distances(galaxy_map):
    galaxy_map.seek(0)
    galaxy_map = galaxy_map.read().strip().split("\n")

    for i in range(len(galaxy_map)-1, -1, -1):
        line = galaxy_map[i]
        if "#" not in line:
            galaxy_map.insert(i, line)

    transposed_galaxy_map = [list(i) for i in zip(*galaxy_map)]
    for i in range(len(transposed_galaxy_map)-1, -1, -1):
        line = transposed_galaxy_map[i]
        if "#" not in line:
            transposed_galaxy_map.insert(i, line)

    galaxy_map = [list(i) for i in zip(*transposed_galaxy_map)]
    galaxy_list = []
    for i, line in enumerate(galaxy_map):
        for j, char in enumerate(galaxy_map[i]):
            if galaxy_map[i][j] == "#":
                galaxy_list.append((i, j))

    total_manhattan_distance = 0
    for no, galaxy in enumerate(galaxy_list):
        galaxy_no = no + 1
        while galaxy_no < len(galaxy_list):
            total_manhattan_distance = total_manhattan_distance + calculate_manhattan_distance(galaxy, galaxy_list[galaxy_no])
            galaxy_no = galaxy_no + 1
    return total_manhattan_distance


def calculate_manhattan_distance(start_coord, end_coord):
    return abs((start_coord[1] - end_coord[1])) + abs((start_coord[0] - end_coord[0]))


if __name__ == "__main__":
    main()
