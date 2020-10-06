import cards
import doclear
from random import randint
from time import sleep


def show_cards(d_hand: list, p_hand: list) -> None:
    """Simply prints out the player and dealer's hands"""
    card_split = [card.split("\n") for card in d_hand]
    zipped = zip(*card_split)
    print("Dealer:")
    for elems in zipped:
        print("".join(elems))
    print()
    card_split = [card.split("\n") for card in p_hand]
    zipped = zip(*card_split)
    print("Player:")
    for elems in zipped:
        print("".join(elems))


def add_to_hand(
    new_deck: list, hands: list, display_hands: list, is_player: bool
) -> None:
    current_card = new_deck.pop()
    if is_player == True:
        hands.append(current_card)
        display_hands.append(cards.print_card(current_card))
    else:
        hands.append(current_card)
        display_hands.append(cards.print_card([]))


def dealer_ai(value: int, difficulty: int) -> bool:
    """This function will take in the current card value, and return on whether the dealer
    should hit or stand depending on this value. False is for standing, True is for hitting."""
    if value <= 10:
        return True
    elif value <= 13:
        random_value = randint(1, 2)
        if random_value == 2:
            return False
        else:
            return True
    elif value <= 14:
        if difficulty == 0:
            return True
        else:
            random_value = randint(1, 20)
            if random_value == 20:
                return False
            else:
                return True
    elif value <= 17:
        if difficulty == 0:
            random_value = randint(1, 5)
            if random_value == 5:
                return True
            else:
                return False
        elif difficulty == 1:
            random_value = randint(1, 10)
            if random_value == 10:
                return True
            else:
                return False
        else:
            random_value = randint(1, 15)
            if random_value == 10:
                return True
            else:
                return False
    elif value <= 20:
        if difficulty == 0:
            random_value = randint(1, 15)
            if random_value == 10:
                return True
            else:
                return False
        else:
            random_value = randint(1, 100)
            if random_value == 10:
                return True
            else:
                return False
    elif value == 21:
        if difficulty == 0:
            random_value = randint(1, 1000)
            if random_value == 10:
                return True
            else:
                return False
        else:
            return False

def play_round(difficulty: int) -> int:
    """This function is the main game loop itself: it is responsible for I/O, and also
    calling in helper functions. Intakes dealer difficulty and returns who won (or if
    it was a tie)"""
    new_deck = cards.make_new_deck()
    hands = []
    display_hands = []
    dealer_hands = []
    display_dealer_hands = []
    for i in range(2):
        add_to_hand(new_deck, hands, display_hands, True)
        add_to_hand(new_deck, dealer_hands, display_dealer_hands, False)

    # this section is for the player's turn
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
        elif player_choice == "stand":
            doclear.clear()
            break
        doclear.clear()
    hand_value = cards.get_hand_value(hands)

    # this section starts the dealer's turn
    dealer_hand_value = 0
    while dealer_hand_value <= 21 and hand_value <= 21:
        show_cards(display_dealer_hands, display_hands)
        print("Dealer is deciding...")
        sleep(2)
        dealer_hand_value = cards.get_hand_value(dealer_hands)
        choice = dealer_ai(dealer_hand_value, difficulty)
        if choice == False:
            break
        else:
            add_to_hand(new_deck, dealer_hands, display_dealer_hands, False)
            dealer_hand_value = cards.get_hand_value(dealer_hands)
            doclear.clear()
    dealer_hand_value = cards.get_hand_value(dealer_hands)
    doclear.clear()
    if hand_value > 21:
        print("You have busted!")
    if dealer_hand_value > 21:
        print("Dealer has busted!")
    if dealer_hand_value == hand_value:
        print("Tie!")
    show_cards(display_dealer_hands, display_hands)
    print(f"Player: {hand_value}, Dealer: {dealer_hand_value}")
    status = 0
    if hand_value > dealer_hand_value and hand_value <= 21 and dealer_hand_value <= 21:
        status = 0
    elif hand_value < dealer_hand_value and dealer_hand_value <= 21 and hand_value <= 21:
        status = 1
    elif hand_value > 21:
        status = 1
    elif dealer_hand_value > 21:
        status = 0
    else:
        status = 2
    return status
