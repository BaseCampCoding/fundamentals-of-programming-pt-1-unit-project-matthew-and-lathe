import random
import doclear
import cards
import greeting
import gameloop
import threecard
from memory_game import main_memory_game
from time import sleep

opensave = input("Open save file? [Y/N]: ")
opensave.upper

if opensave == "Y":
    with open("savefile.json", "w") as savefile:
        money = json.load(savefile)
if opensave == "N":
    break
else:
    print("Please enter valid input, Y or N.")

difficulty = 0
money = 100
greeting.hello_player()
choice = ""
while money >= 10:
    difficulty = greeting.choose_dealer(money)
    if difficulty == 4:
        break
    game_mode = greeting.choose_game()
    sleep(1.5)
    doclear.clear()
    choice = ""
    while choice != "leave" and money >= 10:
        min_bet = 0
        if difficulty == 0:
            min_bet = 10
        elif difficulty == 1:
            min_bet = 25
        elif difficulty == 2:
            min_bet = 50
        else:
            min_bet = 100
        bet = greeting.get_bet(money, min_bet)
        if game_mode == "blackjack":
            status = gameloop.play_round(difficulty)
        elif game_mode == "minipoker":
            status = threecard.three_card_poker(difficulty)
        else:
            status = main_memory_game(difficulty)
        if status == 0:
            print("You won!")
            money += bet
        elif status == 1:
            print("You lost!")
            money -= bet
            if money < min_bet:
                print("You no longer meet the minimum bet for this table.")
                sleep(2)
                break
        else:
            print("It was a tie!")
        choice = input("Enter 'leave' to pick another table or 'again' to play again: ")
        choice = choice.lower()
        while choice != "leave" and choice != "again":
            print("Invalid input.")
            choice = input(
                "Enter 'leave' to pick another table or 'again' to play again: "
            )
            choice = choice.lower()
    if money < 10:
        break
if money < 10:
    cards.colored_text("Get outta here!", 0)
else:
    cards.colored_text("See ya later, then.", 2)