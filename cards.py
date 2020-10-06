from random import shuffle
# ♣, ♦, ♥, ♠
def make_new_deck () -> list:
    """This function takes in no data, but returns a shuffled deck, in which is stored
    as a 2D List, with the first element of every sublist being the suit, and the second
    element being the rank, both being strings"""
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    SUITS = ['♣', '♦', '♥', '♠']
    new_deck = []
    for s in SUITS:
        for r in RANKS:
            new_deck.append([s, r])
    shuffle(new_deck)
    return new_deck

def print_card (card: list) -> str:
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
        #♠+♥#
        #+++#
        #♦+♣#
        #####
        """
    elif card[1] != '10':
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
        if c[1] == 'A':
            has_seen_ace += 1
            print("ACE CARD")
        elif c[1] == 'K':
            value += 10
            print("FACE CARD")
        elif c[1] == 'Q':
            value += 10
            print("FACE CARD")
        elif c[1] == 'J':
            value += 10
            print("FACE CARD")
        else:
            value += int(c[1])
    while has_seen_ace > 0:
        if (value + 11) > 21:
            value += 1
        else:
            value += 11
        has_seen_ace -= 1
    return value