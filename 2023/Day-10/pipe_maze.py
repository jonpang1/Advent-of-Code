import math
import time


def profiler(func):
    def wrapper_method(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, time.time()-start, result)
        return result
    return wrapper_method


def main():
    pipe_maze = open("mirage.py")
    find_farthest_point(pipe_maze)


@profiler
def find_farthest_point(pipe_maze):
    pipe_maze.seek(0)
    pipe_maze = pipe_maze.read().strip().split("\n")
    for i, line in enumerate(pipe_maze):
        if "S" in line:
            starting_point = (i, line.find("S"))
    visited_points = []
    visited_symbols = []
    distance = 0
    location = starting_point
    previous_symbol = "S"
    while "S" not in visited_symbols:
        if previous_symbol == "J":
            possible_locations = [(location[0] - 1, location[1]), (location[0], location[1] - 1)]
        elif previous_symbol == "L":
            possible_locations = [(location[0], location[1] + 1), (location[0] - 1, location[1])]
        elif previous_symbol == "7":
            possible_locations = [(location[0], location[1] - 1), (location[0] + 1, location[1])]
        elif previous_symbol == "F":
            possible_locations = [(location[0], location[1] + 1), (location[0] + 1, location[1])]
        elif previous_symbol == "-":
            possible_locations = [(location[0], location[1] + 1), (location[0], location[1] - 1)]
        elif previous_symbol == "|":
            possible_locations = [(location[0] + 1, location[1]), (location[0] - 1, location[1])]
        else:
            possible_locations = [(location[0] + 1, location[1]),
                                  (location[0] - 1, location[1]),
                                  (location[0], location[1] + 1),
                                  (location[0], location[1] - 1)]
        if (((location[0], location[1] + 1) in possible_locations) and
                ((location[0], location[1] + 1) not in visited_points) and
                ((pipe_maze[location[0]][location[1] + 1] == "J") or
                 (pipe_maze[location[0]][location[1] + 1] == "7") or
                 (pipe_maze[location[0]][location[1] + 1] == "-"))):
            location = (location[0], location[1] + 1)
            distance = distance + 1
        elif (((location[0], location[1] - 1) in possible_locations) and
              ((location[0], location[1] - 1) not in visited_points) and
                ((pipe_maze[location[0]][location[1] - 1] == "F") or
                 (pipe_maze[location[0]][location[1] - 1] == "L") or
                 (pipe_maze[location[0]][location[1] - 1] == "-"))):
            location = (location[0], location[1] - 1)
            distance = distance + 1
        elif (((location[0] - 1, location[1]) in possible_locations) and
              ((location[0] - 1, location[1]) not in visited_points) and
                ((pipe_maze[location[0] - 1][location[1]] == "F") or
                 (pipe_maze[location[0] - 1][location[1]] == "7") or
                 (pipe_maze[location[0] - 1][location[1]] == "|"))):
            location = (location[0] - 1, location[1])
            distance = distance + 1
        elif (((location[0] + 1, location[1]) in possible_locations) and
              ((location[0] + 1, location[1]) not in visited_points) and
                ((pipe_maze[location[0] + 1][location[1]] == "J") or
                 (pipe_maze[location[0] + 1][location[1]] == "L") or
                 (pipe_maze[location[0] + 1][location[1]] == "|"))):
            location = (location[0] + 1, location[1])
            distance = distance + 1

        previous_symbol = pipe_maze[location[0]][location[1]]
        visited_points.append(location)
        visited_symbols.append(previous_symbol)
    return math.ceil(distance/2)


if __name__ == "__main__":
    main()
