import random
import doclear
from time import sleep

# ♣, ♦, ♥, ♠
def main_memory_game(difficulty: int):
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
    shuffle_cards3 = random.choice(memory_cards)
    shuffle_cards4 = random.choice(memory_cards)
    # Easy mode
    if difficulty == 0 or difficulty == 1:
        print("Here we go...")
        sleep(2)
        print(shuffle_cards1[0], shuffle_cards2[0])
        sleep(2)
        doclear.clear()
        print("[Example: ace of spades, queen of hearts]")
        question1 = input("What was the first card you saw? ")
        question1 = question1.lower()
        if question1 == shuffle_cards1[1]:
            print("You got it!")
        if question1 != shuffle_cards1[1]:
            print("Nope!")

        question2 = input("What was the second card you saw? ")
        print("[Example: ace of spades, queen of hearts]")
        question2 = question2.lower()
        if question2 == shuffle_cards2[1]:
            print("You got it!")
        if question2 != shuffle_cards2[1]:
            print("Nope!")
        if question1 == shuffle_cards1[1] and question2 == shuffle_cards2[1]:
            return 0
        else:
            return 1
    # Hard mode
    if difficulty == 2 or difficulty == 3:
        print("Here we go...")
        sleep(2)
        print(
            shuffle_cards1[0], shuffle_cards2[0], shuffle_cards3[0], shuffle_cards4[0]
        )
        sleep(2)
        doclear.clear()
        print("[Example: ace of spades, queen of hearts]")
        question1 = input("What was the first card you saw? ")
        question1 = question1.lower()
        if question1 == shuffle_cards1[1]:
            print("You got it!")
        if question1 != shuffle_cards1[1]:
            print("Nope!")

        question2 = input("What was the second card you saw? ")
        print("[Example: ace of spades, queen of hearts]")
        question2 = question2.lower()
        if question2 == shuffle_cards2[1]:
            print("You got it!")
        if question2 != shuffle_cards2[1]:
            print("Nope!")

        question3 = input("What was the third card you saw? ")
        print("[Example: ace of spades, queen of hearts]")
        question3 = question3.lower()
        if question3 == shuffle_cards3[1]:
            print("You got it!")
        if question3 != shuffle_cards3[1]:
            print("Nope!")

        question4 = input("What was the fourth card you saw? ")
        print("[Example: ace of spades, queen of hearts]")
        question4 = question4.lower()
        if question4 == shuffle_cards4[1]:
            print("You got it!")
        if question4 != shuffle_cards4[1]:
            print("Nope!")

        if (
            question1 == shuffle_cards1[1]
            and question2 == shuffle_cards2[1]
            and question3 == shuffle_cards3[1]
            and question4 == shuffle_cards4[1]
        ):
            return 0
        else:
            return 1
