import time


def main():
    engine_schematic = open("input.txt")
    calculate_engine_parts(engine_schematic)
    calculate_gear_ratios(engine_schematic)


def profiler(func):
    def wrapper_method(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, time.time()-start, result)
        return result
    return wrapper_method


@profiler
def calculate_engine_parts(engine_schematic):
    engine_schematic.seek(0)
    engine_schematic = engine_schematic.read().strip().split("\n")
    total_engine_parts = 0

    for row, row_char in enumerate(engine_schematic):
        number = []
        symbol_adjacent = False
        for col, col_char in enumerate(engine_schematic[row] + "."):
            if col_char.isdigit():
                number.append(col_char)
                for iter_row in range(max(0, row-1), min(row+2, len(engine_schematic)-1)):
                    for iter_col in range(max(0, col-1), min(col+2, len(engine_schematic[iter_row])-1)):
                        if engine_schematic[iter_row][iter_col] not in [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                            symbol_adjacent = True
            else:
                if number and symbol_adjacent:
                    total_engine_parts = total_engine_parts + int("".join(number))
                number = []
                symbol_adjacent = False
    return total_engine_parts


@profiler
def calculate_gear_ratios(engine_schematic):
    engine_schematic.seek(0)
    engine_schematic = engine_schematic.read().strip().split("\n")
    total_engine_parts = 0
    asterisk_dict = {}

    for row, row_char in enumerate(engine_schematic):
        number = []
        asterisk_coord = 0

        for col, col_char in enumerate(engine_schematic[row] + "."):
            if col_char.isdigit():
                number.append(col_char)
                for iter_row in range(max(0, row-1), min(row+2, len(engine_schematic)-1)):
                    for iter_col in range(max(0, col-1), min(col+2, len(engine_schematic[iter_row])-1)):
                        if engine_schematic[iter_row][iter_col] not in [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                            asterisk_coord = (iter_row, iter_col)
            else:
                if number and asterisk_coord:
                    asterisk_dict[asterisk_coord] = asterisk_dict[asterisk_coord] + [int("".join(number))] if asterisk_coord in asterisk_dict else [int("".join(number))]
                number = []
                asterisk_coord = 0

    for keys in asterisk_dict.keys():
        if len(asterisk_dict[keys]) > 1:
            total_engine_parts = total_engine_parts + asterisk_dict[keys][0]*asterisk_dict[keys][1]
    return total_engine_parts


if __name__ == "__main__":
    main()
