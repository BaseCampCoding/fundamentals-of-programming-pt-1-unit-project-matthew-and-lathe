import cards
import doclear
from random import randint
from time import sleep

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
        elif difficulty == 2:
            random_value = randint(1, 15)
            if random_value == 10:
                return True
            else:
                return False
        elif difficulty == 3:
            random_value = randint(1, 18)
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
        elif difficulty == 1 or difficulty == 2:
            random_value = randint(1, 100)
            if random_value == 10:
                return True
            else:
                return False
        else:
            random_value = randint(1, 200)
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


def char_dialogue(diff_level: int):
    """Determines chances of certain dialogue being said by each character/difficulty chosen"""
    num1 = randint(0, 10)
    if diff_level == 0:
        if num1 > 0 and num1 <= 3:
            print("[Billy: Get ready to go down!]")
        if num1 > 3 and num1 <= 5:
            print("[Billy: Believe it!]")
        if num1 > 5 and num1 <= 10:
            print("[Billy: I'm the best!] ")
    if diff_level == 1:
        if num1 > 0 and num1 <= 5:
            print("[Karen: Is butter a carb?]")
    if diff_level == 2:
        if num1 > 0 and num1 <= 6:
            print("[Lathe: The only thing I'm allergic to is criticism.]")
    if diff_level == 3:
        if num1 > 0 and num1 <= 2:
            print(
                "[Matt: I gave you the chance of aiding me willingly, but you have elected the way of pain.]"
            )


def play_round(difficulty: int) -> int:
    """This function is the main game loop itself: it is responsible for I/O, and also
    calling in helper functions. Intakes dealer difficulty and returns who won (or if
    it was a tie)"""
    new_deck = cards.make_new_deck()
    hands = []
    display_hands = []
    dealer_hands = []
    #this list is only for showing the back of the dealer's hand
    default_card= """
        #####
        #♠|♥#
        #-+-#
        #♦|♣#
        #####
        """
    display_dealer_hands = [default_card, default_card]
    #this list is specifically for showing the dealer's hand at the end of the game
    real_dealer_hands = []
    for i in range(2):
        add_to_hand(new_deck, hands, display_hands, True)
        add_to_hand(new_deck, dealer_hands, real_dealer_hands, True)
    
    # this section is for the player's turn
    hand_value = 0
    while hand_value <= 21:
        cards.show_cards(display_dealer_hands, display_hands, 0, 1)
        cards.colored_text("-------------", 4)
        print("Hit or Stand?")
        cards.colored_text("-------------", 4)
        player_choice = input()
        player_choice = player_choice.lower()
        while player_choice != "hit" and player_choice != "stand":
            print("Please enter hit or stand.")
            player_choice = input()
            player_choice = player_choice.lower()
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
        cards.show_cards(display_dealer_hands, display_hands, 0, 1)
        char_dialogue(difficulty)
        print("Dealer is deciding...")
        sleep(4)
        dealer_hand_value = cards.get_hand_value(dealer_hands)
        choice = dealer_ai(dealer_hand_value, difficulty)
        if choice == False:
            break
        else:
            add_to_hand(new_deck, dealer_hands, real_dealer_hands, True)
            display_dealer_hands.append(default_card)
            dealer_hand_value = cards.get_hand_value(dealer_hands)
            doclear.clear()
    dealer_hand_value = cards.get_hand_value(dealer_hands)
    doclear.clear()
    if hand_value > 21:
        cards.colored_text("You have busted!", 0)
    if dealer_hand_value > 21:
        cards.colored_text("Dealer has busted!", 2)
    if dealer_hand_value == hand_value:
        cards.colored_text("Tie!", 3)
    cards.show_cards(real_dealer_hands, display_hands, 1, 1)
    print(f"Player: {hand_value}, Dealer: {dealer_hand_value}")
    status = 0
    if hand_value > dealer_hand_value and hand_value <= 21 and dealer_hand_value <= 21:
        status = 0
    elif (
        hand_value < dealer_hand_value and dealer_hand_value <= 21 and hand_value <= 21
    ):
        status = 1
    elif hand_value > 21:
        status = 1
    elif dealer_hand_value > 21:
        status = 0
    else:
        status = 2
    return status
