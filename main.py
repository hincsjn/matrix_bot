import telebot
import config
import numpy as np
from telebot import types

bot = telebot.TeleBot(config.token)
user_mx = []  # матрица, введенная пользователем
chat = ''  # в этой переменной будет храниться message.chat.id
operation = 0


@bot.message_handler(commands=['start'])  # хендлер, начинающий программу после команды /start
def say_welcome(message):
    global chat
    msg = bot.send_message(message.chat.id, '''Привет!\n 
    Я провожу операции над матрицами\nВведи 
    матрицу в формате 1 2 3; 4 5 6''')
    chat = message.chat.id
    bot.register_next_step_handler(msg, print_mx)


def print_mx(message):
    global user_mx

    if user_mx == []:
        user_mx = np.matrix(message.text)
    else:
        pass

    bot.send_message(chat, 'Полученная матрица: ')
    for i in user_mx:
        bot.send_message(chat, i)
    msg = bot.send_message(chat, 'Выберете одно из действий:\n'
          '1: операция сложения элементов матрицы и числа (в разработке)\n'
          '2: операция умножения элементов матрицы и числа\n'
          '3: операция транспонирования матрицы\n'
          '4: операция возведения элементов матрицы в неотрицательную степень\n'
          '5: операция нахождения определителя матрицы\n'
          '6: операция нахождения союзной матрицы (в разработке)\n'
          '7: операция нахождения прикрепленной матрицы (в разработке)\n'
          '8: операция нахождения обратной матрицы\n')
    bot.register_next_step_handler(msg, choose_operation)


def choose_operation(message):
    global operation

    operation = int(message.text)
    msg = bot.send_message(chat, 'Отправь 1 для продолжения')
    if operation == 1:
        bot.register_next_step_handler(msg, mx_add())
    elif operation == 2:
        bot.register_next_step_handler(msg, mx_mult())
    elif operation == 3:
        bot.register_next_step_handler(msg, mx_transp)
    elif operation == 4:
        bot.register_next_step_handler(msg, mx_exp())
    elif operation == 5:
        bot.register_next_step_handler(msg, mx_det())
    elif operation == 6:
        bot.register_next_step_handler(msg, mx_transp)
    elif operation == 7:
        bot.register_next_step_handler(msg, mx_transp)
    elif operation == 8:
        bot.register_next_step_handler(msg, mx_transp)
    else:
        bot.send_message(message, 'Да иди нахуй, просил же нормально ввести')


def mx_add(message):
    global user_mx
    bot.reply_to(message, 'Введите число, с которым требуется сложить элементы матрицы: ')

    num = message.text
    for i in user_mx:
        for j in i:
            j += int(num)

    result = user_mx

    for i in result:
        bot.send_message(chat, i)

    bot.send_message(chat, result)

    msg = bot.send_message(chat, 'Если желаете продолжить работу с данной матрицей, нажмите 1')
    if message.text == '1':
        user_mx = result
        bot.register_next_step_handler(msg, print_mx)


def mx_mult(message):
    global user_mx
    bot.send_message(chat, 'Введите число, с которым требуется сложить элементы матрицы: ')

    num = int(message.text)
    for i in user_mx:
        for j in i:
            j *= num

    result = user_mx

    for i in result:
        bot.send_message(chat, i)

    bot.send_message(chat, result)

    msg = bot.send_message(chat, 'Если желаете продолжить работу с данной матрицей, нажмите 1')
    if message.text == '1':
        user_mx = result
        bot.register_next_step_handler(msg, print_mx)


def mx_transp(message):
    global user_mx
    matrix = user_mx
    result = np.matrix(matrix).transpose()

    for i in result:
        bot.send_message(chat, i)

    msg = bot.send_message(chat, 'Если желаете продолжить работу с данной матрицей, нажмите 1')
    if message.text == '1':
        user_mx = result
        bot.register_next_step_handler(msg, print_mx)


def mx_exp(message):
    pass


def mx_det(message):
    global user_mx
    result = np.linalg.det(user_mx)

    bot.send_message(chat, result)
    result = user_mx
    msg = bot.send_message(chat, 'Если желаете продолжить работу с данной матрицей, нажмите 1')

    if message.text == '1':
        user_mx = result
        bot.register_next_step_handler(msg, print_mx)


bot.polling()
