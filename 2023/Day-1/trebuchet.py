import time


def profiler(func):
    def wrapper_method(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, time.time()-start, result)
        return result
    return wrapper_method


def main():
    cal_inputs = open("input.txt")
    extract_numerical_digits(cal_inputs)
    extract_any_digits(cal_inputs)


@profiler
def extract_numerical_digits(cal_inputs):
    cal_inputs.seek(0)
    total_cal_values = 0

    for cal_input in cal_inputs:
        cal_digits = list(filter(str.isdigit, cal_input))
        total_cal_values = total_cal_values + int(str(list(cal_digits)[0]) + str(list(cal_digits)[-1]))
    return total_cal_values


@profiler
def extract_any_digits(cal_inputs):
    cal_inputs.seek(0)
    word_digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}
    total_cal_values = 0

    for cal_input in cal_inputs:
        min_word_indices = {cal_input.find(word_digit): word_digit for word_digit in word_digits}
        min_word_index = min(filter(lambda x: x > -1, min_word_indices.keys()), default=None)
        max_word_indices = {cal_input.rfind(word_digit): word_digit for word_digit in word_digits}
        max_word_index = max(filter(lambda x: x > -1, max_word_indices.keys()), default=None)
        digit_indices = [x for x, is_digit in enumerate([x.isdigit() for x in cal_input]) if is_digit is True]
        digit_1 = word_digits[min_word_indices[min_word_index]] if min_word_index is not None and (min_word_index < digit_indices[0]) else cal_input[digit_indices[0]]
        digit_2 = word_digits[max_word_indices[max_word_index]] if max_word_index is not None and (max_word_index > digit_indices[-1]) else cal_input[digit_indices[-1]]
        total_cal_values = total_cal_values + int(str(digit_1) + str(digit_2))
    return total_cal_values


if __name__ == "__main__":
    main()
