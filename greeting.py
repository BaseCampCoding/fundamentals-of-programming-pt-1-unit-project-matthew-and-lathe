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

    print(table_string)
    characters = """
    Billy is the youngest dealer, far from the best at cards.
    Karen is one of the better ones, moderately good.
    Lathe is the most handsome of the group, but not quite the best.
    Matt: The man, the myth, the legend himself. Need I say more?
    """
    print(characters)
    difficulty_selection = input("Choose your dealer with their corresponding number:")
    if doclear.RepresentsInt(difficulty_selection) == True:
        difficulty_selection = int(difficulty_selection)
    while (doclear.RepresentsInt(difficulty_selection) == False or (difficulty_selection < 0 or difficulty_selection > 3)):
        print("Please enter value between 0-3")
        difficulty_selection = input(
            "Choose your dealer with their corresponding number:"
        )
    return difficulty_selection
