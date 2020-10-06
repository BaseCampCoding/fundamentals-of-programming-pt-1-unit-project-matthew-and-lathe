import cards

def play_round():
    new_deck = cards.make_new_deck()
    hands = []
    dealer_hands = []
    for i in range(2):
        hands.append(new_deck.pop())
        dealer_hands.append(new_deck.pop())
    
