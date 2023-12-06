import time


def profiler(func):
    def wrapper_method(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, time.time()-start, result)
        return result
    return wrapper_method


def main():
    scratchcards = open("input.txt")
    calculate_winnings(scratchcards)
    calculate_total_scratchcards(scratchcards)


@profiler
def calculate_winnings(scratchcards):
    scratchcards.seek(0)
    total_winnings = 0
    for card in scratchcards:
        no_wins = 0
        winning_nos = card[card.find(":") + 1:].split("|")[0].strip().replace("  ", " ").split(" ")
        own_nos = card[card.find(":"):].split("|")[1].strip().replace("  ", " ").split(" ")
        for own_no in own_nos:
            if own_no in winning_nos:
                no_wins = no_wins + 1
        total_winnings = total_winnings + (2 ** (no_wins - 1)) if no_wins else total_winnings
    return total_winnings


@profiler
def calculate_total_scratchcards(scratchcards):
    scratchcards.seek(0)
    scratchcards = list(scratchcards)
    no_wins_dict = {}
    no_cards_dict = {}
    for card_no, card in enumerate(scratchcards):
        winning_nos = card[card.find(":") + 1:].split("|")[0].strip().replace("  ", " ").split(" ")
        own_nos = card[card.find(":"):].split("|")[1].strip().replace("  ", " ").split(" ")
        no_wins = 0
        for own_no in own_nos:
            if own_no in winning_nos:
                no_wins = no_wins + 1
        no_wins_dict[card_no + 1] = no_wins
        no_cards_dict[card_no + 1] = 1

    for card_no, card in enumerate(scratchcards):
        for i in range(1, no_wins_dict[card_no + 1] + 1):
            no_cards_dict[card_no + 1 + i] = no_cards_dict[card_no + 1 + i] + no_cards_dict[card_no + 1]
    return sum(no_cards_dict.values())


if __name__ == "__main__":
    main()
