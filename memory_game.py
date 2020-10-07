import random
# ♣, ♦, ♥, ♠

print(
    """
    Welcome to Memory!
    The cards will flash in front of you for a few seconds.
    See if you can remember them all.
    """
)
cardset_1= ["""
    ##### 
    #A  # 
    #   # 
    #  ♠# 
    #####  
    """,
    "ace of spades"]

cardset_2 = ["""
    #####
    #K  #
    #   #
    #  ♥#
    #####
    """
    , "king of hearts"]

cardset_3 = ["""
    #####
    #Q  #
    #   #
    #  ♣#
    #####
    """
    , "queen of clubs"]

cardset_4_art = """
    #####
    #J  #
    #   #
    #  ♦#
    #####
    """,
"jack of diamonds"]


question = input("What two cards did you see?")
