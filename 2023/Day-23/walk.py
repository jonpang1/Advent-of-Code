import time
import sys

sys.setrecursionlimit(10000000)

def profiler(func):
    def wrapper_method(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, time.time()-start, result)
        return result
    return wrapper_method


def main():
    island_map = open("input.txt")
    find_longest_path_1(island_map)
    find_longest_path_2(island_map)


@profiler
def find_longest_path_2(island_map):
    island_map.seek(0)
    island_map = island_map.read().strip().split("\n")
#     island_map = """#.#####################
# #.......#########...###
# #######.#########.#.###
# ###.....#.>.>.###.#.###
# ###v#####.#v#.###.#.###
# ###.>...#.#.#.....#...#
# ###v###.#.#.#########.#
# ###...#.#.#.......#...#
# #####.#.#.#######.#.###
# #.....#.#.#.......#...#
# #.#####.#.#.#########v#
# #.#...#...#...###...>.#
# #.#.#v#######v###.###v#
# #...#.>.#...>.>.#.###.#
# #####v#.#.###v#.#.###.#
# #.....#...#...#.#.#...#
# #.#########.###.#.#.###
# #...###...#...#...#.###
# ###.###.#.###v#####v###
# #...#...#.#.>.>.#.>.###
# #.###.###.#.###.#.#v###
# #.....###...###...#...#
# #####################.#""".split("\n")

    starting_point = (0, island_map[0].find("."))
    previous_location = "up"
    visited_nodes = [starting_point]
    for i, point in enumerate(calculate_longest_path_2(island_map, (1, starting_point[1]), previous_location, visited_nodes.copy())[0]):
        if point == (140, 139):
            print(i)
    print(calculate_longest_path_2(island_map, (1, starting_point[1]), previous_location, visited_nodes.copy())[0])


def calculate_longest_path_2(island_map, point, previous_location, visited_nodes):
    ending_point = (len(island_map)-1, island_map[-1].find("."))
    previous_next = {"up": "down",
                     "down": "up",
                     "left": "right",
                     "right": "left"}
    single_path = True
    single_path_length = 1
    visited_nodes.append(point)
    while single_path:
        if len(island_map) == point[0] + 1:
            return visited_nodes, single_path_length

        next_locations = {"up": (point[0] - 1, point[1]),
                          "down": (point[0] + 1, point[1]),
                          "left": (point[0], point[1] - 1),
                          "right": (point[0], point[1] + 1)}

        del next_locations[previous_location]

        for item in list(next_locations):
            if (island_map[next_locations[item][0]][next_locations[item][1]] == "#") or (next_locations[item] in visited_nodes):
                del next_locations[item]

        if len(next_locations) == 1:
            single_path_length = single_path_length + 1
            location, point = next_locations.popitem()
            previous_location = previous_next[location]
            visited_nodes.append(point)
        elif len(next_locations) == 0:
            return [], 0
        else:
            single_path = False

    max_path_length = 0
    for previous_location in next_locations:
        nodes, path_length = calculate_longest_path_2(island_map, next_locations[previous_location], previous_next[previous_location], visited_nodes.copy())
        if (ending_point in nodes) and (max_path_length < path_length):
            max_path_length = path_length
            visited_nodes = nodes
    return visited_nodes, single_path_length + max_path_length


@profiler
def find_longest_path_1(island_map):
    island_map.seek(0)
    island_map = island_map.read().strip().split("\n")

    starting_point = (0, island_map[0].find("."))
    previous_location = "up"
    return calculate_longest_path_1(island_map, (1, starting_point[1]), previous_location)


def calculate_longest_path_1(island_map, point, previous_location):
    if (len(island_map) == point[0]) or \
            (island_map[point[0]][point[1]] == "#") or \
            (island_map[point[0]][point[1]] == ">" and previous_location == "right") or \
            (island_map[point[0]][point[1]] == "<" and previous_location == "left") or \
            (island_map[point[0]][point[1]] == "v" and previous_location == "down") or \
            (island_map[point[0]][point[1]] == "^" and previous_location == "up"):
        return 0
    next_locations = {"up": (point[0] - 1, point[1]),
                      "down": (point[0] + 1, point[1]),
                      "left": (point[0], point[1] - 1),
                      "right": (point[0], point[1] + 1)}
    if island_map[point[0]][point[1]] == ">":
        return 1 + calculate_longest_path_1(island_map, (point[0], point[1] + 1), "left")
    elif island_map[point[0]][point[1]] == "<":
        return 1 + calculate_longest_path_1(island_map, (point[0], point[1] - 1), "right")
    elif island_map[point[0]][point[1]] == "v":
        return 1 + calculate_longest_path_1(island_map, (point[0] + 1, point[1]), "up")
    elif island_map[point[0]][point[1]] == "^":
        return 1 + calculate_longest_path_1(island_map, (point[0] - 1, point[1]), "down")
    elif previous_location == "up":
        return 1 + max(calculate_longest_path_1(island_map, next_locations["down"], "up"),
                       calculate_longest_path_1(island_map, next_locations["left"], "right"),
                       calculate_longest_path_1(island_map, next_locations["right"], "left"))
    elif previous_location == "down":
        return 1 + max(calculate_longest_path_1(island_map, next_locations["up"], "down"),
                       calculate_longest_path_1(island_map, next_locations["left"], "right"),
                       calculate_longest_path_1(island_map, next_locations["right"], "left"))
    elif previous_location == "left":
        return 1 + max(calculate_longest_path_1(island_map, next_locations["up"], "down"),
                       calculate_longest_path_1(island_map, next_locations["down"], "up"),
                       calculate_longest_path_1(island_map, next_locations["right"], "left"))
    elif previous_location == "right":
        return 1 + max(calculate_longest_path_1(island_map, next_locations["up"], "down"),
                       calculate_longest_path_1(island_map, next_locations["down"], "up"),
                       calculate_longest_path_1(island_map, next_locations["left"], "right"))


if __name__ == "__main__":
    main()
