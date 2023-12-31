import math
import functools
import time


def profiler(func):
    def wrapper_method(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, time.time()-start, result)
        return result
    return wrapper_method


def main():
    network = open("../Day-9/mirage.py")
    calculate_steps_1(network)
    calculate_steps_2(network)


@profiler
def calculate_steps_1(network):
    network.seek(0)
    directions, paths = network.read().split("\n\n")
    network_dict = {}
    for path in paths.strip().split("\n"):
        network_dict[path.split("=")[0].strip()] = (path.split("=")[1].strip()[1:4], path.split("=")[1].strip()[6:9])

    node = "AAA"
    direction_index = 0
    directions = directions.replace("L", "0")
    directions = directions.replace("R", "1")
    while node != "ZZZ":
        node = network_dict[node][int(directions[direction_index % len(directions)])].strip()
        direction_index = (direction_index + 1)
    return direction_index


@profiler
def calculate_steps_2(network):
    network.seek(0)
    directions, paths = network.read().split("\n\n")
    network_dict = {}
    for path in paths.strip().split("\n"):
        network_dict[path.split("=")[0].strip()] = (path.split("=")[1].strip()[1:4], path.split("=")[1].strip()[6:9])

    direction_index_list = []
    directions = directions.replace("L", "0")
    directions = directions.replace("R", "1")
    for node in network_dict.keys():
        direction_index = 0
        next_node = network_dict[node][int(directions[direction_index % len(directions)])].strip()
        direction_index = direction_index + 1
        if node[2] == "A":
            while next_node[2] != "Z":
                next_node = network_dict[next_node][int(directions[direction_index % len(directions)])].strip()
                direction_index = direction_index + 1
        direction_index_list.append(direction_index)

    return functools.reduce(lambda x,y: math.lcm(x, y), direction_index_list)


if __name__ == "__main__":
    main()
