import random
import os

ready_word = [] # Array with characters entered by the user, characters will be written only those that have not yet been named by the user and that are found in the hidden word
word = [] # Array with characters of the hidden word, this array will lose the character if the user entered it.
history = [] # Array that will store all characters that the user enters
attention_input = False # This is a trigger that will change to True if the user enters the correct character a second time
lives = 10 # Number of attempts\lives of the user, this variable will decrease if the user enters a character that does not exist in the hidden word
count_end = 0
attention_wrong_input = False

def input_check_quit(text_command):
    input_command = input(text_command)
    if(input_command.lower() == "quit"):
        print("Good bye!")
        quit()
    else:
        return input_command.lower()

def take_grafics_from_f():
    global lives
    print("Select difficulty:\n    1 - Easy\n    2 - Normal\n    3 - Hard")
    file_dir = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(file_dir, "Grafics.txt")
    while True:
        try:
            command = int(input_check_quit("Command - "))
            with open(my_file,"r") as words_f:
                try:
                    os.system("cls || clear")
                    if command == 2:
                        lives = 8
                    elif command == 3:
                        lives = 6
                    return words_f.read().split(",,")[command-1]
                except IndexError:
                    print(f"Please selecet command from 1 to {len(words_f.readlines())}")
                    continue
        except ValueError:
            print("Please input a number!")
            continue


def take_words_from_f():
    print("Select the type of words:\n    1 - Home\n    2 - Cities\n    3 - Countries\n    4 - Animals  ")
    file_dir = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(file_dir, "Words.txt")
    while True:
        try:
            command = int(input_check_quit("Command - "))
            with open(my_file,"r") as words_f:
                try:
                    os.system("cls || clear")
                    return words_f.readlines()[command-1]
                except IndexError:
                    print(f"Please selecet command from 1 to {len(words_f.readlines())}")
                    continue
        except ValueError:
            print("Please input a number!")
            continue
    
def check_quant_symb (list_check, letter_check): # Function that is used to output the number of characters already entered in the array(in our case, we check how many identical letters are in the history array)
    count = 0 
    for element in range(len(list_check)): # Every element in the array is checked
        if list_check[element] == letter_check: # If the array element is equal to a character then increase the counter by one
            count +=1
    return count
    
def start(): # A function which serves as the base for launching the application, greetings and assign values to some variables
    global ready_word
    global word
    global hangman
    os.system("cls || clear")
    print("Welcome to Hangman!")
    hangman = take_grafics_from_f().split(",")
    hangman.reverse()
    words = take_words_from_f().split(",") # We divide the string into words, the separator is a space
    word = list(words[random.randint(0,len(words)-1)]) # Select a random word and divide it into characters by placing it in an array
<<<<<<< HEAD
    word.remove("\n")
=======
    if "\n" in word:
        word.remove("\n")
>>>>>>> 725cbecb4bbb6083380be7d1eca17ffde36871cc
    for element in range(len(word)): # Filling the array with empty characters relative to the hidden word. this array will be updated every time you enter the correct character
        ready_word.append("_")
    print(f"You have {lives} attempts to guess the word \nHere is your word - " + " ".join(ready_word))
    print(word)
    
def user_input(): # A function that is responsible for user input and everything that reads it
    print("Please input ANY letter")
    letter = ""
    while len(letter) != 1: # The loop checks the number of characters entered by the user, if the number of characters entered is not equal to 1, then try again
        letter = input_check_quit("Command - ")
        history.append(letter)
        if len(letter) != 1: # If the number of characters is not equal to 1, then output a notification
            print("Numbers of letters aren't equal \"1\"!") 
    return letter

def prog_logic(user_input): # This function is responsible for all the main logic of the global ready_word program
    global ready_word
    global word
    global lives
    global attention_input
    global history
    global count_end
    global attention_wrong_input
    if check_quant_symb(history,user_input) > 1: #If the number of characters in the "history" is equal to the one entered, more than 1, then we change the trigger to 1, the trigger is responsible for signaling such cases 
            attention_input = True 
    if (user_input not in "".join(word).lower() and (user_input not in "".join(ready_word).lower()) and (check_quant_symb(history,user_input) < 2)): # If the entered character does not exist in the array of the hidden word and the array is constantly updated, then one point of attempts

        lives-=1
        attention_wrong_input = True
    for element in range(len(word)): # Given each index in the array of the hidden word
        if word[element].lower() == user_input: # If the entered character is equal to the character in the hidden word 
            ready_word[element] = word[element] # Changing the empty character of the updated array to the entered character
            word[element] = " " # Changing the same character in the array of the hidden word to a space
            count_end += 1
    return ready_word

def prog_output(ready_word): # This function is used for displaying game data
    global word
    global attention_input
    global lives
    os.system("cls || clear")
    print(word)
    print(f"{lives} attempts remaining")
    print(" ".join(ready_word))
    if attention_input: #
       print("History: "+"|".join(history))
       print("Be attentive!")
       attention_input = False
    elif attention_wrong_input == True:
        print("History: "+"|".join(history))
    print(hangman[lives])
    print("\n")

def winner():
    if count_end >= len(word):
        print("You're WINNER Take a candy!")
    elif lives <=0:
        print("You're HANGMAN!")    

def main(): #
    start() 
    while count_end < len(word) and lives > 0: #
        user_input_variable = user_input()
        prog_output(prog_logic(user_input_variable)) 
    winner()

if __name__ == "__main__": #
    main()