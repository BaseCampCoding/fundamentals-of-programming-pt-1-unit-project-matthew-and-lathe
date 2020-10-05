from dataclasses import dataclass
from random import shuffle
# ♣, ♦, ♥, ♠
@dataclass
class Card ():
    rank: str
    suit: str


def makeNewDeck () -> list:
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    SUITS = ['♣', '♦', '♥', '♠']
    newDeck = []
    for s in SUITS:
        for r in RANKS:
            newDeck.append([s, r])
    shuffle(newDeck)
    return newDeck

    