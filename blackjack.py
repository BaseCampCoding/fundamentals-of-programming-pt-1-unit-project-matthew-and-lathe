import random
import doclear
import cards
import greeting
import gameloop

difficulty = 0
difficulty = greeting.hello_player()
doclear.clear()
while True:
    status = gameloop.play_round(difficulty)
    if status == 0:
        print("You won!")
    elif status == 1:
        print("You lost!")
    else:
        print("It was a tie!")
    choice = input("Enter '0' to exit or P to play again: ")
    choice = choice.lower()
    if choice == "0":
        break
    elif choice.lower() == "p":
        doclear.clear()
        continue
    else:
        doclear.clear()
        continue