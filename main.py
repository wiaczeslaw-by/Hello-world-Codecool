import Hangman_1
import HOT_WARM_COLD

def user_input(text):
    u_input = input(text)
    if u_input.lower() == "quit":
        quit()
    else:
        return u_input


def main():
    while True:
        print("Please enter the name of game:\n   Hangman\n   Hot-Warm-Cold")
        game_input = user_input("Game: ")
        if game_input.lower() == "hangman":
            Hangman_1.main()
        elif game_input.lower() == "hot-warm-cold":
            HOT_WARM_COLD.main()



if __name__ == "__main__":
    main()