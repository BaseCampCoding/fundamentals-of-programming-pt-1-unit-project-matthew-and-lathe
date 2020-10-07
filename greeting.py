import doclear
from tableart import table_string


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
    print(bigwelcome)
    mission_statement = """
    You have entered the casino with $100.
    Your goal is to turn that into $1000 dollars by playing blackjack.
    Good luck.
    """
    print(mission_statement)
    input("Press any key to play ")
    doclear.clear()


def choose_dealer():
    print(table_string)
    characters = """
    Billy is the youngest dealer, far from the best at cards. He is also a loud mouth. (Min Bet: 10)
    Karen is one of the better ones, moderately good. Not as talkative as Billy, but not scared to chit-chat. (Min Bet: 25)
    Lathe is the most handsome of the group, but not quite the best. He is usually pretty quiet. (Min Bet: 50)
    Matt: The man, the myth, the legend himself. Need I say more? (Min Bet: 100)
    """
    print(characters)
    difficulty_selection = input("Choose your dealer with their corresponding number:")
    if doclear.RepresentsInt(difficulty_selection) == True:
        difficulty_selection = int(difficulty_selection)
    while doclear.RepresentsInt(difficulty_selection) == False or (
        difficulty_selection < 0 or difficulty_selection > 3
    ):
        print("Please enter value between 0-3")
        difficulty_selection = input(
            "Choose your dealer with their corresponding number:"
        )
    if difficulty_selection == (0):
        print("[Billy: Get ready to eat it!]")
    if difficulty_selection == (1):
        print(
            "[Karen: I’m sorry that people are so jealous of me but I can’t help it that I’m popular.]"
        )
    if difficulty_selection == (2):
        print("[Lathe: I'm not conceited. Conceit is a fault and I have no faults.]")
    if difficulty_selection == (3):
        print("[Matt: So you have chosen death.]")

    return difficulty_selection
