import time


def profiler(func):
    def wrapper_method(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, time.time()-start, result)
        return result
    return wrapper_method


def main():
    platform = open("mirage.py")
    calculate_total_load_1(platform)
    calculate_total_load_2(platform)


@profiler
def calculate_total_load_2(platform):
    platform.seek(0)
    platform = platform.read().strip().split("\n")
    transposed_platform = [list(i) for i in zip(*platform)]

    score = 0
    for i, line in enumerate(transposed_platform):
        rocks_dict = {"O": [], "#": []}
        for j, char in enumerate(transposed_platform[i]):
            if char == "O":
                rocks_dict["O"].append(j)
            elif char == "#":
                rocks_dict["#"].append(j)

        position = 0
        while len(rocks_dict["O"]) > 0:
            if (len(rocks_dict["#"]) == 0) or (rocks_dict["O"][0] < rocks_dict["#"][0]):
                position = position + 1
                score = score + len(line) - position + 1
                rocks_dict["O"].pop(0)
            else:
                position = rocks_dict["#"][0] + 1
                rocks_dict["#"].pop(0)


@profiler
def calculate_total_load_1(platform):
    platform.seek(0)
    platform = platform.read().strip().split("\n")
    transposed_platform = [list(i) for i in zip(*platform)]

    score = 0
    for i, line in enumerate(transposed_platform):
        rocks_dict = {"O": [], "#": []}
        for j, char in enumerate(transposed_platform[i]):
            if char == "O":
                rocks_dict["O"].append(j)
            elif char == "#":
                rocks_dict["#"].append(j)

        position = 0
        while len(rocks_dict["O"]) > 0:
            if (len(rocks_dict["#"]) == 0) or (rocks_dict["O"][0] < rocks_dict["#"][0]):
                position = position + 1
                score = score + len(line) - position + 1
                rocks_dict["O"].pop(0)
            else:
                position = rocks_dict["#"][0] + 1
                rocks_dict["#"].pop(0)
    return score


if __name__ == "__main__":
    main()
