import time


def profiler(func):
    def wrapper_method(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, time.time()-start, result)
        return result
    return wrapper_method


def main():
    seed_map = open("input.txt")
    calculate_lowest_location_1(seed_map)
    calculate_lowest_location_2(seed_map)


@profiler
def calculate_lowest_location_1(seed_map):
    seed_map.seek(0)

    seed_map = seed_map.read().split("\n\n")
    lowest_location = None

    seeds = seed_map[0].split(":")[1].strip().split(" ")
    seed2soil = seed_map[1].split(":")[1].strip().split("\n")
    soil2fertilizer = seed_map[2].split(":")[1].strip().split("\n")
    fertilizer2water = seed_map[3].split(":")[1].strip().split("\n")
    water2light = seed_map[4].split(":")[1].strip().split("\n")
    light2temperature = seed_map[5].split(":")[1].strip().split("\n")
    temperature2humidity = seed_map[6].split(":")[1].strip().split("\n")
    humidity2location = seed_map[7].split(":")[1].strip().split("\n")

    for seed in seeds:
        soil = find_mapped_value(seed, seed2soil)
        fertilizer = find_mapped_value(soil, soil2fertilizer)
        water = find_mapped_value(fertilizer, fertilizer2water)
        light = find_mapped_value(water, water2light)
        temperature = find_mapped_value(light, light2temperature)
        humidity = find_mapped_value(temperature, temperature2humidity)
        location = find_mapped_value(humidity, humidity2location)

        lowest_location = location if (not lowest_location) or (location < lowest_location) else lowest_location

    return lowest_location


def find_mapped_value(value, map_list):
    for lines in map_list:
        line_values = lines.split(" ")
        if (int(value) >= int(line_values[1])) and (int(value) <= int(line_values[1]) + int(line_values[2])):
            return int(line_values[0]) + int(value) - int(line_values[1])
    return value


@profiler
def calculate_lowest_location_2(seed_map):
    seed_map.seek(0)

    seed_map = seed_map.read().split("\n\n")
    seeds = seed_map[0].split(":")[1].strip().split(" ")
    seed2soil = seed_map[1].split(":")[1].strip().split("\n")
    soil2fertilizer = seed_map[2].split(":")[1].strip().split("\n")
    fertilizer2water = seed_map[3].split(":")[1].strip().split("\n")
    water2light = seed_map[4].split(":")[1].strip().split("\n")
    light2temperature = seed_map[5].split(":")[1].strip().split("\n")
    temperature2humidity = seed_map[6].split(":")[1].strip().split("\n")
    humidity2location = seed_map[7].split(":")[1].strip().split("\n")

    unmapped_seed_ranges = []
    for no, seed in enumerate(seeds):
        if no % 2 == 0:
            unmapped_seed_ranges.append((int(seed), int(seed) + int(seeds[no+1])))

    unmapped_soil_ranges = find_mapped_range(unmapped_seed_ranges, seed2soil)
    unmapped_fertilizer_ranges = find_mapped_range(unmapped_soil_ranges, soil2fertilizer)
    unmapped_water_ranges = find_mapped_range(unmapped_fertilizer_ranges, fertilizer2water)
    unmapped_light_ranges = find_mapped_range(unmapped_water_ranges, water2light)
    unmapped_temperature_ranges = find_mapped_range(unmapped_light_ranges, light2temperature)
    unmapped_humidity_ranges = find_mapped_range(unmapped_temperature_ranges, temperature2humidity)
    unmapped_location_ranges = find_mapped_range(unmapped_humidity_ranges, humidity2location)
    return min([min(location) for location in unmapped_location_ranges])


def find_mapped_range(unmapped_ranges, map_list):
    mapped_ranges = []
    while unmapped_ranges:
        starting_val, ending_val = unmapped_ranges[0]
        starting_val, ending_val = int(starting_val), int(ending_val)

        for line in map_list:
            line_values = line.split(" ")
            if (starting_val <= int(line_values[1])) and (ending_val >= int(line_values[1]) + int(line_values[2])):
                mapped_ranges.append((int(line_values[0]), int(line_values[0]) + int(line_values[2])))
                unmapped_ranges.remove((starting_val, ending_val))
                if starting_val < int(line_values[1]):
                    unmapped_ranges.insert(0, (starting_val, int(line_values[1])-1))
                if ending_val > (int(line_values[1]) + int(line_values[2])):
                    unmapped_ranges.insert(0, (int(line_values[1]) + int(line_values[2]) + 1, ending_val))
                break
            elif (starting_val >= int(line_values[1])) and (starting_val <= int(line_values[1]) + int(line_values[2]) - 1):
                mapped_ranges.append((starting_val - int(line_values[1]) + int(line_values[0]), min([ending_val, int(line_values[1]) + int(line_values[2])]) - int(line_values[1]) + int(line_values[0])))
                unmapped_ranges.remove((starting_val, ending_val))
                if ending_val > (int(line_values[1]) + int(line_values[2])):
                    unmapped_ranges.insert(0, (int(line_values[1]) + int(line_values[2]), ending_val))
                break
            elif (ending_val > int(line_values[1])) and (ending_val < int(line_values[1]) + int(line_values[2])):
                mapped_ranges.append((max([starting_val, int(line_values[1])]) - int(line_values[1]) + int(line_values[0]), ending_val - int(line_values[1]) + int(line_values[0])))
                unmapped_ranges.remove((starting_val, ending_val))
                if starting_val < (int(line_values[1])):
                    unmapped_ranges.insert(0, (starting_val, int(line_values[1])-1))
                break

        if (starting_val, ending_val) in unmapped_ranges:
            unmapped_ranges.remove((starting_val, ending_val))
            mapped_ranges.append((starting_val, ending_val))
    return mapped_ranges


if __name__ == "__main__":
    main()
