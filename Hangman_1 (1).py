import random
import os
inport os2

row_of_words = "gizmo glowworm glyph gnarly gnostic gossip grogginess haiku haphazard yphen iatrogenic icebox injury ivory" # Строка с словами
ready_word = [] # Массив с символами введенными пользователем, символы будут записываться только те которых еще не называл пользователь и которые находяться в загаданном слове
word = [] # Массив с символами загаданного слова, данный масив будет терять символ если его ввел пользователь.
history = [] # Массив который будет хранить все символы которые вводит пользователь
attention_input = False # Это тригер который будет меняться на True если пользователь введет правельный символ второй раз
lives = 10 # Количество попыток\жизней у пользователя, данная переменная будет уменьшаться если пользователь вводит символ который не существует в загаданном слове
n = "\n"
p = " "
drawing = "|\n  |\n  |  \n  |\n / \ "
drawing2 = "\n   ___\n  |   |\n  |   ò\n  |"
hangman = ["",f"{6*n} / \ ",f"   {5*n}  |\n / \ ",f"   {4*n}  |  \n  |\n / \ ",f"   {3*n}  |\n  |  \n  |\n / \ ",f"   {2*n}  {drawing}",f"\n   ___\n  {drawing}",f"   \n   ___\n  |   {drawing}",f"   {drawing2}  / \ \n  |\n / \ ",f"   {drawing2}  /|\ \n  |\n / \ ",f"   {drawing2}  /|\ \n  |  / \ \n / \ "]
count_end = 0
attention_wrong_input = False

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
    hangman.reverse()
    words = row_of_words.split(" ") # Разделяем строку на слова, разделителем являеться пробел
    word = list(words[random.randint(0,len(words)-1)]) # Выбираем рандомное слово и делим его на символы, помещая в массив
    for element in range(len(word)): # Заполняем массив пустыми символами относительно загаданного слова, данный массив будет обновляться при каждом правильном вводе символа
        ready_word.append("_")
    print(f"Welcome to Hangman!\nYou have {lives} attempts to guess the word \nHere is your word - " + " ".join(ready_word))
    print(word)
    

def user_input(): # Функция которая отвечает за пользовательский ввод и все что его касссаеться
    print("Please input ANY letter")
    letter = ""
    while len(letter) != 1: # Цикл проверяет количество символов введенные пользователем, если количество введенных символов не равно 1, тогда повторяем попытки 
        letter = input("letter - ").lower()
        if letter.lower() == "quit":
            break
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
        if word[element] == user_input: # Если введенный символ равняется символу в загаданном слове 
            ready_word[element] = user_input # Меняем пустой символ обновляющегося массива на ввеведенный символ
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
        if user_input_variable.lower() == "quit":
            print("Good bye!")
            break
        prog_output(prog_logic(user_input_variable)) #<=================New(Сократил код с двух до одной строчки)
    winner()




if __name__ == "__main__": #
    main()

























    """     if lives is 9:
       print(" \n\n\n\n\n\n / \ ")
    if lives is 8:
        print("\n\n\n\n\n  |\n / \ ")
    if lives is 7:
        print("\n\n\n\n  |  \n  |\n / \ ")
    if lives is 6:
        print("\n\n\n  |\n  |  \n  |\n / \ ")
    if lives is 5:
        print("\n\n  |\n  |\n  |  \n  |\n / \ ")
    if lives is 4:
        print("\n   ___\n  |\n  |\n  |  \n  |\n / \ ")
    if lives is 3:
        print("\n   ___\n  |   |\n  |\n  |  \n  |\n / \ ")
    if lives is 2:
        print ("\n   ___\n  |   |\n  |   ò\n  |  / \ \n  |\n / \ ")
    if lives is 1:
        print("\n   ___\n  |   |\n  |   ò\n  |  /|\ \n  |\n / \ ")
    if lives is 0:
        print("\n   ___\n  |   |\n  |   ò\n  |  /|\ \n  |  / \ \n / \ \n You're HANGMAN!") """
