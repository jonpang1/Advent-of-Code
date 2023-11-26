def main():
    rucksack_contents = open("input.txt")
    print(find_common_1(rucksack_contents))
    print(find_common_2(rucksack_contents))


def find_common_1(rucksack_contents):
    rucksack_contents.seek(0)
    total_priorities = 0

    for items in rucksack_contents:
        items = items[:-1]
        length = int(len(items[:-1])/2 + 1)

        common = set(items[:length]).intersection(set(items[length:]))
        total_priorities = total_priorities + sum([ord(x)-ord("a")+1 if x.islower() else ord(x)-ord("A")+27 for x in common])

    return total_priorities


def find_common_2(rucksack_contents):
    rucksack_contents.seek(0)
    total_priorities = 0

    no_groups = int(len(rucksack_contents.readlines())/3)
    rucksack_contents.seek(0)

    for index in range(no_groups):
        rucksack1 = rucksack_contents.readline()[:-1]
        rucksack2 = rucksack_contents.readline()[:-1]
        rucksack3 = rucksack_contents.readline()[:-1]

        common = set(rucksack1).intersection(set(rucksack2)).intersection(set(rucksack3))
        total_priorities = total_priorities + sum([ord(x)-ord("a")+1 if x.islower() else ord(x)-ord("A")+27 for x in common])

    return total_priorities


if __name__ == "__main__":
    main()
