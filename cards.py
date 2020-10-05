from random import shuffle
# ♣, ♦, ♥, ♠
def makeNewDeck () -> list:
    """This function takes in no data, but returns a shuffled deck, in which is stored
    as a 2D List, with the first element of every sublist being the suit, and the second
    element being the rank, both being strings"""
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    SUITS = ['♣', '♦', '♥', '♠']
    newDeck = []
    for s in SUITS:
        for r in RANKS:
            newDeck.append([s, r])
    shuffle(newDeck)
    return newDeck

def printCard (card: list) -> None:
    """This function prints the specially formatted cards
    >>> printCard(['♠', 'A'])
    #####
    #A  #
    #   #
    #  ♠#
    #####
    
    """
    newString = f"""
    #####
    #{card[1]}  #
    #   #
    #  {card[0]}#
    #####
    """
    print(newString)