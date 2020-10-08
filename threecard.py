import cards
from doclear import clear
from time import sleep
from gameloop import add_to_hand
from cards import show_cards
from random import randint

def replace_cards (new_deck: list, hands: list, display_hands: list, marks: list) -> None:
    """Note that this function is soley for the player, not for the dealer. This function
    takes in what cards the player chose to replace, and replaces them."""
    while 1 in marks or 2 in marks or 3 in marks:
        if 1 in marks:
            popped = hands.pop(0)
            display_hands.pop(0)
            random = randint(0, 51)
            new_deck.insert(random, popped)
            add_to_hand(new_deck, hands, display_hands, True)
            marks.remove(1)
        if 2 in marks:
            popped = hands.pop(1)
            display_hands.pop(1)
            random = randint(0, 51)
            new_deck.insert(random, popped)
            add_to_hand(new_deck, hands, display_hands, True)
            marks.remove(2)
        if 3 in marks:
            popped = hands.pop(2)
            display_hands.pop(2)
            random = randint(0, 51)
            new_deck.insert(random, popped)
            add_to_hand(new_deck, hands, display_hands, True)
            marks.remove(3)

def evalutate_hand (hands: list) -> int:
    """This function will determine how valuable a hand it, and return that integer
    pairs are worth 20 times their card's value, triples are worth 300 times their card's
    value, flushes are worth their highest card value times 4000, and royal flushes are worth
    more than anything else possible"""
    #list for keeping track of how many of each card a player has (for pairs and triples)
    templet_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    has_pair = False
    has_triple = False
    has_flush = False
    #bools for seeing the 3 royal cards
    jack = False
    queen = False
    king = False
    #these are for keeping up with whether we have a valid flush
    spades = 0
    clubs = 0
    diamonds = 0
    hearts = 0

    value = 0
    for i in hands:
        if i[1] == 'J':
            jack = True
            counts[9] += 1
            value += 11
        elif i[1] == 'Q':
            queen = True
            counts[10] += 1
            value += 12
        elif i[1] == 'K':
            king = True
            counts[11] += 1
            value += 13
        else:
            temp = templet_list.index(i[1])
            counts[temp] += 1
            value += temp + 2
        #♣, ♦, ♥, ♠
        if i[0] == "♠":
            spades += 1
        elif i[0] == "♣":
            clubs += 1
        elif i[0] == "♦":
            diamonds += 1
        elif i[0] == "♥":
            hearts += 1
    has_seen = 0
    #stores what value the pair, triple, or what items are in a flush
    temp_value = 0
    if jack == True and queen == True and king == True:
        #this final check is to be sure they are of the same suit
        if clubs == 3 or spades == 3 or diamonds == 3 or hearts == 3:
            return 100000
    else:
        for i in counts:
            if i == 1 and has_seen == 0:
                has_seen = 1
            elif i == 0 and has_seen == 1:
                has_seen = 0
            elif i == 1 and has_seen == 1:
                has_seen = 2
            elif i == 0 and has_seen == 2:
                has_seen = 0
            elif i == 1 and has_seen == 2:
                has_flush = True
                temp_value += counts.index(i) + 1
                break
            elif i == 2:
                has_pair = True
                temp_value += counts.index(i) + 1
                break
            elif i == 3:
                has_triple = True
                temp_value += counts.index(i) + 1
                break
        if has_pair == True:
            value += temp_value * 20
        elif has_triple == True:
            value += temp_value * 300
        elif has_flush == True:
            #this final check is to be sure they are of the same suit
            if clubs == 3 or spades == 3 or diamonds == 3 or hearts == 3:
                value += temp_value * 4000
    return value

