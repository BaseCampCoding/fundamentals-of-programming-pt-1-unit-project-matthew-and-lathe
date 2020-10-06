import random
import doclear
import cards
import greeting
import gameloop

greeting.hello_player()
difficulty = 0
while True:
    status = gameloop.play_round(difficulty)
    if status == 0:
        print("You won!")
    elif status == 1:
        print("You lost!")
    else:
        print("It was a tie!")
    choice = input("Enter '0' to exit: ")
    if choice == "0":
        break