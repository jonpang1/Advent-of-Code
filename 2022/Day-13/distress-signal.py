import itertools


def main():
    distress_signals = open("input.txt")
    # print(compare_packet_pairs(distress_signals))
    print(compare_packet2([[10], [7, 5, 7], [], [[[8, 7, 5], [10, 2, 1], 9, 2]], [[1]]],
                         [[10], [7, 5, 7], [], [[[8, 7, 5], [10, 2, 1], 9, 2]], [[]]]))
    # print(order_packets(distress_signals))


def compare_packet_pairs(distress_signals):
    distress_signals.seek(0)
    distress_signals = distress_signals.read().split("\n\n")

    sum_indices = 0
    for index, distress_signal_pair in enumerate(distress_signals):
        distress_signal_1 = eval(distress_signal_pair.split("\n")[0])
        distress_signal_2 = eval(distress_signal_pair.split("\n")[1])

        if compare_packet2(distress_signal_1, distress_signal_2):
            sum_indices = sum_indices + index + 1

    return sum_indices


def order_packets(distress_signals):
    distress_signals.seek(0)
    distress_signals = list(filter(None, distress_signals.read().split("\n")))
    print(distress_signals)


def compare_packet2(packet1, packet2):
    print(packet1)
    print(packet2)
    result = ""
    for item1, item2 in itertools.zip_longest(packet1, packet2):
        if isinstance(item1, int) and isinstance(item2, int):
            if item1 < item2:
                return True
            elif item1 > item2:
                return False
        elif isinstance(item1, list) and isinstance(item2, list):
            result = compare_packet2(item1, item2)
        elif (list in (type(item1), type(item2))) and (int in (type(item1), type(item2))):
            items = [([item1, ], item2) if (type(item1) is int) else (item1, [item2, ])]
            result = compare_packet(items[0][0], items[0][1])
        elif item1 is None:
            return True
        elif item2 is None:
            return False

        if result is not None:
            return result
    return result

def compare_packet(packet1, packet2):
    result = ""

    # Check if empty list
    if (len(packet1) == 0) or (len(packet2) == 0):
        if (not packet1) and (not packet2):
            result = "Equal"
        elif not packet1:
            return True
        else:
            return False
    for item1, item2 in itertools.zip_longest(packet1, packet2, fillvalue=None):
        if packet1 is None:
            return True
        elif packet2 is None:
            return False
        # Compare ints
        if (type(item1) is int) and (type(item2) is int):
            if item1 < item2:
                return True
            elif item1 > item2:
                return False
            else:
                result = "Equal"
                continue
        # Compare lengths
        elif (item1 is None) or (item2 is None):
            if item1 is None:
                return True
            elif item2 is None:
                return False
        # Compare mixed types
        elif (list in (type(item1), type(item2))) and (int in (type(item1), type(item2))):
            items = [([item1, ], item2) if (type(item1) is int) else (item1, [item2, ])]
            result = compare_packet(items[0][0], items[0][1])

        # Compare list of lists
        else:
            result = compare_packet(item1, item2)

        if result != "Equal":
            return result

    return result


if __name__ == "__main__":
    main()
