import random
import doclear
from time import sleep

# ♣, ♦, ♥, ♠

print(
    """
    Welcome to Memory!
    The cards will flash in front of you for a few seconds.
    See if you can remember them all.
    """
)
input("Press Enter to begin")
doclear.clear()

cardset_1 = [
    """
    ##### 
    #A  # 
    #   # 
    #  ♠# 
    #####  
    """,
    "ace of spades",
]

cardset_2 = [
    """
    #####
    #K  #
    #   #
    #  ♥#
    #####
    """,
    "king of hearts",
]

cardset_3 = [
    """
    #####
    #Q  #
    #   #
    #  ♣#
    #####
    """,
    "queen of clubs",
]

cardset_4 = [
    """
    #####
    #J  #
    #   #
    #  ♦#
    #####
    """,
    "jack of diamonds",
]

memory_cards = [cardset_1, cardset_2, cardset_3, cardset_4]
shuffle_cards1 = random.choice(memory_cards)
shuffle_cards2 = random.choice(memory_cards)
print("Here we go...")
sleep(3)
print(shuffle_cards1[0], shuffle_cards2[0])
sleep(0.3)
doclear.clear()
question = input("What two cards did you see?")
