import random
import os
rand_comp = [] # Randomowe liczby od komputera
num_user = [] # Liczby od użytkownika
difficulty_level = None # Trudność zadania/ilość liczb od komputera oraz użytkownika
hot_count = 0 # Count "HOT"

def start(): # Funkcja do wprowadzenia podstawowych danych 
    global difficulty_level
    os.system("cls || clear")
    print("Welcome to the Hot Warm Cold game")
    while(difficulty_level == None):
        try:
            difficulty_level = int(check_user_input("Enter complexity: "))
        except ValueError:
            os.system("cls || clear")
            print("Miała być liczba\nProszę sprobować ponownie")
    for i in range(difficulty_level):
        rand_comp.append(random.randint(0,9))
#    print(rand_comp) # Do testowania

def check_user_input(text):
    u_input = input(text)
    if u_input.lower() == "quit":
        print("Have a good day!")
        quit()
    return u_input

def user_input():
    while len(num_user) < difficulty_level:
        try:
            num = int(check_user_input("Enter number: "))
            num_user.append(num)
        except ValueError:
            print("Miła być liczba!")

def prog_logick():
    global hot_count
    result = ""
    for i in range(difficulty_level):
        if num_user[i] == rand_comp[i]:
            result += "HOT "
            hot_count += 1
        elif num_user[i] in rand_comp:
            result += "Warm "
        else:
            result += "Cold "
    return result

def prog_output():
    global hot_count
    result = prog_logick()
    if hot_count == difficulty_level:
        os.system("cls || clear")
        print(result)
        print("Winner! Thank you for the game!")
    else:
        os.system("cls || clear")
        print(result)
        print("Your last input: " + "".join(str(num_user)))
        print("Try again")
        num_user.clear()
        hot_count = 0


def main():
    start()
    while hot_count < difficulty_level:
        user_input()
        prog_output()

if __name__ == "__main__":
    main()






lis_1 = [1,2,5,8,2,3]
lis_2 = []