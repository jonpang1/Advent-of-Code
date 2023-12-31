import time


def profiler(func):
    def wrapper_method(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, time.time()-start, result)
        return result
    return wrapper_method


def main():
    camel_cards = open("input.txt")
    calculate_winnings_1(camel_cards)
    calculate_winnings_2(camel_cards)


@profiler
def calculate_winnings_1(camel_cards):
    camel_cards.seek(0)
    camel_cards = camel_cards.read().strip().split("\n")
    ordered_hands = {7: [], 6: [], 5: [], 4: [], 3: [], 2: [], 1: []}
    all_ordered_hands = []
    total_winnings = 0
    for camel_card in camel_cards:
        hand, bid = camel_card.split(" ")
        strength = calculate_hand_1(hand)
        ordered_hands[strength].append((hand, bid))

    for i in range(1, 8):
        all_ordered_hands = all_ordered_hands + order_hands_1(ordered_hands[i])

    for i in range(len(all_ordered_hands)):
        total_winnings = total_winnings + int(all_ordered_hands[i][1]) * (i + 1)
    return total_winnings


def order_hands_1(hands):
    if len(hands) < 2:
        return hands

    midpoint = len(hands) // 2
    return merge_1(
        order_hands_1(hands[:midpoint]),
        order_hands_1(hands[midpoint:])
    )


def merge_1(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if compare_hands_1(left[index_left][0], right[index_right][0]):
            result.append(left[index_left])
            index_left = index_left + 1
        else:
            result.append(right[index_right])
            index_right = index_right + 1

        if index_right == len(right):
            result = result + left[index_left:]
            break

        if index_left == len(left):
            result = result + right[index_right:]
    return result


def compare_hands_1(hand1, hand2):
    card_values = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2, "1": 1}
    for i, char in enumerate(hand1):
        if card_values[char] > card_values[hand2[i]]:
            return False
        elif card_values[char] < card_values[hand2[i]]:
            return True
        else:
            continue


def calculate_hand_1(hand):
    duplicates = {}
    for char in hand:
        if char not in duplicates.keys():
            duplicates[char] = 1
        else:
            duplicates[char] = duplicates[char] + 1

    if 5 in duplicates.values():
        return 7
    elif 4 in duplicates.values():
        return 6
    elif (3 in duplicates.values()) and (2 in duplicates.values()):
        return 5
    elif 3 in duplicates.values():
        return 4
    elif 2 in duplicates.values():
        remove_2_duplicates = list(duplicates.values())
        remove_2_duplicates.remove(2)
        if 2 in remove_2_duplicates:
            return 3
        else:
            return 2
    else:
        return 1


@profiler
def calculate_winnings_2(camel_cards):
    camel_cards.seek(0)
    camel_cards = camel_cards.read().strip().split("\n")
    ordered_hands = {7: [], 6: [], 5: [], 4: [], 3: [], 2: [], 1: []}
    all_ordered_hands = []
    total_winnings = 0
    for camel_card in camel_cards:
        hand, bid = camel_card.split(" ")
        strength = calculate_hand_2(hand)
        ordered_hands[strength].append((hand, bid))

    for i in range(1, 8):
        all_ordered_hands = all_ordered_hands + order_hands_2(ordered_hands[i])

    for i in range(len(all_ordered_hands)):
        total_winnings = total_winnings + int(all_ordered_hands[i][1]) * (i + 1)
    return total_winnings


def order_hands_2(hands):
    if len(hands) < 2:
        return hands

    midpoint = len(hands) // 2
    return merge_2(
        order_hands_2(hands[:midpoint]),
        order_hands_2(hands[midpoint:])
    )


def merge_2(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if compare_hands_2(left[index_left][0], right[index_right][0]):
            result.append(left[index_left])
            index_left = index_left + 1
        else:
            result.append(right[index_right])
            index_right = index_right + 1

        if index_right == len(right):
            result = result + left[index_left:]
            break

        if index_left == len(left):
            result = result + right[index_right:]
    return result


def compare_hands_2(hand1, hand2):
    card_values = {"A": 14, "K": 13, "Q": 12, "J": 0, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2, "1": 1}
    for i, char in enumerate(hand1):
        if card_values[char] > card_values[hand2[i]]:
            return False
        elif card_values[char] < card_values[hand2[i]]:
            return True
        else:
            continue


def calculate_hand_2(hand):
    duplicates = {}
    for char in hand:
        if char not in duplicates.keys():
            duplicates[char] = 1
        else:
            duplicates[char] = duplicates[char] + 1

    if ("J" in duplicates.keys()) and (len(duplicates.keys()) > 1):
        add_value = duplicates["J"]
        del duplicates["J"]
        for key in duplicates.keys():
            if duplicates[key] == max(duplicates.values()):
                duplicates[key] = duplicates[key] + add_value
                break

    if 5 in duplicates.values():
        return 7
    elif 4 in duplicates.values():
        return 6
    elif (3 in duplicates.values()) and (2 in duplicates.values()):
        return 5
    elif 3 in duplicates.values():
        return 4
    elif 2 in duplicates.values():
        remove_2_duplicates = list(duplicates.values())
        remove_2_duplicates.remove(2)
        if 2 in remove_2_duplicates:
            return 3
        else:
            return 2
    else:
        return 1


if __name__ == "__main__":
    main()
