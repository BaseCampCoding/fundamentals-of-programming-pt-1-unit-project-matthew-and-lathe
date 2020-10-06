import cards

def play_round():
    new_deck = cards.make_new_deck()
    hands = []
    display_hands = []
    dealer_hands = []
    display_dealer_hands = []
    for i in range(2):
        current_card = new_deck.pop()
        hands.append(current_card)
        display_hands.append(cards.print_card(current_card))

        current_card = new_deck.pop()
        dealer_hands.append(current_card)
        display_dealer_hands.append(cards.print_card([]))
    
    for card in display_dealer_hands:
        print(card, sep='')  
    
play_round()