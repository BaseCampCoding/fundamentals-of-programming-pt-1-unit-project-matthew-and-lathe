import cards
from gameloop import add_to_hand
from gameloop import show_cards

def three_card_poker (difficulty: int) -> int:
    """This will be our new addition to the casino, with a simplified version of poker.
    First, the player and dealer are dealt 3 cards. Next, both are given the chance to 
    trade in cards from their hand. Finally, they compare hands, and the one with a higher
    value wins. If they have equal values, it is a tie, and they get their bets back.
    """
    new_deck = cards.make_new_deck()
    hands = []
    display_hands = []
    dealer_hands = []
    display_dealer_hands = []
    for i in range(3):
        add_to_hand(new_deck, hands, display_hands, True)
        add_to_hand(new_deck, dealer_hands, display_dealer_hands, False)

    hand_value = 0
    player_choice = ''
    while player_choice != 'go':
        show_cards(display_dealer_hands, display_hands)
        print("-------------------------------------------------------------")
        print("Which card do you want to give up? (enter one, two, or three)")
        print("-------------------------------------------------------------")
        player_choice = input()
        player_choice = player_choice.lower()
        while player_choice != "one" and player_choice != "two" and player_choice != "three":
            print("Please enter one, two, or three")
            player_choice = input()
            player_choice = player_choice.lower()
        