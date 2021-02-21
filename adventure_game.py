import time
import random


def pause_print(delay=2):
    time.sleep(delay)


def make_selection():
    while True:
        response = input("Please enter 1 or 2.\n").lower()
        if "1" in response:
            play_game()
        elif "2" in response:
            break
        else:
            print("Please enter 1 or 2.\n")
            pause_print()


def play_again():
    print("Would you like to play again?")
    pause_print()
    print("Enter 1 to play again.")
    pause_print()
    print("Enter 2 to exit the game.")
    pause_print()
    make_selection()


def drink_elixir():
    list = ["live", "die"]
    fate = random.choice(list)
    if fate == "live":
        print("You passed the forest without any danger! You won the game.")
        pause_print()
    elif fate == "die":
        print("The elixir was poisonous and you died! Game over.")
        pause_print()
    else:
        print("The game encountered an error and will start again.")
        pause_print()
    play_again()


def walk_to_forest():
    print("You do not have the elixir to be protected and you died.")
    pause_print()
    play_again()


def play_game():
    print("Welcome to the adventure game.")
    pause_print()
    print("You are a mighty knight.")
    pause_print()
    print("You are about to enter a forest with evil souls.")
    pause_print()
    print("At the entrance, you saw a monk.")
    pause_print()
    print("Enter 1 to talk to the monk.")
    pause_print()
    print("Enter 2 to walk into the forest without talking with the monk.")
    pause_print()

    while True:
        response = input("Please enter 1 or 2.\n").lower()
        if "1" in response:
            print("The monk gave you a protection elixir.")
            pause_print()
            drink_elixir()
            break
        elif "2" in response:
            print("You passed the monk and walked into the forest.")
            pause_print()
            walk_to_forest()
            break
        else:
            print("Please enter 1 or 2.\n")
            pause_print()


play_game()
