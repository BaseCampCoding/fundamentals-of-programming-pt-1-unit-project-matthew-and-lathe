import random
import doclear
import cards
import greeting
import gameloop

greeting.hello_player()
while True:
    gameloop.play_round()
    choice = input("Enter '0' to exit: ")
    if choice == "0":
        break