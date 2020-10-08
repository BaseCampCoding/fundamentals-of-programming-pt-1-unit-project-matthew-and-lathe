import random
import doclear
import cards
import greeting
import gameloop
import threecard
from memory_game import main_memory_game
from time import sleep

difficulty = 0
money = 100
greeting.hello_player()
choice = ''
while money >= 10:
    difficulty = greeting.choose_dealer(money)
    game_mode = greeting.choose_game()
    sleep(1.5)
    if difficulty == 4:
        break
    doclear.clear()
    choice = ''
    while choice != 'leave' and money >= 10:
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
            money += bet * 2
        elif status == 1:
            print("You lost!")
            money -= bet
            if money < min_bet:
                break
        else:
            print("It was a tie!")
        choice = input("Enter 'leave' to pick another table or 'again' to play again: ")
        choice = choice.lower()
        while choice != 'leave' and choice != 'again':
            print("Invalid input.")
            choice = input("Enter 'leave' to pick another table or 'again' to play again: ")
            choice = choice.lower()
    if money < 10:
        break
if money < 10:
    print("Get outta here!")
else:
    print("See ya later, then.")