import Hangman_1
import HOT_WARM_COLD
import os

def user_input(text): # Modified function for user input, this function checks certain commands from the user
    u_input = input(text)
    if u_input.lower() == "quit":
        print("Have a good day!")
        quit()
    else:
        return u_input


def main(): #The main function of the program that allows you to select a game
    os.system("cls || clear")
    while True:
        print("Select game:\n   1 - Hangman\n   2 - Hot Warm Cold")
        game_input = user_input("Game: ")
        if game_input.lower() == "1":
            Hangman_1.main()
        elif game_input.lower() == "2":
            HOT_WARM_COLD.main()



if __name__ == "__main__":
    main()