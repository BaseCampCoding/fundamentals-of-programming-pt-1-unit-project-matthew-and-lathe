import cards


def main_game(money, minumum_bet):
    newdeck = cards.makeNewDeck()
    current_card = newdeck.pop()
    cards.printCard(current_card)
