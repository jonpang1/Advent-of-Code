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
    # find_page_order(inputs)
    correct_page_order(inputs)


@profiler
def find_page_order(inputs):
    inputs.seek(0)
    rules_dict = {}
    total = 0

    for line in inputs:
        if "|" in line:
            nums = line.strip().split("|")
            if nums[1] not in rules_dict:
                rules_dict[nums[1]] = [nums[0]]
            else:
                rules_dict[nums[1]].append(nums[0])

        elif "," in line:
            rules_followed = True
            pages = line.strip().split(",")
            for i, page in enumerate(pages):
                if rules_followed is False:
                    break
                for j in range(i + 1, len(pages)):
                    if pages[j] in rules_dict[page]:
                        rules_followed = False
                        break
            if rules_followed:
                total = total + int(pages[int(len(pages) / 2)])
    return total


@profiler
def correct_page_order(inputs):
    inputs.seek(0)
    rules_dict = {}
    total = 0

    for line in inputs:
        if "|" in line:
            nums = line.strip().split("|")
            if nums[1] not in rules_dict:
                rules_dict[nums[1]] = [nums[0]]
            else:
                rules_dict[nums[1]].append(nums[0])
        elif "," in line:
            pages = line.strip().split(",")

            new_pages = []
            original_rules_followed = True
            while len(pages) > 0:
                rules_followed = True
                i = 0

                for j in range(i + 1, len(pages)):
                    if (pages[i] in rules_dict) and (pages[j] in rules_dict[pages[i]]):
                        original_rules_followed = False
                        rules_followed = False
                        pages.insert(j, pages.pop(i))
                        break

                if rules_followed:
                    new_pages.append(pages.pop(i))

            if original_rules_followed is False:
                total = total + int(new_pages[int(len(new_pages) / 2)])
    return total


if __name__ == "__main__":
    main()
