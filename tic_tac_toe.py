from telegram.ext import ConversationHandler

from fun import keyboard

board = list(range(1, 10))#последовательность от 1 до 9


def d_board(bot, update):
    global board
    for i in range(3):
        update.message.reply_text(f"| {board[0 + i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |",
                                  reply_markup=keyboard())#вертикальные линии


def st_game(bot, update):
    global board
    text = 'Игра начинается:'
    update.message.reply_text(text)#выводим текст пользователю
    board = list(range(1, 10))# в board помещаем список последовательность от 1 до 9
    d_board(bot, update)#активируем поле
    update.message.reply_text(f"Куда поставим X?")
    return "СHOISE_X"


def ch_win():
    global board
    win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))#выигрышные комбинации
    for eh in win:#прогоняем элементы кортежа
        if board[eh[0]] == board[eh[1]] == board[eh[2]]:#проверяем комбинацию
            return board[eh[0]]#возврат выигрышной комбинации
    # проверяем на ничью
    counter = 0
    for i in board:
        if type(i) == int:
            continue
        else:
            counter += 1
    if counter == 9:
        return counter
    else:
        return False


def tic(bot, update):
    global board
    player_answer = int(update.message.text)#принимаем сообщение пользователя и конвертируем в число
    if str(board[player_answer - 1]) not in "XO":#если в этой клетки нет Х или О
        board[player_answer - 1] = "X"#индексу из роследовательности board введенный пользователем присвоить Х
        d_board(bot, update) #активируется поле
    else:# если клетка уже занята
        update.message.reply_text("Эта клеточка уже занята,выберите другую")
        return f"CHOISE_X"#Вернуть строку,возврат к выбору чтобы был выбор там где эта функция будет вызвана
    tp = ch_win()#функцию проверки помещаем в переменную
    if type(tp) == str:#если результат выполнения функции проверки не число(число там только counter)
        update.message.reply_text(f"{tp} Win!") # значит победа
        return ConversationHandler.END
    elif type(tp) == int:# по аналогии c counter
        update.message.reply_text("Ничья!")
        return ConversationHandler.END
    else:
        update.message.reply_text(f"Куда поставим X?") #если все не то тогда заного
    return "CHOISE_X"#Вернуть строку,возврат к выбору чтобы был выбор там где эта функция будет вызвана


def tac(bot, update):
    global board
    player_answer = int(update.message.text)
    if str(board[player_answer - 1]) not in "XO":
        board[player_answer - 1] = "O"
        d_board(bot, update)
    else:
        update.message.reply_text("Эта клеточка уже занята,выберите другую")
        return f"CHOISE_O"#Вернуть строку,возврат к выбору чтобы был выбор там где эта функция будет вызвана
    tmp = ch_win()
    if type(tmp) == str:
        update.message.reply_text(f"{tmp} выиграл!")
        return ConversationHandler.END
    else:
        update.message.reply_text(f"Куда поставим O?")
    return "CHOISE_O"#Вернуть строку,возврат к выбору чтобы был выбор там где эта функция будет вызвана