import time


def profiler(func):
    def wrapper_method(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, time.time()-start, result)
        return result
    return wrapper_method


def main():
    race_records = open("input.txt")
    calculate_record_possibilities_1(race_records)
    calculate_record_possibilities_2(race_records)


@profiler
def calculate_record_possibilities_1(race_records):
    race_records.seek(0)
    race_records = race_records.read().strip().split("\n")
    times = " ".join(race_records[0].split(":")[1].split()).split(" ")
    distances = " ".join(race_records[1].split(":")[1].split()).split(" ")

    multiplied_no_ways = 1
    for i, record_time in enumerate(times):
        no_ways = 0
        for j in range(0, int(record_time)+1):
            if j * (int(record_time) - j) > int(distances[i]):
                no_ways = (int(record_time) + 1) - (j * 2)
                break
            else:
                no_ways
        multiplied_no_ways = multiplied_no_ways * no_ways
    return multiplied_no_ways


@profiler
def calculate_record_possibilities_2(race_records):
    race_records.seek(0)
    race_records = race_records.read().strip().split("\n")
    times = [race_records[0].split(":")[1].replace(" ", "")]
    distances = [race_records[1].split(":")[1].replace(" ", "")]

    multiplied_no_ways = 1
    for i, record_time in enumerate(times):
        no_ways = 0
        for j in range(0, int(record_time)+1):
            if j * (int(record_time) - j) > int(distances[i]):
                no_ways = (int(record_time) + 1) - (j * 2)
                break
            else:
                no_ways
        multiplied_no_ways = multiplied_no_ways * no_ways
    return multiplied_no_ways


if __name__ == "__main__":
    main()