def dealer_choices (value: int, hands: list, difficulty: int) -> list:
    """This function will determine the overall worth of the hand, and then
    send out the 'marks' of what cards they wish to replace (this is represented
    through a list)"""
    templet_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    ran = 0
    if value <= 12:
        if difficulty == 0:
            if randint(1, 20) != 1:
                return [1, 2, 3]
            else:
                ran = randint(1, 3)
                return [ran]
        else:
            return [1, 2, 3]
    elif value <= 40:
        if difficulty == 0:
            return [1, 2, 3]
        elif difficulty == 1 or difficulty == 2:
            if randint(1, 2) != 1:
                return [1, 2, 3]
            else:
                return []
    elif value <= 260:
        ran = randint(1, 100)
        if difficulty == 0:
            if ran < 5:
                return [1, 2, 3]
            else:
                ran = randint(1, 3)
                return [ran]
        elif difficulty == 1:
            if ran == 1:
                return [1, 2 ,3]
            elif ran > 98:
                ran = randint(1, 3)
                return [ran]
            else:
                return []
        else:
            if ran == 1:
                ran = randint(1, 3)
                return [ran] 
            else:
                return []
    elif value <= 660:
        ran = randint(1, 100)
        if difficulty == 0:
            if ran == 1:
                ran = randint(1, 3)
                return [ran]
    


def three_card_poker (difficulty: int) -> int:
    """This will be our new addition to the casino, with a simplified version of poker.
    First, the player and dealer are dealt 3 cards. Next, both are given the chance to 
    trade in cards from their hand. Finally, they compare hands, and the one with a higher
    value wins. If they have equal values, it is a tie, and they get their bets back.
    """
    clear()
    new_deck = cards.make_new_deck()
    hands = []
    display_hands = []
    dealer_hands = []
    real_dealer_hands = [] #this new variable will be for showing the dealer's hand at the end
    #of the game
    default_card= """
        #####
        #♠|♥#
        #-+-#
        #♦|♣#
        #####
        """
    display_dealer_hands = [default_card, default_card, default_card]
    for i in range(3):
        add_to_hand(new_deck, hands, display_hands, True)
        add_to_hand(new_deck, dealer_hands, real_dealer_hands, True)

    hand_value = 0
    player_choice = ''
    marks = []
    while player_choice != 'go':
        show_cards(display_dealer_hands, display_hands, 2, 3)
        print("-------------------------------------------------------------------------")
        cards.colored_text("Pairs beat a random hand, Three of a Kind beats a pair, a Flush", 1, False)
        cards.colored_text("(three consecutive cards) beat Three of a kind, and a Royal Flush", 1, False)
        cards.colored_text("trumps all. Flushes, Royal or not, must share suit among all three.", 1, False)
        print("-------------------------------------------------------------------------")
        print(" Which card do you want to give up? (enter 'one', 'two', or 'three')")
        print(" You can enter 'one', 'two', or 'three' again if you want to cancel")
        print(" giving it up.")
        print(" Once you make your choices, enter 'go' to continue.")
        print("-------------------------------------------------------------------------")
        player_choice = input()
        player_choice = player_choice.lower()
        while player_choice != "one" and player_choice != "two" and player_choice != "three" and player_choice != "go":
            print("Please enter 'one', 'two', 'three', or 'go'")
            player_choice = input()
            player_choice = player_choice.lower()

        if player_choice == "one" and 1 in marks:
            cards.colored_text("Card will no longer be sent into the deck.", 1, False)
            marks.remove(1)
        elif player_choice == "one" and not 1 in marks:
            cards.colored_text("Card will be sent into the deck.", 0, False)
            marks.append(1)
        elif player_choice == "two" and not 2 in marks:
            cards.colored_text("Card will be sent into the deck.", 0, False)
            marks.append(2)
        elif player_choice == "two" and 2 in marks:
            cards.colored_text("Card will no longer be sent into the deck.", 1, False)
            marks.remove(2)
        elif player_choice == "three" and not 3 in marks:
            cards.colored_text("Card will be sent into the deck.", 0, False)
            marks.append(3)
        elif player_choice == "three" and 3 in marks:
            cards.colored_text("Card will no longer be sent into the deck.", 1, False)
            marks.remove(3)
        elif player_choice == "go":
            break
        sleep(1)
        clear()
    replace_cards(new_deck, hands, display_hands, marks)
    dealer_choices = (evalutate_hand(dealer_hands), dealer_hands, difficulty)
    replace_cards(new_deck, dealer_hands, real_dealer_hands, dealer_choices)
    hand_value = evalutate_hand(hands)
    dealer_hand_value = evalutate_hand(dealer_hands)
    clear()
    show_cards(real_dealer_hands, display_hands, 3, 3)
    print(f"Dealer: {dealer_hand_value}. Player: {hand_value}")
    if hand_value > dealer_hand_value:
        return 0
    elif hand_value < dealer_hand_value:
        return 1
    else:
        return 2        