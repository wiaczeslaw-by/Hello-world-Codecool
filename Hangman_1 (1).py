import random
import os

ready_word = [] # Массив с символами введенными пользователем, символы будут записываться только те которых еще не называл пользователь и которые находяться в загаданном слове
word = [] # Массив с символами загаданного слова, данный масив будет терять символ если его ввел пользователь.
history = [] # Массив который будет хранить все символы которые вводит пользователь
attention_input = False # Это тригер который будет меняться на True если пользователь введет правельный символ второй раз
lives = 10 # Количество попыток\жизней у пользователя, данная переменная будет уменьшаться если пользователь вводит символ который не существует в загаданном слове
drawing = []
drawing2 = []
hangman = []
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
    
def check_quant_symb (list_check, letter_check): # Функция которая служит для вывода количеста уже введенных символов в массив(в нашем случае проверяем сколько одинаковых букв в массиве history)
    count = 0 
    for element in range(len(list_check)): # Проверяется каждый елемент в масисве
        if list_check[element] == letter_check: # Если елемент массива равняеться символу тогда увеличиваем счетчик на один
            count +=1
    return count
    
def start(): # Функция которая служит для базогого запуска приложения, приветствий и присвоения значений некоторым переменным
    global ready_word
    global word
    global hangman
    os.system("cls || clear")
    print("Welcome to Hangman!")
    hangman = take_grafics_from_f().split(",")
    hangman.reverse()
    words = take_words_from_f().split(",") # Разделяем строку на слова, разделителем являеться пробел
    word = list(words[random.randint(0,len(words)-1)]) # Выбираем рандомное слово и делим его на символы, помещая в массив
    if "\n" in word:
        word.remove("\n")
    for element in range(len(word)): # Заполняем массив пустыми символами относительно загаданного слова, данный массив будет обновляться при каждом правильном вводе символа
        ready_word.append("_")
    print(f"You have {lives} attempts to guess the word \nHere is your word - " + " ".join(ready_word))
    print(word)
    
def user_input(): # Функция которая отвечает за пользовательский ввод и все что его касссаеться
    print("Please input ANY letter")
    letter = ""
    while len(letter) != 1: # Цикл проверяет количество символов введенные пользователем, если количество введенных символов не равно 1, тогда повторяем попытки 
        letter = input_check_quit("Command - ")
        history.append(letter)
        if len(letter) != 1: # Если количество символов не равно 1, тогда выводим уведомление <====================New(Добавил вывод предупрежденния)
            print("Numbers of letters aren't equal \"1\"!") 
    return letter

def prog_logic(user_input): # Данная функция отвечает за всю основную логику программы <===============New(Поменял название, на более подходящеее)
    global ready_word
    global word
    global lives
    global attention_input
    global history
    global count_end
    global attention_wrong_input
    if check_quant_symb(history,user_input) > 1: #Если количество символов в "истории символов" равных введенному, больше чем 1 тогда меняем тригер на 1, триггер отвечает за сигнализиррование таких случаев 
            attention_input = True # <==================New(Перенес дааное условие в логику, так как оно тут более уместно)
    if (user_input not in word) and (user_input not in ready_word) and (check_quant_symb(history,user_input) < 2): # Если введенного символа не существует в массиве загаданного слова и массиве который постоянно обновляеться, тогда одно очко попыток
        lives-=1
        attention_wrong_input = True
    for element in range(len(word)): # Учитывая каждый индекс в массиве загаданного слова
        if word[element].lower() == user_input: # Если введенный символ равняется символу в загаданном слове 
            ready_word[element] = word[element] # Меняем пустой символ обновляющегося массива на ввеведенный символ
            word[element] = " " # Меняем тот же символ в массиве загаданного слова на пробел
            count_end += 1
    return ready_word

def prog_output(ready_word): # Функция служит для вывода данных об игре, попытках,<===============New(Поменял название, на более подходящеее)
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
        prog_output(prog_logic(user_input_variable)) #<=================New(Сократил код с двух до одной строчки)
    winner()

if __name__ == "__main__": #
    main()