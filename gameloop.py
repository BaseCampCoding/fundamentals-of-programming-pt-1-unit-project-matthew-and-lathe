import cards


def show_cards(d_hand: list, p_hand: list) -> None:
    """Simply prints out the player and dealer's hands"""
    card_split = [card.split("\n") for card in d_hand]
    zipped = zip(*card_split)
    for elems in zipped:
        print("".join(elems))
    print()
    card_split = [card.split("\n") for card in p_hand]
    zipped = zip(*card_split)
    for elems in zipped:
        print("".join(elems))

def add_to_hand(new_deck: list, hands: list, display_hands: list, is_player: bool) -> None:
    current_card = new_deck.pop()
    if is_player == True:
        hands.append(current_card)
        display_hands.append(cards.print_card(current_card))
    else:
        hands.append(current_card)
        display_hands.append(cards.print_card([]))

def play_round():
    new_deck = cards.make_new_deck()
    hands = []
    display_hands = []
    dealer_hands = []
    display_dealer_hands = []
    for i in range(2):
        add_to_hand(new_deck, hands, display_hands, True)
        add_to_hand(new_deck, dealer_hands, display_dealer_hands, False)

    hand_value = 0
    while hand_value <= 21:
        show_cards(display_dealer_hands, display_hands)
        print("-------------")
        print("Hit or Stand?")
        print("-------------")
        player_choice = input()
        player_choice = player_choice.lower()
        while player_choice != "hit" and player_choice != "stand":
            print("Please enter hit or stand.")
        if player_choice == "hit":
            add_to_hand(new_deck, hands, display_hands, True)
            hand_value = cards.get_hand_value(hands)
        if player_choice == "stand":
            break
    hand_value = cards.get_hand_value(hands)
    print(f"Hand's Value: {hand_value}")

play_round()
