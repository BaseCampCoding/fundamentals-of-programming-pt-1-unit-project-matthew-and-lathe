import cards

# ♣, ♦, ♥, ♠
print(
    """
    Welcome to Memory!
    The cards will flash in front of you for a few seconds.
    See if you can remember them all.
    """
)
cardset_1_art = """
    #####  #####
    #A  #  #3  #
    #   #  #   #
    #  ♠#  #  ♦#
    #####  #####
    """
cardset_1_values = ["ace of spades", "3 of diamonds", "three of diamonds"]

cardset_2_art = """
    #####  #####
    #K  #  #K  #
    #   #  #   #
    #  ♥#  #  ♥#
    #####  #####
    """
cardset_2_values = ["king of hearts", "king of hearts"]

cardset_3_art = """
    #####  #####
    #Q  #  #4  #
    #   #  #   #
    #  ♣#  #  ♥#
    #####  #####
    """
cardset_3_values = ["queen of clubs", "4 of hearts", "four of hearts"]

cardset_4_art = """
    #####  #####
    #3  #  #10 #
    #   #  #   #
    #  ♦#  #  ♠#
    #####  #####
    """
cardset_4_values = ["3 of diamonds", "10 of spades", "ten of spades"]

question = input("What two cards did you see?")
