import time


def profiler(func):
    def wrapper_method(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, time.time()-start, result)
        return result
    return wrapper_method


def main():
    condition_records = open("input.txt")
    calculate_possible_conditions(condition_records)


def calculate_possible_conditions(condition_records):
    condition_records.seek(0)
    condition_records = condition_records.read().strip().split("\n")

    for condition_record in condition_records:
        conditions, counts = condition_record.split(" ")
        conditions = conditions.replace("#", 1)
        conditions = conditions.replace(".", 0)

        unknown_conditions = []
        for i, condition in enumerate(conditions):
            if conditions[i] == "?":
                unknown_conditions.append(i)

        full_conditions_list = []
        for no, values in enumerate(unknown_conditions):
            for i in range(2):
                condition = [i]
                for j in range(2):
                    condition.append(j)
                    full_conditions_list.append(conditions)


if __name__ == "__main__":
    main()
