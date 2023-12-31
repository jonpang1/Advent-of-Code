import time


def profiler(func):
    def wrapper_method(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, time.time()-start, result)
        return result
    return wrapper_method


def main():
    histories = open("input.txt")
    extrapolate_next_value(histories)
    extrapolate_previous_value(histories)


@profiler
def extrapolate_next_value(histories):
    histories.seek(0)
    histories = histories.read().strip().split("\n")

    total_next_number = 0
    for history in histories:
        history = history.split(" ")
        total_next_number = total_next_number + find_next_number(history)
    return total_next_number


def find_next_number(history):
    history_set = set(history)
    if (len(history_set) == 1) and (0 in history_set):
        return int(history[1]) - int(history[0])
    return find_next_number([int(history[i+1]) - int(history[i]) for i, _ in enumerate(history) if i + 1 < len(history)]) + int(history[-1])


@profiler
def extrapolate_previous_value(histories):
    histories.seek(0)
    histories = histories.read().strip().split("\n")

    total_previous_number = 0
    for history in histories:
        history = history.split(" ")
        total_previous_number = total_previous_number + find_previous_number(history)
    return total_previous_number


def find_previous_number(history):
    history_set = set(history)
    if (len(history_set) == 1) and (0 in history_set):
        return int(history[1]) - int(history[0])
    return int(history[0]) - find_previous_number([int(history[i+1]) - int(history[i]) for i, _ in enumerate(history) if i + 1 < len(history)])


if __name__ == "__main__":
    main()
