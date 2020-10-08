import doclear
from tableart import table_string
from cards import colored_text


def hello_player():
    bigwelcome = """
    #####    #        #######  #######  #     #      #####   #######  #######  #     #
    #     #  #        #     #  #        #    #          #    #     #  #        #    #
    #     #  #        #     #  #        #   #           #    #     #  #        #   #
    #######  #        #######  #        #  #            #    #######  #        #  #
    #     #  #        #     #  #        #   #      #    #    #     #  #        #   #
    #     #  #        #     #  #        #    #     #    #    #     #  #        #    #
    #####    #######  #     #  #######  #     #    ######    #     #  #######  #     #    
    """
    colored_text(bigwelcome, 0, False)
    mission_statement = """
    You have entered the casino with $100.
    Your goal is to turn that into $1000 dollars by playing blackjack.
    Good luck.
    """
    colored_text(mission_statement, 0, False)
    input("Press any key to play ")
    doclear.clear()


def choose_dealer(money: int):
    colored_text(table_string, 5, True)
    characters = [
        [
            "Billy",
            "is the youngest dealer, far from the best at cards. He is also a loud mouth. (Min Bet: 10)",
        ],
        [
            "Karen",
            "is one of the better ones, moderately good. Not as talkative as Billy. (Min Bet: 25)",
        ],
        [
            "Lathe",
            "is the most handsome of the group, but not quite the best. He is pretty quiet. (Min Bet: 50)",
        ],
        [
            "Matt",
            "The man, the myth, the legend himself. Need I say more? (Min Bet: 100)",
        ],
    ]
    # Prints colored name then description of character
    colored_text(characters[0][0], 2, False)
    print(characters[0][1])
    print(" ")
    colored_text(characters[1][0], 4, False)
    print(characters[1][1])
    print(" ")
    colored_text(characters[2][0], 0, False)
    print(characters[2][1])
    print(" ")
    colored_text(characters[3][0], 1, False)
    print(characters[3][1])

    difficulty_selection = input("Choose your dealer with their corresponding number:")
    if doclear.RepresentsInt(difficulty_selection) == True:
        difficulty_selection = int(difficulty_selection)
    if difficulty_selection == 0 and money < 10:
        difficulty_selection = -1
    elif difficulty_selection == 1 and money < 25:
        difficulty_selection = -1
    elif difficulty_selection == 2 and money < 50:
        difficulty_selection = -1
    elif difficulty_selection == 3 and money < 100:
        difficulty_selection = -1
    elif difficulty_selection == 4 and money < 1000:
        print("Not yet, you have got to get to $1000 first!")
        difficulty_selection = -1
    while doclear.RepresentsInt(difficulty_selection) == False or (
        difficulty_selection < 0 or difficulty_selection > 3
    ):
        print(
            "Please enter value between 0-3, and a dealer with a minimum bet you can meet."
        )
        difficulty_selection = input(
            "Choose your dealer with their corresponding number:"
        )
        if doclear.RepresentsInt(difficulty_selection) == True:
            difficulty_selection = int(difficulty_selection)
        else:
            continue
        # these if-elif s are for making sure the player meets the minimum bet,
        # or for them to leave the casino
        if difficulty_selection == 0 and money < 10:
            difficulty_selection = -1
        elif difficulty_selection == 1 and money < 25:
            difficulty_selection = -1
        elif difficulty_selection == 2 and money < 50:
            difficulty_selection = -1
        elif difficulty_selection == 3 and money < 100:
            difficulty_selection = -1
        elif difficulty_selection == 4 and money >= 1000:
            break
        elif difficulty_selection == 4 and money < 1000:
            print("Not yet, you have got to get to $1000 first!")
    if difficulty_selection == (0):
        colored_text("[Billy: Get ready to eat it!]", 2, False)
    if difficulty_selection == (1):
        colored_text(
            "[Karen: I’m sorry that people are so jealous of me but I can’t help it that I’m popular.]",
            4,
            False,
        )
    if difficulty_selection == (2):
        colored_text(
            "[Lathe: I'm not conceited. Conceit is a fault and I have no faults.]",
            0,
            False,
        )
    if difficulty_selection == (3):
        colored_text("[Matt: So you have chosen death.]", 1, False)
    if difficulty_selection == (4):
        colored_text("Thanks for coming, hope to see you again!", 4, False)
    return difficulty_selection


def get_bet(money: int, min_bet: int) -> int:
    print(f"You have ${money}")
    bet = input(f"Please enter a bet of atleast ${min_bet}: ")
    is_int = doclear.RepresentsInt(bet)
    while is_int == False or int(bet) < min_bet:
        print("Invalid input.")
        bet = input(f"Please enter a bet of atleast ${min_bet}: ")
        is_int = doclear.RepresentsInt(bet)
    bet = int(bet)
    return bet


def choose_game() -> str:
    print("What game do you want to play? Enter the name of the game.")
    choice = input("blackjack, minipoker, or memory? ")
    while choice != "blackjack" and choice != "minipoker" and choice != "memory":
        print("Invalid input.")
        choice = input("blackjack, minipoker, or memory? ")
    return choice