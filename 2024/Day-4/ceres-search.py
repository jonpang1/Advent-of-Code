import time


def profiler(func):
    def wrapper_method(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, time.time() - start, result)
        return result

    return wrapper_method


def main():
    inputs = open("input.txt")
    

@profiler
def something():
    pass


if __name__ == "__main__":
    main()
