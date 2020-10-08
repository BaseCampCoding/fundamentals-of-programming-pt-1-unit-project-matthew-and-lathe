from random import shuffle

# ♣, ♦, ♥, ♠


def colored_text(line: str, color: int):
    """This function allows the printing out of different colored text
    0 is for red, 1 is for cyan, 2 is for green, 3 is for yellow, 4 is for purple
    for background, False for no background, True for a colorful background"""
    if color == 0:
        print("\033[91m {}\033[00m".format(line))
    elif color == 1:
        print("\033[96m {}\033[00m".format(line))
    elif color == 2:
        print("\033[92m {}\033[00m".format(line))
    elif color == 3:
        print("\033[93m {}\033[00m".format(line))
    elif color == 4:
        print("\033[95m {}\033[00m".format(line))
    elif color == 5:
        print("\033[31m {}\033[00m".format(line))


def show_cards(d_hand: list, p_hand: list, color_one: int, color_two: int) -> None:
    """Simply prints out the player and dealer's hands"""
    card_split = [card.split("\n") for card in d_hand]
    zipped = zip(*card_split)
    print("Dealer:")
    for elems in zipped:
        colored_text("".join(elems), color_one)
    print()
    card_split = [card.split("\n") for card in p_hand]
    zipped = zip(*card_split)
    print("Player:")
    for elems in zipped:
        colored_text("".join(elems), color_two)


def make_new_deck() -> list:
    """This function takes in no data, but returns a shuffled deck, in which is stored
    as a 2D List, with the first element of every sublist being the suit, and the second
    element being the rank, both being strings"""
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["♣", "♦", "♥", "♠"]
    new_deck = []
    for s in SUITS:
        for r in RANKS:
            new_deck.append([s, r])
    shuffle(new_deck)
    return new_deck


def print_card(card: list) -> str:
    """This function prints the specially formatted cards
    >>> printCard(['♠', 'A'])
    #####
    #A  #
    #   #
    #  ♠#
    #####

    """
    new_string = ""
    if not card:
        new_string = """
        #####
        #♠|♥#
        #-+-#
        #♦|♣#
        #####
        """
    elif card[1] != "10":
        new_string = f"""
        #####
        #{card[1]}  #
        #   #
        #  {card[0]}#
        #####
        """
    else:
        new_string = f"""
        #####
        #{card[1]} #
        #   #
        #  {card[0]}#
        #####
        """
    return new_string


def get_hand_value(cards: list) -> int:
    """takes in a hand's cards and determines the value of the hand"""
    has_seen_ace = 0
    value = 0
    for c in cards:
        if c[1] == "A":
            has_seen_ace += 1
        elif c[1] == "K":
            value += 10
        elif c[1] == "Q":
            value += 10
        elif c[1] == "J":
            value += 10
        else:
            value += int(c[1])
    while has_seen_ace > 0:
        if (value + 11) > 21:
            value += 1
        else:
            value += 11
        has_seen_ace -= 1
    return value