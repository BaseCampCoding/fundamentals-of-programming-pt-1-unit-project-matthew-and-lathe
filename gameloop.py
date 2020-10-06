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

    show_cards(display_dealer_hands, display_hands)

    print("-------------")
    print("Hit or Stand?")
    print("-------------")
    player_choice = input()
    player_choice = player_choice.lower()
    while player_choice != "hit" and player_choice != "stand":
        print("Please enter hit or stand.")
    if player_choice == "hit":
        print()  # here goes function
    if player_choice == "stand":
        hand_value = cards.get_hand_value(hands)
