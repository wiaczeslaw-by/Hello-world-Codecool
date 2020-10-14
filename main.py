import Hangman_1
import 

def user_input(text):
    user_input = input(text)
    if(user_input.lower == "quit"):
        quit()
    return user_input


def main():
    while True:
        print("Please enter the name of game:\n   Hangman\n   Hot-Warm-Cold")
        user_input = user_input("Game: ")
        if user_input == "Hangman":
            Hangman_1.main()
        elif user_input == "hot-warm-cold".lower():


main()