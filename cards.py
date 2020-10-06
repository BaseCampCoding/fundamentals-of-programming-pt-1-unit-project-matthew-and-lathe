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
    else:
        new_string = f"""
        #####
        #{card[1]}  #
        #   #
        #  {card[0]}#
        #####
        """
    return new_string